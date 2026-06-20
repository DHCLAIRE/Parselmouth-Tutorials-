# resample

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
result = sound.resample()
print(result)
```

## Signature

```text
resample(self: parselmouth.Sound, new_frequency: float, precision: int = 50) -> parselmouth.Sound
```

## Toolkit Comparison

Covered by Change speed and several preset scripts.

[Back to Parselmouth API index](../index.md)
