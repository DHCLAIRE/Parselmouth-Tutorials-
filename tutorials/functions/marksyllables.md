# Mark regions by syllables...

- Praat source: `marksyllables.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `marksyllables.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- TextGrid or interval annotation.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Silence threshold (dB)` | `real` | `-25` | `silence_threshold` |
| `Minimum pause duration (s)` | `positive` | `0.3` | `minimum_pause_duration` |
| `Minimum dip between peaks (dB)` | `positive` | `2` | `minimum_dip_between_peaks` |
| `Show speech rate info` | `boolean` | `1` | `show_speech_rate_info` |
| `Trim initial and final silences` | `boolean` | `1` | `trim_initial_and_final_silences` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "marksyllables.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, -25, 0.3, 2, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "marksyllables.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    -25,  # Silence threshold (dB)
    0.3,  # Minimum pause duration (s)
    2,  # Minimum dip between peaks (dB)
    1,  # Show speech rate info
    1,  # Trim initial and final silences
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `fixdc.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
