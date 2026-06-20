# Change duration...

- Praat source: `changeduration.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `changeduration.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Manipulation and resynthesis.
- Mixing, convolution, or copying between sounds.
- TextGrid or interval annotation.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `New duration (s)` | `positive` | `3.0` | `new_duration` |
| `Method` | `choice` | `1; options: Stretch, Cut or add time, Change speed` | `method` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "changeduration.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 3.0, 1, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "changeduration.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    3.0,  # New duration (s)
    1,  # Method
    1,  # Preview (Apply. Uncheck to publish)
)
```

### Direct Parselmouth Version

For this command, a compact direct version is practical without running the plugin script.

```python
import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
longer = sound.lengthen(minimum_pitch=75, maximum_pitch=600, factor=1.25)
longer.save("voice-duration-x1.25.wav", SoundFileFormat.WAV)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `changespeed.praat`, `fixdc.praat`, `minmaxf0.praat`, `preview.inc`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
