import json
from pathlib import Path
from bs4 import BeautifulSoup

def main():
    html = Path("debug/stripe_final.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    scripts = soup.select('script[type="application/ld+json"]')
    print("JSON-LD script tags found:", len(scripts))

    for i, sc in enumerate(scripts, start=1):
        raw = sc.get_text(strip=True)
        if not raw:
            continue

        # Sometimes JSON-LD has multiple objects or whitespace issues
        try:
            data = json.loads(raw)
        except Exception as e:
            print(f"\nScript {i}: JSON parse failed:", e)
            continue

        # JSON-LD might be a dict or list
        items = data if isinstance(data, list) else [data]

        for item in items:
            if not isinstance(item, dict):
                continue

            # Look for job posting schema
            if item.get("@type") in ["JobPosting", "jobposting"]:
                print("\n✅ Found JobPosting JSON-LD")
                title = item.get("title", "")
                org = (item.get("hiringOrganization") or {}).get("name", "")
                emp = item.get("employmentType", "")

                job_loc = item.get("jobLocation")
                # jobLocation can be dict or list
                locs = job_loc if isinstance(job_loc, list) else ([job_loc] if job_loc else [])

                locations = []
                for loc in locs:
                    if not isinstance(loc, dict):
                        continue
                    addr = (loc.get("address") or {})
                    city = addr.get("addressLocality", "")
                    region = addr.get("addressRegion", "")
                    country = addr.get("addressCountry", "")
                    combined = ", ".join([x for x in [city, region, country] if x])
                    if combined:
                        locations.append(combined)

                print("Title:", title)
                print("Org:", org)
                print("EmploymentType:", emp)
                print("Locations:", locations if locations else "(not found in JSON-LD)")
                return

    print("\nNo JobPosting JSON-LD found.")

if __name__ == "__main__":
    main()
