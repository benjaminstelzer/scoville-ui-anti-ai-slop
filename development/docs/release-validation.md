# UI v1.1.0 release validation

Checked on 2026-09-04. This release packages the existing optional Design
composition changes. The executable instructions were not changed during
publication preparation.

## Current checks

- Canonical Agent Skill validation passed for the five-file package.
- The Design repository's current boundary validator passed against this
  package and Design v1.0.0, including active Design ownership and UI's
  standalone fallback.
- The package matches the recorded five-file manifest
  `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`.
- The complete `SKILL.md`, including frontmatter, measures 1,533
  `o200k_base` tokens. This is file size, not total execution cost.

The whole-diff whitespace scan reports existing terminal blank lines in the
benchmark records and a Markdown hard break in the historical evidence
header. They are preserved, not reported as a clean whole-diff formatting pass.

The manifest is SHA-256 over lexicographically sorted UTF-8 rows containing
relative path, NUL, byte count, NUL, uppercase file SHA-256 and LF.

## Retained behavior evidence

[Composition evidence](design-composition-evidence.md) records ten
active-context composition cases and later 3/3 open Validation plus 4/4
consumed Test regressions. The record preserves the original failure and Gold
adjudication. These are configuration-specific development and regression
results, not fresh unseen evidence. They were not rerun for this release.

The eleven source-level scenarios in `tests/evaluation-cases.json` describe
activation, opt-outs, standalone fallback, composition and handoff boundaries.
Their presence does not prove those host states were executed.

Historical 30/30 evidence belongs to the earlier UI package. No new full
holdout, cross-host activation proof or general visual-quality claim is made.
The related Design successor has its own release evidence and limitations.
