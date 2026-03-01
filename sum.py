from playwright.sync_api import sync_playwright

total = 0

with sync_playwright() as p:

    browser = p.chromium.launch()

    page = browser.new_page()

    for seed in range(13,23):

        url = f"https://sanand0.github.io/tdsdata/playwright_sum/seed_{seed}.html"

        page.goto(url)

        numbers = page.query_selector_all("td")

        for n in numbers:

            total += int(n.inner_text())

    browser.close()

print("TOTAL =", total)
