# Formants...

- Praat source: `copyformants.praat`
- Tutorial type: `copy`
- Selection model: two selected `Sound` objects

## What The Praat Script Does

- The mean F1-F5 frequencies will be shifted to match those of the first Sound.
- Formant determination
- Set 5000 Hz for men, 5500 Hz for women or up to 8000 Hz for children.
- Formant or LPC processing.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Maximum formant first Sound (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant_first_sound` |
| `Maximum formant second Sound (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant_second_sound` |
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
SCRIPT = os.path.join(TOOLKIT_DIR, "copyformants.praat")

source = parselmouth.Sound("source.wav")
target = parselmouth.Sound("target.wav")
result = praat.run_file([source, target], SCRIPT, 5500, 5500, 1, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "copyformants.praat",
    ["source.wav", "target.wav"],
    # Positional arguments follow the Praat form order.
    5500,  # Maximum formant first Sound (Hz)
    5500,  # Maximum formant second Sound (Hz)
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
- This script calls or includes: `copyintensitycontour.praat`, `copymix.praat`, `declip.praat`, `extractvowels.praat`, `preview.inc`, `voicedunvoiced.praat`, `workpost.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
