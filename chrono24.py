import os
import time
import csv
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# به Playwright بگو مرورگر کنار exe است
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(BASE_DIR, "ms-playwright")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(
        "https://www.chrono24.com/rolex/datejust--mod45.htm",
        wait_until="domcontentloaded",
        timeout=180000
    )

    # قبول کوکی
    try:
        page.wait_for_selector("button:has-text('OK')", timeout=8000)
        page.click("button:has-text('OK')")
    except:
        pass

    # اسکرول
    for _ in range(20):
        page.mouse.wheel(0, 3000)
        time.sleep(1)

    # صبر تا دیتا بیاد
    page.wait_for_function(
        "document.querySelectorAll('div.p-t-3').length > 10",
        timeout=120000
    )

    products = page.query_selector_all("div.p-t-3")

    with open("rolex.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price", "Country"])

        for item in products:
            try:
                name = item.query_selector("p.text-bold").inner_text()
                price = item.evaluate(
                    "el => el.nextElementSibling.querySelector('p.text-bold')?.innerText"
                )
                country = item.evaluate(
                    "el => el.nextElementSibling.querySelector('span')?.innerText"
                )
                writer.writerow([name, price, country])
            except:
                continue

    print("✅ CSV saved successfully")
    browser.close()
