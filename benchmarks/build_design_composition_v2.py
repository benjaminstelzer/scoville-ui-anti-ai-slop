#!/usr/bin/env python3
"""Create the adjudicated W-004 composition regression suite without rewriting v1."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "scoville-ui-design-composition-v1"
TARGET = ROOT / "scoville-ui-design-composition-v2"
SKILL = ".agents/skills/scoville-ui-anti-ai-slop/SKILL.md"
FRAMEWORK = ".agents/skills/scoville-ui-anti-ai-slop/references/framework-alignment.md"
QUALITY = ".agents/skills/scoville-ui-anti-ai-slop/references/ui-quality.md"
VALIDATION = ".agents/skills/scoville-ui-anti-ai-slop/references/validation.md"
NEUTRAL = "scope.txt"


def main() -> int:
    for split in ("train", "val", "test"):
        items = json.loads((SOURCE / split / "items.json").read_text(encoding="utf-8"))
        items = copy.deepcopy(items)
        for item in items:
            if item["id"] != "ui-comp-test-bounded-design-with-system":
                continue
            required = [SKILL, FRAMEWORK, QUALITY, VALIDATION]
            item["scoring"].update(
                {
                    "required_file_reads": required,
                    "forbidden_file_reads": [NEUTRAL],
                    "exact_once_file_reads": required,
                    "required_read_phases": [[SKILL], [FRAMEWORK, QUALITY, VALIDATION]],
                    "max_shell_calls": len(required),
                }
            )
        out = TARGET / split / "items.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("wrote adjudicated UI composition benchmark-v2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

