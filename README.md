# Scoville UI Anti-AI-Slop

Improves the interface without replacing the design system that owns it.

UI slop is not a particular font, gradient, radius, or card layout. It is an
interface that looks finished while the task remains hard to understand, the
hierarchy is accidental, states are unclear, narrow layouts discard content,
or success is claimed from source code without inspecting the rendered result.

Scoville UI Anti-AI-Slop is an Agent Skill for designing, implementing,
auditing, and refining interactive web, native mobile, desktop, and terminal
interfaces. It applies framework-independent UI-quality principles through the
project's own components, tokens, variants, patterns, and supported framework
APIs. It does not supply a fashionable visual preset.

## Install

Use a coding agent that supports the Agent Skills format and ask it to install:

```text
Install this Agent Skill from GitHub and make it available for my UI work:
https://github.com/benjaminstelzer/scoville-ui-anti-ai-slop/tree/main/scoville-ui-anti-ai-slop
```

Add "for all my projects" or "only for this project" when the installation
scope matters. The final installation path must retain the skill name:

```text
<skills-dir>/scoville-ui-anti-ai-slop/SKILL.md
```

For Claude Code, `<skills-dir>` is `~/.claude/skills/` globally or
`.claude/skills/` inside one repository. For Codex and other compatible agents,
use the skills directory documented by that host and refresh its skill list.

Try a non-visual activation request after installation:

```text
Make this dense table easier to scan without changing the product's design system.
```

The agent should load the UI skill, inspect the actual design owner before
prescribing changes, and distinguish rendered evidence from source-only claims.
A backend-only request should not load it.

## One family, three owners

- [Scoville Code Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-code-anti-ai-slop)
  owns engineering scope, canonical code ownership, implementation integrity,
  risk, and proportionate proof.
- Scoville UI Anti-AI-Slop owns framework alignment, information and visual
  hierarchy, layout behavior, interaction presentation, responsive adaptation,
  and rendered UI evidence.
- [Scoville Scribe Anti-AI-Slop](https://github.com/benjaminstelzer/scoville-scribe-anti-ai-slop)
  owns visible and accessible wording, terminology, localization contracts,
  factual meaning, and source fidelity.

Mixed tasks use the relevant skills together. For an error state, Code proves
the state transition, UI verifies its placement and focus behavior, and Scribe
verifies the message. UI owns whether a required label or accessible name
exists and is associated; Scribe owns what it says.

## Framework alignment

The skill first determines which layer owns each decision:

- A styled design system owns its visual language, semantic tokens, component
  conventions, variants, and supported customization paths.
- A headless component library owns the behavior and semantics it implements,
  not a visual language the library does not provide.
- A utility or application framework may supply coherent implementation values
  without defining the product's information hierarchy or visual direction.
- A native, desktop, or terminal stack inherits its platform conventions.
- A true greenfield surface starts with the user brief and platform defaults,
  then makes only the minimum coherent, reversible local choices it needs.

General UI principles fill only the gaps those owners leave. The skill does not
invent a second token set, component library, theme, or project-wide design
system. When the task legitimately creates or extends the canonical design
system, the change belongs at that owner rather than in one feature.

## What it protects

- **Task and information clarity.** Primary decisions, supporting information,
  and secondary actions receive a deliberate hierarchy through the mechanisms
  the project already uses.
- **Readable content.** Reading order, scaling, wrapping, localization, and
  programmatic relationships survive realistic content instead of working only
  in an ideal screenshot.
- **Predictable interaction.** Relevant focus, keyboard, touch, state feedback,
  error recovery, and accessible relationships remain intact.
- **Responsive adaptation.** The task survives changes in space, content, text
  size, orientation, and input method; required content is not clipped or hidden
  to manufacture a clean narrow view.
- **Truthful evidence.** Builds and automated checks support the result but do
  not replace rendered inspection. Unrendered behavior stays explicitly
  unverified.

The skill has no preferred fonts, palettes, shadows, radii, card patterns,
breakpoint matrix, or universal pixel values. Quantitative requirements come
from the applicable accessibility standard, target platform, or detected
design system.

## Accessibility floor

When a web project names no target, the skill uses WCAG 2.2 Level AA. Native,
desktop, and terminal interfaces use the owning platform's current
accessibility guidance. Defects are resolved through supported components,
tokens, variants, and customization APIs. If the canonical owner cannot meet
the applicable floor, the agent reports that conflict instead of quietly
forking the design language.

## Validation

The installable directory passes the canonical Agent Skill validator. Fresh
Claude Code sessions also exercised three discovery cases:

- a dense-table scannability request activated the skill;
- a backend-only queue retry request did not; and
- a Mantine form request activated the skill, retained the provider theme,
  semantic tokens, Shared Components, and theme breakpoints, and reported the
  missing rendered application as unverified.

Fable reviewed the saved plan and then reviewed successive skill drafts. The
final fresh review returned `ACCEPT` with no material finding. The retained
[PLAN.md](PLAN.md) records the contract, review loop, and acceptance evidence.

## Research basis

The skill uses principles rather than copying another skill's aesthetic rules.
Its framework and quality model draws from primary design-system and platform
guidance, including:

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for the default web accessibility
  floor;
- [MUI theming](https://mui.com/material-ui/customization/theming/) and
  [Mantine theming](https://mantine.dev/theming/theme-object/) for theme and
  token ownership in styled systems;
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)
  for the behavior-versus-appearance boundary of headless components;
- [Fluent 2](https://fluent2.microsoft.design/),
  [Carbon](https://carbondesignsystem.com/), and
  [Atlassian Design System](https://atlassian.design/) for system-level
  consistency and reusable product conventions; and
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
  for platform-owned interaction, adaptation, and accessibility conventions.

Popular frontend-design skills were also reviewed as counterexamples and
inspiration. Their useful attention to hierarchy and rendered quality remains;
their prescribed aesthetics or generated design systems do not.

## Repository contents

The installable `scoville-ui-anti-ai-slop/` directory contains the core skill,
three conditionally loaded references, and display metadata. This README, the
changelog, license, and retained implementation plan remain at the repository
root and are not loaded as runtime skill instructions. The repository contains
no executable software, framework database, assets, or runtime network fetches.

## License

MIT, see [LICENSE](LICENSE).
