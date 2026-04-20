# EDH Tactical Review: Atogatog, The Recursion Goat

**Review date:** 2026-04-19  
**Deck file:** [decks/atogatog-the-recursion-goat.md](../decks/atogatog-the-recursion-goat.md)  
**Data:** [decks/incoming/atogatog-the-recursion-goat-archidekt.json](../decks/incoming/atogatog-the-recursion-goat-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/19516885/atogatog_the_recursion_goat](https://archidekt.com/decks/19516885/atogatog_the_recursion_goat)
* **Commander:** **Atogatog**
* **Bracket:** **Estimated current:** high **4**. **Target (deck file):** 4.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 + commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 10 | Reference only |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Absent** | N/A |

No `local_bans` in the deck file frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **3.06** with histogram `{1:10, 2:14, 3:20, 4:5, 5:7, 6:5, 7:1}`. With that AMV and five colors, **37** lands is on target.

**Synergy overrides (Atogatog recursion shell):**

* **Board wipes:** The list intentionally leans on **mass recursion** (**Living Death**, **Twilight's Call**) and protection tricks, so classic wipe density can be a little lower than generic guidance.
* **Synergy density:** This build should run high synergy by design: Atogs, Changelings, sacrifice outlets, death triggers, and graveyard recursion loops.
* **Draw count:** Dedicated draw appears low, but **Greater Good**, **Moldervine Reclamation**, **Grim Haruspex**, and recursion lines produce substantial card churn once online.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 37 | In band | AMV about **3.06** and five-color requirements support the higher end |
| Mana ramp | 10 to 12 | 11 | In band | Good spread of rocks, dorks, and 2-3 MV land ramp |
| Card draw | ~10 | 5 | -5 on paper | **Override:** death-recursion engines create ongoing flow after setup |
| Interaction (removal + wipes + stack) | 9 to 14 | 8 | Slightly low | You rely more on board state recursion than reactive stack play |
| Synergy / strategy | 25 to 30 | 37 | +7 to +12 | Expected for a dedicated Atog recursion-combo shell |
| Utility | N/A | 2 | N/A | **Heroic Intervention**, **Teferi's Protection** |

**Velocity note:** Atogatog costs five mana. Ramp package supports a realistic turn-four cast in strong hands.

**Dependency score (1 to 10):** **7**. The deck has independent recursion engines, but Atogatog and Atog-type density are needed to convert value into kills.

**Non-game check (lands):** Roughly **55.5%** chance to see at least four lands in first ten cards (hypergeometric: 37 lands in 99). Functional with your ramp package.

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Build board with Atogs, changeling support, and recursion permanents. Sacrifice boards for value, then rebuild with **Living Death**, **Patriarch's Bidding**, **Thrilling Encore**, **Lifeline**, or one-shot protection recursion like **Second Sunrise** and **Faith's Reward**.
* **The spice:** **Maskwood Nexus** makes your creature base share types for tribal recursion lines. **Marchesa, the Black Rose** and **Mazirek, Kraul Death Priest** turn sacrifice loops into persistent pressure.
* **Tactical vulnerabilities:** Graveyard hate, instant-speed exile on key engine creatures, and hands that draw recursion without setup bodies.

## Interaction & Protection Quality

* **Stack interaction density:** Low to medium. You are mostly proactive and resilient, not reactive.
* **Board wipe asymmetry:** **Living Death** and **Twilight's Call** are often one-sided if you sequence sacrifice outlets first.
* **Engine protection:** Good coverage from undying tricks, **Heroic Intervention**, and **Teferi's Protection**. This keeps loops alive through removal turns.

## Tutor targets by game stage

**Tutors in main + commander:** **Vampiric Tutor**, **Buried Alive**, plus death chain potential from **Protean Hulk**.

| Stage | Efficient targets | Why |
|-------|-------------------|-----|
| Early (1 to 4) | **Bloom Tender**, **Birds of Paradise**, **Farseek**, **Nature's Lore** | Fix colors and accelerate to engine turns |
| Mid | **Maskwood Nexus**, **Marchesa, the Black Rose**, **Mazirek, Kraul Death Priest**, **Greater Good** | Turn board presence into recursive value and counters |
| Late / win | **Living Death**, **Patriarch's Bidding**, **Rite of Consumption**, **Protean Hulk** lines | Rebuild massively or convert one giant body into lethal damage |

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** **Vampiric Tutor**, **Teferi's Protection**.
* **Other flags:** Recursion mass-reset lines, sacrifice combo texture, strong tutoring into engine pieces.
* **Current vs target:** **Bracket 4** is a good fit. If you want to drift toward 3, reduce tutor density and lower instant-speed protection.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land, **Birds of Paradise**.
* **T2:** Land, **Arcane Signet**.
* **T3:** Land, **Buried Alive** to set graveyard package.
* **T4:** Atogatog or value engine piece with protection available soon.

### Hand B (Grinder)

* **T1-T2:** Land, tapped fixing land, **Farseek**.
* **T3:** Additional ramp and first sac outlet creature.
* **T4:** **Marchesa** or **Greater Good**, then set up recursion turn.

### Hand C (Mulligan test)

* **Opening:** Three lands but no ramp and only top-end recursion spells.
* **Line:** Keep only if colors are perfect and you have one cheap setup piece; otherwise ship for faster engine access.

## Recommended Play Lines & Piloting

* **Opening hands:** Prefer two to three lands with at least one ramp card and one setup piece (Atog/changeling/draw engine/tutor).
* **Deployment timing:** Do not fire mass recursion into open graveyard hate. Force interaction first, then commit **Living Death** or **Patriarch's Bidding**.
* **Closing the game:** Build one oversized Atogatog or Mazirek board, then finish with **Rite of Consumption** or combat backed by protection.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Ashnod's Altar](https://scryfall.com/search?q=%21%22Ashnod%27s%20Altar%22) | **Soul's Fire** | Cleaner sac-loop mana and recursion burst turns | Pushes toward high 4 |
| [Victimize](https://scryfall.com/search?q=%21%22Victimize%22) | *(already in list)* | Already present and correctly supports plan | Already accounted |
| [Zulaport Cutthroat](https://scryfall.com/search?q=%21%22Zulaport%20Cutthroat%22) | **Taurean Mauler** | Adds deterministic drain finish to sacrifice loops | Neutral to slight upshift |
| [Rhystic Study](https://scryfall.com/search?q=%21%22Rhystic%20Study%22) | **Garruk's Uprising** | Stronger steady draw in five-color shell | Table tolerance dependent |
| [Chromatic Lantern](https://scryfall.com/search?q=%21%22Chromatic%20Lantern%22) | **Prismatic Omen** | Improves fixing while still tapping for mana | Mostly neutral |

## Bracket tuning plan

1. Stay at 4: keep tutors and protection, but telegraph recursion turns for cleaner games.
2. Tune down to 3: cut **Vampiric Tutor**, swap one mass recursion spell for fair midrange value, and trim one protection trick.
3. Tune up within 4: add one deterministic aristocrats finisher from maybeboard package.

## Organization audit

* Deck file uses expected sections and keeps maybeboard separate from core 99.
* Card roles are coherent for this archetype, with recursion concentrated in synergy bucket.

## Prioritized changes

1. Add one more flexible interaction piece if your meta has frequent graveyard hate.
2. Promote **Zulaport Cutthroat** from maybeboard for cleaner endgames.
3. Consider **Chromatic Lantern** if five-color color pips feel strained in testing.
4. Goldfish for sequencing windows around **Living Death** and instant-speed protection.
