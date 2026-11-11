#!/usr/bin/env python3
"""Scaffold a new day's folder and update the progress table in the root README.

Usage:
    python scripts/new_day.py 2 "file-organizer" --topic "Batch-organize files"

This creates days/day002-file-organizer/ with a TODO-only main.py and a README
based on the daily template, then fills in the date, topic and link for day 002
in the root README progress table. The status column is left untouched.

Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DAYS_DIR = REPO_ROOT / "days"
ROOT_README = REPO_ROOT / "README.md"

TOTAL_DAYS = 100
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TABLE_START = "<!-- progress:start -->"
TABLE_END = "<!-- progress:end -->"
# Split a Markdown table row on pipes that are not escaped as "\|".
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")

MAIN_TEMPLATE = '''\
"""Day {num}: {doc_title}"""


def main() -> None:
    # TODO: write today's exercise here.
    pass


if __name__ == "__main__":
    main()
'''

README_TEMPLATE = """\
# Day {num}: {title}

- **Date:** {date}
- **Folder:** `{folder}`

## Goal

<!-- What should this script do by the end of today? One or two sentences. -->

## Concepts Used

<!-- Syntax, modules and libraries touched today. -->

- ...

## Problems Encountered

<!-- One block per problem: symptom → cause → fix. Remove the block if nothing went wrong. -->

### 1. Short title

- **Symptom:** ...
- **Cause:** ...
- **Fix:** ...

## Improvements for Tomorrow

- ...
"""


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def slug_to_title(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def escape_cell(text: str) -> str:
    """Make text safe to put inside a single Markdown table cell."""
    return text.replace("|", r"\|").replace("\n", " ").strip()


def update_progress_row(readme: str, num: str, date: str, topic: str, link: str) -> str:
    """Return the README text with the progress row for `num` filled in.

    Only the date, topic and link cells change; the status cell is preserved.
    """
    start = readme.find(TABLE_START)
    end = readme.find(TABLE_END)
    if start == -1 or end == -1 or end < start:
        fail(f"progress table markers not found in {ROOT_README.name}")

    head, table, tail = readme[:start], readme[start:end], readme[end:]
    row_re = re.compile(rf"^\|\s*{num}\s*\|.*$", re.MULTILINE)
    match = row_re.search(table)
    if match is None:
        fail(f"no row for day {num} in the progress table")

    cells = [cell.strip() for cell in CELL_SPLIT_RE.split(match.group(0))[1:-1]]
    if len(cells) != 5:
        fail(f"row for day {num} does not have 5 columns: {match.group(0)!r}")
    status = cells[3]

    new_row = f"| {num} | {date} | {escape_cell(topic)} | {status} | {link} |"
    table = table[: match.start()] + new_row + table[match.end() :]
    return head + table + tail


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create days/dayNNN-<slug>/ and update the README progress table.",
    )
    parser.add_argument("day", type=int, help=f"day number (1-{TOTAL_DAYS})")
    parser.add_argument("slug", help='short kebab-case name, e.g. "file-organizer"')
    parser.add_argument("--topic", help="one-line topic for the progress table")
    args = parser.parse_args(argv)

    if not 1 <= args.day <= TOTAL_DAYS:
        parser.error(f"day must be between 1 and {TOTAL_DAYS}, got {args.day}")
    if not SLUG_RE.match(args.slug):
        parser.error(
            f"slug must be lowercase letters, digits and single hyphens, got {args.slug!r}"
        )
    return args


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    num = f"{args.day:03d}"
    topic = " ".join((args.topic or "").split()) or slug_to_title(args.slug)
    title = topic
    date = dt.date.today().isoformat()
    folder_name = f"day{num}-{args.slug}"
    day_dir = DAYS_DIR / folder_name

    if day_dir.exists():
        fail(f"{day_dir.relative_to(REPO_ROOT)} already exists; refusing to overwrite")
    existing = sorted(DAYS_DIR.glob(f"day{num}-*"))
    if existing:
        fail(f"day {num} already has a folder: {existing[0].relative_to(REPO_ROOT)}")
    if not ROOT_README.is_file():
        fail(f"{ROOT_README} not found")

    # Build the new README text first so a bad table aborts before any file is created.
    link = f"[{folder_name}](days/{folder_name}/)"
    readme = ROOT_README.read_text(encoding="utf-8")
    new_readme = update_progress_row(readme, num, date, topic, link)

    day_dir.mkdir(parents=True)
    fields = {
        "num": num,
        "title": title,
        "doc_title": title.replace("\\", "/").replace('"""', "'''"),
        "date": date,
        "folder": folder_name,
    }
    (day_dir / "main.py").write_text(MAIN_TEMPLATE.format(**fields), encoding="utf-8")
    (day_dir / "README.md").write_text(README_TEMPLATE.format(**fields), encoding="utf-8")
    ROOT_README.write_text(new_readme, encoding="utf-8")

    print(f"Created {day_dir.relative_to(REPO_ROOT)}/ (main.py, README.md)")
    print(f"Updated progress row for day {num} in README.md")


if __name__ == "__main__":
    main()
