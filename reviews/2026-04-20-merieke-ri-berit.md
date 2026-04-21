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
| Maybeboard | 20 | Reference options present |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Check present cards manually** | Replace if present and outside pod agreement |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **2.57**. This Esper theft-control shell remains interactive, but your latest edits reduced combo compression.

**Synergy overrides (steal-and-control + blink value + untap timing):**

* **Lands:** 36-38 still ideal for color-intensive interaction.
* **Ramp:** Slightly low ramp is acceptable if curve stays low and land count is stable.
* **Interaction:** This shell naturally runs above baseline interaction by design.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 36 | -1 vs midpoint | On target for Esper control mana |
| Mana ramp | 10 to 12 | 4 | -7 vs midpoint | Lower than baseline; compensate with land drops |
| Card draw | ~10 | 7 | -3 | Still a little below ideal for grind mirrors |
| Interaction (removal + wipes + stack) | 9 to 14 | 24 | +13 vs midpoint | High interaction aligns with Merieke game plan |
| Synergy / strategy | 25 to 30 | 25 | -2 vs midpoint | Healthy theft/blink/untap density |
| Utility | N/A | 3 | N/A | Protection and support slots |

**Velocity note:** Turn-three Merieke remains realistic, but low ramp count makes opening-land quality more important.

**Dependency score (1 to 10):** **7**. Deck can play control without commander, but Merieke still provides the sharpest swing turns.

**Non-game check (lands):** About **52.7%** chance to see at least four lands in first ten cards (36 in 99).

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Control early board texture, deploy Merieke with protection, and leverage untap/blink windows for sustained advantage.
* **The spice:** Theft plus flicker timing creates pseudo-removal and card advantage in one line.
* **Tactical vulnerabilities:** Fast combo pods and draws with no early mana acceleration.

## Interaction & Protection Quality

* **Stack interaction density:** Strong and still above average for bracket-3 tables.
* **Board wipe asymmetry:** Good when you sequence around stolen creatures and phase protection.
* **Engine protection:** `Teferi's Protection` plus boots effects remain high-impact safeguards.

## Tutor targets by game stage

**Tutors in main + commander:** light to moderate.

| Stage | Targets | Why |
|------|---------|-----|
| Early (T1-T4) | cheap rock, protective equipment, low-cost interaction | Enables safe commander deployment |
| Mid | theft enabler, blink piece, flexible answer | Converts tempo into persistent board control |
| Late | value finisher or hard reset | Closes once opponents are resource constrained |

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** 1 (Teferi's Protection).
* **Other flags:** high interaction density, but reduced deterministic combo pressure.
* **Current vs target:** Current configuration looks like a strong **high 3**.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land plus one-mana cantrip or setup.
* **T2:** Two-mana rock.
* **T3:** Merieke with protection or interaction up.
* **T4:** First theft activation and board stabilization.

### Hand B (Grinder)

* **T1-T2:** Tapped land sequencing and setup spell.
* **T3:** Hold interaction, delay commander if table is explosive.
* **T4:** Commander plus one supporting piece.

### Hand C (Mulligan test)

* **Opening:** Three lands, no ramp, expensive reactive spells.
* **Line:** Keepable in slower pods; mulligan in faster pods.

## Recommended Play Lines & Piloting

* **Opening hands:** Prioritize 3-land hands with at least one low-cost interaction or setup piece.
* **Deployment timing:** Do not jam Merieke into obvious instant-speed removal unless value is immediate.
* **Closing the game:** Convert creature control into attrition lock, then finish with sustained board leverage.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Commander's Sphere](https://scryfall.com/search?q=%21%22Commander%27s%20Sphere%22) | lowest-impact flex slot | Fair ramp that also cycles to a card | Keeps power in high 3 |
| [Fact or Fiction](https://scryfall.com/search?q=%21%22Fact%20or%20Fiction%22) | weakest cantrip slot | Midgame refill aligned with control pacing | Strong but fair |
| [Mulldrifter](https://scryfall.com/search?q=%21%22Mulldrifter%22) | clunky top-end filler | Blink-compatible value body | Synergy upgrade without compression |
| [Didn't Say Please](https://scryfall.com/search?q=%21%22Didn%27t%20Say%20Please%22) | most efficient hard counter | Slightly softer counter for bracket-3 pods | Lowers efficiency spike |
| [High Market](https://scryfall.com/search?q=%21%22High%20Market%22) | weakest utility land | Clean sac outlet for stolen creatures | Thematic control utility |

## Bracket tuning plan

1. Stay high 3: keep current cuts to tutor/untap compression and maintain fair interaction.
2. If still too strong: trim one additional premium counter for a slower draw engine.
3. If too weak: add one ramp slot back before adding more hard counters.

## Organization audit

* Deck file remains in EvalDragons section order.
* Sideboard and maybeboard are separated and excluded from core math.

## Prioritized changes

1. Add 1-2 fair ramp slots to smooth early sequencing.
2. Raise sustained draw count toward 8-10 for longer games.
3. Keep interaction density, but bias toward fair-rate answers over free/ultra-efficient effects.
