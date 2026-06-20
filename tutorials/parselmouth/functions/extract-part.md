# extract_part

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
result = sound.extract_part()
print(result)
```

## Signature

```text
extract_part(self: parselmouth.Sound, from_time: Optional[float] = None, to_time: Optional[float] = None, window_shape: parselmouth.WindowShape = <WindowShape.RECTANGULAR: 0>, relative_width: Positive[float] = 1.0, preserve_times: bool = False) -> parselmouth.Sound
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
