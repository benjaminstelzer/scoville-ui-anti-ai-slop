# Why source inspection comes first

The change followed reported spacing inconsistencies, unequal element heights
and misaligned text despite use of the UI Skills. The earlier instructions
could leave source inspection conditional and rely on visual inspection before
asking whether the implementation itself was wrong.

The revised order checks the generating code first, then measures and views the
result. The reason is practical: a local CSS adjustment can make a screenshot
look better while leaving the wrong component or spacing rule in charge.
Measurements and visual inspection are still needed because correct source
alone cannot establish the final layout.

The [decision](docs/decisions/0001-check-source-before-rendered-validation.md)
records that reasoning. The reported failures were not independently reproduced
in this review. Browser and agent regression work remains deferred in
[the plan](docs/plans/0001-source-first-ui-validation.md).
