#!/usr/bin/env python3
"""Generate Parselmouth tutorial pages for the Praat Vocal Toolkit scripts."""

import os
import json
import keyword
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLUGIN_DIR = Path("/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")
PLUGIN_DIR = Path(os.environ.get("VOCAL_TOOLKIT_DIR", str(DEFAULT_PLUGIN_DIR))).expanduser()
API_MANIFEST = ROOT / "data" / "parselmouth_api_manifest.json"


FORM_FIELD_TYPES = {
    "real",
    "positive",
    "natural",
    "integer",
    "boolean",
    "word",
    "sentence",
    "text",
    "choice",
    "optionmenu",
}

DIRECT_EXAMPLES = {
    "calculatevtl.praat": '''from math import isnan

import parselmouth
from parselmouth import praat


def estimate_vocal_tract_length(sound_path, formant_number=4, maximum_formant=5500):
    sound = parselmouth.Sound(sound_path)
    formants = sound.to_formant_burg(
        time_step=0.005,
        max_number_of_formants=5,
        maximum_formant=maximum_formant,
        window_length=0.025,
        pre_emphasis_from=50,
    )
    formant_frequency = praat.call(formants, "Get mean", formant_number, 0, 0, "Hertz")
    if isnan(formant_frequency):
        raise ValueError("The selected formant could not be measured.")
    return 35000 * ((formant_number / 2) - 0.25) / formant_frequency


vtl_cm = estimate_vocal_tract_length("voice.wav")
print(f"Estimated vocal tract length: {vtl_cm:.2f} cm")
''',
    "normalize.praat": '''import parselmouth
from parselmouth import praat
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
normalized = sound.copy()
praat.call(normalized, "Scale peak", 0.99)
normalized.save("voice-normalized.wav", SoundFileFormat.WAV)
''',
    "extractpitch.praat": '''import numpy as np
import parselmouth


sound = parselmouth.Sound("voice.wav")
pitch = sound.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=600)
f0 = pitch.selected_array["frequency"].astype(float)
f0[f0 == 0] = np.nan

print("Median F0:", np.nanmedian(f0))
''',
    "fixdc.praat": '''import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
fixed = sound.copy()
fixed.values[:] = fixed.values - fixed.values.mean(axis=1, keepdims=True)
fixed.save("voice-fixdc.wav", SoundFileFormat.WAV)
''',
    "changeduration.praat": '''import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
longer = sound.lengthen(minimum_pitch=75, maximum_pitch=600, factor=1.25)
longer.save("voice-duration-x1.25.wav", SoundFileFormat.WAV)
''',
    "changespeed.praat": '''import parselmouth
from parselmouth import SoundFileFormat


sound = parselmouth.Sound("voice.wav")
faster = sound.resample(sound.sampling_frequency * 1.25)
faster.override_sampling_frequency(sound.sampling_frequency)
faster.save("voice-speed-x1.25.wav", SoundFileFormat.WAV)
''',
}

TOPIC_NOTES = [
    ("pitch", "Most pitch-changing scripts create a `Pitch` or `Manipulation` object. In Python, start with `sound.to_pitch(...)`, inspect `pitch.selected_array['frequency']`, and use `praat.call` when you need Praat commands that do not have a Python method."),
    ("formant", "Formant pages usually call `To Formant (robust)` or LPC commands. Parselmouth exposes Burg formants as `sound.to_formant_burg(...)`; for robust formants, LPC filtering, and `Formula (frequencies)`, use `praat.call`."),
    ("intensity", "Intensity copying and scaling can often be done with `sound.scale_intensity(...)` or an `Intensity` object from `sound.to_intensity(...)`."),
    ("reverb", "Reverb presets rely on impulse-response files in the toolkit `reverb/` folder. Keep the plugin folder intact so relative `Read from file` calls can resolve the WAV files."),
    ("eq", "EQ pages often convert sounds to spectra or use saved preset `Sound` objects from the toolkit `eq/` folder. Keep that folder next to the scripts when using `run_file`."),
    ("vocoder", "Vocoder and carrier/modulator pages combine several Praat objects. The `run_file` wrapper is usually the shortest faithful route."),
]

DIRECT_TOOLKIT_EQUIVALENTS = {
    "calculatevtl.praat": ["Formant.get_value_at_time", "praat.call"],
    "changeduration.praat": ["Sound.lengthen"],
    "changespeed.praat": ["Sound.resample", "Sound.override_sampling_frequency"],
    "extractpitch.praat": ["Sound.to_pitch"],
    "fixdc.praat": ["Sound.subtract_mean"],
    "normalize.praat": ["Sound.scale_peak"],
}

API_TO_TOOLKIT_HINTS = {
    "praat.call": "All faithful Vocal Toolkit wrappers use this when calling individual Praat commands.",
    "praat.run_file": "All generated Vocal Toolkit extension wrappers use this to run the original scripts.",
    "lengthen": "Covered by Change duration.",
    "override_sampling_frequency": "Covered by Change speed.",
    "resample": "Covered by Change speed and several preset scripts.",
    "scale_peak": "Covered by Normalize.",
    "scale_intensity": "Covered by intensity and effect scripts.",
    "subtract_mean": "Covered by Fix DC offset.",
    "to_formant_burg": "Related to formant-changing and vocal-tract calculations.",
    "to_harmonicity": "Related to breathiness/voice-quality analysis workflows.",
    "to_harmonicity_ac": "Related to breathiness/voice-quality analysis workflows.",
    "to_harmonicity_cc": "Related to breathiness/voice-quality analysis workflows.",
    "to_harmonicity_gne": "Related to breathiness/voice-quality analysis workflows.",
    "to_intensity": "Covered by intensity contour and mixing scripts.",
    "to_pitch": "Covered by Extract pitch and pitch-changing scripts.",
    "to_pitch_ac": "Related to Extract pitch.",
    "to_pitch_cc": "Related to Extract pitch.",
    "to_pitch_shs": "Related to Extract pitch.",
    "to_pitch_spinet": "Related to Extract pitch.",
    "to_sound": "Covered by synthesis/resynthesis workflows.",
    "to_spectrogram": "Related to EQ, filtering, and spectral processing.",
    "to_spectrum": "Related to EQ, filtering, and spectral processing.",
    "convolve": "Covered by Reverb.",
    "formula": "Used by many Vocal Toolkit processing scripts.",
}


def slugify(text):
    text = text.lower()
    text = text.replace(".praat", "")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def qstrings(line):
    return re.findall(r'"([^"]*)"', line)


def parse_buttons(path):
    commands = {}
    order = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("Add action command:"):
            continue
        quoted = qstrings(line)
        if len(quoted) < 3:
            continue
        script = quoted[-1]
        title = quoted[-3]
        if not script:
            continue
        match = re.search(r'Add action command:\s*"Sound",\s*(\d+)', line)
        selected = int(match.group(1)) if match else 0
        kind = "copy" if selected == 2 else "process"
        commands[script] = {"title": title, "selected": selected, "kind": kind}
        order.append(script)
    return commands, order


def parse_form(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    in_form = False
    title = None
    fields = []
    comments = []
    current_choice = None

    def handle_form_line(line):
        nonlocal current_choice
        if not line:
            return
        if line.startswith("comment:"):
            values = qstrings(line)
            if values:
                comments.append(values[0])
            return
        if line.startswith("include "):
            include_path = path.parent / line.split(None, 1)[1]
            if include_path.exists():
                for inc_raw in include_path.read_text(encoding="utf-8").splitlines():
                    handle_form_line(inc_raw.strip())
            return
        key = line.split(":", 1)[0]
        if key in FORM_FIELD_TYPES:
            values = qstrings(line)
            name = values[0] if values else ""
            if len(values) > 1:
                default = values[1]
            else:
                default_match = re.search(r',\s*([^,]+)\s*$', line)
                default = default_match.group(1).strip() if default_match else ""
            field = {"type": key, "name": name, "default": default, "options": []}
            fields.append(field)
            current_choice = field if key in {"choice", "optionmenu"} else None
            return
        if line.startswith("option:") and current_choice:
            values = qstrings(line)
            if values:
                current_choice["options"].append(values[0])

    for raw in lines:
        line = raw.strip()
        if line.startswith("form:"):
            in_form = True
            values = qstrings(line)
            title = values[0] if values else path.stem
            continue
        if in_form and line.startswith("endform"):
            break
        if not in_form:
            continue
        handle_form_line(line)
    return {"title": title, "fields": fields, "comments": comments}


def summarize_operations(path):
    text = path.read_text(encoding="utf-8")
    patterns = [
        ("Pitch analysis", r"To Pitch|PitchTier|pitch"),
        ("Formant or LPC processing", r"Formant|LPC|formant"),
        ("Intensity scaling or contour work", r"Intensity|Scale intensity|scale_intensity"),
        ("Filtering or spectrum processing", r"Filter|Spectrum|band|EQ|Formul"),
        ("Manipulation and resynthesis", r"Manipulation|resynthesis|overlap-add|PSOLA"),
        ("Mixing, convolution, or copying between sounds", r"Mix|Convolve|plusObject|copymix"),
        ("TextGrid or interval annotation", r"TextGrid|interval|tier"),
        ("Batch processing over selected sounds", r"include batch\.praat"),
        ("File or preset loading", r"Read from file|presetslist|reverb/|eq/"),
    ]
    found = [label for label, pattern in patterns if re.search(pattern, text, re.IGNORECASE)]
    return found[:5] or ["Praat object selection and command calls"]


def extract_run_scripts(path):
    text = path.read_text(encoding="utf-8")
    names = sorted(set(re.findall(r'runScript:\s*"([^"]+)"', text) + re.findall(r"include\s+([A-Za-z0-9_.-]+)", text)))
    return [name for name in names if name != path.name]


def field_variable_name(label):
    name = label.lower()
    name = re.sub(r"\([^)]*\)", "", name)
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_") or "value"


def format_default(field):
    if field["type"] == "boolean":
        return "1" if field["default"] in {"1", "yes", "true", "True"} else "0"
    if field["type"] in {"choice", "optionmenu"}:
        return field["default"] or "1"
    if field["type"] in {"real", "positive", "natural", "integer"}:
        default = field["default"].strip()
        numeric = re.match(r"^(-?\d+(\.\d+)?)", default)
        if numeric:
            return numeric.group(1)
    if field["default"]:
        return repr(field["default"])
    return "None"


def argument_list(fields):
    if not fields:
        return ""
    return ", ".join(format_default(field) for field in fields)


def python_args(fields):
    if not fields:
        return ""
    lines = ["    # Positional arguments follow the Praat form order."]
    for field in fields:
        lines.append("    {0},  # {1}".format(format_default(field), field["name"]))
    return "\n".join(lines)


def topic_note_for(script, title):
    haystack = (script + " " + title).lower()
    notes = [note for key, note in TOPIC_NOTES if key in haystack]
    return notes[0] if notes else "Use the wrapper first for a faithful translation, then replace individual Praat commands with direct Parselmouth methods as you validate each step."


def load_api_manifest():
    if not API_MANIFEST.exists():
        return None
    return json.loads(API_MANIFEST.read_text(encoding="utf-8"))


def owner_example_name(owner):
    if owner == "Sound":
        return "sound"
    if owner == "parselmouth.praat":
        return "praat"
    return "obj"


def function_status(entry, toolkit_terms):
    name = entry["name"]
    short = entry["short_name"]
    if name in API_TO_TOOLKIT_HINTS:
        return "Covered", API_TO_TOOLKIT_HINTS[name]
    if short in API_TO_TOOLKIT_HINTS:
        return "Covered", API_TO_TOOLKIT_HINTS[short]
    tokens = [token for token in re.split(r"[^a-z0-9]+", short.lower()) if len(token) > 2]
    if tokens and any(token in toolkit_terms for token in tokens):
        return "Related", "A related term appears in the Vocal Toolkit command set or scripts."
    return "Not in Vocal Toolkit", "No matching Vocal Toolkit command or script keyword was found."


def parselmouth_function_page(entry, toolkit_terms):
    status, note = function_status(entry, toolkit_terms)
    owners = entry["owners"]
    primary_owner = owners[0] if owners else "object"
    short = entry["short_name"]
    kind = entry["kind"]
    lines = [
        "# {0}".format(entry["name"]),
        "",
        "- Kind: `{0}`".format(kind),
        "- Available on: {0}".format(", ".join("`{}`".format(owner) for owner in owners)),
        "- Vocal Toolkit coverage: **{0}**".format(status),
        "",
        "## What It Does",
        "",
        entry.get("summary") or "This public Parselmouth API member is documented in the official API reference.",
        "",
        "## Tutorial Pattern",
        "",
        "```python",
    ]
    if entry["name"].startswith("praat."):
        if short == "call":
            lines += [
                "import parselmouth",
                "from parselmouth import praat",
                "",
                'sound = parselmouth.Sound("voice.wav")',
                'pitch = praat.call(sound, "To Pitch", 0.01, 75, 600)',
                'median_f0 = praat.call(pitch, "Get quantile", 0, 0, 0.5, "Hertz")',
            ]
        elif short == "run_file":
            lines += [
                "import os",
                "import parselmouth",
                "from parselmouth import praat",
                "",
                'sound = parselmouth.Sound("voice.wav")',
                'script = os.path.join(os.environ["VOCAL_TOOLKIT_DIR"], "normalize.praat")',
                "result = praat.run_file(sound, script)",
            ]
        else:
            lines += [
                "from parselmouth import praat",
                "",
                'script = "Create Sound from formula: \\"tone\\", 1, 0, 0.25, 44100, \\"0.2*sin(2*pi*220*x)\\""',
                "result = praat.run(script)",
            ]
    elif kind == "property":
        variable = owner_example_name(primary_owner)
        if primary_owner == "Sound":
            lines += [
                "import parselmouth",
                "",
                '{0} = parselmouth.Sound("voice.wav")'.format(variable),
                "value = {0}.{1}".format(variable, short),
                "print(value)",
            ]
        else:
            lines += [
                "# Replace `obj` with an instance of {0}.".format(primary_owner),
                "value = obj.{0}".format(short),
                "print(value)",
            ]
    else:
        variable = owner_example_name(primary_owner)
        if primary_owner == "Sound":
            lines += [
                "import parselmouth",
                "",
                '{0} = parselmouth.Sound("voice.wav")'.format(variable),
                "# Add required arguments according to the signature below.",
                "result = {0}.{1}()".format(variable, short),
                "print(result)",
            ]
        else:
            lines += [
                "# Replace `obj` with an instance of {0}.".format(primary_owner),
                "# Add required arguments according to the signature below.",
                "result = obj.{0}()".format(short),
                "print(result)",
            ]
    lines += [
        "```",
        "",
        "## Signature",
        "",
        "```text",
        entry.get("signature") or "See the official API reference for overload details.",
        "```",
        "",
        "## Toolkit Comparison",
        "",
        note,
        "",
        "[Back to Parselmouth API index](../index.md)",
        "",
    ]
    return "\n".join(lines)


def parselmouth_index(manifest, toolkit_terms):
    lines = [
        "# Parselmouth API Tutorials",
        "",
        "Generated from the public Parselmouth API manifest. The manifest was introspected from `praat-parselmouth {0}` with embedded Praat `{1}`.".format(
            manifest.get("parselmouth_version", ""), manifest.get("praat_version", "")
        ),
        "",
        "Source reference: [{0}]({0})".format(manifest.get("source_url", "")),
        "",
        "## Functions And Properties",
        "",
        "| API member | Kind | Owners | Vocal Toolkit coverage |",
        "| --- | --- | --- | --- |",
    ]
    for entry in manifest["functions"]:
        status, _ = function_status(entry, toolkit_terms)
        lines.append("| [{0}](functions/{1}.md) | `{2}` | {3} | {4} |".format(
            entry["name"],
            slugify(entry["name"]),
            entry["kind"],
            ", ".join("`{}`".format(owner) for owner in entry["owners"][:5]),
            status,
        ))
    lines += [
        "",
        "## Classes And Enums",
        "",
        "| Class or enum | Values |",
        "| --- | --- |",
    ]
    for cls in manifest["classes"]:
        values = ", ".join("`{}`".format(value) for value in cls.get("enum_values", [])) or ""
        lines.append("| `{0}` | {1} |".format(cls["name"], values))
    lines.append("")
    return "\n".join(lines)


def toolkit_terms(commands, scripts):
    terms = set()
    for script, command in commands.items():
        parts = [script, command["title"]]
        form = parse_form(PLUGIN_DIR / script)
        parts.extend(field["name"] for field in form["fields"])
        parts.extend(form["comments"])
        for text in parts:
            terms.update(token for token in re.split(r"[^a-z0-9]+", text.lower()) if len(token) > 2)
    return terms


def parameter_name(field):
    name = field_variable_name(field["name"])
    if field["type"] in {"choice", "optionmenu"} and not name.endswith("_index"):
        name += "_index"
    if keyword.iskeyword(name) or name in {"type", "format", "input", "file"}:
        name += "_value"
    return name


def python_default_value(field):
    raw = format_default(field)
    if field["type"] == "boolean":
        return "True" if raw == "1" else "False"
    return raw


def extension_function_name(script, command):
    title = command["title"].replace("(in-place)", "").replace("(scale peak 0.99)", "")
    base = slugify(title).replace("-", "_")
    if command["kind"] == "copy" and not base.startswith("copy_"):
        base = "copy_" + base
    if not base:
        base = slugify(script).replace("-", "_")
    return base


def toolkit_extension_module(commands, order):
    lines = [
        '"""Python functions for Vocal Toolkit commands implemented with Parselmouth."""',
        "",
        "from src.vocal_toolkit_parselmouth import run_toolkit_script",
        "",
        "",
        "def _bool_arg(value):",
        "    return int(bool(value))",
        "",
        "",
    ]
    for script in order:
        command = commands[script]
        fields = parse_form(PLUGIN_DIR / script)["fields"]
        function_name = extension_function_name(script, command)
        sound_args = ["source_sound", "target_sound"] if command["selected"] == 2 else ["sound"]
        params = sound_args + ["{0}={1}".format(parameter_name(field), python_default_value(field)) for field in fields]
        lines.append("def {0}({1}):".format(function_name, ", ".join(params)))
        lines.append('    """Run `{0}` ({1}) through Parselmouth."""'.format(script, command["title"]))
        selected = "[source_sound, target_sound]" if command["selected"] == 2 else "sound"
        arg_exprs = []
        for field in fields:
            name = parameter_name(field)
            if field["type"] == "boolean":
                arg_exprs.append("_bool_arg({0})".format(name))
            else:
                arg_exprs.append(name)
        if arg_exprs:
            lines.append("    return run_toolkit_script(")
            lines.append('        "{0}",'.format(script))
            lines.append("        {0},".format(selected))
            for expr in arg_exprs:
                lines.append("        {0},".format(expr))
            lines.append("    )")
        else:
            lines.append('    return run_toolkit_script("{0}", {1})'.format(script, selected))
        lines += ["", ""]
    return "\n".join(lines)


def toolkit_missing_page(commands, order):
    lines = [
        "# Vocal Toolkit Commands Without Native Parselmouth Equivalents",
        "",
        "Every command below has a generated Python function in `src/vocal_toolkit_extensions.py`. Commands marked `Direct equivalent` have a compact native Parselmouth route; the others are implemented as Parselmouth wrappers around the original Praat script.",
        "",
        "| Command | Script | Status | Python function |",
        "| --- | --- | --- | --- |",
    ]
    for script in order:
        command = commands[script]
        status = "Direct equivalent" if script in DIRECT_TOOLKIT_EQUIVALENTS else "Extension wrapper"
        function_name = extension_function_name(script, command)
        lines.append("| {0} | `{1}` | {2} | `vocal_toolkit_extensions.{3}` |".format(
            command["title"], script, status, function_name
        ))
    lines.append("")
    return "\n".join(lines)


def parselmouth_missing_page(manifest, toolkit_terms):
    missing = [entry for entry in manifest["functions"] if function_status(entry, toolkit_terms)[0] == "Not in Vocal Toolkit"]
    lines = [
        "# Parselmouth API Not Covered By Vocal Toolkit",
        "",
        "These public Parselmouth API members do not have an obvious Vocal Toolkit command or script keyword match. They are still documented in the Parselmouth API tutorial pages.",
        "",
        "| API member | Kind | Owners |",
        "| --- | --- | --- |",
    ]
    for entry in missing:
        lines.append("| [{0}](../parselmouth/functions/{1}.md) | `{2}` | {3} |".format(
            entry["name"],
            slugify(entry["name"]),
            entry["kind"],
            ", ".join("`{}`".format(owner) for owner in entry["owners"][:5]),
        ))
    lines.append("")
    return "\n".join(lines)


def page_for_script(script, command, form, helper_names):
    title = command.get("title") or form.get("title") or script.replace(".praat", "")
    selected = command.get("selected", 0)
    selected_text = "two selected `Sound` objects" if selected == 2 else "one or more selected `Sound` objects"
    kind = command.get("kind", "helper")
    source = PLUGIN_DIR / script
    fields = form["fields"]
    operations = summarize_operations(source)
    dependencies = extract_run_scripts(source)
    direct = DIRECT_EXAMPLES.get(script)
    args = argument_list(fields)
    wrapper_args = python_args(fields)
    slug = slugify(script)
    back = "../index.md" if kind != "helper" else "../internal/index.md"

    lines = [
        "# {0}".format(title),
        "",
        "- Praat source: `{0}`".format(script),
        "- Tutorial type: `{0}`".format(kind),
        "- Selection model: {0}".format(selected_text if kind != "helper" else "usually called by another toolkit script"),
        "",
        "## What The Praat Script Does",
        "",
    ]
    if form["comments"]:
        for comment in form["comments"][:4]:
            lines.append("- {0}".format(comment))
    else:
        lines.append("- Runs the logic in `{0}` from the Vocal Toolkit plugin.".format(script))
    for operation in operations:
        lines.append("- {0}.".format(operation))

    lines += ["", "## Parameters", ""]
    if fields:
        lines.append("| Praat form field | Type | Default | Python argument |")
        lines.append("| --- | --- | --- | --- |")
        for field in fields:
            default = field["default"] or ""
            if field["type"] in {"choice", "optionmenu"} and field["options"]:
                opt_preview = "; options: " + ", ".join(field["options"][:8])
                if len(field["options"]) > 8:
                    opt_preview += ", ..."
                default += opt_preview
            lines.append("| `{0}` | `{1}` | `{2}` | `{3}` |".format(
                field["name"], field["type"], default.replace("|", "\\|"), field_variable_name(field["name"])
            ))
    else:
        lines.append("This script has no interactive Praat form. Call it with the selected sound object(s), or use the direct equivalent when one is shown below.")

    lines += [
        "",
        "## Parselmouth Tutorial",
        "",
        "### Faithful Toolkit Call",
        "",
        "This route asks Parselmouth to execute the original Praat script. It is the best starting point when the script uses complex object selection, relative includes, or Praat commands without a direct Python method.",
        "",
        "```python",
        "import os",
        "import parselmouth",
        "from parselmouth import praat",
        "",
        'TOOLKIT_DIR = os.environ.get("VOCAL_TOOLKIT_DIR", "/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit")',
        'SCRIPT = os.path.join(TOOLKIT_DIR, "{0}")'.format(script),
        "",
    ]
    if selected == 2:
        lines += [
            'source = parselmouth.Sound("source.wav")',
            'target = parselmouth.Sound("target.wav")',
            "result = praat.run_file([source, target], SCRIPT{0})".format((", " + args) if args else ""),
        ]
    else:
        lines += [
            'sound = parselmouth.Sound("voice.wav")',
            "result = praat.run_file(sound, SCRIPT{0})".format((", " + args) if args else ""),
        ]
    lines += [
        "",
        "# Many Vocal Toolkit scripts leave the processed Sound selected.",
        "# Depending on the script, `result` can be a Praat object, a list-like result, or text output.",
        "print(result)",
        "```",
        "",
        "### Reusable Python Wrapper",
        "",
        "```python",
        "from src.vocal_toolkit_parselmouth import run_toolkit_script",
        "",
    ]
    if selected == 2:
        if wrapper_args:
            lines += [
                'result = run_toolkit_script(',
                '    "{0}",'.format(script),
                '    ["source.wav", "target.wav"],',
                wrapper_args,
                ")",
            ]
        else:
            lines.append('result = run_toolkit_script("{0}", ["source.wav", "target.wav"])'.format(script))
    else:
        if wrapper_args:
            lines += [
                'result = run_toolkit_script(',
                '    "{0}",'.format(script),
                '    "voice.wav",',
                wrapper_args,
                ")",
            ]
        else:
            lines.append('result = run_toolkit_script("{0}", "voice.wav")'.format(script))
    lines += [
        "```",
        "",
    ]
    if direct:
        lines += [
            "### Direct Parselmouth Version",
            "",
            "For this command, a compact direct version is practical without running the plugin script.",
            "",
            "```python",
            direct.rstrip(),
            "```",
            "",
        ]
    lines += [
        "## Translation Notes",
        "",
        "- {0}".format(topic_note_for(script, title)),
        "- Choice and option-menu fields are safest as 1-based numeric indexes when supplied to `praat.run_file`; use the table above to map indexes to labels.",
        "- Boolean fields can be supplied as `1`/`0` or `True`/`False`.",
        "- Preview fields in the original plugin are UI-oriented. In Python tutorials, set preview-like fields to `0` when you want a published object name.",
    ]
    if dependencies:
        lines.append("- This script calls or includes: {0}.".format(", ".join("`{}`".format(dep) for dep in dependencies[:12])))
    lines += [
        "",
        "## Check Yourself",
        "",
        "1. Run the faithful toolkit call on a short WAV file.",
        "2. Save or inspect the returned object with `praat.call(result, \"Save as WAV file...\", \"out.wav\")` if the result is a `Sound`.",
        "3. Compare the output against Praat's menu command using the same parameter values.",
        "",
        "[Back to index]({0})".format(back),
        "",
    ]
    return "\n".join(lines)


def reference_page(scripts, commands):
    lines = [
        "# Parselmouth Patterns For Praat Vocal Toolkit",
        "",
        "The Vocal Toolkit scripts are Praat scripts. Parselmouth can either call individual Praat commands with `praat.call(...)` or execute a full script with `praat.run_file(...)`.",
        "",
        "## Setup",
        "",
        "```bash",
        "python -m pip install praat-parselmouth numpy matplotlib",
        "export VOCAL_TOOLKIT_DIR=\"/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit\"",
        "```",
        "",
        "```python",
        "import parselmouth",
        "print(parselmouth.PRAAT_VERSION)",
        "```",
        "",
        "The plugin `setup.praat` requires Praat 6.4.20 or newer. If your installed Parselmouth embeds an older Praat, direct `praat.run_file` calls may fail for commands added after that embedded Praat version.",
        "",
        "## One Sound",
        "",
        "```python",
        "import os",
        "import parselmouth",
        "from parselmouth import praat",
        "",
        "toolkit_dir = os.environ[\"VOCAL_TOOLKIT_DIR\"]",
        "sound = parselmouth.Sound(\"voice.wav\")",
        "result = praat.run_file(sound, os.path.join(toolkit_dir, \"normalize.praat\"))",
        "```",
        "",
        "## Two Sounds",
        "",
        "```python",
        "source = parselmouth.Sound(\"source.wav\")",
        "target = parselmouth.Sound(\"target.wav\")",
        "result = praat.run_file([source, target], os.path.join(toolkit_dir, \"copypitchcontour.praat\"))",
        "```",
        "",
        "## Individual Praat Commands",
        "",
        "```python",
        "sound = parselmouth.Sound(\"voice.wav\")",
        "pitch = praat.call(sound, \"To Pitch\", 0.01, 75, 600)",
        "median_f0 = praat.call(pitch, \"Get quantile\", 0, 0, 0.5, \"Hertz\")",
        "```",
        "",
        "## Generated Coverage",
        "",
        "This repository currently documents {0} Praat scripts, including {1} user-facing Vocal Toolkit commands registered in `buttons.praat`.".format(len(scripts), len(commands)),
        "",
    ]
    return "\n".join(lines)


def wrapper_module():
    return '''"""Small Parselmouth helpers for Praat Vocal Toolkit tutorials."""

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
'''


def example_batch():
    return '''"""Batch-run a Vocal Toolkit script with Parselmouth.

Set VOCAL_TOOLKIT_DIR to the plugin_VocalToolkit folder before running this.
"""

from pathlib import Path

from parselmouth import SoundFileFormat

from src.vocal_toolkit_parselmouth import run_toolkit_script


INPUT_DIR = Path("audio")
OUTPUT_DIR = Path("processed")
OUTPUT_DIR.mkdir(exist_ok=True)

for wav_path in sorted(INPUT_DIR.glob("*.wav")):
    result = run_toolkit_script("normalize.praat", wav_path)
    try:
        result.save(str(OUTPUT_DIR / wav_path.name), SoundFileFormat.WAV)
    except AttributeError:
        print(f"{wav_path}: script returned {type(result)!r}; inspect it before saving")
'''


def root_readme(commands, helper_count, manifest, toolkit_terms):
    missing_count = 0
    api_count = 0
    class_count = 0
    if manifest:
        api_count = len(manifest["functions"])
        class_count = len(manifest["classes"])
        missing_count = sum(1 for entry in manifest["functions"] if function_status(entry, toolkit_terms)[0] == "Not in Vocal Toolkit")
    lines = [
        "# Parselmouth Tutorials",
        "",
        "This repository documents the [Parselmouth](https://github.com/YannickJadoul/Parselmouth) Python API and shows how to reproduce or call Praat Vocal Toolkit scripts from Python.",
        "",
        "The Vocal Toolkit tutorials are generated from the local plugin scripts in `/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit`. The Parselmouth tutorials are generated from `data/parselmouth_api_manifest.json`, which was introspected from the official `praat-parselmouth` package.",
        "",
        "## Start Here",
        "",
        "1. Install Parselmouth: `python -m pip install praat-parselmouth`.",
        "2. Point Python at the toolkit: `export VOCAL_TOOLKIT_DIR=\"/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit\"`.",
        "3. Read [Parselmouth patterns](tutorials/parselmouth-patterns.md).",
        "4. Pick a Parselmouth API member from [the Parselmouth index](tutorials/parselmouth/index.md) or a Vocal Toolkit command from [the toolkit index](tutorials/index.md).",
        "",
        "## What Is Included",
        "",
        "- `{0}` Parselmouth API function/property tutorials across `{1}` classes and enums.".format(api_count, class_count),
        "- `{0}` user-facing Vocal Toolkit command tutorials.".format(len(commands)),
        "- `{0}` internal/helper script references.".format(helper_count),
        "- `src/vocal_toolkit_parselmouth.py`, a reusable Python wrapper for `praat.run_file`.",
        "- `src/vocal_toolkit_extensions.py`, Python functions for all Vocal Toolkit commands that can be imported directly.",
        "- `examples/batch_process.py`, a minimal batch-processing example.",
        "",
        "## Coverage Checklist",
        "",
        "- Toolkit commands with compact direct Parselmouth equivalents: `{0}`.".format(len(DIRECT_TOOLKIT_EQUIVALENTS)),
        "- Toolkit commands implemented as generated Python extension wrappers: `{0}`.".format(len(commands) - len(DIRECT_TOOLKIT_EQUIVALENTS)),
        "- Parselmouth API members marked as not covered by Vocal Toolkit: `{0}`.".format(missing_count),
        "",
        "Full comparison tables:",
        "",
        "- [Vocal Toolkit commands without native Parselmouth equivalents](tutorials/comparisons/toolkit-not-in-parselmouth.md)",
        "- [Parselmouth API not covered by Vocal Toolkit](tutorials/comparisons/parselmouth-not-in-toolkit.md)",
        "",
        "Major Parselmouth areas marked as outside the Vocal Toolkit scope include low-level object/file I/O, Matrix and Vector cell operations, Spectrum bin statistics, TextGrid conversion helpers, time-grid utility methods, and enum/metadata properties.",
        "",
        "## Compatibility Note",
        "",
        "The current manifest was generated from `praat-parselmouth {0}` with embedded Praat `{1}`. The Vocal Toolkit `setup.praat` asks for Praat 6.4.20 or newer, so check `parselmouth.PRAAT_VERSION` if a toolkit script fails in your environment.".format(
            manifest.get("parselmouth_version", "") if manifest else "",
            manifest.get("praat_version", "") if manifest else "",
        ),
        "",
        "## Regenerate",
        "",
        "```bash",
        "VOCAL_TOOLKIT_DIR=\"/Users/neuroling/Downloads/Praat Vocal Toolkit/plugin_VocalToolkit\" \\",
        "python3 tools/generate_vocal_toolkit_tutorials.py",
        "```",
        "",
        "To refresh the Parselmouth API manifest from an installed Parselmouth package:",
        "",
        "```bash",
        "python3 tools/introspect_parselmouth_api.py",
        "```",
        "",
    ]
    return "\n".join(lines)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    if not PLUGIN_DIR.exists():
        raise SystemExit("Plugin directory not found: {}".format(PLUGIN_DIR))

    manifest = load_api_manifest()
    commands, order = parse_buttons(PLUGIN_DIR / "buttons.praat")
    scripts = sorted(path.name for path in PLUGIN_DIR.glob("*.praat"))
    helper_scripts = [script for script in scripts if script not in commands]
    terms = toolkit_terms(commands, scripts)

    user_index = ["# Vocal Toolkit Command Tutorials", ""]
    user_index.append("These pages are generated from `buttons.praat` in menu order. Copy commands expect two selected `Sound` objects; process commands usually accept one or more selected `Sound` objects.")
    user_index.append("")
    user_index.append("| Command | Script | Selection |")
    user_index.append("| --- | --- | --- |")

    for script in order:
        if script not in scripts:
            continue
        form = parse_form(PLUGIN_DIR / script)
        command = commands[script]
        page_path = ROOT / "tutorials" / "functions" / (slugify(script) + ".md")
        write(page_path, page_for_script(script, command, form, helper_scripts))
        user_index.append("| [{0}](functions/{1}.md) | `{2}` | `{3}` |".format(
            command["title"], slugify(script), script, command["selected"]
        ))

    user_index += [
        "",
        "## Internal And Helper Scripts",
        "",
        "These are not registered as menu actions, but the user-facing commands call them. They are included so the translation trail stays inspectable.",
        "",
        "[Open helper index](internal/index.md)",
        "",
    ]
    write(ROOT / "tutorials" / "index.md", "\n".join(user_index))

    helper_index = ["# Internal And Helper Scripts", "", "| Script | Purpose |", "| --- | --- |"]
    for script in helper_scripts:
        form = parse_form(PLUGIN_DIR / script)
        command = {"title": form.get("title") or script.replace(".praat", ""), "selected": 0, "kind": "helper"}
        page_path = ROOT / "tutorials" / "internal" / (slugify(script) + ".md")
        write(page_path, page_for_script(script, command, form, helper_scripts))
        helper_index.append("| [{0}](./{1}.md) | `{2}` |".format(command["title"], slugify(script), script))
    helper_index.append("")
    write(ROOT / "tutorials" / "internal" / "index.md", "\n".join(helper_index))

    write(ROOT / "tutorials" / "parselmouth-patterns.md", reference_page(scripts, commands))
    write(ROOT / "src" / "vocal_toolkit_parselmouth.py", wrapper_module())
    write(ROOT / "src" / "vocal_toolkit_extensions.py", toolkit_extension_module(commands, order))
    write(ROOT / "examples" / "batch_process.py", example_batch())
    write(ROOT / "tutorials" / "comparisons" / "toolkit-not-in-parselmouth.md", toolkit_missing_page(commands, order))

    if manifest:
        write(ROOT / "tutorials" / "parselmouth" / "index.md", parselmouth_index(manifest, terms))
        for entry in manifest["functions"]:
            write(
                ROOT / "tutorials" / "parselmouth" / "functions" / (slugify(entry["name"]) + ".md"),
                parselmouth_function_page(entry, terms),
            )
        write(ROOT / "tutorials" / "comparisons" / "parselmouth-not-in-toolkit.md", parselmouth_missing_page(manifest, terms))

    write(ROOT / "README.md", root_readme(commands, len(helper_scripts), manifest, terms))

    api_count = len(manifest["functions"]) if manifest else 0
    print("Generated {} command tutorials, {} helper references, and {} Parselmouth API tutorials.".format(
        len(commands), len(helper_scripts), api_count
    ))


if __name__ == "__main__":
    main()
