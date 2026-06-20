#!/usr/bin/env python3
"""Write a public Parselmouth API manifest used by the tutorial generator."""

import inspect
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data" / "parselmouth_api_manifest.json"
SOURCE_URL = "https://parselmouth.readthedocs.io/en/stable/api_reference.html"


def first_sentence(doc):
    if not doc:
        return ""
    paragraphs = [paragraph.strip() for paragraph in doc.strip().split("\n\n") if paragraph.strip()]
    if not paragraphs:
        return ""
    paragraph = paragraphs[0]
    if " -> " in paragraph and len(paragraphs) > 1:
        paragraph = paragraphs[1]
    elif " -> " in paragraph:
        return ""
    line = " ".join(paragraph.split())
    if "." in line:
        return line.split(".", 1)[0] + "."
    return line[:180]


def signature_for(callable_obj):
    try:
        return str(inspect.signature(callable_obj))
    except (TypeError, ValueError):
        doc = inspect.getdoc(callable_obj) or ""
        paragraphs = [paragraph.strip() for paragraph in doc.strip().split("\n\n") if paragraph.strip()]
        if paragraphs and ")" in paragraphs[0] and "(" in paragraphs[0]:
            return " ".join(paragraphs[0].split())
    return ""


def public_classes(parselmouth):
    classes = []
    for name in sorted(dir(parselmouth)):
        obj = getattr(parselmouth, name)
        if inspect.isclass(obj) and getattr(obj, "__module__", "").startswith("parselmouth"):
            classes.append((name, obj))
    return classes


def member_kind(cls, name, value):
    descriptor = inspect.getattr_static(cls, name, None)
    if isinstance(descriptor, property):
        return "property"
    if callable(value):
        return "method"
    return "attribute"


def build_manifest():
    import parselmouth
    from parselmouth import praat

    grouped = {}

    for name in sorted(dir(praat)):
        if name.startswith("_"):
            continue
        obj = getattr(praat, name)
        grouped["praat." + name] = {
            "name": "praat." + name,
            "short_name": name,
            "kind": "function",
            "owners": ["parselmouth.praat"],
            "signature": signature_for(obj),
            "summary": first_sentence(inspect.getdoc(obj)),
        }

    classes = []
    for class_name, cls in public_classes(parselmouth):
        class_doc = first_sentence(inspect.getdoc(cls))
        enum_values = []
        for name in sorted(dir(cls)):
            if name.startswith("_"):
                continue
            value = getattr(cls, name)
            if name[:1].isupper() and not inspect.isclass(value):
                enum_values.append(name)
        classes.append({
            "name": class_name,
            "summary": class_doc,
            "enum_values": enum_values,
        })
        for name, value in inspect.getmembers(cls):
            if name.startswith("_") or name[:1].isupper():
                continue
            kind = member_kind(cls, name, value)
            if kind not in {"method", "property"}:
                continue
            entry = grouped.setdefault(name, {
                "name": name,
                "short_name": name,
                "kind": kind,
                "owners": [],
                "signature": signature_for(value) if kind == "method" else "",
                "summary": first_sentence(inspect.getdoc(value)),
            })
            if class_name not in entry["owners"]:
                entry["owners"].append(class_name)
            if entry["kind"] != kind:
                entry["kind"] = "method/property"

    return {
        "parselmouth_version": getattr(parselmouth, "__version__", ""),
        "praat_version": getattr(parselmouth, "PRAAT_VERSION", ""),
        "source_url": SOURCE_URL,
        "classes": sorted(classes, key=lambda item: item["name"].lower()),
        "functions": sorted(grouped.values(), key=lambda item: item["name"].lower()),
    }


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    manifest = build_manifest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "Wrote {0} Parselmouth functions across {1} classes to {2}".format(
            len(manifest["functions"]), len(manifest["classes"]), output
        )
    )


if __name__ == "__main__":
    main(sys.argv)
