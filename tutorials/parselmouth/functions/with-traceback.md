# with_traceback

- Kind: `method`
- Available on: `PraatError`, `PraatFatal`, `PraatWarning`
- Vocal Toolkit coverage: **Related**

## What It Does

Exception.

## Tutorial Pattern

```python
# Replace `obj` with an instance of PraatError.
# Add required arguments according to the signature below.
result = obj.with_traceback()
print(result)
```

## Signature

```text
Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.
```

## Toolkit Comparison

A related term appears in the Vocal Toolkit command set or scripts.

[Back to Parselmouth API index](../index.md)
