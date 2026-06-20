# to_pitch_spinet

- Kind: `method`
- Available on: `Sound`
- Vocal Toolkit coverage: **Covered**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
import parselmouth

sound = parselmouth.Sound("voice.wav")
# Add required arguments according to the signature below.
result = sound.to_pitch_spinet()
print(result)
```

## Signature

```text
to_pitch_spinet(self: parselmouth.Sound, time_step: Positive[float] = 0.005, window_length: Positive[float] = 0.04, minimum_filter_frequency: Positive[float] = 70.0, maximum_filter_frequency: Positive[float] = 5000.0, number_of_filters: Positive[int] = 250, ceiling: Positive[float] = 500.0, max_number_of_candidates: Positive[int] = 15) -> parselmouth.Pitch
```

## Toolkit Comparison

Related to Extract pitch.

[Back to Parselmouth API index](../index.md)
