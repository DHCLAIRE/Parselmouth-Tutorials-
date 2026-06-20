# set_to_zero

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
result = sound.set_to_zero()
print(result)
```

## Signature

```text
set_to_zero(self: parselmouth.Sound, from_time: Optional[float] = None, to_time: Optional[float] = None, round_to_nearest_zero_crossing: bool = True) -> None
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
