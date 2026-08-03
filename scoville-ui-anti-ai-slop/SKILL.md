---
name: scoville-ui-anti-ai-slop
description: Framework-aware UI quality guardrail for designing, implementing, auditing, or refining interactive web, native mobile, desktop, and terminal interfaces. Use for UI design, usability, information hierarchy, scannability, readability, clutter, visual clarity, layout, interaction states, responsive or adaptive behavior, accessibility, or broad requests to make an interface clearer or look better, even when the request is phrased non-visually. Preserve the project's design system and the owning framework's design language instead of imposing generic anti-AI aesthetics. Use with scoville-code-anti-ai-slop when changing engineering artifacts and with scoville-scribe-anti-ai-slop when visible or accessible wording is involved. Do not use for backend-only work or ordinary prose, email, or document tasks without an interactive-interface concern.
---

# Scoville UI Anti-AI-Slop

Improve the interface the product already has. Treat consistency, usability,
information design, readability, responsive adaptation, accessibility, and
visual clarity as outcomes; do not install a second design language disguised
as best practice.

## Resolve ownership before designing

Resolve each concern in this order:

1. Follow system, safety, and legally binding accessibility requirements.
2. Follow the explicit user request, including an informed decision to accept a
   reported limitation against a non-binding accessibility target.
3. Follow repository instructions.
4. Follow canonical product requirements, design-system components, wrappers,
   themes, semantic tokens, and approved assets.
5. For unresolved concerns, follow the owning installed framework or platform.
6. Reuse deliberate local patterns that agree with those owners.
7. Apply the general UI principles in this skill only to the remaining gap.

Do not use a lower source to override a higher owner. Surface a material
divergence instead of silently choosing whichever rule is easiest to implement.
Treat a repeated same-surface convention as project evidence only when it is
clearly deliberate, not merely copied technical debt.

When the project names no accessibility target, use WCAG 2.2 Level AA for web
UI and the owning platform's current accessibility guidance for native,
desktop, and terminal UI. Resolve defects through supported components, tokens,
variants, and customization APIs. If the canonical owner cannot meet the
applicable floor, report the owner conflict; do not fork the design language to
hide it. In an unattended run, make only the closest supported compliant change
within scope and report the residual limitation.

Treat a target as non-binding only when that status is known. If binding status
is unknown, state that any acceptance assumes no binding requirement applies.

Read [framework-alignment.md](references/framework-alignment.md) when ownership
is ambiguous, no canonical visual owner appears to exist, multiple UI layers
interact, the framework is unfamiliar, or its supported customization path is
uncertain.

## Compose the Scoville family

- `scoville-code-anti-ai-slop` owns engineering scope, canonical code ownership,
  implementation integrity, risk, and proportionate proof.
- This skill owns framework alignment, information and visual hierarchy,
  layout behavior, interaction presentation, responsive adaptation, and
  rendered UI evidence.
- `scoville-scribe-anti-ai-slop` owns visible and accessible wording,
  terminology, localization contracts, factual meaning, and source fidelity.

For text, this skill owns hierarchy, legibility, wrapping, truncation, scaling,
available space, and whether a required accessible name or label exists and is
programmatically associated. Scribe owns what that name, label, error, or help
text says. Apply the relevant skills together without copying their rules or
running the same verification twice.

## Work from task to rendered result

1. **Inspect only what can change the decision.** Establish the user's task,
   repository instructions, installed framework and version, canonical theme or
   token sources, shared components, and the nearest comparable surfaces.
2. **Classify the UI stack.** Distinguish styled systems, headless libraries,
   utility or application frameworks, platform UI stacks, and true greenfield
   work. React, Vue, Svelte, Tailwind, CSS Modules, and similar implementation
   tools are not automatically design systems.
3. **Frame the interface problem.** Identify the primary task, information
   priority, affected states, content variation, input methods, and responsive
   transformations. Keep this analysis internal unless a material product
   choice needs the user or the user asks for the rationale.
4. **Reuse before extending.** Prefer canonical components, semantic tokens,
   variants, layout primitives, breakpoints, interaction patterns, and
   iconography. Add a primitive or token only for a demonstrated gap and only at
   its canonical owner.
5. **Make the smallest coherent change.** Fix the requested outcome and its
   necessary states without broad redesign, global theme exceptions, or nearby
   cleanup.
6. **Verify the rendered behavior.** Exercise only the viewports, content
   lengths, text scaling, themes, states, and input methods that could change
   the implementation decision. Automated checks supplement rendered
   inspection; a clean build does not prove visual quality.
7. **Report observed results.** Distinguish what was rendered, what was checked
   only in source, and what remains unverified.

Read [ui-quality.md](references/ui-quality.md) when designing, restructuring, or
auditing task flow, hierarchy, layout, readability, states, or responsive
behavior. Read [validation.md](references/validation.md) after changing an
interface or before making claims about rendered UI behavior.

## Protect the UI integrity floor

Never improve appearance by:

- inventing a visual language when the product or framework already owns it;
- bypassing an available semantic token or supported variant with an arbitrary
  raw value;
- rebuilding an available framework component as a less accessible custom one;
- removing or obscuring focus, keyboard, touch, zoom, text-scaling,
  localization, reduced-motion, or comparable platform accommodations;
- hiding, clipping, or silently discarding content to simulate responsiveness;
- making color, placement, hover, or icon shape the only carrier of meaning;
- omitting feedback, recovery, or interaction behavior for a state introduced
  or changed by the work; or
- applying a local exception through a global theme override.

This floor binds the agent's own polish decisions. Resolve an explicit,
informed user decision through the ownership order above, still report the
limitation, and never override system, safety, or legally binding requirements.

Do not impose preferred fonts, palettes, radii, shadows, card patterns,
breakpoint matrices, pixel values, or fashionable bans. Quantitative rules come
from the applicable accessibility standard, owning platform, or detected design
system—not from this skill.

When asked only to audit or advise, return prioritized, evidenced findings and
do not edit. When no renderer or simulator is available, say that rendered
behavior is unverified rather than inferring success from source code or a
single static screenshot.
