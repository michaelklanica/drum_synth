"""Base interfaces for synthesis engines."""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class SynthEngine(ABC):
    """Abstract base class for synth engines."""

    @abstractmethod
    def render(self, params: dict) -> np.ndarray:
        """Render a mono audio buffer for given parameters."""
        raise NotImplementedError
