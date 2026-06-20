"""Small Parselmouth helpers for Praat Vocal Toolkit tutorials."""

import os
from pathlib import Path
from typing import Iterable, Union

import parselmouth
from parselmouth import praat


SoundLike = Union[str, Path, parselmouth.Sound]


def toolkit_dir() -> Path:
    """Return the Vocal Toolkit plugin directory.

    Set VOCAL_TOOLKIT_DIR if the plugin is not in the default local location.
    """
    return Path(os.environ.get(
        "VOCAL_TOOLKIT_DIR",
        "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit",
    )).expanduser()


def load_sound(sound: SoundLike) -> parselmouth.Sound:
    if isinstance(sound, parselmouth.Sound):
        return sound
    return parselmouth.Sound(str(sound))


def run_toolkit_script(script_name: str, sounds: Union[SoundLike, Iterable[SoundLike]], *args):
    """Run a Vocal Toolkit Praat script through Parselmouth.

    `sounds` may be a single sound path/object or an iterable for scripts that
    require two selected Sound objects, such as the copy commands.
    """
    script_path = toolkit_dir() / script_name
    if isinstance(sounds, (str, Path, parselmouth.Sound)):
        selected = load_sound(sounds)
    else:
        selected = [load_sound(sound) for sound in sounds]
    return praat.run_file(selected, str(script_path), *args)


def call(command: str, selected, *args):
    """Thin wrapper around `parselmouth.praat.call` for tutorial readability."""
    return praat.call(selected, command, *args)
