# extract_part_for_overlap

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
result = sound.extract_part_for_overlap()
print(result)
```

## Signature

```text
extract_part_for_overlap(self: parselmouth.Sound, from_time: Optional[float] = None, to_time: Optional[float] = None, overlap: Positive[float]) -> parselmouth.Sound
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
