# Change vocal tract size, pitch and duration...

- Praat source: `changevtpitchduration.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `changevtpitchduration.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Formant or LPC processing.
- Filtering or spectrum processing.
- Manipulation and resynthesis.
- Mixing, convolution, or copying between sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Formant shift ratio` | `positive` | `1.0 (= no change)` | `formant_shift_ratio` |
| `New pitch median (Hz)` | `real` | `0.0 (= no change)` | `new_pitch_median` |
| `Pitch variation (%)` | `real` | `100 (= no change)` | `pitch_variation` |
| `New duration (s)` | `real` | `0.0 (= no change)` | `new_duration` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "changevtpitchduration.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 1.0, 0.0, 100, 0.0, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "changevtpitchduration.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    1.0,  # Formant shift ratio
    0.0,  # New pitch median (Hz)
    100,  # Pitch variation (%)
    0.0,  # New duration (s)
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Most pitch-changing scripts create a `Pitch` or `Manipulation` object. In Python, start with `sound.to_pitch(...)`, inspect `pitch.selected_array['frequency']`, and use `praat.call` when you need Praat commands that do not have a Python method.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `minmaxf0.praat`, `preview.inc`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
