"""Preset loading and saving helpers."""

from __future__ import annotations

import json
from pathlib import Path


def load_preset(path: str | Path) -> dict:
    """Load a preset JSON file into a dictionary."""
    preset_path = Path(path)
    with preset_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_preset(path: str | Path, data: dict) -> None:
    """Save a preset dictionary to JSON."""
    preset_path = Path(path)
    preset_path.parent.mkdir(parents=True, exist_ok=True)
    with preset_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")
