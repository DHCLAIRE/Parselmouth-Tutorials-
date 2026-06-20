# Text to Speech...

- Praat source: `tts.praat`
- Tutorial type: `process`
- Selection model: one or more selected `Sound` objects

## What The Praat Script Does

- Runs the logic in `tts.praat` from the Vocal Toolkit plugin.
- Pitch analysis.
- Filtering or spectrum processing.
- Mixing, convolution, or copying between sounds.
- TextGrid or interval annotation.
- File or preset loading.

## Parameters

| Praat form field | Type | Default | Python argument |
| --- | --- | --- | --- |
| `Language` | `optionmenu` | `31; options: Afrikaans, Albanian, Amharic, Arabic, Aragonese, Armenian (East Armenia), Armenian (West Armenia), Assamese, ...` | `language` |
| `Voice` | `optionmenu` | `25; options: Adam, Alex, Alicia, Andrea, Andy, Anika, AnikaRobot, Annie, ...` | `voice` |
| `Sampling frequency (Hz)` | `positive` | `44100` | `sampling_frequency` |
| `Gap between words (s)` | `real` | `0.01` | `gap_between_words` |
| `Pitch multiplier (0.5-2.0)` | `real` | `1.0` | `pitch_multiplier` |
| `Pitch range multiplier (0-2.0)` | `real` | `1.0` | `pitch_range_multiplier` |
| `Words per minute (80-450)` | `real` | `175` | `words_per_minute` |
| `Create TextGrid with annotations` | `boolean` | `0` | `create_textgrid_with_annotations` |
| `Text` | `text` | `1 2 3 4 5` | `text` |
| `Preview (Apply. Uncheck to publish)` | `boolean` | `1` | `preview` |

## Parselmouth Tutorial

### Faithful Toolkit Call

This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.

```python
import os
import parselmouth
from parselmouth import praat

TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
SCRIPT = os.path.join(TOOLKIT_DIR, "tts.praat")

sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, SCRIPT, 31, 25, 44100, 0.01, 1.0, 1.0, 175, 0, '1 2 3 4 5', 1)

# Many Vocal Toolkit scripts leave the processed Sound selected.
# Depending on the script, `result` can be a Praat object, a list-like result, or text output.
print(result)
```

### Reusable Python Wrapper

```python
from src.vocal_toolkit_parselmouth import run_toolkit_script

result = run_toolkit_script(
    "tts.praat",
    "voice.wav",
    # Positional arguments follow the Praat form order.
    31,  # Language
    25,  # Voice
    44100,  # Sampling frequency (Hz)
    0.01,  # Gap between words (s)
    1.0,  # Pitch multiplier (0.5-2.0)
    1.0,  # Pitch range multiplier (0-2.0)
    175,  # Words per minute (80-450)
    0,  # Create TextGrid with annotations
    '1 2 3 4 5',  # Text
    1,  # Preview (Apply. Uncheck to publish)
)
```

## Translation Notes

- Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step.
- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.
- Boolean fields can be supplied as `1`/`0` or `True`/`False`.
- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.
- This script calls or includes: `declip.praat`, `ttspresetslist.inc`.

## Check Yourself

1. Run the faithful toolkit call on a short WAV file.
2. Save or inspect the returned object with `praat.call(result, "Save as WAV file...", "out.wav")` if the result is a `Sound`.
3. Compare the output against Praat's menu command using the same parameter values.

[Back to index](../index.md)
