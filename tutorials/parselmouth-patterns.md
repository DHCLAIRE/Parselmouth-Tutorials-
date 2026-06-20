# Parselmouth Patterns For Praat Vocal Toolkit

The Vocal Toolkit scripts are Praat scripts. Parselmouth can either call individual Praat commands with `praat.call(...)` or execute a full script with `praat.run_file(...)`.

## Setup

```bash
python -m pip install praat-parselmouth numpy matplotlib
export VOCAL_TOOLKIT_DIR="/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit"
```

```python
import parselmouth
print(parselmouth.PRAAT_VERSION)
```

The plugin `setup.praat` requires Praat 6.4.20 or newer. If your installed Parselmouth embeds an older Praat, direct `praat.run_file` calls may fail for commands added after that embedded Praat version.

## One Sound

```python
import os
import parselmouth
from parselmouth import praat

toolkit_dir = os.environ["VOCAL_TOOLKIT_DIR"]
sound = parselmouth.Sound("voice.wav")
result = praat.run_file(sound, os.path.join(toolkit_dir, "normalize.praat"))
```

## Two Sounds

```python
source = parselmouth.Sound("source.wav")
target = parselmouth.Sound("target.wav")
result = praat.run_file([source, target], os.path.join(toolkit_dir, "copypitchcontour.praat"))
```

## Individual Praat Commands

```python
sound = parselmouth.Sound("voice.wav")
pitch = praat.call(sound, "To Pitch", 0.01, 75, 600)
median_f0 = praat.call(pitch, "Get quantile", 0, 0, 0.5, "Hertz")
```

## Generated Coverage

This repository currently documents 75 Praat scripts, including 66 user-facing Vocal Toolkit commands registered in `buttons.praat`.
