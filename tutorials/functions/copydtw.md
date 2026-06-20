# Dynamic time warping (DTW)...

- Praat source: `copydtw.praat`
- Tutorial type: `copy`
- Selection model: two selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `copydtw.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Manipulation and resynthesis.
- Mixing, convolution, or copying between sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Slope constraint` | `choice` | `3; options: no restriction, 1/3 < slope < 3, 1/2 < slope < 2, 2/3 < slope < 3/2` | `slope_constraint` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "copydtw.praat")

source = parselmouth.Sound("source.wav")
target = parselmouth.Sound("target.wav")
result = praat.run_file([source, target], SCRIPT, 3, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "copydtw.praat",
    ["source.wav", "target.wav"],
    # Positional arguments follow the Praat form order.
    3,  # Slope constraint
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `declip.praat`, `minmaxf0.praat`, `preview.inc`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
