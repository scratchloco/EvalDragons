# EvalDragons

Commander (EDH) deck lab: skills and rules for **Scryfall-backed** reviews, **core slot ratios**, **synergy**, **Wizards Commander Brackets**, and **goldfish** notes.

**Repository**: [https://github.com/scratchloco/EvalDragons](https://github.com/scratchloco/EvalDragons)

## Quick start

1. `git clone https://github.com/scratchloco/EvalDragons.git`
2. Open the folder in **Cursor** so project [`.cursor/skills/edh-deck-review/SKILL.md`](.cursor/skills/edh-deck-review/SKILL.md) and [`.cursor/rules/`](.cursor/rules/) load.
3. **Pull before** a long review session so skills/rules stay current.

## Layout

| Path | Purpose |
|------|---------|
| [`decks/`](decks/) | Deck source URLs, notes, optional exported JSON |
| [`reviews/`](reviews/) | Dated review write-ups (commit for history) |
| [`deck-organization.md`](deck-organization.md) | Section headers = ratio buckets |
| [`.cursor/skills/edh-deck-review/`](.cursor/skills/edh-deck-review/) | Agent skill + `reference.md` |
| [`.cursor/rules/`](.cursor/rules/) | Cursor rules (`.mdc`) |

## Optional script

From repo root, with Python 3:

```bash
python3 scripts/scryfall_collection.py < cardnames.txt > resolved.json
```

See [`scripts/README.md`](scripts/README.md).
