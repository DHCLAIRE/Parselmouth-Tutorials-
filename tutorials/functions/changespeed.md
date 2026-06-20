# Change speed...

- Praat source: `changespeed.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Speeds up or slows down the selected Sounds, affecting duration and pitch.
- “Frame rate conversion” can be used to convert the audio track of a video
- Pitch analysis.
- Filtering or spectrum processing.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Change by` | `choice` | `1; options: Factor, New duration, Semitones, Frame rate conversion (video fps)` | `change_by` |
| `Factor` | `positive` | `0.5` | `factor` |
| `New duration (s)` | `positive` | `2` | `new_duration` |
| `Semitones (-24 to +24)` | `real` | `-1` | `semitones` |
| `Original frame rate (fps)` | `positive` | `25 (= PAL)` | `original_frame_rate` |
| `New frame rate (fps)` | `positive` | `23.976 (= NTSC)` | `new_frame_rate` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "changespeed.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 1, 0.5, 2, -1, 25, 23.976, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "changespeed.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    1,  # Change by
    0.5,  # Factor
    2,  # New duration (s)
    -1,  # Semitones (-24 to +24)
    25,  # Original frame rate (fps)
    23.976,  # New frame rate (fps)
    1,  # Preview (Apply. Uncheck to publish)
)
```

### Direct Parselmouth Version

For this command, a compact direct version is practical without running the plugin script.

```python
import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
faster = sound.resample(sound.sampling_frequency * 1.25)
faster.override_sampling_frequency(sound.sampling_frequency)
faster.save("voice-speed-x1.25.wav", SoundFileFormat.WAV)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `preview.inc`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
