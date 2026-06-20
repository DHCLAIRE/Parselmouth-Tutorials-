# Calculate formants of a vocal tract...

- Praat source: `calculateformantsvt.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Displays in the Info window the average formant values of a vocal tract
- in the neutral configuration, calculated from the entered length value.
- Formant or LPC processing.
- Filtering or spectrum processing.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Vocal tract length (cm)` | `positive` | `17.5` | `vocal_tract_length` |
| `Number of formants` | `natural` | `5` | `number_of_formants` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "calculateformantsvt.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 17.5, 5)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "calculateformantsvt.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    17.5,  # Vocal tract length (cm)
    5,  # Number of formants
)
```

## Translation Notes

- Formant pages usually call `To Formant (robust)` or LPC commands. Parselmouth exposes Burg formants as `sound.to_formant_burg(...)`; for robust formants, LPC filtering, and `Formula (frequencies)`, use `praat.call`.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
