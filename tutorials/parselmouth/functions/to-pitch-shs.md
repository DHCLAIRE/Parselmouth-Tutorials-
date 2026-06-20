# to_pitch_shs

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
result = sound.to_pitch_shs()
print(result)
```

## Signature

```text
to_pitch_shs(self: parselmouth.Sound, time_step: Positive[float] = 0.01, minimum_pitch: Positive[float] = 50.0, max_number_of_candidates: Positive[int] = 15, maximum_frequency_component: Positive[float] = 1250.0, max_number_of_subharmonics: Positive[int] = 15, compression_factor: Positive[float] = 0.84, ceiling: Positive[float] = 600.0, number_of_points_per_octave: Positive[int] = 48) -> parselmouth.Pitch
```

## Toolkit Comparison

Related to Extract pitch.

[Back to Parselmouth API index](../index.md)
