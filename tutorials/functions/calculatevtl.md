# Calculate vocal tract length...

- Praat source: `calculatevtl.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Displays in the Info window the estimated vocal tract length in the
- neutral configuration, calculated from a formant frequency value.
- Formant determination
- Set 5000 Hz for men, 5500 Hz for women or up to 8000 Hz for children.
- Formant or LPC processing.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Formant frequency (Hz)` | `positive` | `3500` | `formant_frequency` |
| `Formant number` | `natural` | `4` | `formant_number` |
| `Calculate from the selected Sounds` | `boolean` | `1` | `calculate_from_the_selected_sounds` |
| `Maximum formant (Hz)` | `positive` | `5500 (= adult female)` | `maximum_formant` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "calculatevtl.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 3500, 4, 1, 5500)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "calculatevtl.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    3500,  # Formant frequency (Hz)
    4,  # Formant number
    1,  # Calculate from the selected Sounds
    5500,  # Maximum formant (Hz)
)
```

### Direct Parselmouth Version

For this command, a compact direct version is practical without running the plugin script.

```python
from math import isnan

import parselmouth
from parselmouth import praat


def estimate_vocal_tract_length(sound_path, formant_number=4, maximum_formant=5500):
    sound = parselmouth.Sound(sound_path)
    formants = sound.to_formant_burg(
        time_step=0.005,
        max_number_of_formants=5,
        maximum_formant=maximum_formant,
        window_length=0.025,
        pre_emphasis_from=50,
    )
    formant_frequency = praat.call(formants, "Get mean", formant_number, 0, 0, "Hertz")
    if isnan(formant_frequency):
        raise ValueError("The selected formant could not be measured.")
    return 35000 * ((formant_number / 2) - 0.25) / formant_frequency


vtl_cm = estimate_vocal_tract_length("voice.wav")
print(f"Estimated vocal tract length: {vtl_cm:.2f} cm")
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `extractvowels.praat`, `workpre.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
