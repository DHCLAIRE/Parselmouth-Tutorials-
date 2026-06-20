# autocorrelate

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
result = sound.autocorrelate()
print(result)
```

## Signature

```text
autocorrelate(self: parselmouth.Sound, scaling: parselmouth.AmplitudeScaling = <AmplitudeScaling.PEAK_0_99: 4>, signal_outside_time_domain: parselmouth.SignalOutsideTimeDomain = <SignalOutsideTimeDomain.ZERO: 1>) -> parselmouth.Sound
```

## Toolkit Comparison

No matching Vocal Toolkit command or script keyword was found.

[Back to Parselmouth API index](../index.md)
