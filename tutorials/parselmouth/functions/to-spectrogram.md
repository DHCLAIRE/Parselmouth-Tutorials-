# to_spectrogram

- Kind: `method`
- Available on: `Sound`, `Spectrum`
- Vocal Toolkit coverage: **Covered**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
import parselmouth

sound = parselmouth.Sound("voice.wav")
# Add required arguments according to the signature below.
result = sound.to_spectrogram()
print(result)
```

## Signature

```text
to_spectrogram(self: parselmouth.Sound, window_length: Positive[float] = 0.005, maximum_frequency: Positive[float] = 5000.0, time_step: Positive[float] = 0.002, frequency_step: Positive[float] = 20.0, window_shape: parselmouth.SpectralAnalysisWindowShape = <SpectralAnalysisWindowShape.GAUSSIAN: 5>) -> parselmouth.Spectrogram
```

## Toolkit Comparison

Related to EQ, filtering, and spectral processing.

[Back to Parselmouth API index](../index.md)
