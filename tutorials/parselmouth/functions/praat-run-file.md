# praat.run_file

- Kind: `function`
- Available on: `parselmouth.praat`
- Vocal Toolkit coverage: **Covered**

## What It Does

Run a Praat script from file.

## Tutorial Pattern

```python
import os
import parselmouth
from parselmouth import praat

sound = parselmouth.Sound("voice.wav")
script = os.path.join(os.environ["VOCAL_TOOLKIT_DIR"], "normalize.praat")
result = praat.run_file(sound, script)
```

## Signature

```text
run_file(path: str, *args, **kwargs) -> object \ run_file(object: parselmouth.Data, path: str, *args, **kwargs) -> object \ run_file(objects: List[parselmouth.Data], path: str, *args, **kwargs) -> object
```

## Toolkit Comparison

All generated Vocal Toolkit extension wrappers use this to run the original scripts.

[Back to Parselmouth API index](../index.md)
