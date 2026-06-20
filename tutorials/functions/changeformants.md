# Change formants...

- Praat source: `changeformants.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Formant determination
- Set 5000 Hz for men, 5500 Hz for women or up to 8000 Hz for children.
- Formant or LPC processing.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `New F1 mean (Hz)` | `real` | `500.0` | `new_f1_mean` |
| `New F2 mean (Hz)` | `real` | `1500.0` | `new_f2_mean` |
| `New F3 mean (Hz)` | `real` | `2500.0` | `new_f3_mean` |
| `New F4 mean (Hz)` | `real` | `0 (= no change)` | `new_f4_mean` |
| `New F5 mean (Hz)` | `real` | `0 (= no change)` | `new_f5_mean` |
| `Maximum formant (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant` |
| `Process only voiced parts` | `boolean` | `1` | `process_only_voiced_parts` |
| `Retrieve intensity contour` | `boolean` | `1` | `retrieve_intensity_contour` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "changeformants.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 500.0, 1500.0, 2500.0, 0, 0, 5500, 1, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "changeformants.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    500.0,  # New F1 mean (Hz)
    1500.0,  # New F2 mean (Hz)
    2500.0,  # New F3 mean (Hz)
    0,  # New F4 mean (Hz)
    0,  # New F5 mean (Hz)
    5500,  # Maximum formant (Hz)
    1,  # Process only voiced parts
    1,  # Retrieve intensity contour
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Formant pages usually call `To Formant (robust)` or LPC commands. Parselmouth exposes Burg formants as `sound.to_formant_burg(...)`; for robust formants, LPC filtering, and `Formula (frequencies)`, use `praat.call`.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `copyintensitycontour.praat`, `copymix.praat`, `declip.praat`, `extractvowels.praat`, `preview1.inc`, `preview2.inc`, `voicedunvoiced.praat`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
