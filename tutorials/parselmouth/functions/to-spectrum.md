# to_spectrum

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
result = sound.to_spectrum()
print(result)
```

## Signature

```text
to_spectrum(self: parselmouth.Sound, fast: bool = True) -> parselmouth.Spectrum
```

## Toolkit Comparison

Related to EQ, filtering, and spectral processing.

[Back to Parselmouth API index](../index.md)
