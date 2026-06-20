# to_intensity

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
result = sound.to_intensity()
print(result)
```

## Signature

```text
to_intensity(self: parselmouth.Sound, minimum_pitch: Positive[float] = 100.0, time_step: Optional[Positive[float]] = None, subtract_mean: bool = True) -> parselmouth.Intensity
```

## Toolkit Comparison

Covered by intensity contour and mixing scripts.

[Back to Parselmouth API index](../index.md)
