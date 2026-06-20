# to_formant_burg

- Kind: `method`
- Available on: `Sound`
- Vocal Toolkit coverage: **Covered**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
import parselmouth

sound = parselmouth.Sound("voice.wav")
# Add required arguments according to the signature below.
result = sound.to_formant_burg()
print(result)
```

## Signature

```text
to_formant_burg(self: parselmouth.Sound, time_step: Optional[Positive[float]] = None, max_number_of_formants: Positive[float] = 5.0, maximum_formant: float = 5500.0, window_length: Positive[float] = 0.025, pre_emphasis_from: Positive[float] = 50.0) -> parselmouth.Formant
```

## Toolkit Comparison

Related to formant-changing and vocal-tract calculations.

[Back to Parselmouth API index](../index.md)
