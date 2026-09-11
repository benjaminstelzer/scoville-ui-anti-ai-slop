# Rendered UI Validation

Use the ordered gates below for affected implementation and audit concerns.
Select relevant conditions by scope and risk, without skipping an applicable gate.

## Contents

- Establish the claim
- Derive the test surface
- Source first, then measurement, then sight
- Measure relationships, not declarations
- Inspect with a comparison and a hypothesis
- Consistency audit coverage
- Use automation as supporting evidence
- Handle reviews and missing renderers
- Report the result

## Establish the claim

State what the change is supposed to improve and which observable result would
show it. Separate claims about:

- source or build correctness;
- framework and token alignment;
- rendered layout and hierarchy;
- interaction and state behavior;
- responsive or adaptive behavior; and
- accessibility conformance.

Evidence for one category does not prove another. A passing build cannot prove
that text is visible; one screenshot cannot prove keyboard operation; an
automated audit cannot prove that a task is understandable.

For composed work, derive claims from the active Design record's `validation
target` and preserve its `current evidence status`. Verify implementation and
framework behavior without re-scoring the settled design decision. If a real
constraint prevents the intended effect, report the exact component/platform
limit and affected concern so Design can revise that decision; do not silently
substitute a different layout or visual system.

## Derive the test surface

Use the project's supported environments and the conditions affected by the
change. Select only relevant combinations of:

- viewport, window mode, orientation, or safe-area constraints;
- mouse, keyboard, touch, switch, or platform navigation;
- default, focus, hover, pressed, selected, disabled, loading, success, error,
  empty, or permission states;
- supported themes and contrast modes;
- realistic short, long, dynamic, and localized content; and
- text scaling, browser zoom, reduced motion, and other supported user settings.

Do not impose a universal breakpoint list or test every possible combination.
Include a condition when it could change the decision or expose a failure in the
requested flow.

When a flow supports multiple input methods and one method can leave focus,
selection, pointer capture, composition, or shared state that affects another,
exercise at least one relevant handoff in the same task, such as pointer to
keyboard. Separate clean-start passes for each method do not prove that the
transition works. Do not create a cross-input matrix when the methods are
behaviorally independent.

When polished presentation is an explicit outcome, rendered evidence must show
a representative populated state rather than only an empty, loading, or error
state. Use realistic information density, content lengths, hierarchy, and at
least one relevant interaction state. Capture each target viewport named by the
task as its own observation so a desktop result does not stand in for mobile or
vice versa. Keep recovery-state evidence separate: a convincing error state
does not prove the primary populated surface, and the reverse is equally true.

## Source first, then measurement, then sight

For implementation, batch related UI changes and complete the planned edits
before running these gates in order within the affected scope. Inspect source
as needed to guide implementation. Validate at the end of the batch.
For an audit, inspect and report source defects first, then measure and inspect
without repairing them. Audit findings never authorize edits.

1. **Source:** Inspect generating markup/components, supported props/variants,
   styles and their owner. Correct known in-scope source defects before the
   first layout measurement or viewed render. Check duplicate spacing owners,
   arbitrary dimensions/offsets, token bypass, primitive rebuilds and obsolete
   overrides. Run relevant existing syntax, lint, component or build checks.
   A build does not audit design-system ownership. Source/API/stylesheet
   inspection is not a layout measurement.
2. **Measurement:** Once the source gate is satisfied, measure the affected
   relationships in the actual runtime against independently established
   references. Follow the measurement contract below.
3. **Sight:** View the rendered image and apply the visual routine below.
   Numeric equality does not establish optical alignment.

Before writing a custom styling exception, including inline styles and styling
props, name the unmet requirement, concrete owner API/component checked, why
it fails and the smallest scope. An official token alone does not justify the
exception. Prefer supported composition and variants. Inspect the final diff
for unnecessary custom styling and remove compensation made obsolete by the fix.

Do not run measurements, screenshots or sight checks after each small layout
edit. Validate the completed change batch once. If validation reveals defects,
collect and implement the related corrections before repeating affected source
checks, measurements and sight checks at the end of that correction batch.
Later edits invalidate only the affected evidence. Refresh it after those edits
are complete, before reporting completion. Associate final measurements and
viewed images with the same revision, content and state. Available usable tools
cannot be skipped for convenience. Missing tools or source limit the conclusion,
never create a pass.
Source-only and screenshot-only requests retain those limits without requiring
unrequested work. Preserve every known required gap in the result.

## Measure relationships, not declarations

Before the evaluated measurement, identify reference elements and edges, the
expected relationship and its source, and any justified tolerance. Derive these
from an unchanged owner contract or demonstrably suitable reference. Do not
choose tolerance after seeing the result or derive a target from candidate CSS.
An unresolved target stays unresolved. There is no universal pixel tolerance.

Record compact evidence for each affected relation:

`target/group | revision/state/viewport | source declaration + owner | expected relation + tolerance | resolved value | measured geometry | result`

Keep the authored unit/expression, computed value and measured distance separate.
Preserve `em`, `rem`, `px`, percentages, unitless line-height, token references,
calculations and logical properties. Equal current pixels do not authorize
substitution. Record the relevant element/root font or container basis.

Wait for required fonts, content and transitions to settle. Inspect loaded
styles and final DOM where they affect the claim. Compare peers with the same
relevant role, variant, state, typography and layout conditions. Explain
deliberate differences. Peers sharing a wrong override can be equally wrong.

For vertically ordered non-overlapping boxes, `B.top - A.bottom` measures their
border-box separation. It does not measure glyph whitespace or a baseline.
Account for margins and collapsing, padding, borders, line boxes, wrapping,
intervening elements and fractional rounding. Do not sum declarations and call
the result observed geometry. A minimum height is not a fixed height.

## Inspect with a comparison and a hypothesis

View the scoped region in context first, then details at a consistent scale.
Keep an unaltered context image/crop when guides help comparison. For each
applicable concern, record a located deviation or scoped pass. Explain relevant
exclusions without producing boilerplate for unrelated lenses.

| Look for | Compare |
| --- | --- |
| Grouping and rhythm | Equivalent relationships within and across sections |
| Content edges and text alignment | Intended shared edge, top, baseline or center, not an assumed universal alignment |
| Apparent whitespace | Line boxes and glyph position alongside measured box gaps |
| Controls and icons | Same-variant size, internal padding and icon/text placement |
| Content/state changes | Wrap, clipping, overlap, hidden-content holes and reading order |

**Worked diagnosis:** Two same-variant controls have equal outer heights, but
the text in B sits visibly lower than in reference A. Mark their shared top
edge or use a side-by-side crop at the same scale. State that observation first.
Then inspect font/line-height, internal padding and alignment props. If an icon
is displaced, inspect its viewBox or font metrics too. Confirm the cause before
correcting its owner. Do not invent a baseline measurement from outer rectangles.
If the optical question cannot be resolved, report it unverified.

**Valid difference:** A compact control and a standard control have different
native heights and padding. Verify their intended variants before treating
their difference as a defect. Do not override native internals for symmetry.

Recheck relevant widths, expanded text and affected states after the correction
batch is complete.
Zoom alone does not test whether `em`, `rem` and fixed pixels behave equivalently.
Where units are at risk, vary element/root font conditions independently.

## Consistency audit coverage

An ordinary request to check page X for consistency selects Audit with a
consistency focus. Keep the named page or region as scope. It is not permission
to redesign, edit, audit unrelated screens or perform a full accessibility audit.

1. Start from source with an inventory of regions, component families, distinct
   variants and known exceptions. Include headings, body/label/help/status text,
   actions, controls, icons, containers, toolbars, data and footer/pagination
   where present. Use stable locators or identifiable labels and owner-backed
   equivalence groups.
2. After source findings, reconcile with final rendered DOM. Include content
   below the first viewport, nested scroll areas and relevant same-page tabs,
   disclosures, menus and overlays. Add newly revealed elements to the inventory.
   Use read-only interactions. Do not save, submit, delete or cause external
   effects just to obtain coverage. Name inaccessible states as unverified.
3. Map every entry to its owner/reference and applicable source, measurement
   and sight evidence. Use `pass`, `defect`, `unverified` or justified
   `not-applicable` for each stage. Compare between as well as within groups.
4. Reconcile all discovered entries before concluding. An unmapped entry is a
   coverage gap. Report coverage and named gaps separately from prioritized
   findings. Required unverified entries prevent a complete consistency pass.

Repeated/virtualized data may use justified representative samples, but state
the uninspected population and variants. A partial sample supports only a
coverage-limited result, never an unqualified complete-page or every-row pass.
Distinct in-scope variants and known exceptions remain inventory requirements.
Do not enumerate every virtual row merely to simulate completeness.

When Skills compose, reuse one compatible inventory and evidence set. Retain
the platform owner's comparisons and valid exceptions. A DOM count, screenshot
or claimed percentage alone proves neither coverage nor correctness.

## Use automation as supporting evidence

Run focused component, integration, visual-regression, and accessibility checks
already owned by the project when they cover the change. Add or change automated
coverage only when it protects a behavior that can regress and the repository
has a canonical test seam. Do not create screenshot churn or assertion-free
tests to simulate proof.

Treat scanner output as a lead and a bounded check. Confirm relevant findings in
the rendered interface and interaction path.

## Handle reviews and missing renderers

For an audit without an implementation request, inspect the available rendered
surface and return prioritized findings with the observed evidence, affected
task, owner, and consequence. Do not silently redesign or edit.

If no browser, simulator, device, terminal harness, or runnable application is
available, inspect source only far enough to identify likely risks. Report
rendered behavior, responsiveness, and visual quality as unverified. Do not turn
absence of evidence into a pass.

## Report the result

Report:

- the surfaces and conditions actually rendered;
- the task and states exercised;
- relevant automated checks and their result;
- framework or design-system alignment observed; and
- residual unverified conditions or owner conflicts.

When supplied evidence explicitly names unobserved conditions that bound the
requested claim, retain those conditions individually or in an equally precise
grouping. A broad caveat does not preserve a narrower evidence gap.

Avoid generic claims such as "responsive," "accessible," or "looks good" when
the evidence covers only a narrower condition.
