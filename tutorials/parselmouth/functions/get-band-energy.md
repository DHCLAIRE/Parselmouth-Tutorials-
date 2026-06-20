# get_band_energy

- Kind: `method`
- Available on: `Spectrum`
- Vocal Toolkit coverage: **Related**

## What It Does

This public Parselmouth API member is documented in the official API reference.

## Tutorial Pattern

```python
# Replace `obj` with an instance of Spectrum.
# Add required arguments according to the signature below.
result = obj.get_band_energy()
print(result)
```

## Signature

```text
get_band_energy(self: parselmouth.Spectrum, band_floor: Optional[float] = None, band_ceiling: Optional[float] = None) -> float \ get_band_energy(self: parselmouth.Spectrum, band: Tuple[Optional[float], Optional[float]] = (None, None)) -> float
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
