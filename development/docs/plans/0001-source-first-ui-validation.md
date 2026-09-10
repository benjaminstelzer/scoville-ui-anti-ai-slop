---
format_version: 1
id: PLAN-0001
status: active
created: 2026-09-10
updated: 2026-09-10
current_item: W-004
---

# Fix source-first UI validation and geometry proof

## Goal

Make Scoville UI require source correction before rendered validation, measured geometry and peer comparisons for affected layout relationships, justified customization, and fresh visual evidence after the final change. Obtain Astra's independent review at high effort before implementation, replacing Fable as explicitly requested. The companion WordPress plan owns platform-specific rules; each Skill must remain independently usable.

## Non-goals

The user now authorizes Skill implementation, local Skill updates and publication after clean final reviews and required checks. Do not edit unrelated plugins or projects. Do not impose a new spacing scale, universal equal heights, arbitrary pixel tolerances, a full-page audit for a local fix, or mandatory browser checks for a source-only request. Do not treat prompt instructions or structural tests as technical enforcement or evidence of model reliability.

## Work items

### W-001 Enforce ordered source and rendered validation

Status: done
Depends on: []
Blocked by: []
Decisions: [ADR-0001]
Outcome: The entrypoint and routed references define one non-optional source-first validation sequence for affected implementation work with explicit audit and unavailable-tool boundaries.
Acceptance: Inspect SKILL.md and references/framework-alignment.md, ui-quality.md and validation.md for consistent routing and gates; run available package checks and git diff --check; verify that no optional phrase can bypass an applicable gate and that standalone, composed, source-only and audit modes preserve scope and authority. Behavioral acceptance is owned by W-002 and cannot be claimed from this inspection.
Steps:
1. Inspect canonical component, variant, token and layout owners plus the generating code and relevant CSS before any visual inspection; identify expected relationships independently of the changed implementation.
2. Require correction of known in-scope source violations before browser measurement or visual inspection: duplicate parent/child spacing, unjustified dimensions or offsets, token bypass, unnecessary wrappers, overrides and custom primitive rebuilds. Run relevant existing syntax, lint, component or build checks; a build alone is not a design-system audit.
3. Require a pre-write justification for each new or changed custom styling exception, including inline styles and styling props: unmet requirement, concrete owner/API checked, reason it fails and narrow scope. Review the final diff and remove obsolete compensating rules. Legitimate owner-supported composition remains allowed.
4. Before the evaluated measurement, record reference elements/edges, expected relation and justified tolerance from the unchanged owner contract or a demonstrably suitable reference. Never infer an expected value from the candidate CSS or choose tolerance after seeing its result; unresolved expectations stay unresolved. After the source gate passes, measure affected relationships and record target/state/viewport, expected source, actual result and pass/fail. Compare peers sharing relevant role, variant, state, typography and layout conditions; explain deliberate differences. Peer equality alone cannot prove conformity when peers share a faulty override.
5. Preserve the owning source expression and its behavior: units such as em/rem/px/percent, unitless line-height, token references, calculations and logical properties are not interchangeable merely because their current pixel result matches. Record the authored declaration separately from its resolved computed value and measured geometry, including the relevant font/root/container basis. Distinguish border boxes, content boxes, line boxes and visible glyph alignment; rectangles do not prove baselines or optical alignment. Resolve font loading, content, viewport and settled state before measurement; explain wrapping, rounding, margins, padding and intervening elements rather than forcing values equal.
6. Inspect the rendered image after measurement using an explicit visual routine: first the affected region in context for grouping and rhythm, then detail crops for shared content edges, intended text baselines/top edges/centering, apparent whitespace including line-height, control size and internal padding, icon/text alignment, wrapping, clipping, overlap and empty slots. Compare equivalent peers side by side against the named intended relation; record a located deviation or a scoped pass for each applicable lens. Explain non-applicable lenses. Screenshots must actually be viewed; box equality or a generic looks-good statement is insufficient. Do not cosmetically override intentional native differences.
7. Add a short worked diagnostic example in a routed reference: equal outer boxes with different text positions beside an allowed native difference. Compare at the same scale using reference edges or guides where useful; preserve the unaltered crop and context. State the located visual observation before testing hypotheses against font/line-height, internal padding, alignment props and icon viewBox. Separate hypothesis from confirmed cause; unresolved optical judgments stay unverified without invented baseline measurements. Do not require overlays or repetitive prose for every image.
8. Test relevant wrapping, content expansion and changed states; choose widths from the affected layout rather than a universal device matrix. Every subsequent layout edit repeats affected source checks, measurement and the visual routine on the final revision. Separate numeric pass from visual pass and trace an optical failure back to its source owner before correction.
9. Define completion as passed applicable gates or a precise incomplete/unverified result. Available usable tooling cannot be skipped for convenience. An audit never repairs without authorization; source-only and screenshot-only tasks report their evidence limits without inventing missing measurements or broadening scope. Audit tasks report source defects first and may then measure without repairing them.
Evidence: [2026-09-10 canonical source gates and unit-preserving rules implemented; source inspection and package structure checks passed; behavior deferred, 2026-09-10 Fable review not performed: requested claude-fable-5-1 high returned HTTP 429 usage credits exhausted; session 9f924450-7635-4ada-a22f-3a3b37f8c306, Astra UI-FIXPLAN-ASTRA-20260910-01 conditionally approved; task 01a08bb2-d93b-74c2-93ca-57a2006e0896; requested gpt-6-astra high; actual metadata unknown; context fresh, Astra UI-FIXPLAN-ASTRA-20260910-02 conditional: units wording + audit acceptance + sampling; all resolved in -03, Astra UI-FIXPLAN-ASTRA-20260910-03 approved final contract; task 01a08bb2-d93b-74c2-93ca-57a2006e0896; requested gpt-6-astra high; actual metadata unknown; context continued, Final review verified authored units + read-only audit acceptance + sampling limits; source/plan review only; runtime efficacy remains unverified]


### W-003 Account for every in-scope element in consistency audits

Status: done
Depends on: [W-001]
Blocked by: []
Decisions: [ADR-0001]
Outcome: A request to audit page X for consistency selects a read-only consistency profile with an explicit inventory and reconciled coverage instead of checking only conspicuous elements or the first viewport.
Acceptance: Entry routing recognizes ordinary consistency requests without a special invocation. Every inventory item has a named owner/reference and an explicit pass, defect, unverified or justified not-applicable result for each applicable source/geometry/visual stage. No required unverified item or partial sample can yield an unqualified complete page-consistency pass. State uninspected populations/variants as coverage limits; all distinct in-scope variants and known exceptions remain inventory requirements. Standalone and composed audits preserve page scope and read-only authority; W-002 executes omission regressions.
Steps:
1. Keep audit intent separate from focus: consistency on the named page covers its relevant hierarchy, typography, spacing, edges, control variants, icons, containers and states; a named subregion restricts the inventory. Do not convert this focus into a redesign, full accessibility audit or review of the whole application.
2. Start with source inspection and inventory page regions, repeated component families and exceptions, including headings, body/label/help/status text, actions, controls, icons, panels, toolbar, data region and footer/pagination where present. Record stable locators or identifiable labels plus equivalence groups. After source findings, reconcile the inventory with final rendered DOM, including lower scroll regions, nested scroll containers and applicable tabs/disclosures/menus/overlays on the same page.
3. Inspect reachable states with read-only interactions and respect permissions; do not submit, save, delete or trigger external actions merely to complete an audit. Inaccessible or unsafe-to-reach states remain individually unverified. Inventory all distinct in-scope variants and known exceptions; representative sampling of repeated/virtualized data supports only findings limited to that coverage, never an unqualified every-row or complete-page consistency pass. Name uninspected populations/variants without requiring enumeration of every virtual row.
4. Match source findings, measurement records and viewed images to inventory entries and final revision/state; compare both within and across relevant groups using owner-backed expectations. Read-only audits report source defects first and then may measure and inspect without unauthorized correction. Expand the inventory when interaction reveals new relevant elements.
5. Close the audit by reconciling every discovered entry with its evidence and result, including deliberate differences and exclusions; an unmapped item is a coverage gap. Report coverage and remaining gaps separately from severity-ranked defects. Coverage completeness and visual correctness are separate judgments; a percentage or generic all-clear is not proof. When another active Skill shares the audit, reuse one inventory and evidence set while retaining platform ownership.
Evidence: [2026-09-10 entrypoint and reference inventory routes inspected; source/measurement/sight coverage and read-only limits implemented; behavior deferred]

### W-002 Demonstrate the sequence on regression tasks

Status: todo
Depends on: [W-001, W-003]
Blocked by: [USER-DEFERRED-TESTS]
Decisions: [ADR-0001]
Outcome: Executed agent tasks demonstrate source-first correction, truthful measured results and final visual verification without unnecessary CSS or false normalization.
Acceptance: Run the cases below and require the complete ordering predicate in Step 4 plus final source, geometry and visual evidence. Implement cases must detect and correct seeded in-scope defects. Audit cases must accurately locate reachable/testable seeded defects and preserve target artifacts; evaluator-established unavailable evidence or unreachable states require explicit gaps instead. Generic unverified cannot excuse an independently reachable/testable defect. Negative controls preserve legitimate differences. Compare old/revised Skills on matched fresh isolated tasks with identical runtime/content/tools and report per-case observations without claiming statistical reliability. Case definitions or structural checks alone do not satisfy acceptance.
Steps:
1. Extend development/tests/evaluation-cases.json with executable task expectations for declared gap plus child margin, nested padding drift, unnecessary custom control CSS, mismatched same-variant heights, equal outer boxes with misaligned text, wrapping and a hidden child leaving an empty slot. Add equal-initial-pixel negative controls for em/rem/px and unitless line-height: preserve original owner expressions and test independently changed element/root font conditions to expose behavioral substitutions; browser zoom alone does not establish unit equivalence.
2. Include controls for correct native differences, legitimate custom layout, source-only audit, missing renderer and a final CSS edit after an earlier passing screenshot; reuse the companion WordPress cases preserving authored margin: 1em 0 (13px only as the resolved value at the checked 13px element font) versus context-specific authored 4px. Scoville UI must not reinterpret platform-owned values through a generic spacing scale or equate token availability with native use.
3. Establish fixture defects and expected outcomes independently before agent execution; keep defect keys and expected answers with the evaluator, not in the agent prompt. Both old/revised conditions receive identical binding user rules without revised solution steps. Do not derive expected values from candidate CSS. Keep runtime fixtures and raw runs in workspace temp storage and reuse suitable project test seams.
4. Verify the full action-order predicate: source inspection and correction of known in-scope defects precede the first layout measurement; measurement precedes the first viewed rendered image; concrete customization justification precedes its styling write. Source/API/stylesheet inspection is not a layout measurement. After a relevant edit repeat the affected chain; associate final measurements and viewed images with the same final revision and state. Audit cases report source defects first and may measure without repairs. Inspect actual tools and evidence rather than self-report; the equal-box optical case must yield a located observation and independently confirmed cause while the native control remains unchanged.
5. Run the ordinary page-consistency audit prompt against evaluator-known omissions: a faulty footer below the first viewport, a distinct control variant in a collapsed section, an in-scope overlay and repeated labels with one outlier. Require each reachable/testable known target in the inventory with a located finding; allow explicit unverified only for evaluator-established evidence limits. A clean first viewport or partial sample must not yield an unqualified complete-page pass. Include an unreachable state and justified virtualized-row sampling with named uninspected population to verify honest limits and unchanged artifacts.
6. Rerun failed cases after corrections and report exact coverage and remaining limits. Keep only a concise maintenance summary; retain permanent evaluation evidence only when linked by a published release, following workspace retention rules.
Evidence: [2026-09-10 user explicitly deferred extensive Skill behavior testing until later; no browser or live-agent qualification claimed]
Next action: Resume the specified regression tasks when the user requests testing; do not execute them during this implementation and release.

### W-004 Install and publish the reviewed Skills

Status: in_progress
Depends on: [W-001, W-003]
Blocked by: []
Decisions: []
Outcome: The locally installed Skills and new GitHub releases match the reviewed canonical packages.
Acceptance: Final Astra high review has no open findings. Lightweight source and structural checks pass; behavior testing is explicitly deferred by the user and remains W-002. Verify installation file manifests, release assets, published commit, repository layout, visibility and one-current-release retention for both named repositories.
Steps:
1. Obtain the requested final Astra high review of both completed Skills and resolve findings without weakening acceptance.
2. Update the existing local Skill installations and verify exact package hashes while preserving unrelated customization.
3. Prepare coherent English README, changelog and release notes, publish new versions and verify assets before retiring older release records/tags.
Evidence: [2026-09-10 final Astra implementation review UI-SKILL-IMPLEMENTATION-ASTRA-20260910-01 approved with no actionable findings, Requested gpt-6-astra high; actual metadata unknown; context continued; reviewer archived; summary development/implementation-review.md, Codex and Claude Code local package manifests match canonical sources; behavior testing deferred]
Next action: Publish v1.2.0 and verify the exact remote commit plus release assets before retiring old versions; W-002 remains deferred.
