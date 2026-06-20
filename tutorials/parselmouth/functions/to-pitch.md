# to_pitch

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
result = sound.to_pitch()
print(result)
```

## Signature

```text
to_pitch(self: parselmouth.Sound, time_step: Optional[Positive[float]] = None, pitch_floor: Positive[float] = 75.0, pitch_ceiling: Positive[float] = 600.0) -> parselmouth.Pitch \ to_pitch(self: parselmouth.Sound, method: parselmouth.Sound.ToPitchMethod, *args, **kwargs) -> object
```

## Toolkit Comparison

Covered by Extract pitch and pitch-changing scripts.

[Back to Parselmouth API index](../index.md)
