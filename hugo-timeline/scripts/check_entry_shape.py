#!/usr/bin/env python3
"""Refuse timeline entries whose frontmatter has lost its shape.

Guards the failure of 2026-11-14: an update hand-spliced into an entry dropped
the `claims:` line, so the claim records parsed as items of `actors:` and the
site build crashed (generate_content.py: unhashable type 'dict').

Checks, per entry:
  - frontmatter parses as a mapping;
  - string lists (actors, tags, previous_ids) hold only strings;
  - claims, when present, is a list of mappings, each with an id;
  - claim records (mappings with id + span/value) appear only under claims;
  - event_date_claim, when set, names a claim that exists;
  - every id in updates[].claims names a claim that exists.

Usage: check_entry_shape.py [FILE ...]   (no files: every cascade-timeline/*.md)
Exit 0 clean, 1 with one line per problem.
"""
import sys
from pathlib import Path

import yaml

STRING_LISTS = ("actors", "tags", "previous_ids")
ROOT = Path(__file__).resolve().parents[2] / "cascade-timeline"


class StrLoader(yaml.SafeLoader):
    pass


# dates stay strings, as the generator reads them
StrLoader.add_constructor("tag:yaml.org,2002:timestamp", lambda l, n: l.construct_scalar(n))


def is_claim(x):
    return isinstance(x, dict) and "id" in x and ("span" in x or "value" in x)


def problems(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end < 0:
        return ["frontmatter never closes"]
    try:
        fm = yaml.load(text[3:end], Loader=StrLoader)
    except yaml.YAMLError as e:
        return [f"frontmatter does not parse: {str(e).splitlines()[0]}"]
    if not isinstance(fm, dict):
        return ["frontmatter is not a mapping"]
    out = []
    for key in STRING_LISTS:
        v = fm.get(key)
        if v is None:
            continue
        if not isinstance(v, list):
            out.append(f"{key} is not a list")
        elif any(not isinstance(x, str) for x in v):
            n = sum(is_claim(x) for x in v)
            out.append(f"{key} holds non-string items" + (f" ({n} claim records: is the `claims:` line missing?)" if n else ""))
    for key, v in fm.items():
        if key != "claims" and key not in STRING_LISTS and isinstance(v, list) and any(is_claim(x) for x in v) \
                and key not in ("updates",):
            out.append(f"claim records under `{key}:` (they belong under `claims:`)")
    ids = set()
    if "claims" in fm:
        c = fm["claims"]
        if not isinstance(c, list) or any(not isinstance(x, dict) or "id" not in x for x in c):
            out.append("claims is not a list of records with ids")
        else:
            ids = {str(x["id"]) for x in c}
    edc = fm.get("event_date_claim")
    if edc and ids and str(edc) not in ids:
        out.append(f"event_date_claim {edc} names no claim")
    if edc and not ids and "claims" not in fm:
        out.append(f"event_date_claim {edc} set but `claims:` is missing")
    for u in fm.get("updates") or []:
        if isinstance(u, dict):
            missing = [str(i) for i in u.get("claims") or [] if str(i) not in ids]
            if missing:
                out.append(f"update {u.get('date')} cites missing claims {missing}")
    return out


def main(argv):
    files = [Path(a) for a in argv if a.endswith(".md")] if argv else sorted(ROOT.glob("*.md"))
    bad = 0
    for f in files:
        if not f.exists():
            continue
        for p in problems(f):
            print(f"{f.name}: {p}")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
