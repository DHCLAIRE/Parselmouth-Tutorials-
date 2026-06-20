# to_harmonicity

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
result = sound.to_harmonicity()
print(result)
```

## Signature

```text
to_harmonicity(self: parselmouth.Sound, method: parselmouth.Sound.ToHarmonicityMethod = <ToHarmonicityMethod.CC: 0>, *args, **kwargs) -> object
```

## Toolkit Comparison

Related to breathiness/voice-quality analysis workflows.

[Back to Parselmouth API index](../index.md)
