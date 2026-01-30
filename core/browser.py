from playwright.sync_api import sync_playwright

def create_browser():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=True,
        args=["--disable-gpu"]
    )

    context = browser.new_context(
        ignore_https_errors=True
    )

    page = context.new_page()
    return playwright, browser, context, page
