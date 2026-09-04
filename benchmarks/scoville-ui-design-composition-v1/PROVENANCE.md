# W-004 Design / UI composition benchmark provenance

Frozen: 2026-09-02 before SkillOpt candidate generation.

- Scope: activation, design-decision ownership, implementation ownership,
  proof ownership, selective UI reference reads, and the implementation-
  constraint loop.
- Target and optimizer: `gpt-5.6-sol`, `xhigh`.
- Train: seven self-authored implementation, fallback, precedence, and opt-out
  cases.
- Validation: three self-authored evidence, UI opt-out, and constraint-loop
  cases, not used as item-specific optimizer examples.
- Test / `valid_unseen`: four self-authored composed implementation cases,
  sealed before training and unavailable to the open-split loader until the
  final SkillOpt test stage.
- Source groups: all wording is original. Train uses atomic ownership
  conditions, Validation uses repair/evidence boundaries, and Test combines
  those rules in new implementation scenarios.
- Static-only boundary: Design-only and neither-active remain in the package
  contract, not this dynamic benchmark, because a target with UI loaded cannot
  honestly represent UI being absent.
- Excluded objectives: visual taste and broad UI effectiveness are not
  machine-scored here.
- Independent check: the sealed-holdout custodian must confirm exact and
  conceptual near-duplicate absence without revealing holdout content before
  optimizer proposals begin.

