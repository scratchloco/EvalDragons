# EDH review: Snail Bomber

**Review date:** 2026-04-18  
**Deck file:** [decks/snail-bomber.md](../decks/snail-bomber.md)  
**Data:** Archidekt API + embedded oracle legality; spot Scryfall checks recommended before events.

## Deck source

- **URL:** [https://archidekt.com/decks/18585903/wick_the_snail_slinger](https://archidekt.com/decks/18585903/wick_the_snail_slinger)
- **Commander:** **Wick, the Whorled Mind** (Archidekt deck title: *Wick, the Snail Slinger*)
- **Target bracket (deck file):** 3 (Upgraded) — edit frontmatter in `decks/snail-bomber.md` if you want a different goal.

## Deck zones (from URL)

| Zone | Total cards (qty sum) | Notes |
|------|-------------------------|--------|
| Main + commander | 100 | 99 + commander |
| Sideboard | 0 | — |
| Maybeboard | 60 | Reference only for core math |

*Archidekt:* each row in the top-level **`cards`** array has its own **`categories`** tags (`Maybeboard`, `Sideboard`, `Commander`, plus user folders like Land, Ramp). See skill §1 / `reference.md`.

## Legality (embedded oracle)

- Main + commander: **all `commander: legal`** in the exported JSON at review time.
- **Re-verify** with `POST https://api.scryfall.com/cards/collection` before tournaments.

## Core ratio table (heuristic)

| Bucket | Target | Approx. actual | Notes |
|--------|--------|----------------|--------|
| Lands | 36–38 | 37 (+ MDFC) | Nonland AMV ~2.74 → 34–35 also defensible |
| Ramp | 10–12 | ~6–8 | Low vs guideline unless counting treasures |
| Card draw | ~10 | ~5–7 | Skullclamp, BMC, Nashi, Wave, etc. |
| Targeted removal | 7–10 | ~12–15 | High interaction density |
| Board wipes | 2–4 | 4 | At top of band |
| Synergy / strategy | 25–30 | remainder | Strong rat + typeline package |

## Strategic summary

Aggressive **Grixis rats** with **typeline payoffs** (Adaptation, Nexus, Xenograft, Leyline), **Panharmonicon** / **Roaming Throne**, and **infect / alt-win** (Glistening Oil, Tainted Strike, Solphim). High ceiling, high variance — mulligans and sweepers matter.

## Recommended play lines

1. Prioritize **fast mana** then **lords** with **protection** (Greaves) or **counter** backup.  
2. **Blasphemous Act** when creature count makes it cheap; watch **own** board.  
3. Infect: only when **lethal** or **two-turn** clock is realistic — do not telegraph into free answers.

## Tutor targets by game stage

**N/A — no classic tutors** in main 99. Pseudo-tutor priorities: **Sol Ring**, **Skullclamp** (with 1-toughness bodies), **Panharmonicon**, **Lord Skitter**, closers **Blasphemous Act** / **Swarmyard Massacre**. Maybeboard includes **Muddle the Mixture** if you promote it.

## WOTC bracket fit

- Reads **Bracket 3–4** depending on table tolerance for **infect** + fast mana.  
- Use official [Commander Brackets](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025) text when claiming bracket fit.

## Outside-list candidates (not limited to maybeboard)

- More **steady draw** and **2 MV ramp** on-colors; optional **protection** if wipes hurt your own board.  
- Promote the best **8–12** from the 60-card maybeboard with a clear plan; still use **Scryfall** for cards not in maybe.

## Prioritized changes

1. Add **2–4 dedicated ramp** pieces.  
2. Add **2–4 card-flow** spells less board-dependent.  
3. Reconcile **four wipes** with **glass-cannon** board presence.  
4. Trim / promote **maybeboard** deliberately.
