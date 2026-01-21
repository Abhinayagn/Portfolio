from pathlib import Path
from bs4 import BeautifulSoup

def main():
    html = Path("debug/stripe_final.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    scripts = soup.find_all("script")
    print("Total <script> tags found:", len(scripts))

    # Look for common modern-app embedded data markers
    needles = [
        "__NEXT_DATA__",
        "jobLocation",
        "addressLocality",
        "addressRegion",
        "employmentType",
        "greenhouse",
        "location",
        "office",
        "JobPosting",
        "posting",
        "cities",
        "country",
    ]

    found_any = False

    for idx, sc in enumerate(scripts, start=1):
        txt = sc.get_text(" ", strip=True)
        if not txt:
            continue

        hits = [n for n in needles if n.lower() in txt.lower()]
        if hits:
            found_any = True
            print("\n--- Script #", idx, "matches:", hits, "---")
            print("Length:", len(txt))
            # print only first 800 chars so terminal doesn't explode
            print(txt[:800])

    if not found_any:
        print("\nNo obvious embedded JSON markers found in any <script> tags.")

if __name__ == "__main__":
    main()
