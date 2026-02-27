import json
from datetime import datetime
from pathlib import Path


def export_widget_json(data, go_home, mode, target_hours, output_path="output/nettime_widget.json"):
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "daily_solde": data.get("daily_solde", ""),
        "monthly_solde": data.get("monthly_solde", ""),
        "go_home": go_home,
        "mode": mode,
        "target_hours": target_hours,
    }

    out_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
