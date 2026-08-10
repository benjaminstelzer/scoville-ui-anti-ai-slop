# Scoville UI Anti-AI-Slop

Clarifies the interface. Keeps the design system in charge.

UI slop is not a particular font, gradient, radius, or card layout. It is an
interface that looks finished while the task remains hard to understand, the
hierarchy is accidental, states are unclear, narrow layouts discard content,
or success is claimed from source code without inspecting the rendered result.

Scoville UI is an Agent Skill for designing, implementing, auditing, and
refining interactive web, native mobile, desktop, and terminal interfaces. It
applies framework-independent quality principles through the project's own
components, tokens, variants, patterns, and supported APIs. It does not supply
a fashionable visual preset.

## Why "Scoville UI"?

The Scoville family is named for signal that remains detectable after
dilution. In an interface, that signal is the user's task: the primary action,
current state, reading order, and path out of an error should survive layers of
components and styling. The goal is enough visual heat to reveal hierarchy,
not to make every button look like it has entered a chili-eating contest.

## Install

Works with any coding agent that supports the Agent Skills format: a `SKILL.md`
instruction file with its name and description at the top. Compatible agents
include Claude Code and Codex.

Usually, let your coding agent install the skill. Send it this prompt:

```text
Install this Agent Skill from GitHub and make it available for my UI work:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
Use Terra 5.6 Medium or a comparably capable executor such as Opus 4.8; this is the minimum supported capability level for this Skill.
```

Add "for all my projects" or "only for this project" when the installation
scope matters. The agent should choose its supported skills directory, install
the skill directory under the unchanged name `scoville-ui-anti-ai-slop`, and
refresh its skill list.

If your agent cannot install skills itself, copy the repository's
`scoville-ui-anti-ai-slop/` directory so the final path is:

```text
<skills-dir>/scoville-ui-anti-ai-slop/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` for all projects or
`.claude/skills/` inside a repository for that project only. For other agents,
consult their documentation; paths differ per agent.

**Verify it works.** Ask the agent: *"Make this dense table easier to scan
without changing the product's design system."* The agent should inspect the
actual design owner before prescribing changes and distinguish rendered
evidence from source-only claims. A backend-only request should not load the UI
skill.

**What it costs.** Compatible hosts expose compact discovery metadata before
loading the full Skill instructions. After
activation, the 1,050-token core selects framework alignment, UI quality, and
rendered validation only when the task needs them. The complete installable
package is 4,155 tokens, but references not selected by the route are not loaded.
In the frozen compression benchmark, the final core reduced loaded Skill context
by 4.63% against the equally reliable 1,173-token control. Provider usage also
depends on the host and conversation. See
[the benchmark evidence](docs/benchmark-evidence.md) for scope and limits.

## What it enforces

- **Task and information clarity.** Primary decisions, supporting information,
  and secondary actions receive a deliberate hierarchy through the mechanisms
  the project already uses.
- **Framework alignment.** Styled design systems own their visual language;
  headless libraries own the behavior and semantics they implement; platform
  stacks retain their platform conventions. The skill does not invent a second
  token set, component library, or theme beside the real owner.
- **Readable content.** Reading order, scaling, wrapping, localization, and
  programmatic relationships survive realistic content instead of working only
  in an ideal screenshot.
- **Predictable interaction.** Relevant focus, keyboard, touch, state feedback,
  error recovery, and accessible relationships remain intact.
- **Responsive adaptation.** The task survives changes in space, content, text
  size, orientation, and input method. Required content is not clipped or
  hidden to manufacture a clean narrow view.
- **Truthful evidence.** Builds and automated checks support the result but do
  not replace rendered inspection. Unrendered behavior remains explicitly
  unverified.

The full rules live in
[SKILL.md](scoville-ui-anti-ai-slop/SKILL.md).

## Use with the Scoville family

UI works independently. When companion Skills are installed, combine them only
for the concerns they own.

Use [Scoville Code Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop)
for engineering scope, canonical code ownership, implementation integrity,
risk, and proportionate proof. Use
[Scoville Scribe Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop)
for visible and accessible wording, terminology, localization contracts,
factual meaning, and source fidelity.

Use [Scoville Plan](https://github.com/benjaminstelzer/scoville-plan) when the
interface work needs durable sequencing across independently resumable
outcomes or handoffs. Plan owns project direction and Work Item lifecycle; UI
owns the interface result and rendered evidence.

Mixed tasks use the relevant skills together. For an error state, Code proves
the state transition, UI verifies placement, focus, and responsive behavior,
and Scribe verifies the message. UI owns whether a required label or accessible
name exists and is associated; Scribe owns what it says.

## Design

The skill first identifies the layer that owns each decision:

- A styled design system owns semantic tokens, components, variants, and
  supported customization paths.
- A headless component library owns its implemented behavior and semantics, not
  a visual language it does not provide.
- A utility or application framework may supply coherent implementation values
  without defining the product's hierarchy or visual direction.
- A native, desktop, or terminal stack inherits its platform conventions.
- A true greenfield surface starts with the user brief and platform defaults,
  then makes only the minimum coherent, reversible local choices it needs.

General UI principles fill only the gaps those owners leave. The skill has no
preferred fonts, palettes, shadows, radii, card patterns, breakpoint matrix, or
universal pixel values.

When a web project names no accessibility target, the skill uses WCAG 2.2
Level AA. Native, desktop, and terminal interfaces use the owning platform's
current accessibility guidance. If the canonical owner cannot meet the
applicable floor, the agent reports the conflict instead of quietly forking the
design language.

The agent conditionally loads three focused guides:

- [references/framework-alignment.md](scoville-ui-anti-ai-slop/references/framework-alignment.md)
  identifies the owning framework and supported customization path.
- [references/ui-quality.md](scoville-ui-anti-ai-slop/references/ui-quality.md)
  covers hierarchy, content, interaction, responsiveness, and accessibility.
- [references/validation.md](scoville-ui-anti-ai-slop/references/validation.md)
  separates source checks from rendered and interaction evidence.

## Sources and inspirations

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for the default web accessibility
  floor.
- [MUI theming](https://mui.com/material-ui/customization/theming/) and
  [Mantine theming](https://mantine.dev/theming/theme-object/) for theme and
  token ownership in styled systems.
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)
  for the behavior-versus-appearance boundary of headless components.
- [Fluent 2](https://fluent2.microsoft.design/),
  [Carbon](https://carbondesignsystem.com/), and
  [Atlassian Design System](https://atlassian.design/) for reusable product
  conventions.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for platform-owned interaction, adaptation, and accessibility conventions.

## Repository contents

The installable `scoville-ui-anti-ai-slop/` directory contains the core skill,
three conditionally loaded references, and display metadata. This README, the
changelog, and the MIT license remain at the repository root and are not loaded
as skill instructions. The repository contains no executable software,
framework database, assets, or runtime network fetches.

## Status

The installable directory passes the canonical Agent Skill validator. It was
optimized with a project-local, reliability-first, token-saving extension of
[Microsoft SkillOpt](https://github.com/microsoft/SkillOpt): `gpt-5.6-sol` at
`xhigh` handled optimization and routing, and `gpt-5.6-terra` at `medium`
executed the frozen A/B benchmark. Across the four-Skill program, **797 run
artifacts** were recorded, including **742 technically valid benchmark runs**,
before the final packages were selected. This Skill passed **30/30** final
Train, Validation, and sealed-Test cases and loaded **4.63% fewer Skill
instruction tokens** than its paired control. Terra 5.6 Medium or a comparably
capable executor such as Opus 4.8 is the minimum supported level. See
[benchmark evidence](docs/benchmark-evidence.md).

## License

MIT - see [LICENSE](LICENSE).
