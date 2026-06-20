# Exciter...

- Praat source: `exciter.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `exciter.praat` from the Vocal Toolkit plugin.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `High pass frequency (Hz)` | `positive` | `2000` | `high_pass_frequency` |
| `Phase rotation` | `optionmenu` | `3; options: No change, +90º Hilbert transform, -90º Hilbert transform, 180º waveform inversion` | `phase_rotation` |
| `Type of distortion` | `optionmenu` | `6; options: Hard clipping, Soft clipping. Quintic, Soft clipping. Cubic, Soft clipping. Hyperbolic tangent, Soft clipping. Algebraic, Soft clipping. Arctangent` | `type_of_distortion` |
| `Input gain (dB)` | `real` | `0.0` | `input_gain` |
| `Positive amplitude limit (Pa)` | `real` | `1.0` | `positive_amplitude_limit` |
| `Negative amplitude limit (Pa)` | `real` | `-0.3` | `negative_amplitude_limit` |
| `Mix (dry/wet balance, 0-100 %)` | `real` | `50` | `mix` |
| `Scale result to original intensity` | `boolean` | `0` | `scale_result_to_original_intensity` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "exciter.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 2000, 3, 6, 0.0, 1.0, -0.3, 50, 0, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "exciter.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    2000,  # High pass frequency (Hz)
    3,  # Phase rotation
    6,  # Type of distortion
    0.0,  # Input gain (dB)
    1.0,  # Positive amplitude limit (Pa)
    -0.3,  # Negative amplitude limit (Pa)
    50,  # Mix (dry/wet balance, 0-100 %)
    0,  # Scale result to original intensity
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `butterworth.praat`, `declip.praat`, `distortion.praat`, `fixdc.praat`, `phaserotation.praat`, `preview1.inc`, `preview2.inc`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
