import re
import time
import random
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests
import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

INCLUDE_TITLE_KEYWORDS = [
    "data analyst",
    "business analyst",
    "analyst",
    "analytics",
    "bi",
    "reporting",
    "insights",
    "product analyst",
    "strategy analyst",
    "operations analyst",
    "accounts receivable analyst",
]

EXCLUDE_TITLE_KEYWORDS = [
    "account executive",
    "sales",
    "recruiter",
    "marketing",
    "customer success",
    "business development",
    "solutions engineer",
    "partner manager",
]

def get_board_urls(slug: str) -> list[str]:
    return [
        f"https://boards.greenhouse.io/{slug}",
        f"https://job-boards.greenhouse.io/{slug}",
    ]

def extract_job_id(url: str) -> str:
    m = re.search(r"/(\d{6,})(?:$|[/?#])", url)
    return m.group(1) if m else ""

def title_matches(title: str) -> bool:
    t = title.lower()
    if any(bad in t for bad in EXCLUDE_TITLE_KEYWORDS):
        return False
    return any(good in t for good in INCLUDE_TITLE_KEYWORDS)

def make_canonical_job_url(board_url: str, company_slug: str, any_job_url: str) -> str:
    job_id = extract_job_id(any_job_url)
    if not job_id:
        return any_job_url
    parsed = urlparse(board_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    return f"{base}/{company_slug}/jobs/{job_id}"

def scrape_greenhouse_list(board_url: str, company_slug: str) -> pd.DataFrame:
    r = requests.get(board_url, headers=HEADERS, timeout=30)
    if r.status_code != 200:
        print(f"Board status {r.status_code} (skipping): {board_url}")
        return pd.DataFrame(columns=["company_slug", "job_title", "job_link", "board_url", "job_id"])

    soup = BeautifulSoup(r.text, "lxml")

    rows = []
    seen = set()

    for a in soup.select('a[href*="/jobs/"]'):
        title = a.get_text(strip=True)
        href = a.get("href", "")
        if not title or not href:
            continue

        raw_link = urljoin(board_url, href)
        job_id = extract_job_id(raw_link)
        if not job_id:
            continue

        job_link = make_canonical_job_url(board_url, company_slug, raw_link)

        if job_link in seen:
            continue
        seen.add(job_link)

        rows.append({
            "company_slug": company_slug,
            "job_title": title,
            "job_link": job_link,
            "board_url": board_url,
            "job_id": job_id,
        })

    return pd.DataFrame(rows)

# -------- Detail extraction helpers --------

def parse_greenhouse_location_department(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")

    # Greenhouse common selectors
    loc_el = soup.select_one("div.location") or soup.select_one(".location")
    dept_el = soup.select_one("div.department") or soup.select_one(".department")

    location = loc_el.get_text(" ", strip=True) if loc_el else ""
    department = dept_el.get_text(" ", strip=True) if dept_el else ""
    return location, department

def extract_stripe_sidebar_fields_with_playwright(url: str) -> dict:
    """
    Stripe page loads content via JS, so requests/BS4 won't show location/team/job type.
    We use Playwright to read rendered content.
    """
    data = {"location": "", "department": "", "job_type": ""}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set False if you want to watch
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Wait for the sidebar section to appear
        page.wait_for_selector("text=Office locations", timeout=30000)

        # The "section container" worked well in your run
        block = page.locator("text=Office locations").locator("xpath=ancestor::section[1]").inner_text()
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]

        # Parse simple label-value pairs
        def value_after(label: str) -> str:
            for i, ln in enumerate(lines):
                if ln.lower() == label.lower() and i + 1 < len(lines):
                    return lines[i + 1]
            return ""

        data["location"] = value_after("Office locations")
        data["department"] = value_after("Team")  # treat Team as department
        data["job_type"] = value_after("Job type")

        browser.close()

    return data

def scrape_job_detail(job_link: str) -> dict:
    """
    1) Request job_link (Greenhouse canonical)
    2) Follow redirects to final_url
    3) If final_url is stripe.com/jobs/listing -> Playwright extraction
       else try Greenhouse HTML parsing
    """
    r = requests.get(job_link, headers=HEADERS, timeout=30, allow_redirects=True)
    final_url = r.url
    status = r.status_code

    result = {
        "final_url": final_url,
        "http_status": status,
        "location": "",
        "department": "",
        "job_type": "",
        "detail_source": "",
    }

    if status != 200:
        return result

    # Stripe special handling
    if "stripe.com/jobs/listing/" in final_url:
        try:
            pw = extract_stripe_sidebar_fields_with_playwright(final_url)
            result["location"] = pw["location"]
            result["department"] = pw["department"]
            result["job_type"] = pw["job_type"]
            result["detail_source"] = "playwright_stripe"
            return result
        except PWTimeout:
            result["detail_source"] = "playwright_timeout"
            return result
        except Exception:
            result["detail_source"] = "playwright_error"
            return result

    # Otherwise, parse HTML (Greenhouse-style)
    location, department = parse_greenhouse_location_department(r.text)
    result["location"] = location
    result["department"] = department
    result["detail_source"] = "requests_bs4"
    return result

# -------- Main --------

def main():
    company_slugs = [
        "stripe",
        # Add more *confirmed* greenhouse slugs later
    ]

    all_rows = []
    scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for slug in company_slugs:
        print("\n==============================")
        print("Company slug:", slug)

        board_df = pd.DataFrame()
        used_board_url = ""

        for board_url in get_board_urls(slug):
            temp_df = scrape_greenhouse_list(board_url, slug)
            if not temp_df.empty:
                board_df = temp_df
                used_board_url = board_url
                break

        print("  Used board URL:", used_board_url if used_board_url else "(none)")
        print("  Real postings found:", len(board_df))

        if board_df.empty:
            continue

        filtered = board_df[board_df["job_title"].apply(title_matches)].reset_index(drop=True)
        print("  After analyst/analytics filter:", len(filtered))

        if filtered.empty:
            continue

        details = []
        for i, link in enumerate(filtered["job_link"].tolist(), start=1):
            print(f"    Detail {i}/{len(filtered)}")
            d = scrape_job_detail(link)
            details.append(d)
            time.sleep(random.uniform(0.8, 1.4))

        # Merge details into dataframe
        filtered["final_url"] = [d["final_url"] for d in details]
        filtered["http_status"] = [d["http_status"] for d in details]
        filtered["location"] = [d["location"] for d in details]
        filtered["department"] = [d["department"] for d in details]
        filtered["job_type"] = [d["job_type"] for d in details]
        filtered["detail_source"] = [d["detail_source"] for d in details]

        filtered["source"] = "Greenhouse"
        filtered["scraped_at"] = scraped_at

        all_rows.append(filtered)

    if not all_rows:
        print("\nNo matching roles found.")
        return

    final = pd.concat(all_rows, ignore_index=True).drop_duplicates(subset=["job_link"])
    final.to_csv("greenhouse_analyst_jobs.csv", index=False)

    print("\n✅ Saved: greenhouse_analyst_jobs.csv")
    print("Total roles:", len(final))
    print(final.to_string(index=False))

if __name__ == "__main__":
    main()
