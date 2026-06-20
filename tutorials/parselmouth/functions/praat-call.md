# praat.call

- Kind: `function`
- Available on: `parselmouth.praat`
- Vocal Toolkit coverage: **Covered**

## What It Does

Call a Praat command.

## Tutorial Pattern

```python
import parselmouth
from parselmouth import praat

sound = parselmouth.Sound("voice.wav")
pitch = praat.call(sound, "To Pitch", 0.01, 75, 600)
median_f0 = praat.call(pitch, "Get quantile", 0, 0, 0.5, "Hertz")
```

## Signature

```text
call(command: str, *args, **kwargs) -> object \ call(object: parselmouth.Data, command: str, *args, **kwargs) -> object \ call(objects: List[parselmouth.Data], command: str, *args, **kwargs) -> object
```

## Toolkit Comparison

All faithful Vocal Toolkit wrappers use this when calling individual Praat commands.

[Back to Parselmouth API index](../index.md)
