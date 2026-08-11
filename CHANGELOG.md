# Changelog

## 2026-08-11: README voice and structure (v1.0.12)

### Changed

- Reworked the public README opening in Benjamin's voice while preserving the
  Skill's activation boundary, mechanism, evidence, sources, and measured
  status.
- Kept the shared Scoville section order and family copy aligned across all six
  project READMEs.
- Updated the Codex Skill-list description to use the same public voice.

### Validation

- Agent Skill package, README structure, shared-copy, internal-link, and
  Markdown whitespace checks passed.
- No model-behavior benchmark was run because the Skill instructions did not
  change.

## 2026-08-11: Standalone family contract (v1.0.11)

### Changed

- Clarified that every Scoville Skill works independently and that family
  discovery does not imply installation, activation, applicability, or a
  dependency.
- Added all five current siblings with scoped ownership and kept sibling
  opt-out local to that sibling.
- Reduced repeated Core wording while retaining the existing activation
  metadata, UI ownership, accessibility floor, and rendered-evidence boundary.

### Validation

- The central family-contract test passed all six packages and rejected all
  five synthetic drift cases; Agent Skill package validation also passed.
- No new model-behavior benchmark was run for this patch release.

## 2026-08-11: Scoville Brainstorm sibling (v1.0.10)

### Changed

- Added Scoville Brainstorm to the optional family composition guide and
  separated pre-decision mechanism exploration from UI judgment.
- Added copy-ready design, audit, and implementation examples.
- Reduced installation, cost, mechanism, and family documentation while
  retaining the Scoville name rationale, sources, and benchmark evidence.
- Added a family run ledger and reconciled the public total across all six
  Scoville Skills.

## 2026-08-10: Scoville Handoff sibling

### Changed

- Added Scoville Handoff to the optional family composition guide and
  reconciled the public run total across all five Scoville Skills.

## 2026-08-10: Clearer usage trade-offs

### Changed

- Explain that activating the Skill adds prompt context and is best suited to
  work where design-system alignment, accessibility, responsive behavior, and
  rendered evidence justify the additional token cost.
- Remove the inline verification example and clarify that the public token
  comparison uses the pre-optimization release.

## 2026-08-10: Reliability-qualified compression

### Changed

- Recast the core as a compact owner, gate, workflow, and reference-routing
  contract while preserving the complete UI integrity floor.
- Made local-exception handling explicit: preserve deliberate current intent,
  normalize proven accidents through the canonical owner, and leave unknown
  intent unresolved.
- Clarified that a requested polished greenfield surface owns its deliberate
  local direction while framework defaults remain primitives rather than the
  visual owner.

### Validation

- The frozen paired benchmark passed Train 18/18, Val 9/9, and sealed Test 3/3
  for both the reliability control and compressed package across routing,
  semantic result, process, and efficiency gates.
- All 60 arm-case executions completed with provider usage, no routing retry,
  no shell call, and exact-once routed reads.
- Core size fell from 1,173 to 1,050 tokens (-10.49%) against the equally
  reliable control. Loaded Skill context across the 30 compressed executions
  fell from 71,691 to 68,370 tokens (-4.63%).
- Against the preceding GitHub package, the final core is 27 tokens smaller;
  the complete package is 88 tokens larger because the reliability repair in
  the framework reference is retained.
- The canonical Agent Skill validator passes. The benchmark used
  `gpt-5.6-terra` at medium reasoning and does not establish behavior on weaker
  executors or arbitrary tasks.

## 2026-08-08: Explicitly optional family composition

### Changed

- Made all sibling Skills explicitly optional: UI remains complete for its own
  concerns and neither requires, installs, nor simulates Plan, Code, or Scribe.

### Validation

- The canonical Agent Skill validator and repository diff checks pass.
- Fable's complete standalone and family review found no remaining UI issue,
  hard sibling dependency, ownership gap, or cycle.
- The tested repository copy and the locally installed Skill are byte-identical.

## 2026-08-07: Progressive disclosure

### Changed

- Reduced the always-loaded core by moving framework diagnosis, detailed UI
  quality rules, and rendered-validation procedures to their existing focused
  references.
- Kept framework ownership, family boundaries, the non-negotiable interface
  integrity floor, audit-only behavior, and reference routing in the core.
- Shortened the frontmatter description while preserving positive, negative,
  sibling-composition, and opt-out boundaries.
- Limited rendered validation to changed or claimed rendered behavior; a
  source-only audit can remain reference-free when it states the unrendered
  boundary explicitly.
- Required named missing evidence such as mobile, zoom, keyboard, touch, screen
  reader, reduced motion, and automated accessibility coverage to remain
  individually visible in the conclusion.

### Validation

- The canonical Agent Skill validator passes.
- Six focused standalone routing cases passed with `gpt-5.6-sol` at medium
  reasoning, including framework ownership, greenfield direction, rendered
  evidence, source-only audit, quality-only work, and fixed strings.
- The full UI/Code/Scribe composition and the source-only Scribe opt-out case
  passed with only their required references.
- The same six standalone cases passed with `gpt-5.6-terra` at medium
  reasoning. Both composition cases also preserved their required ownership,
  fixed-string, opt-out, and evidence boundaries.
- Direct-reference, diff, encoding, and host-neutrality checks pass.

## 2026-08-06: Standalone sibling-Skill composition

### Changed

- Made Scribe routing explicitly conditional so UI remains fully usable when
  no sibling Skill is installed.
- Recounted the documented Skill and reference word costs.

### Validation

- The canonical Skill validator passes and the documented counts match the
  current files.

## 2026-08-06: Greenfield direction and representative evidence

### Changed

- Required polished true-greenfield work to choose a deliberate visual
  direction grounded in the product domain and apply it consistently without
  prescribing a palette or template.
- Required representative populated evidence with realistic density, content
  length, hierarchy, and interaction state at each requested target viewport.
- Separated primary populated-state evidence from error and recovery evidence.

### Validation

- Evaluation fixtures cover a polished greenfield task, framework-owned visual
  work, and separate desktop, mobile, and recovery observations.

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
