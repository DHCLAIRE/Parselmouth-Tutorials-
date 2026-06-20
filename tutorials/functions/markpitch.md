# Mark regions by pitch

- Praat source: `markpitch.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `markpitch.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- TextGrid or interval annotation.

## Parameters

This script has no interactive Praat form. Call it with the selected sound object(s), or use the direct equivalent when one is shown below.

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "markpitch.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script("markpitch.praat", "voice.wav")
```

## Translation Notes

- Most pitch-changing scripts create a `Pitch` or `Manipulation` object. In Python, start with `sound.to_pitch(...)`, inspect `pitch.selected_array['frequency']`, and use `praat.call` when you need Praat commands that do not have a Python method.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `fixdc.praat`, `minmaxf0.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
