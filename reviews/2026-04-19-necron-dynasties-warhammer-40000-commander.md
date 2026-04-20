# EDH Tactical Review: Necron Dynasties - Warhammer 40,000 Commander

**Review date:** 2026-04-19  
**Deck file:** [decks/necron-dynasties-warhammer-40000-commander.md](../decks/necron-dynasties-warhammer-40000-commander.md)  
**Data:** [decks/incoming/necron-dynasties-warhammer-40000-commander-archidekt.json](../decks/incoming/necron-dynasties-warhammer-40000-commander-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/3274244/necron_dynasties_warhammer_40000_commander](https://archidekt.com/decks/3274244/necron_dynasties_warhammer_40000_commander)
* **Commander:** **Szarekh, the Silent King**
* **Bracket:** **Estimated current:** strong **3**. **Target (deck file):** 3.

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

**Nonland AMV (main 99):** about **3.79**. This mono-black artifact-creature precon is top-heavy and wants reliable early mana.

**Synergy overrides (artifact recursion / self-mill):**

* **Synergy concentration:** High synergy density is expected; many cards are purposely narrow but become strong in the Necron shell.
* **Draw profile:** Dedicated draw appears low, but graveyard access and recursion lines function as virtual card advantage.
* **Removal profile:** You have enough creature-centric interaction, but some answers are narrower than generic black goodstuff decks.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 37 | In band | Correct for curve and mono-color consistency |
| Mana ramp | 10 to 12 | 10 | In band | Rocks and mana artifacts support commander pacing |
| Card draw | ~10 | 3 | -7 | Under target, partially offset by recursion/forge effects |
| Interaction (removal + wipes + stack) | 9 to 14 | 10 | In band | Solid creature and board-control package |
| Synergy / strategy | 25 to 30 | 35 | +5 to +10 | Expected for dedicated artifact-necron identity |
| Utility | N/A | 3 | N/A | Key equipment/recursion utility pieces |

**Velocity note:** Szarekh at four mana is easy to deploy; attack trigger setup matters more than commander cost.

**Dependency score (1 to 10):** **7**. Deck can still function without commander, but self-mill into artifact creature recovery is much better with Szarekh online.

**Non-game check (lands):** About **55.5%** chance to see at least four lands in first ten cards (37 in 99). Playability is good, but low dedicated draw can still cause stalls.

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Fill graveyard with artifact creatures and vehicles, then recurse and re-deploy value bodies while scaling artifact synergies.
* **The spice:** Necron flavor package creates recursive board pressure without relying on typical black staples.
* **Tactical vulnerabilities:** Graveyard hate, artifact hate, and draws that are all payoff with no setup.

## Interaction & Protection Quality

* **Stack interaction density:** Very low (as expected in mono-black precon shell).
* **Board wipe asymmetry:** **Mutilate**, **Living Death**, and **Their Name Is Death** can reset hard and often favor your rebuild plan.
* **Engine protection:** Some resilience exists via recursion pieces, but proactive protection is thinner than optimized lists.

## Tutor targets by game stage

**Tutors in main + commander:** No dedicated broad tutors in this list.

**N/A (no dedicated tutors in main + commander).**

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** none in this main list.
* **Other flags:** strong recursive artifact loops and resilient board rebuilds.
* **Current vs target:** Bracket 3 is appropriate for stock configuration.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land + cheap rock if available.
* **T2:** Additional ramp artifact.
* **T3:** Setup creature/artifact that stocks graveyard or stabilizes board.
* **T4:** Cast Szarekh and attack when possible for immediate value.

### Hand B (Grinder)

* **T1-T2:** Land sequencing and one mana rock.
* **T3:** Midrange Necron body.
* **T4:** Commander plus defensive line, preparing recursive turns.

### Hand C (Mulligan test)

* **Opening:** Three lands, no ramp, no draw engine.
* **Line:** Keepable in slower pods, but often a ship in tuned bracket-3 environments.

## Recommended Play Lines & Piloting

* **Opening hands:** Prioritize hands with at least one accelerator and one early board-impact artifact creature.
* **Deployment timing:** Attack with Szarekh as soon as practical to convert trigger velocity into hand quality.
* **Closing the game:** Grind value with recursive bodies, then win by superior board reconstitution after wipes.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Phyrexian Arena](https://scryfall.com/search?q=%21%22Phyrexian%20Arena%22) | weakest slow top-end slot | Adds needed steady draw | Small consistency bump |
| [Buried Ruin](https://scryfall.com/search?q=%21%22Buried%20Ruin%22) | one basic Swamp | Recovers key artifacts post-removal | Mostly neutral |
| [Trading Post](https://scryfall.com/search?q=%21%22Trading%20Post%22) | fringe low-impact creature | Flexible recursion and token utility | Slight upshift |
| [Damnation](https://scryfall.com/search?q=%21%22Damnation%22) | one conditional wipe | Cleaner reset when behind | Slight power increase |
| [Skullclamp](https://scryfall.com/search?q=%21%22Skullclamp%22) | *(already not present in this list)* | Strong draw with recursive bodies | Efficient upgrade |

## Bracket tuning plan

1. Stay at 3: add one or two draw engines and keep thematic recursion core intact.
2. Move toward 4: increase efficient draw/tutoring and add premium board control.
3. Improve floor: trim one clunky top-end card for cheap setup velocity.

## Organization audit

* Deck file follows EvalDragons structure and has clean zone handling.
* Role mapping is coherent for Necron artifact-recursion precon identity.

## Prioritized changes

1. Add 1-2 dedicated draw engines.
2. Keep ramp density at or above 10 for smoother opening turns.
3. Add one flexible noncreature answer if your pod runs heavy enchantment/combo pieces.
4. Mulligan aggressively for ramp plus setup, not just mana count.
