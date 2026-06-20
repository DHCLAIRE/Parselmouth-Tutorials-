# Parselmouth Tutorials For Praat Vocal Toolkit

This repository documents how to reproduce or call the Praat Vocal Toolkit scripts from Python with [Parselmouth](https://github.com/YannickJadoul/Parselmouth).

The tutorials are generated from the local Vocal Toolkit plugin scripts in `/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit`. They cover every user-facing command registered in `buttons.praat` plus the internal helper scripts that those commands call.

## Start Here

1. Install Parselmouth: `python -m pip install praat-parselmouth`.
2. Point Python at the toolkit: `export VOCAL_TOOLKIT_DIR="/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit"`.
3. Read [Parselmouth patterns](tutorials/parselmouth-patterns.md).
4. Pick a command from [the tutorial index](tutorials/index.md).

## What Is Included

- `66` user-facing Vocal Toolkit command tutorials.
- `9` internal/helper script references.
- `src/vocal_toolkit_parselmouth.py`, a reusable Python wrapper for `praat.run_file`.
- `examples/batch_process.py`, a minimal batch-processing example.

## Compatibility Note

Parselmouth embeds Praat internally. The Vocal Toolkit `setup.praat` asks for Praat 6.4.20 or newer, so check `parselmouth.PRAAT_VERSION` if a script fails. Direct Python translations are included where practical; otherwise the pages show a faithful `praat.run_file` route.

## Regenerate

```bash
VOCAL_TOOLKIT_DIR="/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit" \
python3 tools/generate_vocal_toolkit_tutorials.py
```
