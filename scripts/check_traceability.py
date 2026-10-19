"""Fail if any requirement ID cited in the docs is not defined in the requirements document."""

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
REQ_CANDIDATES = [DOCS / "Requirements.md"]
ID_PATTERN = re.compile(r"\bN?FR-\d+(?:\.\d+)?\b")
# A definition is the first cell of a table row: "| FR-2.1 |"
DEF_PATTERN = re.compile(r"^\|\s*(N?FR-\d+(?:\.\d+)?)\s*\|", re.MULTILINE)


def main() -> int:
    req_file = next((p for p in REQ_CANDIDATES if p.exists()), None)
    if req_file is None:
        print("ERROR: docs/Requirements.md not found")
        return 1

    defined = set(DEF_PATTERN.findall(req_file.read_text(encoding="utf-8")))
    print(f"{len(defined)} requirement IDs defined in {req_file.relative_to(DOCS.parent)}")

    failures = 0
    for doc in sorted(DOCS.glob("*.md")):
        if doc == req_file:
            continue
        for lineno, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
            for ref in ID_PATTERN.findall(line):
                if ref not in defined:
                    print(f"{doc.relative_to(DOCS.parent)}:{lineno}: {ref} is not defined in requirements")
                    failures += 1

    if failures:
        print(f"FAIL: {failures} undefined requirement reference(s)")
        return 1
    print("PASS: every cited requirement ID is defined")
    return 0


if __name__ == "__main__":
    sys.exit(main())
