# Scoville UI Anti-AI-Slop

A polished interface can still lose the user's task. Scoville UI keeps that
task visible while the pixels negotiate among themselves.

It usually looks harmless:

- A product with an established design system receives a fresh local language
  of rounded cards, gradients, and pills because this screen wanted a journey.
- Primary, secondary, and destructive actions all receive equal emphasis. The
  hierarchy is now democratic and therefore useless.
- The happy path looks polished. Loading, empty, error, focus, keyboard, and
  long-content states have quietly missed the launch.
- The desktop screenshot is excellent. On mobile, the primary action lives
  beyond a horizontal scroll that users can discover through archaeology.

That is UI slop: familiar polish substitutes for the task, the product's visual
owner, and rendered evidence. The gradient survived. The task did not.

Scoville UI is a framework-aware Agent Skill for implementing and auditing
interfaces through the product framework and incumbent design system. It owns
supported components, states, semantics, focus and input behavior,
announcements, responsive mechanics, and rendered evidence. When Scoville
Design is active and applicable, UI consumes its design decisions without
re-deciding them. Otherwise UI retains a bounded standalone Greenfield
fallback. It does not activate for backend-only work or wording alone.

## Why "Scoville"?

The family is named for useful signal that remains detectable after dilution. In UI work, the
heat is the user's task - primary action, state, reading order, and error
recovery - not making every button look ready for a chili-eating contest.

## How to use

Name Scoville UI for interface design, implementation, or audit work:

```text
Use Scoville UI to implement this settled settings-screen design through the product's existing component system. Cover loading, empty, error, and success states, then verify the rendered result responsively.
```

```text
Use Scoville UI to audit the current checkout for hierarchy, accessibility, keyboard use, responsive behavior, and recovery from errors. Do not change files.
```

```text
Use Scoville UI with Scoville Code to implement this dialog in the owning framework. Reuse established components and verify both behavior and rendered states.
```

```text
Use Scoville Design with Scoville UI. Design owns the workflow, hierarchy, typography, spacing, and design-system decision. UI implements that record through the existing framework and proves component states and interactions.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Install

Use an Agent Skills-compatible host with file access and the tools needed to
implement and inspect your interface. Ask the agent to install:

```text
Install this Agent Skill from GitHub and make it available for all my projects:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
Keep the installed directory name scoville-ui-anti-ai-slop.
```

The final path must end in
`<skills-dir>/scoville-ui-anti-ai-slop/SKILL.md`. For Claude Code, use
`~/.claude/skills/` globally or `.claude/skills/` inside one project. Other
hosts use their supported Skills directory.

**What it costs.** The complete `SKILL.md`, including metadata, uses 1,533
`o200k_base` tokens. Framework,
quality, and validation guidance loads only when needed. The added ownership
contract preserves Design decisions when both Skills apply and preserves UI's
standalone fallback when Design does not. Use it for production interfaces.
Skip it for a disposable mockup when token use matters more. See
[composition evidence](docs/design-composition-evidence.md).

## What it enforces

- **The product keeps its visual owner.** The incumbent design system comes
  first. Within it, an active Design record owns design judgment while UI owns
  implementation. Without Design, UI uses its bounded fallback.
- **The task has a hierarchy.** Primary decisions, supporting information, and
  secondary actions remain distinguishable.
- **Real states exist.** Loading, empty, error, disabled, success, focus,
  keyboard, and touch behavior are covered when relevant.
- **Responsive means adapted.** The task survives narrow, wide, zoomed, and
  content-heavy conditions rather than merely shrinking politely.
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
screen. Audit-only requests remain read-only. Source-only evidence stays
source-only rather than becoming a browser result while nobody is looking.

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

Version 1.1.0 adds optional composition with Scoville Design.
A reliability-first extension of
[Microsoft SkillOpt](https://github.com/microsoft/SkillOpt) tested the revised
ownership boundary with SOL 5.6 XHigh. Ten active-context composition cases
passed, including installed-but-inactive Design, UI-only fallback, both active,
incumbent precedence, both opt-outs, the implementation-constraint loop, and
portable framework, quality, and validation regressions. A later adjudicated
suite passed 3/3 open Validation and 4/4 consumed Test regressions. The current
five-file UI manifest is
`FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`.

Historical 30/30 UI evidence belongs to the earlier package. The composition
and post-diagnosis regression evidence is configuration-specific, not a new
unseen holdout or broad proof of design quality. See
[composition evidence](docs/design-composition-evidence.md) and
[release validation](docs/release-validation.md) for scope and limits.

## Sources

- [Agent Skills specification](https://agentskills.io/specification) for the
  portable package and progressive disclosure.
- [Carbon Design System](https://carbondesignsystem.com/),
  [Atlassian Design System](https://atlassian.design/), and
  [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for system-owned components, patterns, and platform conventions.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for accessibility requirements.

## License

MIT - see [LICENSE](LICENSE).
