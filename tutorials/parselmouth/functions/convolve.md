# convolve

- Kind: `method`
- Available on: `MFCC`, `Sound`
- Vocal Toolkit coverage: **Covered**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
# Replace `obj` with an instance of MFCC.
# Add required arguments according to the signature below.
result = obj.convolve()
print(result)
```

## Signature

```text
convolve(self: parselmouth.MFCC, other: parselmouth.MFCC, scaling: parselmouth.AmplitudeScaling = <AmplitudeScaling.PEAK_0_99: 4>, signal_outside_time_domain: parselmouth.SignalOutsideTimeDomain = <SignalOutsideTimeDomain.ZERO: 1>) -> parselmouth.Sound
```

## Toolkit Comparison

Covered by Reverb.

[Back to Parselmouth API index](../index.md)
