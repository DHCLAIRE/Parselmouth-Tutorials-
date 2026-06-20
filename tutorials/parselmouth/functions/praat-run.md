# praat.run

- Kind: `function`
- Available on: `parselmouth.praat`
- Vocal Toolkit coverage: **Not in Vocal Toolkit**

## What It Does

Run a Praat script.

## Tutorial Pattern

```python
from parselmouth import praat

script = "Create Sound from formula: \"tone\", 1, 0, 0.25, 44100, \"0.2*sin(2*pi*220*x)\""
result = praat.run(script)
```

## Signature

```text
run(script: str, *args, **kwargs) -> object \ run(object: parselmouth.Data, script: str, *args, **kwargs) -> object \ run(objects: List[parselmouth.Data], script: str, *args, **kwargs) -> object
```

## Toolkit Comparison

No matching Vocal Toolkit command or script keyword was found.

[Back to Parselmouth API index](../index.md)
