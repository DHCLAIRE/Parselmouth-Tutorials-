# to_mfcc

- Kind: `method`
- Available on: `Sound`
- Vocal Toolkit coverage: **Not in Vocal Toolkit**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
import parselmouth

sound = parselmouth.Sound("voice.wav")
# Add required arguments according to the signature below.
result = sound.to_mfcc()
print(result)
```

## Signature

```text
to_mfcc(self: parselmouth.Sound, number_of_coefficients: Positive[int] = 12, window_length: Positive[float] = 0.015, time_step: Positive[float] = 0.005, firstFilterFreqency: Positive[float] = 100.0, distance_between_filters: Positive[float] = 100.0, maximum_frequency: Optional[Positive[float]] = None) -> parselmouth.MFCC
```

## Toolkit Comparison

No matching Vocal Toolkit command or script keyword was found.

[Back to Parselmouth API index](../index.md)
