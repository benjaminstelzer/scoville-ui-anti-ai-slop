---
format_version: 1
id: ADR-0001
status: accepted
created: 2026-09-10
accepted: 2026-09-10
scope: ui/validation-order
---

# Check source before rendered validation

## Decision

Benjamin explicitly requires inspection and correction of the generating code and CSS before browser measurement and visual inspection. Record this selected order; implementation has not been requested yet.

## Problem

Benjamin reports inconsistent spacing, inaccurate measurements, unnecessary custom CSS, unequal element heights and misaligned text despite both UI Skills being used. These are user-reported runtime failures, not independently reproduced incidents. The current validation reference makes inspection conditional and permits measurement only when visual inspection is insufficient.

## Drivers

Known implementation defects must not survive because a screenshot appears acceptable. Source correctness and rendered correctness need separate evidence.

## Considered alternatives

A screenshot-first loop can encourage compensating CSS over an incorrect implementation. Source-only validation cannot establish actual geometry or optical alignment. The selected sequence retains both checks in the required order.

## Consequences

Implementation work corrects known in-scope source violations before rendered validation. Audit-only work reports them without unauthorized edits; missing source or runtime limits proof and never produces a pass. Runtime-only questions remain measurement targets after available source checks.

## Confirmation

Observe an agent correcting a source-visible spacing or ownership defect before its first visual inspection, then measuring and inspecting the corrected result. Verify that a later layout edit invalidates affected earlier evidence.

## Revisit when

The user changes the required order or a supported non-web surface requires an equivalent platform-specific inspection method.
