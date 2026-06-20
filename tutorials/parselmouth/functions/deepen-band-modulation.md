# deepen_band_modulation

- Kind: `method`
- Available on: `Sound`
- Vocal Toolkit coverage: **Related**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
import parselmouth

sound = parselmouth.Sound("voice.wav")
# Add required arguments according to the signature below.
result = sound.deepen_band_modulation()
print(result)
```

## Signature

```text
deepen_band_modulation(self: parselmouth.Sound, enhancement: Positive[float] = 20.0, from_frequency: Positive[float] = 300.0, to_frequency: Positive[float] = 8000.0, slow_modulation: Positive[float] = 3.0, fast_modulation: Positive[float] = 30.0, band_smoothing: Positive[float] = 100.0) -> parselmouth.Sound
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
