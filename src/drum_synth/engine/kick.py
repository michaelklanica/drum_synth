"""Kick engine stub used for Phase 0 vertical slice."""

from __future__ import annotations

import numpy as np

from drum_synth.audio.render import render_test_tone
from drum_synth.engine.base import SynthEngine


class KickEngine(SynthEngine):
    """Minimal kick engine placeholder that renders a test tone."""

    def __init__(self, sample_rate: int = 44_100) -> None:
        self.sample_rate = sample_rate

    def render(self, params: dict) -> np.ndarray:
        """Return a short test tone buffer for preview playback."""
        _ = params
        return render_test_tone(sample_rate=self.sample_rate)
