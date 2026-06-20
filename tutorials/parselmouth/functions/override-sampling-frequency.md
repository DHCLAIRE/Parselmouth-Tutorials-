# override_sampling_frequency

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
result = sound.override_sampling_frequency()
print(result)
```

## Signature

```text
override_sampling_frequency(self: parselmouth.Sound, new_frequency: Positive[float]) -> None
```

## Toolkit Comparison

Covered by Change speed.

[Back to Parselmouth API index](../index.md)
