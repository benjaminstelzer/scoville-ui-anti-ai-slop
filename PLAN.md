# Scoville UI Skill Plan

## Objective

Create `scoville-ui-anti-ai-slop`, a framework-aware Agent Skill that improves
UI consistency, usability, information design, readability, responsive
behavior, accessibility, and visual clarity without imposing its own component
styling or replacing the project's design system.

Rename the existing engineering skill from
`scoville-anti-ai-coding-slop` to `scoville-code-anti-ai-slop` so the family
uses one naming scheme:

- `scoville-code-anti-ai-slop`
- `scoville-scribe-anti-ai-slop`
- `scoville-ui-anti-ai-slop`

Keep this plan in the repository after implementation, as requested.

## Binding decisions

1. General UI quality is the subject. Element-level visual prescriptions are
   not. The active product design system or UI framework owns component
   appearance, variants, tokens, sizing, typography, spacing, breakpoints, and
   supported customization paths.
2. Classify the detected stack before applying guidance:
   - a styled design system owns visual language and component conventions;
   - a headless component library owns interaction and accessibility behavior,
     but not visual language;
   - an application or utility framework does not by itself define a complete
     design language;
   - a platform UI stack also inherits its platform conventions.
3. Apply framework-independent principles to outcomes: task clarity,
   information hierarchy, grouping, predictable interaction, state visibility,
   readable content, responsive adaptation, error prevention and recovery, and
   accessible operation.
4. Treat applicable accessibility requirements as a quality floor. Resolve
   accessibility defects through the project's supported components, tokens,
   variants, or customization APIs instead of replacing its design language.
5. Do not create a second token set, component library, visual style, or
   project design-system document when a canonical owner already exists.
6. Do not include universal aesthetic bans, preferred fonts, palettes, radii,
   shadows, card patterns, fixed breakpoint matrices, or mandatory pixel values.
   Quantitative rules belong only to an applicable standard or detected
   framework and platform.
7. Do not fetch mutable third-party instruction files at runtime. Use stable
   framework-routing principles and inspect the installed framework version and
   its official documentation only when current framework details are needed.
8. Keep the installable skill concise. Use progressive disclosure for detailed
   framework routing, UI-quality guidance, and rendered verification.
9. Cover interactive visual interfaces on web, native mobile, desktop, and
   terminal surfaces when layout or interaction presentation is part of the
   task. Exclude ordinary prose, email, documents, and non-interactive output;
   their owning artifact and writing skills apply instead. Scribe continues to
   own CLI and TUI wording even when UI owns their visual arrangement.
10. Make activation outcome-based rather than vocabulary-based. The skill
    description must cover web, native mobile, desktop, and terminal interfaces
    and trigger for requests about UI design, usability, information hierarchy,
    scannability, readability, clutter, visual clarity, interaction states,
    responsiveness, or accessibility, including broad requests such as making
    an interface clearer or making it look better. It must exclude backend-only
    work and ordinary prose, email, or document work owned by Scribe or the
    relevant artifact skill.

## Precedence and conflicts

Resolve each concern from the source that owns it:

1. Follow system, safety, and legally binding accessibility requirements.
2. Follow the explicit user request, including an informed product decision to
   accept a stated limitation against a non-binding accessibility target.
3. Follow repository instructions.
4. Follow the project's canonical product requirements, design-system
   components, wrappers, themes, semantic tokens, and approved design assets.
5. For concerns the project has not resolved, follow the owning installed
   framework or platform: styled systems own their visual conventions; headless
   systems own supported behavior and semantics; platform stacks own their
   platform interaction and adaptation conventions. Terminal UI frameworks
   inherit terminal-platform interaction and presentation constraints.
6. Reuse repeated local patterns on the same surface when they agree with the
   canonical owners and are not isolated accidents.
7. Apply general Scoville UI principles only to the remaining gap.

Do not use a lower source to override a higher owner. If sources conflict
materially, apply the order above and report the specific divergence instead of
silently choosing the most convenient rule. Accessibility remains a default
quality floor. When a project names no target, use WCAG 2.2 Level AA for web UI
and the owning platform's current accessibility guidance for native, desktop,
and terminal UI. When the project's supported components, variants, or tokens
cannot meet that floor, expose the limitation as a product or design-system
decision. An explicit, informed user decision may accept a reported limitation
against a non-binding target, but cannot override system, safety, or legally
binding requirements. In an unattended run, implement only the closest
supported compliant option within scope and report any unresolved owner
conflict; do not silently ship the defect or fork the design language.

When no visual owner or established local pattern exists, use the explicit user
brief and applicable platform or framework defaults first. Then choose only the
minimum internally consistent, reversible local values needed for the requested
surface. Do not present those choices as a project-wide design system or extend
them beyond the task. Ask only when choosing among materially different visual
directions would change the product outcome.

## Skill-family boundaries

- `scoville-code-anti-ai-slop` owns engineering scope, canonical ownership,
  implementation integrity, risk, and proportionate verification.
- `scoville-ui-anti-ai-slop` owns framework alignment, information and visual
  hierarchy, layout behavior, interaction states, responsive adaptation, and
  rendered UI evidence.
- `scoville-scribe-anti-ai-slop` owns visible interface language, terminology,
  errors, label and accessible-name wording, localization contracts, and
  factual wording.

UI owns text presentation, including hierarchy, legibility, wrapping,
truncation, scaling, and available space. Scribe owns the words and their
meaning.

UI also owns whether a required accessible name or label exists and is
programmatically associated with its control or content. Scribe owns the name
or label's wording, terminology, and factual meaning.

For mixed work, apply the relevant skills together without copying their rules.
For example, an error state may require Code to prove the state transition, UI
to verify placement and focus, and Scribe to verify the message.

## Planned repository structure

```text
scoville-ui-anti-ai-slop/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── framework-alignment.md
    ├── ui-quality.md
    └── validation.md
```

The installable directory will not contain a README, changelog, framework
database, scripts, or assets unless implementation evidence shows they are
needed. Repository-level documentation may be added after the skill contract is
accepted, following the established Scoville repository layout.

Load `framework-alignment.md` when ownership is ambiguous, multiple UI layers
interact, the framework is unfamiliar, or a supported customization path is in
question. Load `ui-quality.md` when designing, restructuring, or auditing task
flow, hierarchy, layout, readability, states, or responsive behavior. Load
`validation.md` after an implementation change or when a review makes claims
about rendered behavior. Merge a reference during drafting if its conditional
content is too small to justify a separate load.

## Skill workflow contract

1. Perform the smallest targeted inspection that can answer the UI decision.
   Check the user goal, repository instructions, installed dependencies and
   versions, product design-system documentation, theme and token sources,
   shared components, and the nearest comparable rendered surfaces only as
   relevant to that decision.
2. Identify the canonical visual, behavioral, and content owners. Do not treat
   React, Vue, Svelte, Tailwind, CSS Modules, or another implementation tool as
   a visual design system unless the project has made it one.
3. Define only the user task, information priority, changed states, content
   behavior, and responsive transformations needed for the requested outcome.
   Keep this framing internal unless the user asks for design reasoning or a
   material product choice requires confirmation.
4. Reuse existing components, semantic tokens, variants, layout primitives,
   breakpoints, interaction patterns, and iconography. Add a new primitive or
   token only for a demonstrated gap at the canonical owner.
5. Apply general UI-quality principles only where higher-priority sources leave
   a real gap. Prefer the smallest coherent change over a broad redesign.
6. Verify the rendered result with the interaction methods, states, themes,
   content lengths, text scaling, and viewport changes that could plausibly
   change the implementation decision. Automated checks supplement, but do not
   replace, rendered inspection. This is the same could-change-the-decision
   sufficiency test used by Code; composed use must not duplicate verification.
7. Report only observed results and material residual limits. A clean build is
   not proof of visual quality, and one desktop screenshot is not proof of
   responsive behavior.

## UI integrity floor

The skill must prevent these failures:

- inventing a visual language when a product or framework already owns it;
- bypassing semantic tokens or supported variants with arbitrary raw values
  when such an owner exists;
- rebuilding an available framework component as a less accessible custom one;
- removing focus, keyboard, touch, zoom, text-scaling, localization, or motion
  accommodations for visual polish;
- hiding or clipping content to make a narrow layout appear responsive;
- relying on color, placement, hover, or icon shape as the only carrier of
  meaning;
- leaving a state introduced or altered by the change without the feedback,
  recovery, or interaction behavior needed for the requested flow;
- applying a local exception through a global theme override;
- declaring usability, accessibility, responsiveness, or visual quality from
  source inspection alone when rendered evidence is practical.

## Validation scenarios

Use independent scenarios that expose different ownership models. For each
scenario, pass means the resulting guidance or implementation follows the
named owner, stays within the requested scope, and makes no unsupported success
claim; any contrary instruction or result is a failure.

1. A Mantine or MUI product with an established theme and shared components:
   preserve its tokens, variants, spacing, breakpoints, and customization API.
2. A Tailwind and Radix product: preserve Radix behavior while deriving visuals
   from project tokens and neighboring surfaces, not from an imagined Radix
   aesthetic.
3. A utility framework with no project tokens: use its default value scale as
   an implementation source without treating it as a complete visual language.
4. A true greenfield application with no design system or local patterns: use
   the user brief and platform or framework defaults, then make only the
   minimal coherent local choices needed for the requested surface.
5. A SwiftUI or comparable native interface: follow platform typography,
   scaling, input, layout, and accessibility conventions instead of web-only
   measurements.
6. A UI audit with no implementation request: report observed, prioritized
   findings without redesigning or editing.
7. A mixed error-state task: preserve the separate Code, UI, and Scribe owners.
8. A user-requested style that a popular anti-slop skill might normally ban:
   surface any project divergence, then honor the explicit request when it
   remains usable and does not cross a higher system, safety, legal, or informed
   accessibility boundary.
9. A canonical design-system choice that cannot meet the applicable
   accessibility floor: report the owner conflict instead of bypassing it.
10. A rendered change when no browser or simulator is available: report the
    rendered behavior as unverified rather than inferring success from code.
11. A UI-shaped request phrased non-visually, such as making a dense table
    easier to scan: trigger the skill and address information presentation.
12. A backend-only task: do not trigger the UI skill.
13. A task that builds or extends the canonical design system itself: improve
    that owner at its canonical source without treating the no-parallel-system
    rule as a ban on legitimate design-system work.

Before final acceptance, exercise scenarios 11 and 12 plus at least one styled
or headless ownership scenario as isolated fresh-session prompts with the skill
available through the host's normal discovery path. Record whether the skill
activated and whether the response followed the scenario's owner and evidence
rules. Scenario 11 passes only if UI activates; scenario 12 passes only if it
does not; the ownership scenario passes only if the response preserves the
framework or project design language. Review the remaining scenarios as
contract cases against the current files, and run more fresh-session prompts
when that review exposes ambiguous behavior.

## Review and iteration protocol

1. Ask Fable to review this plan read-only. Require a clear verdict, concrete
   contradictions or omissions, and exact amendments. Fable must distinguish
   framework-independent quality from element-level taste and must assess the
   boundaries with Code and Scribe.
2. Apply only supported review findings. Record material plan changes in this
   file; do not create a second planning source.
3. Initialize the skill with the canonical `skill-creator` script and generate
   `agents/openai.yaml` from the completed skill contract.
4. Write the first draft and run the canonical skill validator.
5. Ask Fable to review the actual skill files read-only. Require findings by
   location and impact, trigger analysis, framework-conflict tests, overlap
   analysis for Code and Scribe, and one of `ACCEPT`, `ACCEPT WITH CHANGES`, or
   `REJECT`.
6. Independently inspect each finding. Revise the skill when the finding is
   supported; reject advice that would add aesthetic taste, duplicate another
   Scoville owner, overfit one framework, or add process without improving the
   UI outcome.
7. Revalidate after each material revision and repeat the independent Fable
   review with the current files, without leaking the expected answer.
8. Stop only when Fable returns `ACCEPT` and the primary implementation review
   finds no material correctness, scope, framework-alignment, activation, or
   validation defect.

Draft UI against the final canonical name `scoville-code-anti-ai-slop`. The
subsequent repository rename makes that referenced target available; it does
not require a mechanical edit to an already accepted UI skill. Do not publish
or install the family as complete while that target name is unresolved.

## Naming migration after skill acceptance

1. Rename the engineering repository to `scoville-code-anti-ai-slop`.
2. Rename its installable directory and frontmatter name together.
3. Update its `agents/openai.yaml`, repository documentation, installation
   paths, links, changelog, and repository description.
4. Update Code references in Scribe and UI to the new canonical name.
5. Update authorized local installation and standing-instruction references
   atomically; do not leave both skill names installed.
6. Validate all three skill directories and inspect every changed repository.
7. Publish only after the local skill contract and migration references agree.

GitHub URL redirects may preserve old repository links, but they do not make an
old skill frontmatter name or installation directory resolve. The migration
therefore does not retain a duplicate compatibility skill.

## Acceptance evidence

- Plan review: Fable returned `ACCEPT` after the precedence, accessibility,
  activation, family-boundary, and scenario amendments were incorporated.
- Skill review loop: Fable reviewed the complete installable directory against
  this plan and both sibling skills. Required revisions clarified the informed
  accessibility exception, kept canonical-owner drift fixes in scope, and made
  greenfield guidance reachable. A fresh final review returned `ACCEPT` with no
  material finding.
- Canonical validation: `quick_validate.py` returned `Skill is valid!`; a
  placeholder search returned no match.
- Isolated host activation, Claude Code 2.1.220 with the skill on its normal
  project-local discovery path:
  - a non-visually phrased dense-table scannability request invoked
    `scoville-ui-anti-ai-slop` and separated rendered proof from source claims;
  - a backend-only queue retry request did not invoke the UI skill; and
  - a Mantine ownership request invoked the UI skill, retained the provider
    theme, semantic tokens, Shared Components, and theme breakpoints, and
    reported the absent rendered application as unverified.
- Final family review: Fable read the prepared Code, UI, and Scribe repository
  states and returned `ACCEPT` with no material finding.
- Naming migration: the public engineering repository is now
  `benjaminstelzer/scoville-code-anti-ai-slop`; its installable directory,
  frontmatter, display metadata, paths, and current documentation use the final
  name. Scribe's published `main` references Code and UI under their final names
  and preserves the concurrent upstream prose update it was rebased onto.
- Migration validation: the canonical validator accepted the final Code,
  Scribe, and UI installable directories. The published Code and Scribe
  repositories each retain only `main`.

## Completion criteria

- Fable accepts the saved plan after any recorded amendments.
- The new skill contains no element-granular visual design system of its own.
- The skill routes framework ownership correctly and composes with Code and
  Scribe without duplicated rules.
- The canonical validator passes and no placeholders remain.
- The required isolated activation and ownership scenarios meet their stated
  pass conditions.
- Fable accepts the final skill files after at least one independent review.
- The primary review independently finds no material defect.
- The Code rename and all authorized references use the new family name.
- The retained plan accurately describes the delivered repository state.

## Status

- [x] Research popular UI skills, design systems, usability principles,
  accessibility requirements, and framework theming conventions.
- [x] Fable review of this plan.
- [x] First skill draft.
- [x] Canonical validation.
- [x] Fable review and revision loop.
- [x] Final independent acceptance.
- [x] Code-skill naming migration.
- [ ] Final repository inspection.
