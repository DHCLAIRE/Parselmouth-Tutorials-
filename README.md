# Parselmouth Tutorials

This repository documents the [Parselmouth](https://github.com/YannickJadoul/Parselmouth) Python API and shows how to reproduce or call Praat Vocal Toolkit scripts from Python.

The Vocal Toolkit tutorials are generated from the local plugin scripts in `/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit`. The Parselmouth tutorials are generated from `data/parselmouth_api_manifest.json`, which was introspected from the official `praat-parselmouth` package.

## Start Here

1. Install Parselmouth: `python -m pip install praat-parselmouth`.
2. Point Python at the toolkit: `export VOCAL_TOOLKIT_DIR="/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit"`.
3. Read [Parselmouth patterns](tutorials/parselmouth-patterns.md).
4. Pick a Parselmouth API member from [the Parselmouth index](tutorials/parselmouth/index.md) or a Vocal Toolkit command from [the toolkit index](tutorials/index.md).

## What Is Included

- `227` Parselmouth API function/property tutorials across `31` classes and enums.
- `66` user-facing Vocal Toolkit command tutorials.
- `9` internal/helper script references.
- `src/vocal_toolkit_parselmouth.py`, a reusable Python wrapper for `praat.run_file`.
- `src/vocal_toolkit_extensions.py`, Python functions for all Vocal Toolkit commands that can be imported directly.
- `examples/batch_process.py`, a minimal batch-processing example.

## Coverage Checklist

- Toolkit commands with compact direct Parselmouth equivalents: `6`.
- Toolkit commands implemented as generated Python extension wrappers: `60`.
- Parselmouth API members marked as not covered by Vocal Toolkit: `93`.

Full comparison tables:

- [Vocal Toolkit commands without native Parselmouth equivalents](tutorials/comparisons/toolkit-not-in-parselmouth.md)
- [Parselmouth API not covered by Vocal Toolkit](tutorials/comparisons/parselmouth-not-in-toolkit.md)

Major Parselmouth areas marked as outside the Vocal Toolkit scope include low-level object/file I/O, Matrix and Vector cell operations, Spectrum bin statistics, TextGrid conversion helpers, time-grid utility methods, and enum/metadata properties.

## Compatibility Note

The current manifest was generated from `praat-parselmouth 0.4.7` with embedded Praat `6.1.38`. The Vocal Toolkit `setup.praat` asks for Praat 6.4.20 or newer, so check `parselmouth.PRAAT_VERSION` if a toolkit script fails in your environment.

## Regenerate

```bash
VOCAL_TOOLKIT_DIR="/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit" \
python3 tools/generate_vocal_toolkit_tutorials.py
```

To refresh the Parselmouth API manifest from an installed Parselmouth package:

```bash
python3 tools/introspect_parselmouth_api.py
```
