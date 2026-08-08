---
name: scoville-ui-anti-ai-slop
description: Framework-aware guardrail for UI design, implementation, and audit. Use for hierarchy, layout, states, responsiveness, accessibility, usability, or clarity. Preserve the product design system and platform language. Excludes backend-only work and prose. Compose with Code for engineering and Scribe for variable UI wording.
---

# Scoville UI Anti-AI-Slop

Improve the interface the product has. Treat usability, information design,
adaptation, accessibility, and clarity as outcomes; do not install a second
design language disguised as best practice.

If the user explicitly excludes this Skill, stop before reading a reference,
using a Skill-directed tool, changing anything, or making a Skill-derived
completion claim. A project or host instruction with higher authority may still
require it; report that exact conflict. Excluding a sibling excludes only that
sibling and does not authorize reproducing its contract here.

## Resolve ownership first

Resolve each concern in this order:

1. system, safety, and legally binding accessibility requirements;
2. the explicit user request, including an informed acceptance of a reported
   limitation against a non-binding target;
3. repository instructions;
4. canonical product requirements, design-system components, wrappers, themes,
   semantic tokens, and approved assets;
5. the owning framework or platform for unresolved concerns;
6. deliberate local patterns that agree with those owners; and
7. this Skill's general UI principles for the remaining gap.

Do not let a lower source override a higher owner. Surface a material conflict.
A repeated local convention counts only when it is deliberate, current, and
appropriate to the same surface.

When no accessibility target is named, use WCAG 2.2 Level AA for web UI and the
owning platform's current guidance elsewhere. Use supported components and APIs.
If the canonical owner cannot meet the floor, report the exact limitation rather
than concealing it with a parallel design language.

Read [framework-alignment.md](references/framework-alignment.md) before deciding
an owner when the stack is unfamiliar, ownership is ambiguous, several UI
layers interact, no canonical visual owner appears to exist, or the supported
customization path is uncertain.

## Keep family ownership distinct

This Skill works alone. Code owns engineering scope, code ownership, integrity,
risk, and proof. UI owns framework alignment, hierarchy, layout, interaction
presentation, responsive adaptation, and rendered evidence. Scribe owns meaning,
terminology, localization, and fidelity only when visible or accessible wording
is variable; fixed source-exact strings do not activate it.

UI owns text layout, legibility, space, scaling, and whether a required label or
accessible name exists and is associated. Scribe, when applicable, owns what it
says. Do not copy sibling rules or repeat their verification.

Every sibling Skill is optional. Do not require, install, or simulate Plan,
Code, or Scribe when it is absent or inapplicable. UI remains complete for its
owned interface concerns and composes only with siblings that are independently
activated for their own concerns.

## Route the work

1. Inspect the requested surface, repository instructions, framework version,
   canonical owners, and nearest comparable surface only as needed.
2. Identify the primary task, priority, affected states, content variation,
   inputs, and responsive transformations.
3. Reuse canonical components, tokens, variants, layouts, breakpoints, and
   interactions. Add a primitive only for a demonstrated gap at its owner.
4. Make the smallest coherent change for the outcome and necessary states.
5. Verify only rendered conditions that could disprove the result. Separate
   rendered evidence, source inspection, and unverified behavior in the report.
   For an unimplemented direction or source-only audit, say explicitly that the
   direction or findings are unrendered and rendered behavior remains unverified;
   do not load validation merely to report that boundary.

Read [ui-quality.md](references/ui-quality.md) before making a quality decision
about task flow, hierarchy, layout, readability, states, accessibility structure,
or responsive behavior. For an evidence-only question, load validation alone
unless the interface itself must also be judged.

Read [validation.md](references/validation.md) after an interface change or
before claiming rendered behavior, responsive behavior, observed interaction,
visual quality, or accessibility. Do not load it for a source-only audit that
confines findings to inspected structure and explicitly leaves rendered and
interactive behavior unverified. A build or source review cannot prove rendered
behavior.

## Protect the UI integrity floor

Never improve appearance by inventing a parallel visual language, bypassing a
semantic token, rebuilding an accessible component, removing focus or input
accommodations, hiding required content, using one visual cue as the sole
carrier of meaning, omitting recovery for a changed state, or applying a local
exception through a global theme override.

Do not impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoints, pixel values, or fashionable bans. Quantitative rules come from
the accessibility standard, platform, or design system—not this Skill.

When asked only to audit or advise, return prioritized findings tied to observed
evidence and do not edit.
