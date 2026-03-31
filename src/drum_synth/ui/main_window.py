"""Main application window for Drum Synth Lab."""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """Minimal main window with a Preview action."""

    preview_requested = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Drum Synth Lab")
        self._build_ui()

    def _build_ui(self) -> None:
        central = QWidget(self)
        layout = QVBoxLayout(central)

        preview_button = QPushButton("Preview", parent=central)
        preview_button.clicked.connect(self.preview_requested.emit)
        layout.addWidget(preview_button)

        self.setCentralWidget(central)
