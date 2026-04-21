# EDH Tactical Review: Merieke Ri Berit

**Review date:** 2026-04-20  
**Deck file:** [decks/merieke-ri-berit.md](../decks/merieke-ri-berit.md)  
**Data:** [decks/incoming/merieke-ri-berit-archidekt.json](../decks/incoming/merieke-ri-berit-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/21722664/merieke_ri_berit](https://archidekt.com/decks/21722664/merieke_ri_berit)
* **Commander:** **Merieke Ri Berit**
* **Bracket:** **Estimated current:** high **3**. **Target (deck file):** 3.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 main + 1 commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 21 | Reference options present |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Check present cards manually** | Replace if present and outside pod agreement |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **2.52**. You have reduced untap-combo compression and shifted into a more stable control-value profile.

**Synergy overrides (steal-control + blink value + fair attrition close):**

* **Lands:** 36 to 38 still ideal for Esper control sequencing.
* **Ramp:** 6-8 is acceptable in low-curve control, but 8-10 improves floor.
* **Draw:** Scalable draw like Blue Sun's Zenith helps late-game conversion.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 36 | -1 vs midpoint | On-plan for color stability |
| Mana ramp | 10 to 12 | 5 | -6 vs midpoint | Lower than baseline, but mitigated by low AMV |
| Card draw | ~10 | 7 | -3 | Improved with Zenith; still could use one more steady source |
| Interaction (removal + wipes + stack) | 9 to 14 | 24 | +13 vs midpoint | High interaction remains your identity |
| Synergy / strategy | 25 to 30 | 24 | -3 vs midpoint | Balanced after combo-piece trims |
| Utility | N/A | 3 | N/A | Protection and support slots |

**Velocity note:** Turn-three Merieke is still common, but openers with one two-mana rock are much stronger than pure land-go keeps.

**Dependency score (1 to 10):** **7**. Core control shell functions independently, with Merieke as a high-leverage engine rather than a sole win route.

**Non-game check (lands):** About **52.7%** chance to see at least four lands in first ten cards (36 in 99).

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Protect Merieke, steal key creatures, and convert tempo into long-game card advantage.
* **The spice:** Blink and copy support still create high-value turns without leaning on compact untap loops.
* **Tactical vulnerabilities:** Fast combo tables and hands with no early ramp plus no cantrip smoothing.

## Interaction & Protection Quality

* **Stack interaction density:** Strong for bracket-3 pods.
* **Board wipe asymmetry:** Good with phased protection and theft timing.
* **Engine protection:** `Teferi's Protection`, boots, and spot interaction keep commander online.

## Tutor targets by game stage

**Tutors in main + commander:** light.

| Stage | Targets | Why |
|------|---------|-----|
| Early (T1-T4) | two-mana rock, protection piece, cheap interaction | Enables safe commander timing |
| Mid | blink/copy support, flexible answer, value draw | Converts control to board leverage |
| Late | scalable draw (`Blue Sun's Zenith`) or mass recursion line | Closes with card advantage and inevitability |

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** 1 (Teferi's Protection).
* **Other flags:** heavy interaction, but reduced compact combo patterns.
* **Current vs target:** This update reads as a healthy **high 3**.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land plus setup spell.
* **T2:** Two-mana ramp.
* **T3:** Merieke with one mana up if possible.
* **T4:** First theft/control pivot while keeping interaction online.

### Hand B (Grinder)

* **T1-T2:** Land sequencing and cantrip/value setup.
* **T3:** Hold up interaction over commander if table is explosive.
* **T4:** Commander plus protective posture.

### Hand C (Mulligan test)

* **Opening:** Three lands, no ramp, reactive-heavy hand.
* **Line:** Keep in slower pods; mulligan in fast pods for acceleration.

## Recommended Play Lines & Piloting

* **Opening hands:** Prefer 3 lands plus either a two-mana rock or cheap card-selection spell.
* **Deployment timing:** Cast Merieke when you can protect or extract immediate value.
* **Closing the game:** Win by repeated resource denial and value conversion, not by racing combo.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Talisman of Dominance](https://scryfall.com/search?q=%21%22Talisman%20of%20Dominance%22) | weakest high-CMC flex slot | Improves turn-two ramp consistency | Strong but fair for high 3 |
| [Talisman of Progress](https://scryfall.com/search?q=%21%22Talisman%20of%20Progress%22) | lowest-impact utility slot | Better early color fixing for Merieke curve | Keeps deck smooth, not spiky |
| [Night's Whisper](https://scryfall.com/search?q=%21%22Night%27s%20Whisper%22) | weakest one-shot cantrip | Efficient draw to maintain interaction density | Fair card velocity |
| [Commander's Sphere](https://scryfall.com/search?q=%21%22Commander%27s%20Sphere%22) | clunky non-engine slot | Ramp plus late draw in one card | Good high-3 glue card |
| [Fact or Fiction](https://scryfall.com/search?q=%21%22Fact%20or%20Fiction%22) | weakest low-impact draw piece | Better refill in control mirrors | Value, not combo pressure |

## Bracket tuning plan

1. Keep high 3: preserve current anti-combo trims and avoid re-adding untap aura loops.
2. Improve floor: add 1-2 fair ramp pieces to raise keepable opener rate.
3. Maintain identity: keep interaction dense, but prioritize fair-rate spells over free tempo spikes.

## Organization audit

* Deck file remains aligned to EvalDragons section structure.
* Sideboard and maybeboard are properly excluded from core-ratio math.

## Prioritized changes

1. Add two fair ramp slots to hit commander timing more reliably.
2. Add one additional steady draw source for long pods.
3. Keep combo-compression pieces in maybeboard for bracket-3 consistency.
