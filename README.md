# Scoville UI Anti-AI-Slop

A good desktop screenshot does not tell you whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI helps implement and audit interfaces through the framework and
design system the product already uses. It covers components, interaction
states, responsive behavior and accessibility, then asks for evidence from the
actual rendered interface.

When Scoville Design is active, UI implements its design decisions. Otherwise
it can develop a bounded direction for a new interface. Backend-only work and
wording alone do not activate it.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution.
In UI, that means keeping the user's task clear across screen sizes, interaction states and visual choices.

## How to use

Name Scoville UI for interface design, implementation, or audit work:

```text
Use Scoville UI to implement this settled settings-screen design through the product's existing component system. Cover loading, empty, error, and success states, then verify the rendered result responsively.
```

```text
Use Scoville UI to audit the current checkout for hierarchy, accessibility, keyboard use, responsive behavior, and recovery from errors. Do not change files.
```

```text
Use Scoville Design with Scoville UI. Design owns the workflow, hierarchy, typography, spacing, and design-system decision. UI implements that record through the existing framework and proves component states and interactions.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Source-first checks and consistency audits

Implementation groups related UI changes before validation. Complete the planned
edits, then check source, measure affected relationships and view the result.
Screenshots and measurements follow the completed batch, not each small edit.
If checks reveal defects, collect the related corrections and validate affected
concerns after that correction batch is complete.

Custom styling needs a concrete owner/API justification
before it is written. Authored units and expressions remain distinct from their
computed pixel values and visible geometry.

An ordinary request to check a page for consistency uses a read-only inventory
of its regions, variants and relevant states, including content below the fold.
Every entry maps to source, measurement and visual evidence or a named gap.
The visual routine compares intended edges, text position, apparent whitespace,
control interiors, icons, wrapping and clipping. Sampling limits remain explicit.

## Compatibility

Agent Skills host with reference access and the project's framework toolchain. Geometry proof needs DOM or equivalent platform measurement; visual proof needs actually viewed renders, and interaction proof needs an interactive runtime. Source-only or screenshot-only tasks report missing evidence. No bundled scripts or mandatory network access. Developed for Codex and Claude Code; other hosts untested.

## Install

### Install this Skill

In a local Codex or Claude Code session, ask:

```text
Install this Agent Skill for all my projects from this exact package directory:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
Preserve existing customizations and ask before overwriting conflicting files.
Report the installed location and whether the host discovers the Skill.
```

The agent needs source access and permission to write to its personal Skills
location. Manual fallback: [Codex Skills guide](https://learn.chatgpt.com/docs/build-skills)
or [Claude Code Skills guide](https://code.claude.com/docs/en/skills).

Install only the linked package for the focused option.

### Install the complete Scoville suite

```text
Install the complete Scoville Skill suite for all my projects. Fetch and install every exact package directory below:

https://github.com/benjaminstelzer/scoville-brainstorm/tree/main/scoville-brainstorm
https://github.com/benjaminstelzer/scoville-research/tree/main/scoville-research
https://github.com/benjaminstelzer/scoville-code-anti-ai-slop/tree/main/scoville-code-anti-ai-slop
https://github.com/benjaminstelzer/scoville-design-anti-ai-slop/tree/main/scoville-design-anti-ai-slop
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop/tree/main/scoville-scribe-anti-ai-slop
https://github.com/benjaminstelzer/scoville-plan/tree/main/scoville-plan
https://github.com/benjaminstelzer/scoville-handoff/tree/main/scoville-handoff

Preserve existing customizations and ask before overwriting conflicting files. Report every installed location and whether the host discovers each Skill.
```

## What it enforces

- **The product keeps its visual owner.** The incumbent design system comes
  first. Within it, an active Design record owns design judgment while UI owns
  implementation. Without Design, UI uses its bounded fallback.
- **The task has a hierarchy.** Primary decisions, supporting information, and
  secondary actions remain distinguishable.
- **Real states exist.** Loading, empty, error, disabled, success, focus,
  keyboard, and touch behavior are covered when relevant.
- **Responsive means adapted.** The task survives narrow, wide, zoomed, and
  content-heavy conditions rather than just scaling down the desktop layout.
- **Accessibility is structural.** Reading order, names, relationships,
  contrast, focus, and input behavior are checked in their real context.
- **Evidence matches the claim.** Source inspection can prove structure.
  Rendered or interactive claims require rendered or interactive evidence.

The complete contract is in
[SKILL.md](scoville-ui-anti-ai-slop/SKILL.md).

## How it works

The Core resolves activation, the incumbent product system, any active Design
record, and the requested implementation outcome. It then loads only the
framework-alignment, UI-quality, or rendered-validation guidance that applies.
UI never searches for or simulates Design. A real framework constraint returns
only the affected decision for revision instead of silently redesigning the
screen. Audit-only requests remain read-only. Browser behavior needs a check in the browser.

## How it was developed

UI developed through interface work and comparisons of how agents use the
instructions. One recurring problem was checking the rendered page before
understanding which component or CSS rule owned it. Another was interrupting
related edits with repeated screenshots. The [changelog](CHANGELOG.md) follows
the changes to source inspection and validation after a completed batch.

I read task histories alongside the interface to see which checks help and
which merely repeat work. Earlier
[optimization runs](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/blob/3b054c35187437743e6994aad1a2d42bac228e53/CHANGELOG.md)
also explored selective loading and the boundary with Design. When SkillOpt
found no better candidate, I kept the existing instructions.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Research](https://github.com/benjaminstelzer/scoville-research) turns web,
  GitHub, and scholarly evidence into a decision-ready, claim-traceable result.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [Design](https://github.com/benjaminstelzer/scoville-design-anti-ai-slop) owns
  visual definition, art direction, design systems, critique, and repair.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  framework-aligned implementation, interface mechanics, accessibility, and
  rendered evidence, with a standalone design fallback.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

The latest change to validation after related edits has not yet been tested
in a browser or through a live agent regression run.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure.
- [Carbon Design System](https://carbondesignsystem.com/),
  [Atlassian Design System](https://atlassian.design/), and
  [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for system-owned components, patterns, and platform conventions.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for accessibility requirements.

## License

MIT. See [LICENSE](LICENSE).
