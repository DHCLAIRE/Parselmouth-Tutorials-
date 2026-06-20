# to_harmonicity_gne

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
result = sound.to_harmonicity_gne()
print(result)
```

## Signature

```text
to_harmonicity_gne(self: parselmouth.Sound, minimum_frequency: Positive[float] = 500.0, maximum_frequency: Positive[float] = 4500.0, bandwidth: Positive[float] = 1000.0, step: Positive[float] = 80.0) -> parselmouth.Matrix
```

## Toolkit Comparison

Related to breathiness/voice-quality analysis workflows.

[Back to Parselmouth API index](../index.md)
