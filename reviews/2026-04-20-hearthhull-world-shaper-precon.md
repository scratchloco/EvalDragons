# EDH Tactical Review: Hearthhull, World Shaper (precon+)

**Review date:** 2026-04-20  
**Deck file:** [decks/hearthhull-world-shaper-precon.md](../decks/hearthhull-world-shaper-precon.md)  
**Data:** [decks/incoming/hearthhull-world-shaper-precon-archidekt.json](../decks/incoming/hearthhull-world-shaper-precon-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/15953809/hearthhull_world_shaper_precon](https://archidekt.com/decks/15953809/hearthhull_world_shaper_precon)
* **Commander:** **Hearthhull, the Worldseed**
* **Bracket:** **Estimated current:** mid **3**. **Target (deck file):** 3.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 main + 1 commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 10 | Reference options present |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Absent** | N/A |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **3.46**. This Jund lands shell wants early ramp plus recurring landfall value.

**Synergy overrides (lands from everywhere + graveyard recursion + token pressure):**

* **Lands:** Slightly above baseline is correct when commander scales with land movement.
* **Ramp:** Favor cheap land-based acceleration to turbocharge landfall turns.
* **Interaction:** Prioritize flexible answers that protect your value engine.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 40+ (landfall override) | 40 | +0 vs override | Landfall commander supports elevated land count |
| Mana ramp | 10 to 12 | 13 | +2 vs midpoint | Keep most ramp at CMC 1-2 where possible |
| Card draw | ~10 | 7 | -3 | Needs enough refill to keep lands flowing |
| Interaction (removal + wipes + stack) | 9 to 14 | 16 | +5 vs midpoint | Flexibility matters against faster pods |
| Synergy / strategy | 25 to 30 | 23 | -4 vs midpoint | Expected for focused lands engine |
| Utility | N/A | 0 | N/A | Protection and glue cards |

**Velocity note:** Commander at six mana wants at least two acceleration pieces by turn three.

**Dependency score (1 to 10):** **7**. The deck functions without commander, but velocity and payoff density jump once Hearthhull is online.

**Non-game check (lands):** About **63.6%** chance to see at least four lands in first ten cards (40 in 99).

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Ramp, move lands between battlefield and graveyard, and convert repeated landfall triggers into board advantage.
* **The spice:** Sacrifice and replay land packages create burst turns that outscale fair midrange decks.
* **Tactical vulnerabilities:** Graveyard hate, fast combo tables, and hands with payoffs but no early ramp.

## Interaction & Protection Quality

* **Stack interaction density:** Low to moderate in Jund colors; table positioning matters.
* **Board wipe asymmetry:** Better when your list includes recursion after a wipe.
* **Engine protection:** Protect key landfall engines before committing to all-in turns.

## Tutor targets by game stage

**Tutors in main + commander:** Light, mostly role-specific search.

**N/A (no dedicated broad tutors in main + commander).**

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** 0.
* **Other flags:** land recursion snowball potential.
* **Current vs target:** Mid bracket 3 is a stable fit for precon-plus tuning.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Tapland or basic plus one-mana setup piece.
* **T2:** Two-mana ramp that adds a land to battlefield.
* **T3:** Additional ramp or early landfall payoff.
* **T4:** Set up commander turn with protection or recursion support.

### Hand B (Grinder)

* **T1-T2:** Land drops plus a rock or ramp spell.
* **T3:** Value permanent, hold interaction if available.
* **T4:** Start recurring lands to stabilize velocity.

### Hand C (Mulligan test)

* **Opening:** Three lands, two expensive spells, no acceleration.
* **Line:** Borderline keep in casual pod, mulligan in tuned pod.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep hands with 3+ lands and one cheap ramp effect.
* **Deployment timing:** Delay commander one turn if it protects a stronger follow-up line.
* **Closing the game:** Chain landfall payoffs and token pressure across two combat steps.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [World Shaper](https://scryfall.com/search?q=%21%22World%20Shaper%22) | weakest high-CMC filler | Massive graveyard-to-battlefield land burst | Stronger snowball turns |
| [Splendid Reclamation](https://scryfall.com/search?q=%21%22Splendid%20Reclamation%22) | low-impact recursion slot | Converts fetch/sac lands into explosive rebuild | Fits bracket 3-4 |
| [Ramunap Excavator](https://scryfall.com/search?q=%21%22Ramunap%20Excavator%22) | clunky value creature | Reliable extra land drops from graveyard | Consistency bump |
| [Valakut Exploration](https://scryfall.com/search?q=%21%22Valakut%20Exploration%22) | weakest draw slot | Turns every landfall into pressure and cards | Fair but efficient |
| [Aftermath Analyst](https://scryfall.com/search?q=%21%22Aftermath%20Analyst%22) | slow ramp piece | Redundant recursion body for your main axis | Improves resilience |

## Bracket tuning plan

1. Keep bracket 3: add one cheap draw engine and one flexible removal spell.
2. Push toward 4: increase fast land recursion density and tighten curve.
3. Reduce non-games: mulligan aggressively for early ramp plus payoffs.

## Organization audit

* Deck file follows EvalDragons bucket headers and keeps sideboard/maybeboard separate.
* Most role assignments are coherent for landfall-recursion strategy.

## Prioritized changes

1. Raise dedicated draw quality if current draw count is under target.
2. Add one more instant-speed flexible answer.
3. Preserve high land density for commander-trigger consistency.
