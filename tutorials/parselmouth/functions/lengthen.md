# lengthen

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
result = sound.lengthen()
print(result)
```

## Signature

```text
lengthen(self: parselmouth.Sound, minimum_pitch: Positive[float] = 75.0, maximum_pitch: Positive[float] = 600.0, factor: Positive[float]) -> parselmouth.Sound
```

## Toolkit Comparison

Covered by Change duration.

[Back to Parselmouth API index](../index.md)
