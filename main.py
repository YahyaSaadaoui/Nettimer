import os
from dotenv import load_dotenv

load_dotenv()

from core.browser import create_browser
from core.time_calc import compute_go_home
from scraper.login import login
from scraper.extract import extract_nettime_data
from notifier.telegram import send_telegram

def main():
    playwright, browser, context, page = create_browser()

    try:
        login(
            page,
            os.getenv("NETTIME_USERNAME"),
            os.getenv("NETTIME_PASSWORD")
        )

        data = extract_nettime_data(page)

        daily = data["daily_solde"]
        monthly = data["monthly_solde"]
        go_home = compute_go_home(daily)

        send_telegram(daily, monthly, go_home)
        print("✅ Telegram notification sent")

    finally:
        context.close()
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    main()
