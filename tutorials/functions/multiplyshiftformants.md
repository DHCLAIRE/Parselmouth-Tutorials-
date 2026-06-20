# Multiply or shift formants...

- Praat source: `multiplyshiftformants.praat`
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
| `Method` | `choice` | `1; options: Multiply (factor), Shift (add Hz)` | `method` |
| `Multiply or shift F1 by` | `real` | `1.1` | `multiply_or_shift_f1_by` |
| `Multiply or shift F2 by` | `real` | `1.1` | `multiply_or_shift_f2_by` |
| `Multiply or shift F3 by` | `real` | `1.1` | `multiply_or_shift_f3_by` |
| `Multiply or shift F4 by` | `real` | `1` | `multiply_or_shift_f4_by` |
| `Multiply or shift F5 by` | `real` | `1` | `multiply_or_shift_f5_by` |
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
SCRIPT = os.path.join(TOOLKIT_DIR, "multiplyshiftformants.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 1, 1.1, 1.1, 1.1, 1, 1, 5500, 1, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "multiplyshiftformants.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    1,  # Method
    1.1,  # Multiply or shift F1 by
    1.1,  # Multiply or shift F2 by
    1.1,  # Multiply or shift F3 by
    1,  # Multiply or shift F4 by
    1,  # Multiply or shift F5 by
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
- This script calls or includes: `batch.praat`, `copyintensitycontour.praat`, `copymix.praat`, `declip.praat`, `preview1.inc`, `preview2.inc`, `voicedunvoiced.praat`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
