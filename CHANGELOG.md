# Changelog

## 2026-08-06: Cross-input validation and narrower Scribe routing

### Changed

- Required one relevant handoff between input methods when focus, selection,
  capture, composition, or shared state can make the transition behaviorally
  distinct.
- Clarified that separate clean-start passes for pointer, keyboard, touch, or
  other methods do not prove a stateful transition between them.
- Limited Scribe composition to interface work where wording or meaning must be
  created, changed, localized, audited, or reconciled with behavior.

### Validation

- The installable directory passed the canonical Agent Skill validator.
- A focused interaction review confirmed that pointer focus affecting a later
  keyboard activation now selects a same-task cross-input check.

## 2026-08-03: Family documentation alignment

### Changed

- Aligned the README structure and installation guidance with Scoville Code and
  Scoville Scribe.
- Added the UI-specific explanation of the Scoville family name.
- Kept published repository documentation focused on the installable skill and
  its supported behavior.

### Validation

- The installable directory passed the canonical Agent Skill validator.
- README links, documented word costs, and repository contents matched the
  current files.
- Published documentation contains only product, installation, design, and
  validation information.

## 2026-08-03: Initial release

### Added

- A framework-aware UI quality contract for interactive web, native mobile,
  desktop, and terminal interfaces.
- Concern-specific routing for styled design systems, headless component
  libraries, utility and application frameworks, platform UI stacks, mixed
  stacks, and true greenfield work.
- General guidance for task and information hierarchy, readable content,
  interaction states, responsive adaptation, accessibility, and rendered
  evidence without a prescribed visual style.
- Explicit composition boundaries with `scoville-code-anti-ai-slop` and
  `scoville-scribe-anti-ai-slop`.
- Focused references for framework alignment, UI quality, and rendered
  validation.

### Validation

- The canonical Agent Skill validator accepted the installable directory and no
  placeholders remained.
- Fresh host sessions covered non-visual UI activation, backend non-activation,
  and Mantine design-system ownership.
