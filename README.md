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
Use Scoville Design with Scoville UI. Design owns the workflow, hierarchy, typography, spacing, and design-system decision. UI implements that record through the existing framework and proves component states and interactions.
```

Explicit `$scoville-ui-anti-ai-slop` invocation also works on hosts that
support named Skill invocation.

## Compatibility

Any Agent Skills host that can read references/ and run the project's framework toolchain. Rendered and interaction proof needs a browser, renderer or screenshot tool provided by the host; build or source alone cannot prove rendering. No bundled scripts, no network access required. Developed for Codex and Claude Code; other hosts untested.

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
Implementation and rendered checks need the relevant framework and browser tools.

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

For repository structure and development tools, see
[maintenance notes](development/docs/maintenance.md).

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

The Design/UI ownership boundary has ten active-context composition cases and
later 3/3 open Validation plus 4/4 consumed Test regressions. These are
configuration-specific results, not an unseen holdout or broad proof of design
quality. Earlier 30/30 UI evidence belongs to another package.

See [composition evidence](development/docs/design-composition-evidence.md) and
[release validation](development/docs/release-validation.md) for exact identities and limits.
Adding a license to the package does not add behavioral evidence.

Repository development and the current path mapping are in [development/](development/README.md).

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
