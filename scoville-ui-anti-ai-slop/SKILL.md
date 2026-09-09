---
name: scoville-ui-anti-ai-slop
description: Framework-aware guardrail for implementing and auditing UI through the product framework and incumbent design system. Use for components, states, responsiveness, accessibility mechanics, interaction, and rendered proof. When Scoville Design is active and applicable, consume its design decisions without re-deciding them; otherwise retain a bounded standalone Greenfield fallback. Excludes backend-only work and prose.
compatibility: "Any Agent Skills host that can read references/ and run the project's framework toolchain. Rendered and interaction proof needs a browser, renderer or screenshot tool provided by the host; build or source alone cannot prove rendering. No bundled scripts, no network access required. Developed for Codex and Claude Code; other hosts untested."
---

Implement and verify UI through its canonical framework, platform, and design
system. Do not silently redesign a settled concern.

## Gates and owners

**OPT-OUT:** If the user explicitly excludes this Skill, STOP before references,
Skill tools, changes, or Skill-derived completion claims. If higher-authority
host/project rules require it, report exact conflict.

Apply the highest owner per concern:

1. system, safety, legally binding accessibility;
2. explicit user request, including informed acceptance of a reported
   limitation against a non-binding target;
3. repository instructions;
4. canonical product requirements, design-system components, wrappers, themes,
   semantic tokens, approved assets;
5. an active and applicable Scoville Design decision for the concern;
6. owning framework/platform for unresolved concerns;
7. deliberate owner-aligned local patterns;
8. this Skill's standalone principles for the remaining gap.

Lower sources never override higher owners; report material conflicts.

- **LOCAL:** A repeated pattern counts only if deliberate, current, and right for
  the same surface.
- **UNKNOWN EXCEPTION:** Ownership is unresolved. Inspect or ask; normalize only
  with evidence it is accidental or stale.
- **DESIGN ACTIVE:** Only instructions present in the current task context count
  as active, and only for the concrete concern. Consume its compact decision
  record without re-deciding hierarchy, workflow, responsive transformation
  intent, corporate-design/visual-identity constraints, design-system
  definition, typography, spacing, colour, imagery, or visual style. Never
  search for or simulate the sibling.
- **GREENFIELD FALLBACK:** If Design is absent, inactive, inapplicable, or
  explicitly excluded and no visual owner exists, retain this Skill's bounded
  standalone direction; framework defaults remain primitives.
- **ACCESSIBILITY:** No target: web uses WCAG 2.2 AA; elsewhere use current
  platform guidance; always use supported components and APIs.
- **OWNER LIMIT:** Report exact canonical owner and limit; no parallel language.
  Informed acceptance may waive the reported non-binding target, never higher
  system, safety, or legal rules.

## Skill family

Family standalone: discovery != installed|active|applicable|required;
absent|inactive => ignore/no require|install|simulate|reimplement;
active+applicable => owner concern only, self continues; opt-out local. Owners:
`scoville-brainstorm` divergence;
`scoville-code-anti-ai-slop` engineering/proof;
`scoville-scribe-anti-ai-slop` wording/fidelity; `scoville-plan`
records/lifecycle; `scoville-handoff` transfer.

`scoville-design-anti-ai-slop`, when active and applicable, owns design
definition and visual judgment. UI owns framework-valid implementation,
component semantics and states, focus/input behavior, announcements,
responsive mechanics, and rendered/interaction proof. Each Skill stays useful
alone; discovery or installation does not change ownership.

UI owns presentation and required label/accessibility-name existence and
association. Fixed source-exact strings do not activate Scribe.
When active, Scribe owns what text says; UI owns its presentation. Do not copy
or reverify siblings.

## Workflow

1. Inspect as needed: surface, repository rules, framework version, canonical
   owners, nearest comparable surface.
2. Resolve Design applicability from current context only. If a consequential
   Design record exists, consume `concern`, `canonical owner`,
   `decision/status`, `intended effect`, `authority/source/version`,
   `preserved constraints`, `allowed variation`, any `deliberate exception and
   compensation`, `validation target`, `current evidence status`, and
   `unknowns`. An unresolved or invalidated field is not permission to invent a
   replacement.
3. Identify implementation concerns: affected components and states, content
   variation, inputs, breakpoints/adaptation mechanisms, semantics, and proof.
4. Reuse canonical components, tokens, variants, layouts, breakpoints, and
   interactions. Add a primitive only for a demonstrated owner gap.
5. Make the smallest framework-valid change. If a real implementation
   constraint conflicts with Design, report it against the affected record;
   Design revises that decision and UI re-implements it. Do not silently redesign.
6. Verify only rendered conditions able to disprove. Report rendered, source,
   and unverified evidence separately. Mark unimplemented or source-only work
   unrendered and rendered behavior unverified; never load Validation merely to
   state this boundary. Rendered and interaction proof requires a host-provided
   browser, renderer, or screenshot capability whose output the agent can
   actually view. Without it, report rendered and interaction behavior as
   unverified. Build, source, or an unviewed screenshot file never substitutes.

## Reference router

**OWNERSHIP-ONLY:** For a routing-only hypothetical asking only for status and
owners, load Framework when ownership or fallback is unresolved. Omit Quality
and Validation unless also judging UI/design quality, implementation mechanics,
or proof. Greenfield or polished intent alone does not broaden this route.

- **Framework:** Load
  [framework-alignment.md](references/framework-alignment.md) before choosing an
  owner if stack unfamiliar, ownership ambiguous, UI layers interact, no
  canonical visual owner exists, or customization path is uncertain.
- **Quality:** Load [ui-quality.md](references/ui-quality.md) before judging task
  flow, hierarchy, layout, readability, states, accessibility structure, or
  responsive behavior that an active Design record has not already settled, or
  when implementation mechanics could violate the settled intent.
- **Validation:** Load [validation.md](references/validation.md) after an
  interface change or before claims of rendered/responsive behavior, observed
  interaction, visual quality, or accessibility. Build/source cannot prove
  rendering.

**EVIDENCE-ONLY:** UI decision fixed; judge proof only. Load Validation alone
unless judging UI. Classifying the problem or owner, choosing layout, or
selecting remaining rendered checks requires Quality and Validation.

**COMPOSED:** A Design record settles the design concern. Load Framework for
the canonical implementation path and Validation for the requested proof.
Load Quality for unresolved design gaps or whenever implementation must reason
about component states, semantics, accessibility structure, focus/input,
announcements, or responsive mechanics; never to re-litigate the supplied
design decision.

**SOURCE-ONLY AUDIT:** If structure-only, omit Validation; explicitly mark
rendered/interactive behavior unverified. For unimplemented direction, omit it
only to report the same unrendered boundary.

## Integrity floor

Never improve appearance through: parallel visual language; semantic-token
bypass; accessible-component rebuild; removed focus/input accommodation; hidden
required content; meaning carried solely by one visual cue; missing changed-state
recovery; local exception applied through a global theme override.

Never impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoints, pixel values, or fashionable bans. Quantitative rules come only
from the applicable accessibility standard, platform, or design system.

Audit/advice only: return prioritized findings tied to observed evidence; make
no edits.
