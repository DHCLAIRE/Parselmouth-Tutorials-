# get_band_density_difference

- Kind: `method`
- Available on: `Spectrum`
- Vocal Toolkit coverage: **Related**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
# Replace `obj` with an instance of Spectrum.
# Add required arguments according to the signature below.
result = obj.get_band_density_difference()
print(result)
```

## Signature

```text
get_band_density_difference(self: parselmouth.Spectrum, low_band_floor: Optional[float] = None, low_band_ceiling: Optional[float] = None, high_band_floor: Optional[float] = None, high_band_ceiling: Optional[float] = None) -> float \ get_band_density_difference(self: parselmouth.Spectrum, low_band: Tuple[Optional[float], Optional[float]] = (None, None), high_band: Tuple[Optional[float], Optional[float]] = (None, None)) -> float
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
