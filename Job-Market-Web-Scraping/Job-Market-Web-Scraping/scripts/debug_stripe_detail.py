import requests
from bs4 import BeautifulSoup
from pathlib import Path

HEADERS = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"}
URL = "https://boards.greenhouse.io/stripe/jobs/7369428"

def main():
    r = requests.get(URL, headers=HEADERS, timeout=30, allow_redirects=True)
    print("Status:", r.status_code)
    print("Final URL:", r.url)
    r.raise_for_status()

    Path("debug").mkdir(exist_ok=True)
    Path("debug/stripe_final.html").write_text(r.text, encoding="utf-8")
    print("Saved: debug/stripe_final.html")

    soup = BeautifulSoup(r.text, "lxml")
    print("Title:", soup.title.get_text(strip=True) if soup.title else "(no title)")

if __name__ == "__main__":
    main()
