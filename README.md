# Drum Synth Lab (Phase 0)

A minimal, runnable scaffold for a modular desktop drum synthesizer.

## Features

- PySide6 desktop window titled **Drum Synth Lab**
- A single **Preview** button
- Button click renders and plays a short low-frequency test tone
- Modular package layout for app, engine, audio, UI, and presets

## Requirements

- Python 3.10+
- PySide6
- numpy
- sounddevice

## Install

```bash
python -m pip install -e .
```

## Run

```bash
python -m drum_synth
```

## Project layout

```text
drum_synth/
  pyproject.toml
  README.md
  src/
    drum_synth/
      __init__.py
      __main__.py
      app/
      engine/
      audio/
      ui/
      presets/
  presets/
    default_kick.json
```
