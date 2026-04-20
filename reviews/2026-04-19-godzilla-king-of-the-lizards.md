# EDH Tactical Review: Godzilla, King of the Lizards

**Review date:** 2026-04-19  
**Deck file:** [decks/godzilla-king-of-the-lizards.md](../decks/godzilla-king-of-the-lizards.md)  
**Data:** [decks/incoming/godzilla-king-of-the-lizards-archidekt.json](../decks/incoming/godzilla-king-of-the-lizards-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/16143775/godzilla_king_of_the_lizards](https://archidekt.com/decks/16143775/godzilla_king_of_the_lizards)
* **Commander:** **Zilortha, Strength Incarnate**
* **Bracket:** **Estimated current:** upper **3** into **4** depending on how often extra-combat and one-shot lines connect. **Target (deck file):** 4.

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|-------|
| Main + commander | 100 | 99 + commander |
| Sideboard | 0 | Empty on Archidekt |
| Maybeboard | 42 | Reference only |

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Absent** | N/A |

No `local_bans` in deck frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **3.94**. This is a genuinely top-heavy Gruul monster shell, so **37** lands is appropriate.

**Synergy overrides (Zilortha beatdown):**

* **Ramp target pressure:** At this AMV and curve profile, being at the **high end** of ramp is not optional. You need repeated acceleration to avoid clunky hands.
* **Removal profile:** Some of your interaction is creature-based or damage-based (**Kogla** package, **Sarkhan's Unsealing**, **Chandra's Ignition**) rather than stack control. That is fine for this archetype, but it is board-state dependent.
* **Draw density:** The draw suite is lean, but your best draw pieces scale with high power creatures and are thematically aligned.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|-------------|-------|----------------------|
| Lands | 36 to 38 | 37 | In band | AMV near 4 and big-spell density justify 37 |
| Mana ramp | 10 to 12 | 14 | +2 to +4 | Correct for your top-end; improves turn-4/5 commander and threat sequencing |
| Card draw | ~10 | 5 | -5 | Under target, but quality is high (**Guardian Project**, **Beast Whisperer**, **Elemental Bond**, **Return of the Wildspeaker**, **Garruk's Uprising**) |
| Interaction (removal + wipes + stack) | 9 to 14 | 11 | In band | Good permanent removal spread and two sweeper effects |
| Synergy / strategy | 25 to 30 | 27 | In band | Extra combats, trample/evasion, giant body payoffs |
| Utility | N/A | 5 | N/A | Boots + instant team/board protection package |

**Velocity note:** Zilortha costs five mana. With 14 ramp pieces, turn-four commander is realistic on strong draws; turn-five is consistent.

**Dependency score (1 to 10):** **6**. Commander is strong but not required; your deck can still win through Xenagos/Stampede/Ibex lines.

**Non-game check (lands):** About **55.5%** chance to see at least four lands in first ten cards (hypergeometric: 37 in 99). Ramp density is what prevents non-games.

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Curve dork/rock/ramp into oversized bodies, then convert power into lethal pressure through trample, forced blocks, and burst combat turns.
* **The spice:** **Zilortha** flipping damage rules around toughness makes your high-power creatures unusually resilient in combat math. **Anzrag, the Quake-Mole** and **Combat Celebrant** add explosive close-outs.
* **Tactical vulnerabilities:** Mass exile, repeated bounce, and early hand stumbles with too many 5+ MV spells and no draw/ramp opener.

## Interaction & Protection Quality

* **Stack interaction density:** Low by design (typical Gruul). You fight on board, not on stack.
* **Board wipe asymmetry:** **Blasphemous Act** and **Chandra's Ignition** can swing heavily in your favor with one big creature in play.
* **Engine protection:** **Heroic Intervention**, **Wrap in Vigor**, **Rhythm of the Wild**, **Lightning Greaves**, **Swiftfoot Boots** provide a solid anti-wrath/anti-target package.

## Tutor targets by game stage

**Tutors in main + commander:** **Worldly Tutor**, **Green Sun's Zenith**.

| Stage | Efficient targets | Why |
|-------|-------------------|-----|
| Early (1 to 4) | **Birds of Paradise**, **Elvish Mystic**, **Goreclaw, Terror of Qal Sisma**, **Oracle of Mul Daya** | Smooth mana and jump curve |
| Mid | **Xenagos, God of Revels**, **Pathbreaker Ibex**, **Kogla, the Titan Ape**, **Beast Whisperer** | Turn pressure into damage while staying fueled |
| Late / win | **Ghalta, Stampede Tyrant**, **Apex Devastator**, **Anzrag, the Quake-Mole**, **Malignus** | End games quickly with damage spikes and cascade density |

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** **Worldly Tutor**.
* **Other flags:** Fast mana package, high-impact top end, extra combat lines.
* **Current vs target:** Your `target_bracket: 4` is reasonable if the pod expects swingy combat kills and tutors. For lower-power pods, trim tutor/extra-combat density.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (Ideal)

* **T1:** Land + dork (**Birds** or **Elvish Mystic**).
* **T2:** Land + 2 MV ramp (or **Arcane Signet/Talisman**), keep curve live.
* **T3:** 4-5 mana available, deploy mid threat (**Goreclaw** / **Beast Whisperer**).
* **T4:** Zilortha or another heavy attacker with protection up.

### Hand B (Grinder)

* **T1-T2:** Tapland/fixing into **Cultivate/Farseek/Nature's Lore**.
* **T3:** Setup permanent draw engine.
* **T4:** First large creature + pressure line, hold board-centric removal.

### Hand C (Mulligan test)

* **Opening:** Three lands, no ramp, all 5+ MV spells.
* **Line:** Usually ship. This deck's floor is poor without acceleration or one early draw engine.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep only if you can cast 2-3 spells by turn three (ramp counts as spells here).
* **Deployment timing:** Prioritize mana and draw before dumping top-end. One protected threat is better than two exposed ones.
* **Closing the game:** Sequence haste/protection, then force trample/lethal swings with **Xenagos**, **Pathbreaker Ibex**, **Overwhelming Stampede**, or extra-combat threats.

## Outside-List Upgrades (The Spice Rack)

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Greater Good](https://scryfall.com/search?q=%21%22Greater%20Good%22) | **Archetype of Aggression** | Turns oversized bodies into real card velocity | Mostly neutral |
| [Selvala, Heart of the Wilds](https://scryfall.com/search?q=%21%22Selvala%2C%20Heart%20of%20the%20Wilds%22) | **Goblin Anarchomancer** | Ramp plus draw in one slot for creature-heavy plan | Slight power increase |
| [Return of the Wildspeaker](https://scryfall.com/search?q=%21%22Return%20of%20the%20Wildspeaker%22) | *(already present)* | Already doing exactly what this shell needs | Already included |
| [Kessig Wolf Run](https://scryfall.com/search?q=%21%22Kessig%20Wolf%20Run%22) | One basic land | Mana sink that closes stalled boards | Slight upshift |
| [Deflecting Swat](https://scryfall.com/search?q=%21%22Deflecting%20Swat%22) | **Wrap in Vigor** | Better stack interaction while preserving proactive plan | Bracket 4 texture |

## Bracket tuning plan

1. Stay at 4: keep tutor + extra-combat package and maintain high ramp density.
2. Move toward 3: cut **Worldly Tutor** and one explosive finisher, add one fair draw engine.
3. Improve consistency: add 1-2 card-flow effects even if a top-end threat has to leave.

## Organization audit

* Deck file sections follow EvalDragons format and keep maybeboard excluded from core counts.
* Card categorization is coherent for a Gruul big-power strategy.

## Prioritized changes

1. Add 2-3 more reliable card-flow effects to reduce post-wrath stalls.
2. Keep ramp at 13-14; this is the backbone of your curve.
3. Decide whether you want bracket 3 or 4 table texture, then tune tutor and extra-combat package accordingly.
4. Goldfish mulligans aggressively: no-ramp seven-card hands are usually traps in this shell.
