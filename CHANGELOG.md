# Changelog

## v1.2.2 - 2026-09-11

- Group related UI changes before source checks, measurements and visual
  inspection. Run validation after the completed batch instead of taking
  screenshots after each small edit.
- Group any corrections found during validation and recheck affected concerns
  after that correction batch is complete. Final evidence still needs to match
  the final revision, content and state.
- Browser and live-agent regression testing has not been run for this change.

## v1.2.0 - 2026-09-10

- Require source correction before measurement and viewed-render checks. Add a
  consistency inventory and explicit visual comparisons, with authored units,
  independent expectations and before-write custom styling justification.
- Keep framework owners and platform exceptions intact across standalone and
  composed audits.
- Defer behavior regression testing. This release makes no new browser,
  live-agent or cross-host qualification claim.

## v1.1.3 - 2026-09-09

- Require host-provided render and interaction tools for visual proof. Source
  and build checks alone cannot establish rendered behavior.

## v1.1.0 - 2026-09-04

- Let an active Scoville Design Skill own visual direction, hierarchy,
  typography, spacing judgment, and art direction.
- Keep framework implementation, component states, semantics, focus and input
  behavior, announcements, responsive mechanics, accessibility, and rendered
  proof with Scoville UI.
- Preserve the incumbent product design system above a new proposal.
- Keep a bounded standalone Greenfield fallback when Design is absent,
  inactive, inapplicable, or explicitly excluded.
- Added a Design-to-UI handoff and a constraint loop that returns only the
  affected decision instead of silently redesigning the interface.

## v1.0.11 - 2026-08-11

- Made every Scoville Skill optional and independently usable. Discovering a
  sibling does not install or activate it.

## 2026-08-07: Progressive disclosure

- Load framework diagnosis, detailed quality guidance, and rendered validation
  only when the current interface task needs them.
- Keep framework ownership, family boundaries, interface integrity, and
  reference routing in the Core.
- Require every missing requested proof, such as mobile, zoom, keyboard, touch,
  screen reader, reduced motion, or automated accessibility coverage, to remain
  visible in the conclusion.

## 2026-08-06: Greenfield direction and representative evidence

- Require polished Greenfield work to choose a deliberate visual direction
  grounded in the product domain without prescribing a palette or template.
- Require representative populated evidence at each requested viewport, with
  realistic density, content length, hierarchy, and interaction state.
- Keep primary populated states separate from error and recovery evidence.

## 2026-08-06: Cross-input validation and narrower Scribe routing

- Require a relevant cross-input handoff check when focus, selection, capture,
  composition, or shared state can change behavior between input methods.
- Do not treat separate clean-start pointer, keyboard, or touch passes as proof
  of a stateful transition.
- Activate Scribe only when interface wording or meaning must be created,
  changed, localized, audited, or reconciled with behavior.

## 2026-08-03: Initial release

- Added framework-aware implementation and audit guidance for web, native
  mobile, desktop, and terminal interfaces.
- Added routing for design systems, headless libraries, utility frameworks,
  platform UI stacks, mixed stacks, and true Greenfield work.
- Added guidance for hierarchy, states, responsive adaptation, accessibility,
  and rendered evidence without prescribing a visual style.
