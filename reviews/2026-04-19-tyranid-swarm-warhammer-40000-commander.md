# EDH Tactical Review: Tyranid Swarm - Warhammer 40,000 Commander

**Review date:** 2026-04-19  
**Deck file:** [decks/tyranid-swarm-warhammer-40000-commander.md](../decks/tyranid-swarm-warhammer-40000-commander.md)  
**Data:** [decks/incoming/tyranid-swarm-warhammer-40000-commander-archidekt.json](../decks/incoming/tyranid-swarm-warhammer-40000-commander-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/3263022/tyranid_swarm_warhammer_40000_commander](https://archidekt.com/decks/3263022/tyranid_swarm_warhammer_40000_commander)
* **Commander:** **The Swarmlord**
* **Bracket:** **Estimated current:** strong **3** with occasional spike turns. **Target (deck file):** 3.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 + commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 0 | Empty on Archidekt |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Absent** | N/A |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **3.32**. This is a counters-creature combat deck with respectable curve discipline for a precon.

**Synergy overrides (counters + X-spells + combat pressure):**

* **Ramp count:** Above baseline by design; X-cost and high body density reward extra mana.
* **Draw profile:** Raw dedicated draw is low, but commander death-trigger draw plus counters engines add virtual cards.
* **Interaction shape:** Creature-based answers and combat tricks dominate; stack interaction is light.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 39 | +1 to +3 | Slightly high, but supports X-spell and top-end Tyranids |
| Mana ramp | 10 to 12 | 12 | In band | Correct for commander pacing and X scaling |
| Card draw | ~10 | 2 | -8 | Low dedicated draw; relies on commander and engine effects |
| Interaction (removal + wipes + stack) | 9 to 14 | 7 | Slightly low | Needs one or two more flexible answers for faster pods |
| Synergy / strategy | 25 to 30 | 35 | +5 to +10 | Expected in focused Tyranid counters shell |
| Utility | N/A | 4 | N/A | Protection and anti-cast-tax support |

**Velocity note:** The Swarmlord at six mana is expensive, but your ramp density and land count make turn-five to six casts realistic.

**Dependency score (1 to 10):** **7**. Deck can pressure without commander, but card-flow texture improves meaningfully once Swarmlord is active.

**Non-game check (lands):** About **61.0%** chance to see at least four lands in first ten cards (39 in 99). Mana consistency is strong.

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Ramp early, deploy evolving Tyranid threats, stack counters, and turn board size into lethal combat turns.
* **The spice:** Counter multipliers and X-scaling creatures make each extra mana source matter more than in generic creature decks.
* **Tactical vulnerabilities:** Board wipes before commander value turns, low dedicated draw in attrition games, and stack-heavy pods.

## Interaction & Protection Quality

* **Stack interaction density:** Low, mostly expected in Temur precon context.
* **Board wipe asymmetry:** **Tyranid Invasion** and **Starstorm** can reset selectively, but full asymmetry is inconsistent.
* **Engine protection:** **Inspiring Call**, **Tyrant Guard**, and **Venomthrope** provide meaningful but not exhaustive insulation.

## Tutor targets by game stage

**Tutors in main + commander:** No dedicated broad library tutors in this list.

**N/A (no dedicated tutors in main + commander).**

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** none in this main list.
* **Other flags:** high creature pressure and occasional explosive counter scaling.
* **Current vs target:** Bracket 3 is a good fit for stock configuration.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land + one mana ramp start.
* **T2:** Additional ramp or early counters enabler.
* **T3:** Mid-size Tyranid body with counters support.
* **T4:** Board-development plus protection setup for commander curve.

### Hand B (Grinder)

* **T1-T2:** Land sequencing with two-mana ramp.
* **T3:** Utility creature plus incremental setup.
* **T4:** First major threat and prepare for Swarmlord turn.

### Hand C (Mulligan test)

* **Opening:** Four lands and only expensive creatures.
* **Line:** Usually keepable, but weak versus tuned pods unless one ramp piece appears.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep hands with ramp and one actionable early creature or engine piece.
* **Deployment timing:** Do not rush commander into open removal unless you can convert immediate value.
* **Closing the game:** Stack counters and trample/evasion support, then commit one decisive combat cycle.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Guardian Project](https://scryfall.com/search?q=%21%22Guardian%20Project%22) | least-impact draw slot | Big draw boost for creature-dense shell | Slight consistency bump |
| [The Ozolith](https://scryfall.com/search?q=%21%22The%20Ozolith%22) | low-impact flex card | Preserves counters through wipes | Moderate power increase |
| [Beast Within](https://scryfall.com/search?q=%21%22Beast%20Within%22) | narrow removal slot | Flexible answer coverage | Improves interaction floor |
| [Herald's Horn](https://scryfall.com/search?q=%21%22Herald%27s%20Horn%22) | clunkier top-end slot | Cost reduction plus card selection for tribe | Neutral to slight upshift |
| [Return of the Wildspeaker](https://scryfall.com/search?q=%21%22Return%20of%20the%20Wildspeaker%22) | weakest one-shot effect | Better card refill and combat push | Strong but fair in 3-4 |

## Bracket tuning plan

1. Stay at 3: add 1-2 draw/interaction upgrades while preserving thematic core.
2. Move toward 4: tighten interaction and add one high-impact counter synergy piece.
3. Improve floor: trim one expensive creature for a cheap draw engine.

## Organization audit

* Deck file follows EvalDragons structure and zone handling.
* Role mapping is coherent for Tyranid counters/ramp shell.

## Prioritized changes

1. Add one dedicated draw engine.
2. Add one flexible instant-speed answer.
3. Keep ramp density high because commander and threats scale with mana.
4. Mulligan for acceleration plus board plan, not raw threat count.
