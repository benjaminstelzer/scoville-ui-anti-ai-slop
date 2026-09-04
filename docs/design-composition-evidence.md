# Scoville Design / UI composition evidence

This is a historical development record for the candidates named below. Its
paired Design and holdout statements describe those stages, not the later
Design v1.0.0 successor. Current publication checks and limits are in
[release validation](release-validation.md).

Date: 2026-09-02  
Scope: local pre-SkillOpt W-003 candidate; SOL-only

## Candidate hashes

- UI `SKILL.md`: `5E4005BCC9EBC4476E3B2AB14CD4A4D5CEA7837A15EA17A3C39563E9E3575C48`
- `framework-alignment.md`: `73A5ECF950DA8FC797F6D065EFE876027651CC35D690263064E4968C76E71C3F`
- `ui-quality.md`: `B14F89B01F58D639D6F127FD1E11F10D49A5B0B958CA040A06494EE22D1585B8`
- `validation.md`: `9EDB6C49667133BAFAAA70B4FEA8FB73298FE11DE2DF5E544C34D21C809B3374`
- Paired Design `SKILL.md`: `DEA073D4FB341BFEBCA0E1A14CAC78A758F3E07ECDED226CEF54A7BD9AF808D1`

Post-W-004 retained candidates:

- UI `SKILL.md`: `217F298D4B98808012FE41C024D5B92B01B6F06929245DCC3C8206CE288F462C`
- Design `SKILL.md`: `671B6BAC24569360D23AC0300BEFEC0B478FE035EC9EF79B19E144239369AEF8`

Prior SOL clean-qualification snapshots:

- UI five-file manifest:
  `1A71357254A1961A2D44F788CE8FDE7C895BD5D27CADF3FDE267DB29DA369A0B`
- Design RC7 seventeen-file manifest:
  `623AF68CE12F8E8934DF3DACC7BD8A67CCCB37D0FD16EFFD3D0C1FBE8D74FE85`
- Taste v2 pinned one-file manifest:
  `5B1DB242FF406F7539E3E2D86FAFC5CED471914C15AED9A76786A480D7DC7D47`

The independent custodian verified all three custody-owned snapshots before
case execution. No clean holdout case ran under a superseded Design package.

Current Terra High UI routing candidate:

- UI `SKILL.md`:
  `C785BABF95B600A503C0BA80DB349A915628997ED15AA133FE6A1D9A93D47554`
- UI five-file manifest:
  `2519263462CEF1E2B7008888AD601E4F56F486A1BF06D31558D9924A7E288FF7`
- immutable snapshot:
  `Z:\Projekts\AI\SkillOpt-Studio\frozen-controls\scoville-ui-routing-c785b-final`

The first open Terra High UI-only run returned the correct owners but loaded
Quality and Validation unnecessarily. The focused `OWNERSHIP-ONLY` repair
passed the same case with only Core and Framework loaded: hard, behavior, and
efficiency 1/1/1. Receipt SHA-256:
`197FF013D6F0C4C53442E6F58823EE8B12C56988AB797CDF6EDDFE6A8FE2A124`.
This is one open routing result, not sealed qualification.

A following composed ownership-only run returned `design / ui / ui`, read only
the UI Core, and did not read or simulate Design. The preregistered Framework
expectation was overbroad because the complete Design record had already
settled ownership and no implementation path or proof was requested. Receipt
SHA-256:
`A4DBAD14A0A903F3760650A63E5A56F72521DB95CFBA1A386AFE31FAA5C50FB4`.

Target was `gpt-5.6-sol`, `xhigh`, local Codex desktop, network disabled,
through SkillOpt commit `ba820b500f9da96685cf2780c7dc85ed4eb6563e`.

## Contract implemented

- Incumbent product design system remains above an active Design decision.
- Design is active only when its instructions are in the current task context
  and applicable to the concrete concern; installation/discovery is irrelevant.
- Active Design owns design definition and visual judgment. UI consumes the
  canonical record and owns framework-valid implementation, component states,
  semantics, focus/input behavior, announcements, responsive mechanics, and
  rendered/interaction proof.
- UI retains its bounded Greenfield fallback when Design is absent, inactive,
  inapplicable, or explicitly excluded.
- Both Skills remain standalone and never search for or simulate one another.
- A real implementation constraint returns only the affected decision to
  Design; UI does not silently redesign.

The canonical handoff fields are identical in both Skills: concern, decision,
intended effect, authority/source, preserved constraints, allowed variation,
deliberate exception and compensation when any, validation target, and current
evidence status.

## Dynamic routing result

Final runs:

- `ui-design-composition-train-r6`: 7/7
- `ui-design-composition-val-r6`: 3/3

The ten active-context cases cover:

- Design installed but inactive;
- UI-only Greenfield fallback;
- both active with a complete Design record;
- incumbent design-system precedence;
- Design opt-out;
- UI opt-out;
- Design/UI implementation-constraint loop;
- framework-only customization routing;
- Quality plus Validation routing; and
- Evidence-only Validation routing.

Every case passed exact owner enums, expected-answer matching, Core-before-
reference phases, exact-once reads, forbidden-reference reads, and shell-call
budgets. The incumbent-owner wording was additionally repeated three times in
`ui-design-composition-incumbent-r4`, `-r5`, and `-r6`; all three passed.

Design-only and Neither-active cannot be faithfully instrumented while the UI
Skill is itself loaded. They remain explicit static family-contract cases in
`tests/evaluation-cases.json`, along with the canonical record, for a total of
eleven source-level cases. Treating a loaded UI Skill as absent would be a false
test.

## Regression boundary

The earlier locked `SkillOpt-Studio/benchmarks/scoville-ui-routing-v4` could not
be rerun because its existing `BENCHMARK_LOCK.json` no longer matched the
referenced controller hash. The locked evidence was not edited or bypassed.
Three portable equivalents were added to the new composition suite:

- Framework-only customization: passed;
- Quality plus Validation responsive/state audit: passed;
- Evidence-only Validation: passed.

Skill Creator validation passed, `tests/evaluation-cases.json` parses with 11
cases, and `git diff --check` reports no whitespace error. This evidence does
not replace W-004 optimization, full legacy regression, rendered product UI
tests, or W-005 qualification.

## W-004 repair and adjudicated regression

SkillOpt run `ui-w4-train-r1` passed all seven Train and all three Selection
cases and produced no usable patch. The initial source remained the winner.
The first sealed W-004 Test then passed 3/4. Its one failure returned the
correct ownership values but omitted UI Quality for a composed implementation
that explicitly required keyboard, error, loading, and narrow-width mechanics.

The Core was corrected narrowly. Under COMPOSED work, Quality now loads when
implementation must reason about component states, semantics, accessibility
structure, focus/input, announcements, or responsive mechanics. A separate
frozen row that required responsive and state proof had originally forbidden
Quality. Independent SOL adjudication classified that v1 Gold as defective.
The original v1 lock and result remain unchanged.

Adjudicated v2 results on the retained candidate:

- open Validation: `ui-w4-v2-val-r1`, 3/3 Hard;
- consumed Test regression: `ui-w4-v2-test-regression-r1`, 4/4 Hard;
- v2 benchmark lock:
  `D10D6AFEE2CE221634E7FA5A6BD472CC15B81F9F1E14231FCC9C15F89049A33C`.

These are post-diagnosis regressions, not renewed unseen evidence.

## Final local candidate boundary

The retained five executable UI files match manifest
`FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`.
Skill Creator validation passes, the static composition fixture contains 11
cases, and the Design/UI boundary validator reports active Design with strict
UI implementation plus standalone UI Greenfield fallback.

The paired Design project later replaced a complete sealed-holdout rerun with
user-directed targeted verification of its demonstrated routing defect. No
Holdout shard completed. This UI evidence therefore remains configuration-
specific composition and regression evidence, not a complete sealed
qualification or a broad quality claim.
