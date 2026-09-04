#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


SKILL = ".agents/skills/scoville-ui-anti-ai-slop/SKILL.md"
REFERENCES = {
    "framework": ".agents/skills/scoville-ui-anti-ai-slop/references/framework-alignment.md",
    "quality": ".agents/skills/scoville-ui-anti-ai-slop/references/ui-quality.md",
    "validation": ".agents/skills/scoville-ui-anti-ai-slop/references/validation.md",
}
NEUTRAL = "scope.txt"


def item(case_id: str, task: str, selected: list[str], expected: dict) -> dict:
    selected_reads = [REFERENCES[name] for name in selected]
    required = [SKILL, *selected_reads]
    forbidden = [path for name, path in REFERENCES.items() if name not in selected]
    forbidden.append(NEUTRAL)
    phases = [[SKILL]]
    if selected_reads:
        phases.append(selected_reads)
    return {
        "id": case_id,
        "task_type": "ui_design_composition_probe",
        "prediction": {
            "task_text": (
                "Routing-only hypothetical ownership probe. " + task +
                " Read only applicable UI references. Do not edit files. "
                "Return only the contracted JSON."
            ),
            "files": {NEUTRAL: "No additional context.\n"},
            "output_contract": (
                "Return exactly one JSON object with string keys status, "
                "design_decision_owner, implementation_owner, and proof_owner. "
                "Use only these exact values. status: ok, ui-inactive, owner-conflict, "
                "opted-out, not-active, design-revision-required, or record-required. "
                "owner fields: design, ui, ui-standalone-fallback, incumbent-product-system, "
                "design-bounded, or none."
            ),
            "skill_activation": "explicit",
        },
        "scoring": {
            "expected": expected,
            "required_file_reads": required,
            "forbidden_file_reads": forbidden,
            "exact_once_file_reads": required,
            "required_read_phases": phases,
            "required_command_patterns": [],
            "forbidden_command_patterns": [
                "curl|wget|Invoke-WebRequest|Set-Content|Remove-Item|apply_patch"
            ],
            "max_shell_calls": len(required),
        },
    }


def result(status: str, design: str, implementation: str, proof: str) -> dict:
    return {
        "status": status,
        "design_decision_owner": design,
        "implementation_owner": implementation,
        "proof_owner": proof,
    }


TRAIN = [
    (
        "ui-comp-train-framework-regression",
        "An existing Mantine product system owns tokens, wrappers, and variants. Determine the supported customization path only; new design judgment and rendered proof are out of scope.",
        ["framework"],
        result("ok", "incumbent-product-system", "ui", "none"),
    ),
    (
        "ui-comp-train-quality-regression",
        "The incumbent product system and implementation owner are already settled. Audit task hierarchy, responsive transformation, populated state, and recoverable error using rendered evidence.",
        ["quality", "validation"],
        result("ok", "incumbent-product-system", "ui", "ui"),
    ),
    (
        "ui-comp-train-installed-inactive",
        "Design may be installed but its instructions are absent. UI is active and ownership is otherwise unresolved.",
        ["framework"],
        result("ok", "ui-standalone-fallback", "ui", "ui"),
    ),
    (
        "ui-comp-train-ui-only",
        "UI is active, Design is absent, and a polished Greenfield workflow has no visual owner.",
        ["framework"],
        result("ok", "ui-standalone-fallback", "ui", "ui"),
    ),
    (
        "ui-comp-train-both-active",
        "Design and UI are active. A complete Design record settles hierarchy, workflow, typography, spacing, responsive intent, and validation target. Classify implementation and proof ownership without re-judging design.",
        ["framework", "validation"],
        result("ok", "design", "ui", "ui"),
    ),
    (
        "ui-comp-train-incumbent",
        "An incumbent product design system conflicts with an active Design proposal. Classify precedence and implementation ownership. No proof plan is requested now, but report the canonical proof owner for any later UI implementation.",
        ["framework"],
        result("owner-conflict", "incumbent-product-system", "ui", "ui"),
    ),
    (
        "ui-comp-train-design-optout",
        "The user explicitly excludes Design but keeps UI active for a polished Greenfield component with no visual owner.",
        ["framework"],
        result("ok", "ui-standalone-fallback", "ui", "ui"),
    ),
]

VAL = [
    (
        "ui-comp-val-evidence-only-regression",
        "An active Design record fixed the UI decision. Judge only supplied rendered and interaction evidence; do not choose layout, design direction, or customization path.",
        ["validation"],
        result("ok", "design", "ui", "ui"),
    ),
    (
        "ui-comp-val-ui-optout",
        "The user explicitly excludes UI while Design remains active. Apply UI's opt-out gate.",
        [],
        result("opted-out", "design", "none", "none"),
    ),
    (
        "ui-comp-val-constraint-loop",
        "Both Skills are active. UI finds a real framework constraint that blocks one settled responsive Design decision. Classify ownership after reporting the conflict and before re-implementation; proof planning and rendered claims come only after the revised implementation.",
        ["framework", "quality"],
        result("design-revision-required", "design", "ui", "ui"),
    ),
]

TEST = [
    (
        "ui-comp-test-active-design-implementation",
        "Design and UI are active. A complete Design record settles a new account-recovery workflow, responsive intent, typography, and spacing. Implement it through the supported framework path and prove keyboard, error, loading, and narrow-width behavior.",
        ["framework", "quality", "validation"],
        result("ok", "design", "ui", "ui"),
    ),
    (
        "ui-comp-test-incumbent-accessibility",
        "Design is absent. An incumbent product system fixes the visual language. UI must correct semantics, focus order, validation messaging, and responsive state behavior without redefining tokens or art direction, then supply rendered and interaction proof.",
        ["framework", "quality", "validation"],
        result("ok", "incumbent-product-system", "ui", "ui"),
    ),
    (
        "ui-comp-test-inapplicable-design-greenfield",
        "Design instructions are present but explicitly inapplicable to this concern. UI remains active for a Greenfield transactional flow with no incumbent visual owner and must implement and validate all required states.",
        ["framework", "quality", "validation"],
        result("ok", "ui-standalone-fallback", "ui", "ui"),
    ),
    (
        "ui-comp-test-bounded-design-with-system",
        "An incumbent system fixes tokens and component variants. Active Design has chosen the page hierarchy and workflow inside those constraints. UI must map that bounded decision to supported components and provide responsive and state proof.",
        ["framework", "validation"],
        result("ok", "design-bounded", "ui", "ui"),
    ),
]


def write(root: Path, split: str, cases: list[tuple]) -> None:
    path = root / split / "items.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([item(*case) for case in cases], indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    root = Path(__file__).resolve().parent
    write(root, "train", TRAIN)
    write(root, "val", VAL)
    write(root, "test", TEST)
    print(f"wrote composition benchmark: train={len(TRAIN)} val={len(VAL)} test={len(TEST)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
