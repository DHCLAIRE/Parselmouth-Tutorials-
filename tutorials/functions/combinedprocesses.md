# Combined processes...

- Praat source: `combinedprocesses.praat`
- Tutorial type: `copy`
- Selection model: two selected `Sound` objects

## What The Praat Script Does

- Characteristics to be copied from the first to the second selected Sound:
- Modification parameters (non-default values override the above):
- General settings:
- Vocal tract length estimation
- Pitch analysis.
- Formant or LPC processing.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Manipulation and resynthesis.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Vocal tract size` | `boolean` | `0` | `vocal_tract_size` |
| `Pitch` | `optionmenu` | `1; options: -- None --, Contour, Median, Variation, Median and variation` | `pitch` |
| `Time` | `optionmenu` | `1; options: -- None --, Dynamic time warping (DTW), Duration (stretch)` | `time` |
| `EQ curve` | `boolean` | `0` | `eq_curve` |
| `Formant shift ratio` | `positive` | `1.0 (= no change)` | `formant_shift_ratio` |
| `New pitch median (Hz)` | `real` | `0.0 (= no change)` | `new_pitch_median` |
| `Pitch variation (%)` | `real` | `100 (= no change)` | `pitch_variation` |
| `Duration factor` | `positive` | `1.0 (= no change)` | `duration_factor` |
| `Trim initial and final silences first` | `boolean` | `0` | `trim_initial_and_final_silences_first` |
| `DTW slope constraint` | `optionmenu` | `3; options: no restriction, 1/3 < slope < 3, 1/2 < slope < 2, 2/3 < slope < 3/2` | `dtw_slope_constraint` |
| `Calculate from formant` | `positive` | `4` | `calculate_from_formant` |
| `Maximum formant first Sound (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant_first_sound` |
| `Maximum formant second Sound (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant_second_sound` |
| `Show info` | `boolean` | `1` | `show_info` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "combinedprocesses.praat")

source = parselmouth.Sound("source.wav")
target = parselmouth.Sound("target.wav")
result = praat.run_file([source, target], SCRIPT, 0, 1, 1, 0, 1.0, 0.0, 100, 1.0, 0, 3, 4, 5500, 5500, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "combinedprocesses.praat",
    ["source.wav", "target.wav"],
    # Positional arguments follow the Praat form order.
    0,  # Vocal tract size
    1,  # Pitch
    1,  # Time
    0,  # EQ curve
    1.0,  # Formant shift ratio
    0.0,  # New pitch median (Hz)
    100,  # Pitch variation (%)
    1.0,  # Duration factor
    0,  # Trim initial and final silences first
    3,  # DTW slope constraint
    4,  # Calculate from formant
    5500,  # Maximum formant first Sound (Hz)
    5500,  # Maximum formant second Sound (Hz)
    1,  # Show info
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `copyeq.praat`, `extractvowels.praat`, `minmaxf0.praat`, `preview.inc`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
