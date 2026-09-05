# Benchmark evidence

## Qualified package

The 2026-08-10 package was selected for reliability first and compression only
among equally reliable candidates. The evaluated core has SHA-256
`CA491C09A8301419FD2AFCADAB5249CF241CF03EDC0C19BF823BC6A70692272E`.
The substantive framework reference has SHA-256
`9776FBD685E503514F60099CECC57E554F7699A9363FF524D3BA8BBF42063581`.

The frozen benchmark used `gpt-5.6-sol` with xhigh reasoning for routing and
`gpt-5.6-terra` with medium reasoning for execution. Network access and
prediction reuse were disabled. The benchmark lock, controller configuration,
candidate package hashes, and sealed-Test access ledger are retained in the
Scoville optimization workspace.

| Split | Reliability control | Compressed package |
| --- | ---: | ---: |
| Train | 18/18 | 18/18 |
| Validation | 9/9 | 9/9 |
| Sealed Test | 3/3 | 3/3 |
| Total | 30/30 | 30/30 |

Every row passed the hard result, routing, execution-semantic, process, and
efficiency gates. Across both arms, 60/60 executions completed with provider
usage, zero routing retries, zero shell calls, and exact-once routed reads. The
final report has SHA-256
`18E586066352EFD029692608AEA4F7BD5C059617B8DC2349AF5A3FAD8FA8319E`.

## Token effect

Token counts use `o200k_base` over UTF-8 Skill files.

| Measure | Reliability control | Compressed package | Change |
| --- | ---: | ---: | ---: |
| Always-loaded core | 1,173 | 1,050 | -123 (-10.49%) |
| Complete package | 4,278 | 4,155 | -123 (-2.87%) |
| Loaded Skill context over 30 executions | 71,691 | 68,370 | -3,321 (-4.63%) |

The pre-optimization `v1.0.6` package contained a 1,077-token core and 4,067
package tokens. The qualified version's always-loaded core is therefore 27
tokens smaller (-2.51%), while its complete package is 88 tokens larger because
it retains the explicit local-exception reliability repair. Complete package
size is not runtime prompt cost because only selected references load.

## Overall optimization history

The final four-Skill inventory records 797 run artifacts, including 742
technically valid benchmark runs, 5,762 observed model calls, and 3,452 case
executions. UI accounts for 131 artifacts, 126 valid benchmark runs, 743 model
calls, and 513 case executions. The central machine-readable snapshot has
SHA-256
`1270F95CF9777EBC8E97151E37DFA5525D3E2DB8A6F0163DFBD71C8DA395A781`.

## Interpretation limits

The result proves non-regression and lower prompt payload on the frozen cases.
It does not prove universal correctness, deterministic behavior, or the same
result on a weaker executor. An early GitHub-control diagnostic scored 4/6, but
it predates the corrected read-phase broker and is not treated as a paired
percentage comparison with this benchmark.
