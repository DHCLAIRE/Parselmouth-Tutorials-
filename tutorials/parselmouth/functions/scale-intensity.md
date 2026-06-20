# scale_intensity

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
result = sound.scale_intensity()
print(result)
```

## Signature

```text
scale_intensity(self: parselmouth.Sound, new_average_intensity: float) -> None
```

## Toolkit Comparison

Covered by intensity and effect scripts.

[Back to Parselmouth API index](../index.md)
