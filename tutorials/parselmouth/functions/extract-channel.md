# extract_channel

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
result = sound.extract_channel()
print(result)
```

## Signature

```text
extract_channel(self: parselmouth.Sound, channel: int) -> parselmouth.Sound \ extract_channel(self: parselmouth.Sound, arg0: str) -> parselmouth.Sound
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
