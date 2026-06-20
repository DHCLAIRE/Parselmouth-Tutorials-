# Fix DC offset (in-place)

- Praat source: `fixdc.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `fixdc.praat` from the Vocal Toolkit plugin.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Batch processing over selected sounds.

## Parameters

This script has no interactive Praat form. Call it with the selected sound object(s), or use the direct equivalent when one is shown below.

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "fixdc.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script("fixdc.praat", "voice.wav")
```

### Direct Parselmouth Version

For this command, a compact direct version is practical without running the plugin script.

```python
import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
fixed = sound.copy()
fixed.values[:] = fixed.values - fixed.values.mean(axis=1, keepdims=True)
fixed.save("voice-fixdc.wav", SoundFileFormat.WAV)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `declip.praat`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
