---
name: edh-deck-review
description: >-
  Evaluates Commander (EDH) decks from Moxfield or Archidekt URLs using Scryfall
  for oracle-accurate card data. URL ingest parses mainboard, sideboard, and
  maybeboard separately (Moxfield keys; Archidekt per-card category tags on the
  cards array), then uses main +
  commander only for core analysis. Legality and bans, core slot
  ratios (lands,
  ramp, draw, removal, wipes, synergy), commander synergy axes, Wizards
  Commander Brackets and game changers, outside-list upgrade searches, and a
  four-turn goldfish narrative, build sentiment, strategic summary, recommended
  play lines, and tutor targets by game stage when tutors are present. Use when
  the user asks for an EDH deck review,
  power level, bracket tuning, card suggestions, or deckbuilding help in the
  EvalDragons project.
---

# EDH deck review (EvalDragons)

## Source of truth

- Prefer an in-repo deck note under `decks/` with `Source: <url>` and sections from [`deck-organization.md`](../../../deck-organization.md).
- Full review write-ups: suggest saving under `reviews/` and committing.

## Workflow (order matters)

### 1. Ingest list from URL

**Always triage zones first** so mainboard, sideboard, and maybeboard stay distinct in the write-up—even though only one zone feeds **core** analysis.

#### 1a. Zone extraction (required for URL ingest)

Build **three named lists** (quantity × card name) before Scryfall:

| Zone | Purpose in review |
|------|-------------------|
| **Main + commander** | Core evaluation (§2–§6, §8–§9): merge commander(s) and main-deck cards only. |
| **Sideboard** | Not in core counts; list separately; optional add hints in §7. |
| **Maybeboard** | Not in core counts; list separately; optional add hints in §7. |

**Moxfield** — `GET https://api.moxfield.com/v2/decks/all/{id}` (id = last segment of `https://www.moxfield.com/decks/{id}`):

| JSON key | Zone |
|----------|------|
| `commanders` | **Main + commander** (object map: values have `quantity`, `card.name`) |
| `mainboard` | **Main + commander** |
| `sideboard` | **Sideboard** |
| `maybeboard` | **Maybeboard** |

Each of those keys is an **object** (map of deck-slot id → `{ quantity, card: { name, … } }`). Sum `quantity` per zone for the **Deck zones** report section. Do not use `tokens` or other keys as main unless the user asks.

**Archidekt** — `GET https://archidekt.com/api/decks/{id}/`:

- **Primary deck list:** the top-level **`cards`** array. Each element is one deck row with **`quantity`**, **`categories`** (string tags: e.g. `Land`, `Commander`, `Maybeboard`, `Sideboard`, `Ramp`, `Creature`, …), and **`card.oracleCard`** (oracle `name`, `cmc`, `legalities`, etc.). Skip rows where **`deletedAt`** is set.
- **Do not rely on `deck.categories[].cards` alone** — on many exports those inner **`cards`** arrays are **empty**; zone logic must use each **`cards[]` row’s `categories`**.
- **Per-row zone** (case-insensitive tag match on that row’s `categories`):
  - If **`Maybeboard`** (or common synonym **`Considering`**) → **Maybeboard** zone.
  - Else if **`Sideboard`** → **Sideboard** zone.
  - Else if the row represents the commander (typically includes **`Commander`** and **not** maybe/side) → **Main + commander** (command zone).
  - Else → **Main** (counts toward the 99; still **Main + commander** bucket for the Deck zones table’s main slice).
- User folder tags (`Ramp`, `Creature`, …) **do not** imply maybe/side; they are main-deck organization unless **Maybeboard** / **Sideboard** tags are present.

If blocked, use export JSON in `decks/incoming/` and apply the **same** row rules.

**Scope (strict) for core math:** Only **Main + commander** cards feed Scryfall bulk resolution for legality, ratios, synergy, brackets, and goldfish. **Never** merge sideboard or maybeboard quantities into those steps.

Record **quantity × name** per zone; printings are metadata only.

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

**Sideboard / maybeboard and suggestions:** You may mention cards that appear in the list’s **sideboard** or **maybeboard** (or Archidekt out-of-main categories) as *optional “already in your ecosystem” add candidates*—but **do not** cap or narrow the improvement set to only those cards. The primary upgrade pool remains **Scryfall discovery** (and the main 99); treat SB/MB as a short optional subsection, not the full search space.

### 8. Wizards Commander Brackets

Use **official articles** linked in `reference.md` — do not invent bracket rules. Count **game_changer** from API; flag MLD, extra turns, heuristic two-card infinites. Compare **estimated current** bracket vs user **target** (from frontmatter or message). Deliver **adjustment playbook**: cuts, swaps, adds.

### 9. Four-turn goldfish

Three hands (fast / medium / flood-screw). Turns 1–4: lands, ramp, spells, mana floating, hand size — only real cards. No opponents. Note assumptions.

## Report template

Fill every section. Use **N/A** with a brief reason only where instructed (e.g. no tutors). Sentiment, strategy, play lines, and tutor guidance must be **grounded in the resolved main+commander list** and Scryfall text—not generic Commander advice.

```markdown
# EDH review: <Deck name>

## Deck source
- URL / file:
- Commander:
- **Core list scope:** main + commander only (sideboard / maybeboard excluded from counts and core analysis; see Outside-list section for optional SB/MB add hints).

## Deck zones (from URL) — required when ingesting from Moxfield / Archidekt
| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|--------|
| Main + commander | … | Source keys / category names used |
| Sideboard | … | |
| Maybeboard | … | |
- If any zone is empty, write `0` and note.

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

## Build value — general sentiment
- Short qualitative take: is the deck coherent for its goals, under/over-built for its stated bracket, and does the card quality **support** the strategy (not a dollar value unless the user asked).

## Strategic summary
- 2–4 tight paragraphs: what the deck is trying to do, how it wins or stabilizes, main risks (speed, interaction, consistency), and how it wants the first few turns to feel.

## Recommended play lines
- Concrete **how to pilot** guidance: opening priorities (lands vs ramp vs setup), when to commit commander vs hold up mana, when to be the aggressor vs hold interaction, and 1–2 **example sequences** (real card names from the main list) for early / mid / late if relevant.

## Tutor targets by game stage
- **Include this section only if** the main+commander list contains **tutors** (cards that search library for cards, e.g. `Demonic Tutor`, `Worldly Tutor`, `Gamble`, equipment/artifact/creature tutors). If **no tutors**, write **N/A — no tutors in main+commander** and skip the table.
- Otherwise provide a **stage table** (early ≈ turns 1–4, mid, late / win-ready). For each stage, list **the most efficient tutor targets** (3–6 per stage max) with one line each: **why this stage**, **what it enables**, and **which tutor** usually finds it.

## WOTC bracket fit
- Game changers count:
- Other flags (MLD, extra turns, combos heuristic):
- Current vs target:

## Outside-list candidates
| Add | Why | Cut | Bracket note |
|-----|-----|-----|--------------|
- **Primary pool:** Scryfall-driven rows above (not limited to builder zones).
- **Optional:** Cards from sideboard/maybeboard only as extra ideas — must not replace or shrink the Scryfall-based list.

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
