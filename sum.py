from playwright.sync_api import sync_playwright

total = 0

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for seed in range(13, 23):

        url = f"https://sanand0.github.io/tdsdata/playwright_sum/seed_{seed}.html"

        page.goto(url)

        page.wait_for_selector("table")

        cells = page.query_selector_all("table td")

        for cell in cells:

            value = cell.inner_text().strip()

            if value.isdigit():

                total += int(value)

    browser.close()

print("TOTAL =", total)
