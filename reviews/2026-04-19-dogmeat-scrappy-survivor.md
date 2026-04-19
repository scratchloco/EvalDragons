# EDH Tactical Review: Dogmeat, Scrappy Survivor (precon)

**Review date:** 2026-04-19  
**Deck file:** [decks/dogmeat-scrappy-survivor.md](../decks/dogmeat-scrappy-survivor.md)  
**Data:** [decks/incoming/dogmeat-scrappy-survivor-archidekt.json](../decks/incoming/dogmeat-scrappy-survivor-archidekt.json) (Archidekt oracle fields). Re-check on [Scryfall](https://scryfall.com) before events.

## Source & Metadata

* **Source:** [https://archidekt.com/decks/16131196/dogmeat_scrappy_survivor_precon](https://archidekt.com/decks/16131196/dogmeat_scrappy_survivor_precon)
* **Commander:** **Dogmeat, Ever Loyal** (deck title on Archidekt: *Dogmeat, Scrappy Survivor (precon)*)
* **Bracket:** **Estimated current:** **4** (Powerful) with spikes toward **5** when **Hammer** lines and **Enlightened Tutor** resolve early. **Target (deck file):** 4.

## Legality & Local Bans

| Card | Status | Suggested replacement (synergy focus) |
|------|--------|----------------------------------------|
| Main + commander (export snapshot) | **Commander legal** | None required |
| **Mana Crypt**, **Jeweled Lotus**, **Dockside Extortionist** | **Absent** | N/A |

No `local_bans` in the deck file frontmatter.

## Core Ratios & Synergy Overrides

**Nonland AMV (main 99):** about **2.54** (Archidekt `cmc` on nonland main rows). **36** lands fits the **34 to 38** band with your low curve.

**Synergy overrides (equipment / aura Voltron):**

* **Interaction (9 to 14 target):** **Override:** you run **protection** and **fight-on-stack** tools (**Deflecting Swat**, **Flawless Maneuver**, **Teferi's Protection**, **Heroic Intervention**, **Sheltered by Ghosts**) that **do not** always show up as **destroy/exile** lines. Your **true** defense layer is **don't get blown out in combat** plus **free** or **cheap** protection.
* **Synergy bucket:** **High** counts are **expected** because most nonlands are **Auras**, **Equipment**, or **payoffs** that **stack** with **Dogmeat** and **Sram**-style engines.
* **Draw (~10 target):** **Sram**, **Puresteel**, **Top**, **Pip-Boy**, and **Sticky Fingers** are **real** engines; you are **not** as draw-thin as a pure **stompy** list, but you still **lean** on **resolving** engines.

| Bucket | Target (see `edh-core-ratios.mdc`) | Actual (99) | Delta | Rationale / override |
|--------|--------------------------------------|---------------|-------|----------------------|
| Lands | 36 to 38 | 36 | In band | AMV about **2.54**; strong **fetch** and **shock** density for **Naya** pips |
| Mana ramp | 10 to 12 | 7 | **−3 to −5** | **Sol Ring**, **Signet**, **Birds**, **Cultivate**, **Sword of the Animist**, **Kodama** land drops, **Sword of Feast and Famine** untaps. **Velocity** is **good** but **count** is **below** the default band |
| Card draw | ~10 | 5 dedicated | **−5** on paper | **Override:** **Equipment** density plus **commander** **mill** and **Junk** selection **adds** effective **card flow** when **online** |
| Interaction (removal + wipes + stack) | 9 to 14 | 12 | In band | **5** spot answers + **2** mass + **5** stack / team **protection** style pieces (see deck file split) |
| Synergy / strategy | 25 to 30 | 37 | **+7 to +12** | **Voltron** identity: **Hammer** package, **tutors**, **support** creatures |
| Utility | N/A | 7 | N/A | **Ghostly Prison**, **Sheltered by Ghosts**, **Inventory Management**, plus **free** **commander** protection instants |

**Velocity note:** Dogmeat costs **three** mana. **Sol Ring**, **Arcane Signet**, and **Birds of Paradise** (plus **cost reducers** like **Danitha Capashen, Paragon**) make a **turn-three** first cast common on keeps that curve.

**Dependency score (1 to 10):** **8**. Junk tokens and attack triggers want Dogmeat (or another suited-up creature) on board; you still cast equipment and auras without him, but most of your real card flow is commander-centric.

**Non-game check (lands):** Roughly **53%** chance to see at least **four** lands in your first **ten** cards (hypergeometric: **36** lands in **99**). Mulligan one-land hands that lack fast mana.

## The "Plan A" Audit (Strategic Summary)

* **The engine:** Dogmeat mills on ETB, returns an Aura or Equipment to hand, and turns modified attackers into Junk tokens that impulse from the top of your library. **Sram, Senior Edificer**, **Puresteel Paladin**, **Stoneforge Mystic**, **Enlightened Tutor**, and **Steelshaper's Gift** assemble Colossus Hammer lines and large swords quickly.
* **The spice:** **Cass, Hand of Vengeance** rebuilds auras and equipment after wraths; **Grim Reaper's Sprint** adds a splashy extra combat step that pairs with Junk velocity. **Codsworth, Handy Helper** gives commanders ward and moves equipment at sorcery speed.
* **Tactical vulnerabilities:** Edict effects if you only have one big body; exile-based removal on Dogmeat; **Stony Silence** / **Null Rod** style hate (you run **Vandalblast**, but timing matters); few hard counters compared to a control deck.

## Interaction & Protection Quality

* **Stack interaction density:** Medium on hard counters; high on protection (**Deflecting Swat**, **Flawless Maneuver**, **Teferi's Protection**, **Heroic Intervention**, **Sheltered by Ghosts**). You protect one threat rather than counter the whole table.
* **Board wipe asymmetry:** **Blasphemous Act** depends on creature count; **Single Combat** is a political mini-wipe that can hurt you if you go wide with tokens.
* **Engine protection:** **Lightning Greaves**, **Swiftfoot Boots**, **Champion's Helm**, **Robe of Stars**, **Sheltered by Ghosts**, plus free commander protection instants. Greaves and boots also pair with **Hammer of Nazahn** lines.

## Tutor targets by game stage

**Tutors in main + commander:** **Enlightened Tutor**, **Steelshaper's Gift**, **Fighter Class** (levels), **Stoneforge Mystic**.

| Stage | Efficient targets | Why |
|-------|-------------------|-----|
| Early (1 to 4) | **Sigarda's Aid**, **Colossus Hammer**, **Lightning Greaves**, **Swiftfoot Boots** | **Fast** **protection** or **combo** **setup** for **lethal** **math** |
| Mid | **Hammer of Nazahn**, **Sword of Feast and Famine**, **Sword of the Animist**, **Basilisk Collar** | **Power** **spikes**, **mana** **unlocks**, **lifelink** **stabilization** |
| Late / win | **Eldrazi Conscription**, **All That Glitters**, **Mantle of the Ancients**, **Open the Vaults** | **Close** **games** or **reload** after **mass** **enchantment** **hate** |

## WOTC bracket fit

* **Game changers (Archidekt oracle flags):** **Teferi's Protection**, **Enlightened Tutor** (confirm on Scryfall if your group uses printed lists).
* **Other flags:** **Colossus Hammer** **one-shot** **potential** with **Sigarda's Aid**; **Sword of Feast and Famine** **mana** **explosion**; **Sol Ring** **fast** **mana**. No **extra turns** flagged in the export.
* **Current vs target:** **Target 4** matches a **tutor** **forward** **equipment** list. **Drop** toward **3** only if you **cut** **Enlightened Tutor** and **some** **free** **protection**.

Official reference: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Turns 1 to 4 Goldfish Simulation

Assumptions: on the play, no opposing interaction.

### Hand A (The Ideal Start)

* **T1:** **Sol Ring** or **Birds of Paradise** plus a land.
* **T2:** **Arcane Signet** or set up **Sigarda's Aid**; hold **Swords to Plowshares** if you expect early creatures.
* **T3:** Cast **Dogmeat**; mill five, return a key Aura or Equipment, plan to attack next turn for Junk.
* **T4:** Equip **Colossus Hammer** or fire a **Stoneforge Mystic** line; **Sword of Feast and Famine** snowballs mana if it connects.

### Hand B (The Grinder)

* **T1 to T2:** Lands plus **Cultivate** fixing.
* **T3:** Dogmeat on curve with protection mana available soon.
* **T4:** **Sram** or **Puresteel** online; you chain equipment casts for cards.

### Hand C (The Mulligan Test)

* **Opening:** Two lands, no rocks, no one-mana ramp. Ship unless the top of the library fixes mana or you have a tutor plus interaction.

## Recommended Play Lines & Piloting

* **Opening hands:** Keep two-plus lands with early action (rocks, Birds, or a clear two-mana plan). Toss fragile keeps in removal-heavy pods if you cannot protect Dogmeat.
* **Deployment timing:** Cast Dogmeat when your yard or hand makes the ETB worthwhile, or when you need the commander online for Junk. Sandbag free protection for the turn that actually wins or saves the game.
* **Closing the game:** **Colossus Hammer** plus **Sigarda's Aid**, double strike from **Fireshrieker**, or **Eldrazi Conscription** after you clear blockers. **Kediss, Emberclaw Familiar** spreads damage in multiplayer.

## Outside-List Upgrades (The Spice Rack)

Focus on **equipment** **synergy** and **protection** before **generic** **value**.

| Add | Cut | Why it elevates the specific strategy | Bracket note |
|-----|-----|----------------------------------------|--------------|
| [Shadowspear](https://scryfall.com/search?q=%21%22Shadowspear%22) | **Fireshrieker** (overlap in **double** **strike** **plan**) | **Trample**, **lifelink**, **maindeck** **grave** **hate** **toggle** | **Mid** **4** |
| [Esper Sentinel](https://scryfall.com/search?q=%21%22Esper%20Sentinel%22) | **Strong Back** or another **marginal** **aura** | **Cards** on **opponent** **development** | **Fine** at **3** to **4** |
| [Blacksmith's Skill](https://scryfall.com/search?q=%21%22Blacksmith%27s%20Skill%22) | **Valorous Stance** (overlap in **save** **creature**) | **Hexproof** **pump** for **one** **mana** **protects** **Dogmeat** **turns** | **Low** **bracket** **impact** |

**Maybeboard (64 on Archidekt):** **Skim** for **strict** **upgrades** before you **import** **random** **staples**; many **slots** may **duplicate** **main** **goals**.

## Bracket tuning plan

1. **Soften** toward **3:** **Trim** **Enlightened Tutor** and **one** **free** **protection** **spell**; **swap** **Eldrazi Conscription** for a **smaller** **finisher** if **tables** **hate** **one-shots**.
2. **Stay** at **4:** **Keep** **tutor** **suite** but **predeclare** **Hammer** **lines** **clearly**.
3. **Avoid** **silent** **Bracket** **5** **without** **table** **buy-in:** **Jeweled Lotus** and **Mana Crypt** are **not** **here**; **do** **not** **add** them **unless** **everyone** **agrees**.

## Organization audit

* Sections follow [`deck-organization.md`](../deck-organization.md).
* **Sheltered by Ghosts** is **filed** under **Utility** as **protection**; **Inventory Management** is **combat** **reconfiguration**.

## Prioritized changes

1. **Add** **2** to **3** **additional** **ramp** pieces if you **want** the **default** **10** to **12** **band** without **changing** **strategy** (**two** **drop** **rocks** or **extra** **land** **tutors** on **curve**).
2. **Track** **artifact** **hate** in your **meta**; **Vandalblast** is **strong** but **not** **always** **enough** **at** **instant** **speed** **everywhere**.
3. **Practice** **Hammer** **math** with **Aid** and **Puresteel** so **turns** **end** **cleanly** **without** **rules** **misses**.
4. **Cull** **maybeboard** **down** to **8** to **12** **real** **swaps** so **testing** **stays** **honest**.
