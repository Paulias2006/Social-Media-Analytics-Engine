from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
CONFIG_PATH = ROOT / "config" / "settings.json"
DB_PATH = DATA_DIR / "social_media_analytics.sqlite"


def load_settings() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
