"""Audio buffer generation helpers."""

from __future__ import annotations

import numpy as np


def render_test_tone(sample_rate: int = 44_100) -> np.ndarray:
    """Render a 0.5 second 60 Hz mono sine wave as float32."""
    duration_seconds = 0.5
    frequency_hz = 60.0

    num_samples = int(sample_rate * duration_seconds)
    time_axis = np.arange(num_samples, dtype=np.float32) / np.float32(sample_rate)
    tone = 0.2 * np.sin(2.0 * np.pi * frequency_hz * time_axis)

    return tone.astype(np.float32)
