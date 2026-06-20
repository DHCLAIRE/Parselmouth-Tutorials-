# Extracting F0, F1, And F2 For Mandarin And Taiwanese

This tutorial shows a practical Parselmouth workflow for extracting pitch
(`F0`) and the first two formants (`F1`, `F2`) from Mandarin and Taiwanese
speech recordings. The same code works for either language; the important
choices are where you measure, how you set pitch and formant parameters, and
how you label the intervals in a TextGrid.

## Why This Needs Care

Mandarin and Taiwanese are tonal languages, so `F0` is not just a speaker
property. It carries lexical tone and often changes across the syllable. For
vowels, `F1` and `F2` are most stable near the vowel nucleus, but `F0` often
needs a contour across the rime or vowel interval.

Use this rule of thumb:

- Extract `F1` and `F2` at the vowel midpoint, or average across the central
  40 percent of the vowel.
- Extract `F0` as a contour at several normalized time points.
- Do not include silent intervals, unvoiced consonants, final stop closures,
  or long aspiration in the measurement interval.

For Mandarin, vowel or rime intervals are usually enough. For Taiwanese, be
especially careful with checked syllables, because final stops make the voiced
part short and can pull measurements toward silence or closure.

## Install

```bash
python -m pip install praat-parselmouth numpy pandas
```

## Minimal Single-Interval Example

This example extracts `F0`, `F1`, and `F2` at the midpoint of a manually chosen
interval.

```python
import math
import parselmouth
from parselmouth import praat


sound = parselmouth.Sound("speaker01_mandarin.wav").convert_to_mono()

# Adjust these to the speaker. See the settings section below.
pitch = sound.to_pitch(time_step=0.005, pitch_floor=75, pitch_ceiling=500)
formants = sound.to_formant_burg(
    time_step=0.005,
    max_number_of_formants=5,
    maximum_formant=5500,
    window_length=0.025,
    pre_emphasis_from=50,
)

start = 1.240
end = 1.410
mid = start + (end - start) / 2

f0 = praat.call(pitch, "Get value at time", mid, "Hertz", "Linear")
f1 = praat.call(formants, "Get value at time", 1, mid, "Hertz", "Linear")
f2 = praat.call(formants, "Get value at time", 2, mid, "Hertz", "Linear")

print({
    "time": mid,
    "f0_hz": None if math.isnan(f0) else f0,
    "f1_hz": None if math.isnan(f1) else f1,
    "f2_hz": None if math.isnan(f2) else f2,
})
```

## TextGrid Layout

The batch script below expects one interval tier with the vowel, rime, or
syllable intervals you want to measure.

Recommended tiers:

- `vowels`: labels such as `a`, `i`, `u`, `e`, `o`, `er`.
- `rimes`: labels such as `ang_T1`, `ian_T2`, `ai_T3`.
- `syllables`: labels such as `ma1`, `mai5`, `tsit4`.

Use a separate metadata file if you need richer information such as language,
speaker, tone category, lexical item, or romanization. Do not hide too much in
one interval label if you will analyze the data later.

## Batch Extraction From WAV And TextGrid

Save this as `extract_f0_f1_f2.py` and put each `.wav` beside a matching
`.TextGrid` with the same stem, for example:

```text
data/
  speaker01_mandarin.wav
  speaker01_mandarin.TextGrid
  speaker02_taiwanese.wav
  speaker02_taiwanese.TextGrid
```

```python
from pathlib import Path
import math

import numpy as np
import pandas as pd
import parselmouth
from parselmouth import praat


SKIP_LABELS = {"", "sil", "sp", "pau", "pause", "noise"}


def clean_number(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(value) else value


def get_tier_number(textgrid, tier_name):
    tier_number = int(praat.call(textgrid, "Get tier number", tier_name))
    if tier_number == 0:
        raise ValueError(f"TextGrid has no tier named {tier_name!r}")
    return tier_number


def iter_intervals(textgrid, tier_name):
    tier_number = get_tier_number(textgrid, tier_name)
    n_intervals = int(praat.call(textgrid, "Get number of intervals", tier_number))

    for i in range(1, n_intervals + 1):
        start = float(praat.call(textgrid, "Get start time of interval", tier_number, i))
        end = float(praat.call(textgrid, "Get end time of interval", tier_number, i))
        label = str(praat.call(textgrid, "Get label of interval", tier_number, i)).strip()
        yield i, start, end, label


def value_at_time(praat_object, command, *args):
    value = praat.call(praat_object, command, *args)
    return clean_number(value)


def extract_file(
    wav_path,
    textgrid_path,
    tier_name="vowels",
    language=None,
    speaker=None,
    pitch_floor=75,
    pitch_ceiling=500,
    maximum_formant=5500,
    contour_points=11,
):
    sound = parselmouth.Sound(str(wav_path)).convert_to_mono()
    textgrid = parselmouth.Data.read(str(textgrid_path))

    pitch = sound.to_pitch(
        time_step=0.005,
        pitch_floor=pitch_floor,
        pitch_ceiling=pitch_ceiling,
    )
    formants = sound.to_formant_burg(
        time_step=0.005,
        max_number_of_formants=5,
        maximum_formant=maximum_formant,
        window_length=0.025,
        pre_emphasis_from=50,
    )

    token_rows = []
    contour_rows = []

    for interval_number, start, end, label in iter_intervals(textgrid, tier_name):
        if label.lower() in SKIP_LABELS:
            continue

        duration = end - start
        if duration <= 0.03:
            continue

        mid = start + duration / 2
        f1_mid = value_at_time(formants, "Get value at time", 1, mid, "Hertz", "Linear")
        f2_mid = value_at_time(formants, "Get value at time", 2, mid, "Hertz", "Linear")
        f0_mid = value_at_time(pitch, "Get value at time", mid, "Hertz", "Linear")

        token_rows.append({
            "file": wav_path.name,
            "speaker": speaker,
            "language": language,
            "tier": tier_name,
            "interval_number": interval_number,
            "label": label,
            "start_s": start,
            "end_s": end,
            "duration_s": duration,
            "mid_s": mid,
            "f0_mid_hz": f0_mid,
            "f1_mid_hz": f1_mid,
            "f2_mid_hz": f2_mid,
        })

        for point_index, proportion in enumerate(np.linspace(0.1, 0.9, contour_points), 1):
            time = start + proportion * duration
            contour_rows.append({
                "file": wav_path.name,
                "speaker": speaker,
                "language": language,
                "tier": tier_name,
                "interval_number": interval_number,
                "label": label,
                "point_index": point_index,
                "proportion": float(proportion),
                "time_s": time,
                "f0_hz": value_at_time(pitch, "Get value at time", time, "Hertz", "Linear"),
                "f1_hz": value_at_time(formants, "Get value at time", 1, time, "Hertz", "Linear"),
                "f2_hz": value_at_time(formants, "Get value at time", 2, time, "Hertz", "Linear"),
            })

    return token_rows, contour_rows


def main():
    data_dir = Path("data")
    all_tokens = []
    all_contours = []

    for wav_path in sorted(data_dir.glob("*.wav")):
        textgrid_path = wav_path.with_suffix(".TextGrid")
        if not textgrid_path.exists():
            print(f"Skipping {wav_path.name}: no matching TextGrid")
            continue

        stem = wav_path.stem.lower()
        language = "Taiwanese" if "taiwanese" in stem else "Mandarin"

        tokens, contours = extract_file(
            wav_path,
            textgrid_path,
            tier_name="vowels",
            language=language,
            speaker=wav_path.stem.split("_")[0],
            pitch_floor=75,
            pitch_ceiling=500,
            maximum_formant=5500,
        )
        all_tokens.extend(tokens)
        all_contours.extend(contours)

    pd.DataFrame(all_tokens).to_csv("mandarin_taiwanese_f0_f1_f2_tokens.csv", index=False)
    pd.DataFrame(all_contours).to_csv("mandarin_taiwanese_f0_f1_f2_contours.csv", index=False)


if __name__ == "__main__":
    main()
```

Run it with:

```bash
python extract_f0_f1_f2.py
```

The script writes two CSV files:

- `mandarin_taiwanese_f0_f1_f2_tokens.csv`: one row per interval, with midpoint
  `F0`, `F1`, and `F2`.
- `mandarin_taiwanese_f0_f1_f2_contours.csv`: multiple normalized time points
  per interval, useful for tone contours.

## Speaker And Language Settings

Start with these values, then inspect the tracks in Praat or plot the output.

| Speaker/recording type | Pitch floor | Pitch ceiling | Maximum formant |
| --- | ---: | ---: | ---: |
| Low adult voice | `50` Hz | `300` Hz | `5000` Hz |
| Typical adult voice | `75` Hz | `500` Hz | `5500` Hz |
| High adult voice or child voice | `100` Hz | `700` Hz | `6000` Hz |

Use a higher pitch ceiling when high tones are being halved. Use a lower pitch
floor when low tones are being missed. If `F1` and `F2` jump wildly, adjust
`maximum_formant` and check whether the interval includes consonant transitions
or final closure.

## Mandarin Notes

- For tone work, measure `F0` over the voiced rime, not over the whole word if
  there is a long voiceless onset.
- For third tones, avoid treating the midpoint as the whole tone. Use contour
  values and model the shape.
- For neutral tone, keep the tone label separate from the vowel label so it can
  be analyzed separately.

## Taiwanese Notes

- Checked syllables can be short. Keep the interval over the voiced vowel or
  rime, not the final stop closure.
- If your labels include citation tone and surface tone, store both in metadata.
  Tone sandhi can make the surface `F0` contour differ from the citation label.
- Creaky or irregular phonation can create missing or unstable `F0` values.
  Keep those missing values visible instead of replacing them with zeros.

## Check Yourself

1. Open one WAV and TextGrid in Praat.
2. Compare the script's midpoint times with the visible interval midpoints.
3. Plot `f0_hz` by `proportion` for each tone label.
4. Plot `F1` by `F2` for vowels and look for obvious tracking errors.
5. Re-run with speaker-specific `pitch_floor`, `pitch_ceiling`, and
   `maximum_formant` values if the tracks look wrong.

## Related Parselmouth Pages

- [Parselmouth patterns](parselmouth-patterns.md)
- [Sound.to_pitch](parselmouth/functions/to-pitch.md)
- [Sound.to_formant_burg](parselmouth/functions/to-formant-burg.md)
- [Pitch.get_value_at_time](parselmouth/functions/get-value-at-time.md)
- [Formant.get_value_at_time](parselmouth/functions/get-value-at-time.md)
