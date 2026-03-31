"""Preset schema definitions for synth engines."""

from __future__ import annotations

from typing import TypedDict


class KickPreset(TypedDict):
    """Minimal kick preset structure for Phase 0."""

    name: str
    engine: str
    params: dict[str, float]
