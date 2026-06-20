"""Batch-run a Vocal Toolkit script with Parselmouth.

Set VOCAL_TOOLKIT_DIR to the plugin_VocalToolkit folder before running this.
"""

from pathlib import Path

from parselmouth import SoundFileFormat

from src.vocal_toolkit_parselmouth import run_toolkit_script


INPUT_DIR = Path("audio")
OUTPUT_DIR = Path("processed")
OUTPUT_DIR.mkdir(exist_ok=True)

for wav_path in sorted(INPUT_DIR.glob("*.wav")):
    result = run_toolkit_script("normalize.praat", wav_path)
    try:
        result.save(str(OUTPUT_DIR / wav_path.name), SoundFileFormat.WAV)
    except AttributeError:
        print(f"{wav_path}: script returned {type(result)!r}; inspect it before saving")
