# to_harmonicity_ac

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
result = sound.to_harmonicity_ac()
print(result)
```

## Signature

```text
to_harmonicity_ac(self: parselmouth.Sound, time_step: Positive[float] = 0.01, minimum_pitch: Positive[float] = 75.0, silence_threshold: float = 0.1, periods_per_window: Positive[float] = 1.0) -> parselmouth.Harmonicity
```

## Toolkit Comparison

Related to breathiness/voice-quality analysis workflows.

[Back to Parselmouth API index](../index.md)
