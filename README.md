# Scoville UI Anti-AI-Slop

A polished interface can still lose the user's task. Scoville UI keeps that
task visible while the pixels negotiate among themselves.

Scoville UI is a framework-aware Agent Skill for hierarchy, layout, states,
responsiveness, accessibility, usability, and rendered evidence. It follows the
product's existing design system and platform language instead of inventing a
second visual owner. It does not activate for backend-only work or wording
alone; visual quality needs an interface, which is an inconvenient but useful
boundary.

## Why "Scoville"?

The family is named for useful signal that survives dilution. In UI work, the
heat is the user's task—primary action, state, reading order, and error
recovery—not making every button look ready for a chili-eating contest.

## How to use

Name Scoville UI for interface design, implementation, or audit work:

```text
Use Scoville UI to redesign this settings screen within the product's existing design system. Preserve platform patterns, cover loading, empty, error, and success states, and verify the rendered result responsively.
```

```text
Use Scoville UI to audit the current checkout for hierarchy, accessibility, keyboard use, responsive behavior, and recovery from errors. Do not change files.
```

```text
Use Scoville UI with Scoville Code to implement this dialog in the owning framework. Reuse established components and verify both behavior and rendered states.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Install

Use an Agent Skills-compatible host and Terra 5.6 Medium or a comparably
capable executor such as Opus 4.8. Ask the agent to install:

```text
Install this Agent Skill and refresh the available Skill list:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
Keep the installed directory name scoville-ui-anti-ai-slop. Use Terra 5.6 Medium or a comparably capable executor such as Opus 4.8.
```

The final path must end in
`<skills-dir>/scoville-ui-anti-ai-slop/SKILL.md`. For Claude Code, use
`~/.claude/skills/` globally or `.claude/skills/` inside one project. Other
hosts use their supported Skills directory.

**What it costs.** The 1,050-token Core is 2.51% smaller than `v1.0.6`;
framework, quality, and validation guidance loads only when needed. The added
context buys design-system alignment, accessibility, state coverage, and
rendered evidence. Use it for production interfaces; skip it for a disposable
vibe-coding mockup when token use matters more. See
[benchmark evidence](docs/benchmark-evidence.md).
The [family run ledger](docs/optimization-history.md) shows the complete count.

## What it enforces

- **The product keeps its visual owner.** Existing components, tokens,
  semantics, and platform conventions come before generic redesign habits.
- **The task has a hierarchy.** Primary decisions, supporting information, and
  secondary actions remain distinguishable.
- **Real states exist.** Loading, empty, error, disabled, success, focus,
  keyboard, and touch behavior are covered when relevant.
- **Responsive means adapted.** The task survives narrow, wide, zoomed, and
  content-heavy conditions rather than merely shrinking politely.
- **Accessibility is structural.** Reading order, names, relationships,
  contrast, focus, and input behavior are checked in their real context.
- **Evidence matches the claim.** Source inspection can prove structure;
  rendered or interactive claims require rendered or interactive evidence.

The complete contract is in
[SKILL.md](scoville-ui-anti-ai-slop/SKILL.md).

## How it works

The Core resolves framework ownership and the requested UI outcome, then loads
only the framework-alignment, UI-quality, or rendered-validation guidance that
applies. Audit-only requests remain read-only. Source-only evidence is reported
as source-only rather than being promoted to a browser result while nobody is
looking.

## Scoville family

Each Skill works independently. Combine only the concerns the task actually
needs:

- [Brainstorm](https://github.com/benjaminstelzer/scoville-brainstorm) explores
  materially different mechanisms before selection.
- [Code](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop) owns
  engineering scope, implementation, risk, and validation.
- [UI](https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop) owns
  interface hierarchy, framework fit, accessibility, and rendered evidence.
- [Scribe](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop) owns
  wording, terminology, factual meaning, and source fidelity.
- [Plan](https://github.com/benjaminstelzer/scoville-plan) owns durable Plans,
  Work Items, Decisions, and lifecycle state.
- [Handoff](https://github.com/benjaminstelzer/scoville-handoff) transfers active
  work to another agent or session.

## Status

A reliability-first extension of
[Microsoft SkillOpt](https://github.com/microsoft/SkillOpt) tested the six
Scoville Skills across **1,201 optimization and evaluation runs**. Scoville UI
passed **30/30 final cases** and its always-loaded instructions use **2.51%
fewer tokens than v1.0.6**. See
[benchmark evidence](docs/benchmark-evidence.md).

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
