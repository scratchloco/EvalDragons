# EDH Tactical Review: The Wise Mothman, Mutant Miller (precon+)

**Review date:** 2026-04-20  
**Deck file:** [decks/the-wise-mothman-mutant-miller-precon.md](../decks/the-wise-mothman-mutant-miller-precon.md)  
**Data:** [decks/incoming/the-wise-mothman-mutant-miller-precon-archidekt.json](../decks/incoming/the-wise-mothman-mutant-miller-precon-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/17228810/the_wise_mothman_mutant_miller_precon](https://archidekt.com/decks/17228810/the_wise_mothman_mutant_miller_precon)
* **Commander:** **The Wise Mothman**
* **Bracket:** **Estimated current:** mid **3**. **Target (deck file):** 3.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 main + 1 commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 61 | Reference options present |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Check present cards manually** | Replace if present and outside pod agreement |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **3.3**. This Sultai mill-mutate-radiation shell needs setup velocity plus resilient payoff engines.

**Synergy overrides (self and table milling + counters growth + graveyard value):**

* **Lands:** Slightly above baseline is acceptable if you want reliable multi-spell turns.
* **Ramp:** Prioritize two-mana acceleration to curve commander into payoff creatures.
* **Draw:** Prefer repeatable engines that trigger from mill or counters.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 39 | +2 vs midpoint | Stable mana for three-color setup |
| Mana ramp | 10 to 12 | 5 | -6 vs midpoint | Needs early velocity for commander turns |
| Card draw | ~10 | 7 | -3 | Consistent refill remains important |
| Interaction (removal + wipes + stack) | 9 to 14 | 10 | -1 vs midpoint | Adequate floor for mid-power pods |
| Synergy / strategy | 25 to 30 | 33 | +6 vs midpoint | Expected in focused Mothman shell |
| Utility | N/A | 5 | N/A | Protection and glue cards |

**Velocity note:** Commander at three mana wants immediate board impact on turn three or four.

**Dependency score (1 to 10):** **7**. The shell has independent lines, but Mothman greatly improves pressure and scaling.

**Non-game check (lands):** About **61.0%** chance to see at least four lands in first ten cards (39 in 99).

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Accumulate counters through mill/radiation patterns, then convert growth into combat and value pressure.
* **The spice:** Cross-utilizing self-mill and opponent-mill axes opens both proactive and disruptive lines.
* **Tactical vulnerabilities:** Graveyard hate, exile-based sweepers, and pods that race before engine setup.

## Interaction & Protection Quality

* **Stack interaction density:** Moderate in Sultai, but sequencing is still key.
* **Board wipe asymmetry:** Better when recursion creatures survive or rebuild quickly.
* **Engine protection:** Prioritize keeping commander and core payoff creature online together.

## Tutor targets by game stage

**Tutors in main + commander:** Limited broad tutoring expected.

**N/A (no dedicated broad tutors in main + commander).**

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** 0.
* **Other flags:** scalable counters pressure and incidental graveyard leverage.
* **Current vs target:** Bracket 3 is a reasonable fit for precon-plus tuning.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land plus one-mana setup piece.
* **T2:** Two-mana ramp or early mill enabler.
* **T3:** Cast Mothman with one trigger line available.
* **T4:** Add payoff creature and start compounding counters.

### Hand B (Grinder)

* **T1-T2:** Develop mana base with tapped lands and one ramp spell.
* **T3:** Value permanent or interaction hold-up.
* **T4:** Commander plus partial setup, pressure begins next turn.

### Hand C (Mulligan test)

* **Opening:** Three lands, no ramp, only expensive payoffs.
* **Line:** Keep in slower pod, mulligan in tuned pod for earlier action.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep 3+ land hands with one accelerator or one reliable setup engine.
* **Deployment timing:** Deploy commander when at least one follow-up trigger is available.
* **Closing the game:** Use stacked counters pressure and selective interaction to force favorable combat cycles.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Mesmeric Orb](https://scryfall.com/search?q=%21%22Mesmeric%20Orb%22) | lowest-impact setup slot | Repeatable mill trigger engine for your core axis | Raises engine consistency |
| [Altar of Dementia](https://scryfall.com/search?q=%21%22Altar%20of%20Dementia%22) | clunky top-end card | Sac outlet that doubles as finisher and self-mill tool | Strong bracket-3/4 bridge |
| [Hardened Scales](https://scryfall.com/search?q=%21%22Hardened%20Scales%22) | weakest counters-adjacent piece | Amplifies every counters event for low cost | Efficient but fair |
| [Ripples of Undeath](https://scryfall.com/search?q=%21%22Ripples%20of%20Undeath%22) | low-value draw slot | Smooths card selection while feeding graveyard plans | Improves consistency |
| [The Master, Transcendent](https://scryfall.com/search?q=%21%22The%20Master%2C%20Transcendent%22) | narrow finisher slot | Strong mutate/surveil payoff bridge in Sultai shell | Medium power bump |

## Bracket tuning plan

1. Keep bracket 3: tighten draw engines and cheap interaction.
2. Move toward 4: add denser repeatable mill/counters pieces plus protection.
3. Improve floor: trim clunky top-end for turn-two ramp and turn-three setup.

## Organization audit

* Deck file follows EvalDragons required headers.
* Sideboard and maybeboard remain separate from core ratios.

## Prioritized changes

1. Add one or two repeatable draw engines that function through self-mill.
2. Keep cheap ramp density high to support commander timing.
3. Add one flexible exile answer for graveyard-centric mirrors.
