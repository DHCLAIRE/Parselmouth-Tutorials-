# Create vowel...

- Praat source: `createvowel.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `createvowel.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Formant or LPC processing.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- TextGrid or interval annotation.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Duration (s)` | `positive` | `0.8` | `duration` |
| `left F0 range (Hz)` | `positive` | `150` | `left_f0_range` |
| `right F0 range (Hz)` | `positive` | `100` | `right_f0_range` |
| `F1 (Hz)` | `real` | `500` | `f1` |
| `F2 (Hz)` | `real` | `1500` | `f2` |
| `F3 (Hz)` | `real` | `2500` | `f3` |
| `F4 (Hz)` | `real` | `3500` | `f4` |
| `Preset vowel (Peterson & Barney 1952)` | `boolean` | `1` | `preset_vowel` |
| `Speaker` | `optionmenu` | `1; options: Man, Woman, Child` | `speaker` |
| `Vowel` | `optionmenu` | `1; options: i	iy	“heed”, ɪ	ih	“hid”, ɛ	eh	“head”, æ	ae	“had”, ɑ	aa	“hod”, ɔ	ao	“hawed”, ʊ	uh	“hood”, u	uw	“who’d”, ...` | `vowel` |
| `Synthesis method` | `choice` | `1; options: VowelEditor (4 formants), Flatter spectrum (extra formants added)` | `synthesis_method` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "createvowel.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 0.8, 150, 100, 500, 1500, 2500, 3500, 1, 1, 1, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "createvowel.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    0.8,  # Duration (s)
    150,  # left F0 range (Hz)
    100,  # right F0 range (Hz)
    500,  # F1 (Hz)
    1500,  # F2 (Hz)
    2500,  # F3 (Hz)
    3500,  # F4 (Hz)
    1,  # Preset vowel (Peterson & Barney 1952)
    1,  # Speaker
    1,  # Vowel
    1,  # Synthesis method
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
