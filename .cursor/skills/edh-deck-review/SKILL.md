---
name: edh-deck-review
description: >-
  Evaluates Commander (EDH) decks from Moxfield or Archidekt URLs using Scryfall
  for oracle-accurate card data, legality and bans, core slot ratios (lands,
  ramp, draw, removal, wipes, synergy), commander synergy axes, Wizards
  Commander Brackets and game changers, outside-list upgrade searches, and a
  four-turn goldfish narrative. Use when the user asks for an EDH deck review,
  power level, bracket tuning, card suggestions, or deckbuilding help in the
  EvalDragons project.
---

# EDH deck review (EvalDragons)

## Source of truth

- Prefer an in-repo deck note under `decks/` with `Source: <url>` and sections from [`deck-organization.md`](../../../deck-organization.md).
- Full review write-ups: suggest saving under `reviews/` and committing.

## Workflow (order matters)

### 1. Ingest list from URL

**Moxfield**: `GET https://api.moxfield.com/v2/decks/all/{id}` — extract `id` from URLs like `https://www.moxfield.com/decks/{id}`. Merge **commanders** + **mainboard**; ignore maybeboard unless asked.

**Archidekt**: `GET https://archidekt.com/api/decks/{id}/` — numeric `id` from deck URLs (e.g. `.../decks/1234567/...`). Map cards from API payload to quantities + names. If blocked, use user-provided export JSON in `decks/incoming/`.

Record **quantity × name**; printings are metadata only.

### 2. Scryfall normalization

- `POST https://api.scryfall.com/cards/collection` with up to **75** `name` identifiers per request (chunk the deck).
- For each card capture: `name`, `type_line`, `mana_cost`, `cmc`, `oracle_text`, `color_identity`, `legalities.commander`, `game_changer`, `scryfall_uri`.
- For long lists prefer [`scripts/scryfall_collection.py`](../../../scripts/scryfall_collection.py).

### 3. Legality and bans

- Flag `legalities.commander != legal` and color identity not subset of commander’s.
- Cross-check banlist via Scryfall (see `reference.md`).
- **Cleaned 99**: for math/synergy/brackets, analyze as if illegal cards were removed (note placeholders).

### 4. Organization audit

Compare file sections to [`deck-organization.md`](../../../deck-organization.md); call out mis-grouped cards and missing buckets.

### 5. Core ratio table (required)

Use targets from [`edh-core-ratios.mdc`](../../rules/edh-core-ratios.mdc):

| Bucket | Target |
|--------|--------|
| Lands | 36–38 (34–35 if nonland AMV < 3; ~40 landfall / high MV) |
| Ramp | 10–12 |
| Card draw | ~10 (burst + steady) |
| Targeted removal | 7–10 |
| Board wipes | 2–4 |
| Synergy / strategy | 25–30 |

Emit a table: bucket, target, actual, delta, rationale. Commander excluded from 99; each nonland once in a primary bucket (document judgment calls).

### 6. Commander axes and synergy

- State **3–6 axes** from commander text/types.
- Score nonlands: commander synergy, internal synergy, role fit, anti-synergy flags (Low/Med/High or 0–2).
- Output synergy matrix, misaligned includes, redundancy, cluster gaps.

### 7. Outside-list candidates (Scryfall)

After gaps are clear, run **targeted** searches (`legal:commander` + identity, see `reference.md`). Return **10–25** cards with: fit reason, suggested cut, bracket impact. Verify each candidate on Scryfall before listing.

### 8. Wizards Commander Brackets

Use **official articles** linked in `reference.md` — do not invent bracket rules. Count **game_changer** from API; flag MLD, extra turns, heuristic two-card infinites. Compare **estimated current** bracket vs user **target** (from frontmatter or message). Deliver **adjustment playbook**: cuts, swaps, adds.

### 9. Four-turn goldfish

Three hands (fast / medium / flood-screw). Turns 1–4: lands, ramp, spells, mana floating, hand size — only real cards. No opponents. Note assumptions.

## Report template

Fill every section.

```markdown
# EDH review: <Deck name>

## Deck source
- URL / file:
- Commander:

## Target Commander Bracket
- Goal (1–5):
- Stated intent (if any):

## Legality table
| Card | Commander legal | Notes |
|------|-----------------|-------|

## Cleaned list delta
- Removed illegal / identity errors for analysis:

## Core ratio table
| Bucket | Target | Actual | Delta | Notes |
|--------|--------|--------|-------|-------|
| Lands | … | … | … | AMV … |
| Ramp | … | … | … | |
| Card draw | … | … | … | burst vs steady |
| Targeted removal | … | … | … | type coverage |
| Board wipes | … | … | … | |
| Synergy / strategy | … | … | … | |

## Mana and curve
- Nonland AMV:
- CMC buckets summary:

## Role density
- Short paragraph + counts if useful.

## Commander axes
1. …

## Synergy and alignment audit
- Matrix summary:
- Misaligned:
- Cluster gaps:

## WOTC bracket fit
- Game changers count:
- Other flags (MLD, extra turns, combos heuristic):
- Current vs target:

## Outside-list candidates
| Add | Why | Cut | Bracket note |
|-----|-----|-----|--------------|

## Bracket tuning plan
1. …

## Organization audit
- …

## Turns 1–4 (three scenarios)
### Hand A — …
### Hand B — …
### Hand C — …

## Prioritized changes
1. …
```

## Limitations

Heuristic ratios, heuristic combos, beta WOTC text — cite Scryfall and Wizards links. Site APIs may rate-limit; fall back to exports.
