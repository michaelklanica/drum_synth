"""Application startup and dependency wiring."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from drum_synth.audio.playback import play_buffer
from drum_synth.engine.kick import KickEngine
from drum_synth.ui.main_window import MainWindow


def run() -> int:
    """Start the Drum Synth Lab desktop application."""
    app = QApplication(sys.argv)

    engine = KickEngine()
    window = MainWindow()

    def on_preview_clicked() -> None:
        buffer = engine.render(params={})
        play_buffer(buffer, sample_rate=engine.sample_rate)

    window.preview_requested.connect(on_preview_clicked)
    window.show()

    return app.exec()
