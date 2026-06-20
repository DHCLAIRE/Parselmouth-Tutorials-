# to_pitch_ac

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
result = sound.to_pitch_ac()
print(result)
```

## Signature

```text
to_pitch_ac(self: parselmouth.Sound, time_step: Optional[Positive[float]] = None, pitch_floor: Positive[float] = 75.0, max_number_of_candidates: Positive[int] = 15, very_accurate: bool = False, silence_threshold: float = 0.03, voicing_threshold: float = 0.45, octave_cost: float = 0.01, octave_jump_cost: float = 0.35, voiced_unvoiced_cost: float = 0.14, pitch_ceiling: Positive[float] = 600.0) -> parselmouth.Pitch
```

## Toolkit Comparison

Related to Extract pitch.

[Back to Parselmouth API index](../index.md)
