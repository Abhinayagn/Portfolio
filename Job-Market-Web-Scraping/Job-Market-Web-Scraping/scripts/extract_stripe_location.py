from bs4 import BeautifulSoup
from pathlib import Path

def main():
    html_path = Path("debug/stripe_final.html")
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    text = soup.get_text("\n", strip=True)
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]

    hits = [ln for ln in lines if "location" in ln.lower()]
    print("\n--- Lines containing 'Location' ---")
    for h in hits[:40]:
        print(h)

    html_lower = html.lower()
    idx = html_lower.find("location")
    if idx != -1:
        start = max(0, idx - 500)
        end = min(len(html), idx + 800)
        snippet = html[start:end]
        Path("debug/location_snippet.html").write_text(snippet, encoding="utf-8")
        print("\nSaved: debug/location_snippet.html")
    else:
        print("\nCould not find the word 'location' in the HTML.")

if __name__ == "__main__":
    main()
