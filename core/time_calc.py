from datetime import datetime, timedelta

from core.work_mode import DEFAULT_MODE, RAMADAN_MODE

NORMAL_TARGET_MINUTES = 8 * 60 + 30
RAMADAN_TARGET_MINUTES = 7 * 60


def _parse_balance_minutes(daily_solde: str) -> int:
    value = (daily_solde or "").strip()
    if not value:
        return 0

    sign = -1 if value.startswith("-") else 1
    cleaned = value.lstrip("+-")
    try:
        h, m = cleaned.split(":")
        minutes = int(h) * 60 + int(m)
    except (ValueError, TypeError):
        return 0
    return sign * minutes


def _compute_remaining_minutes(daily_solde: str, mode: str) -> int:
    # The extracted balance is based on normal work target (8h30).
    remaining = max(0, -_parse_balance_minutes(daily_solde))

    if mode == RAMADAN_MODE:
        delta = NORMAL_TARGET_MINUTES - RAMADAN_TARGET_MINUTES
        return max(0, remaining - delta)

    return remaining


def compute_go_home(daily_solde: str, mode: str = DEFAULT_MODE) -> str:
    remaining_minutes = _compute_remaining_minutes(daily_solde, mode)
    if remaining_minutes == 0:
        return "Maintenant"

    return (datetime.now() + timedelta(minutes=remaining_minutes)).strftime("%H:%M")
