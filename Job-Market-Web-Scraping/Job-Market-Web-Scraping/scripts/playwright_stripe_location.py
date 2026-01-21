from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

URL = "https://stripe.com/jobs/listing/accounts-receivable-analyst/7369428"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Use domcontentloaded (more stable than networkidle for modern sites)
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)

        # Wait for the right-side info card to appear
        # On your screenshot it contains "Office locations"
        try:
            page.wait_for_selector("text=Office locations", timeout=30000)
        except PWTimeout:
            print("Timed out waiting for 'Office locations'. Taking screenshot for debug...")
            page.screenshot(path="debug/stripe_rendered_fail.png", full_page=True)
            browser.close()
            return

        # Grab the whole sidebar card text (contains Office locations, Team, Job type)
        card_text = page.locator("text=Office locations").locator("xpath=ancestor::*[self::div][1]").inner_text()
        # If the above container is too small, we’ll also capture a larger area near it:
        bigger_block = page.locator("text=Office locations").locator("xpath=ancestor::section[1]").inner_text()

        print("\n--- Card text (small container) ---")
        print(card_text)

        print("\n--- Card text (section container) ---")
        print(bigger_block)

        # Screenshot for proof
        page.screenshot(path="debug/stripe_rendered.png", full_page=True)
        print("\nSaved screenshot: debug/stripe_rendered.png")

        browser.close()

if __name__ == "__main__":
    main()
