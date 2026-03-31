"""Audio playback routines."""

from __future__ import annotations

import numpy as np
import sounddevice as sd


def play_buffer(buffer: np.ndarray, sample_rate: int = 44_100) -> None:
    """Play a mono float32 NumPy buffer using blocking output."""
    if buffer.ndim != 1:
        raise ValueError("Expected a mono (1D) audio buffer.")

    sd.play(buffer, samplerate=sample_rate, blocking=True)
