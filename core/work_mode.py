import json
from datetime import datetime
from pathlib import Path


DEFAULT_MODE = "normal"
RAMADAN_MODE = "ramadan"
MODE_STATE_PATH = Path("output/work_mode_state.json")


def get_target_minutes(mode: str) -> int:
    if mode == RAMADAN_MODE:
        return 7 * 60
    return 8 * 60 + 30


def get_target_label(mode: str) -> str:
    minutes = get_target_minutes(mode)
    hours = minutes // 60
    remainder = minutes % 60
    return f"{hours}:{remainder:02d}"


def normalize_mode(value: str | None) -> str:
    if value == RAMADAN_MODE:
        return RAMADAN_MODE
    return DEFAULT_MODE


def load_mode(state_path: Path = MODE_STATE_PATH) -> str:
    if not state_path.exists():
        return DEFAULT_MODE

    try:
        payload = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        return DEFAULT_MODE

    return normalize_mode(payload.get("mode"))


def save_mode(mode: str, state_path: Path = MODE_STATE_PATH) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "mode": normalize_mode(mode),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    state_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
