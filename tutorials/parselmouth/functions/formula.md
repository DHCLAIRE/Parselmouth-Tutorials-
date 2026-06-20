# formula

- Kind: `method`
- Available on: `Harmonicity`, `Intensity`, `Matrix`, `Pitch`, `Sound`, `Spectrogram`, `Spectrum`, `Vector`
- Vocal Toolkit coverage: **Covered**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
# Replace `obj` with an instance of Harmonicity.
# Add required arguments according to the signature below.
result = obj.formula()
print(result)
```

## Signature

```text
formula(self: parselmouth.Matrix, formula: str, from_x: Optional[float] = None, to_x: Optional[float] = None, from_y: Optional[float] = None, to_y: Optional[float] = None) -> None \ formula(self: parselmouth.Matrix, formula: str, x_range: Tuple[Optional[float], Optional[float]] = (None, None), y_range: Tuple[Optional[float], Optional[float]] = (None, None)) -> None
```

## Toolkit Comparison

Used by many Vocal Toolkit processing scripts.

[Back to Parselmouth API index](../index.md)
