# EDH Tactical Review: Prim Dragano

**Review date:** 2026-04-25  
**Deck file:** [decks/prim-dragano.md](../decks/prim-dragano.md)  
**Data:** [decks/incoming/prim-dragano-archidekt.json](../decks/incoming/prim-dragano-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/21985305/prim_dragano](https://archidekt.com/decks/21985305/prim_dragano)
* **Commander:** **Prismari, the Inspiration**
* **Bracket:** **Estimated current:** upper **3**. **Target (deck file):** 3.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 main + 1 commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 16 | Reference options present |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Check present cards manually** | Replace if present and outside pod agreement |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **2.6**. This Izzet shell appears to reward sequencing and spell velocity over raw board density.

**Synergy overrides (spells density + card flow + tempo interaction):**

* **Lands:** 35-36 can work when low curve and cantrip density are high.
* **Ramp:** Keep acceleration cheap to chain commander turns.
* **Interaction:** Izzet often skews toward stack interaction over permanent removal.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 36 | -1 vs midpoint | Low-curve shells can tolerate slight land trim |
| Mana ramp | 10 to 12 | 10 | -1 vs midpoint | Early ramp quality determines tempo |
| Card draw | ~10 | 13 | +3 | Draw quality is core to Izzet consistency |
| Interaction (removal + wipes + stack) | 9 to 14 | 18 | +7 vs midpoint | Healthy interaction count expected |
| Synergy / strategy | 25 to 30 | 21 | -6 vs midpoint | Focused plan density is appropriate |
| Utility | N/A | 1 | N/A | Support and role compression cards |

**Velocity note:** Prioritize turn-two setup into turn-three commander pressure or value line.

**Dependency score (1 to 10):** **7**. Deck likely functions as interactive spells shell even without commander, but ceiling improves significantly when commander sticks.

**Non-game check (lands):** About **52.7%** chance to see at least four lands in first ten cards (36 in 99).

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Convert cheap spells and interaction into incremental value, then snowball with commander synergy.
* **The spice:** Izzet sequencing opens flexible pivots between tempo and value depending on pod speed.
* **Tactical vulnerabilities:** Fast creature-wide boards if spot interaction density is too stack-leaning, and mana-stumble hands.

## Interaction & Protection Quality

* **Stack interaction density:** Typically high in Izzet and likely a strength here.
* **Board wipe asymmetry:** Needs careful timing since red wipes can be symmetric.
* **Engine protection:** Cheap interaction doubles as commander protection in key turns.

## Tutor targets by game stage

**Tutors in main + commander:** light or conditional.

**N/A (no dedicated broad tutors in main + commander).**

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** 2 (Mystical Tutor, Rhystic Study).
* **Other flags:** high velocity spell lines and interaction density.
* **Current vs target:** Upper bracket 3 appears accurate.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land plus one-mana setup/cantrip.
* **T2:** Cheap ramp or value setup permanent.
* **T3:** Commander or high-leverage engine deployment.
* **T4:** Start chaining interaction plus value spell.

### Hand B (Grinder)

* **T1-T2:** Land development with minor setup.
* **T3:** Hold interaction if table speed is high.
* **T4:** Establish commander and begin value loop.

### Hand C (Mulligan test)

* **Opening:** Two lands and expensive top-end with no cantrip support.
* **Line:** Usually mulligan for smoother velocity.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep hands with stable colors plus one setup spell and one interaction piece.
* **Deployment timing:** Deploy commander when you can protect or immediately extract value.
* **Closing the game:** Convert tempo and card quality into a protected finishing turn cycle.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Expressive Iteration](https://scryfall.com/search?q=%21%22Expressive%20Iteration%22) | weakest low-impact draw slot | Efficient card quality to smooth sequencing | Strong but fair high-3 card |
| [Arcane Bombardment](https://scryfall.com/search?q=%21%22Arcane%20Bombardment%22) | clunkiest non-synergy top-end | High-upside spells payoff in long games | Fun ceiling without compact combo |
| [Prismari Command](https://scryfall.com/search?q=%21%22Prismari%20Command%22) | narrow answer slot | Flexible interaction + filtering + treasure | Excellent role compression |
| [Storm-Kiln Artist](https://scryfall.com/search?q=%21%22Storm-Kiln%20Artist%22) | weakest ramp piece | Converts spell cadence into mana velocity | Strong Izzet engine support |
| [Dig Through Time](https://scryfall.com/search?q=%21%22Dig%20Through%20Time%22) | lowest-impact late draw spell | Deep selection for control finish turns | Efficient but still interactive |

## Bracket tuning plan

1. Keep bracket 3: maintain interaction but avoid compact deterministic combo packages.
2. Raise consistency: target 8-10 true draw engines and 8-10 cheap ramp/value accelerants.
3. Improve floor: trim dead top-end for cards that are live on turns 2-4.

## Organization audit

* Deck file uses EvalDragons section headers.
* Sideboard and maybeboard are separated and excluded from core ratios.

## Prioritized changes

1. Ensure enough cheap card selection for stable openers.
2. Keep interaction split between stack and permanent answers.
3. Add one resilient value engine if games in your pod run long.
