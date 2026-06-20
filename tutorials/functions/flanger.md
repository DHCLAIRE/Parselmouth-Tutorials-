# Flanger...

- Praat source: `flanger.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `flanger.praat` from the Vocal Toolkit plugin.
- Intensity scaling or contour work.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- Batch processing over selected sounds.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Delay (0.10 to 20.0 ms)` | `real` | `2.50` | `delay` |
| `Rate (0.01 to 40.0 Hz)` | `real` | `0.20` | `rate` |
| `Depth (%)` | `real` | `70` | `depth` |
| `Waveform:` | `choice` | `1; options: Sine, Triangle` | `waveform` |
| `Feedback (-99 to 99 %)` | `real` | `50` | `feedback` |
| `High pass filter for delay signal` | `boolean` | `1` | `high_pass_filter_for_delay_signal` |
| `Delay cutoff frequency (Hz)` | `real` | `100` | `delay_cutoff_frequency` |
| `Stereo phase offset (180º)` | `boolean` | `1` | `stereo_phase_offset` |
| `Mix (%)` | `real` | `100` | `mix` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "flanger.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 2.50, 0.20, 70, 1, 50, 1, 100, 1, 100, 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "flanger.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    2.50,  # Delay (0.10 to 20.0 ms)
    0.20,  # Rate (0.01 to 40.0 Hz)
    70,  # Depth (%)
    1,  # Waveform:
    50,  # Feedback (-99 to 99 %)
    1,  # High pass filter for delay signal
    100,  # Delay cutoff frequency (Hz)
    1,  # Stereo phase offset (180º)
    100,  # Mix (%)
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `batch.praat`, `declip.praat`, `preview.inc`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
