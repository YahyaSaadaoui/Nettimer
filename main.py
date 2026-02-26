import argparse
import os
from dotenv import load_dotenv

load_dotenv()

from core.browser import create_browser
from core.time_calc import compute_go_home
from core.work_mode import DEFAULT_MODE, RAMADAN_MODE, get_target_label, load_mode, save_mode
from scraper.login import login
from scraper.extract import extract_nettime_data
from notifier.telegram import send_telegram
from exporter.json_exporter import export_widget_json

def parse_args():
    parser = argparse.ArgumentParser(description="Run NetTime extraction and notifications.")
    parser.add_argument(
        "--mode",
        choices=[DEFAULT_MODE, RAMADAN_MODE],
        help="Persist and use a work mode (normal=8:30, ramadan=7:00).",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Print the current persisted mode and exit.",
    )
    return parser.parse_args()


def resolve_mode(requested_mode: str | None) -> tuple[str, str | None]:
    current_mode = load_mode()
    if not requested_mode:
        return current_mode, None

    save_mode(requested_mode)
    return requested_mode, current_mode


def main():
    args = parse_args()
    active_mode, previous_mode = resolve_mode(args.mode)
    target_hours = get_target_label(active_mode)

    if args.mode == RAMADAN_MODE and previous_mode != RAMADAN_MODE:
        print("Ramadan mode activated (7:00 target). It will stay active until you switch back.")
    elif args.mode == RAMADAN_MODE and previous_mode == RAMADAN_MODE:
        print("Ramadan mode is already active (7:00 target).")
    elif args.mode == DEFAULT_MODE and previous_mode == RAMADAN_MODE:
        print("Ramadan mode cancelled. Normal mode is active again (8:30 target).")
    elif args.mode == DEFAULT_MODE and previous_mode == DEFAULT_MODE:
        print("Normal mode is already active (8:30 target).")

    if args.status:
        print(f"Current mode: {active_mode} ({target_hours})")
        return

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
        go_home = compute_go_home(daily, mode=active_mode)

        export_widget_json(data, go_home, mode=active_mode, target_hours=target_hours)
        send_telegram(daily, monthly, go_home, mode=active_mode, target_hours=target_hours)
        print(f"Telegram notification sent (mode: {active_mode}, target: {target_hours})")

    finally:
        context.close()
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    main()
