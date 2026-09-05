# Development

The only installable Skill source is [`scoville-ui-anti-ai-slop/`](../scoville-ui-anti-ai-slop/).
This directory owns repository development and is not an installation package.

## Current layout

Paths recorded before the 2026-09-05 structure change are historical. Use this mapping
for current local files; frozen evidence retains its original contents and hashes.

| Former repository path | Current repository path |
| --- | --- |
| `docs` | `development/docs` |
| `tests` | `development/tests` |
| `benchmarks` | `development/benchmarks` |

Run development commands from this directory unless the command specifies otherwise.
The installable package is one directory above. Tests, when present, run with
`python -B -m unittest discover -s tests` in the existing development environment.
This move does not add dependencies or establish new model or host qualification.
