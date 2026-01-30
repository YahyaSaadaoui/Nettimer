from datetime import datetime, timedelta

def compute_go_home(daily_solde: str) -> str:
    if not daily_solde.startswith("-"):
        return "Maintenant 🎉"

    h, m = daily_solde.replace("-", "").split(":")
    minutes = int(h) * 60 + int(m)

    return (datetime.now() + timedelta(minutes=minutes)).strftime("%H:%M")
