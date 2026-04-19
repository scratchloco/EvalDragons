# EDH review: Rocco's Blink & Burn Toolbox

**Review date:** 2026-04-19  
**Deck file:** [decks/roccos-blink-burn-toolbox.md](../decks/roccos-blink-burn-toolbox.md)  
**Data:** Archidekt API export in [decks/incoming/roccos-blink-burn-toolbox-archidekt.json](../decks/incoming/roccos-blink-burn-toolbox-archidekt.json) (embedded oracle legality). Re-verify with Scryfall before sanctioned play if your environment requires it.

## Deck source

- **URL:** [https://archidekt.com/decks/17678719/roccos_blink_burn_toolbox](https://archidekt.com/decks/17678719/roccos_blink_burn_toolbox)
- **Commander:** **Rocco, Cabaretti Caterer**
- **Core list scope:** main + commander only (sideboard / maybeboard excluded from counts and core analysis; see optional SB notes below).

## Deck zones (from URL)

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|--------|
| Main + commander | 100 | 99 + commander |
| Sideboard | 10 | Archidekt `Sideboard` tag on each row |
| Maybeboard | 0 | — |

Archidekt zone logic uses each `cards[]` row’s `categories` (see project skill §1). Sideboard is a **hidden-commander / variant** pile (e.g. Frodo, Tomb of Annihilation) and does not affect the main 99 math.

## Target Commander Bracket

- **Goal (deck file frontmatter):** 4 (Powerful)
- **Stated intent:** Blink + burn + toolbox (Archidekt tags: Burn, Pingers, Blink, Toolbox, Hidden Commander).

## Legality table

| Card | Commander legal (Archidekt oracle) | Notes |
|------|-------------------------------------|--------|
| Main + commander (100 rows) | **Legal** | No `commander: banned` / `not_legal` flags in export at review time |
| Sideboard | **Not evaluated for Commander 99** | Optional casual modules only |

## Cleaned list delta

- **None** for analysis — no identity or ban issues detected in the export.

## Core ratio table

Counts use **main 99** with one primary bucket per card; **commander** excluded from 99 totals. Utility is tracked separately so synergy density stays readable.

| Bucket | Target | Actual (99) | Delta | Notes |
|--------|--------|---------------|-------|--------|
| Lands | 36–38 | 36 | 0 to −2 | Nonland AMV ≈ **2.81** on the 63 spells/creatures/artifacts — supports **34–38** land band; 36 is reasonable |
| Ramp | 10–12 | 7 | **−3 to −5** | Strong fast mana (Sol Ring, Signet) and dorks, but **few sorcery land-ramp** pieces beyond **Three Visits** / **Nature's Lore** |
| Card draw | ~10 | 6 | **−4** | Good engines (**Guardian Project**, **Welcoming Vampire**, **Tocasia's Welcome**, **Rumor Gatherer**, **Enduring Innocence**); **Reprieve** is mostly tempo with a cantrip |
| Targeted removal | 7–10 | 8 | ~0 | Solid spread: **Swords**, **Path**, **Chaos Warp**, **Generous Gift**, **Stroke**, **Aura Mutation**, **Reclamation Sage**, **Aura Shards** (repeatable) |
| Board wipes | 2–4 | 2 | 0 (low band) | **Blasphemous Act** + **Austere Command** — flexible, but you lean on single sweeper types |
| Synergy / strategy | 25–30 | 37 | **+7 to +12** | Very dense ETB / token / damage package (**Panharmonicon**, **Preston**, **Purphoros**, **Impact Tremors**, **Molten Echoes**, **Norin**, etc.) |
| Utility / MDFC | — | 3 | — | **Deflecting Swat**, **Teferi's Protection**, **Ojer Axonil // Temple of Power** |

## Mana and curve

- **Nonland AMV (main 99):** ≈ **2.81** (Archidekt `cmc` on nonland main rows).
- **CMC shape:** heavy **2–3** (low curve) with a few anchors (**Blasphemous Act**, **Austere Command**, **City on Fire**, planeswalker). The list wants to **sequence ETBs early** and snowball.

## Role density

You are built as a **linear synergy deck** with a **medium interaction** outer shell. **Aura Shards** and **Aura Mutation** give game against artifacts/enchantments; **Boseiju** on the manabase adds noncreature answer density without spending a spell slot.

## Commander axes

1. **Creature toolbox:** Rocco’s cast trigger tutors a creature with mana value ≤ X onto the battlefield — rewards **curve discipline** and **high-impact ETBs**.
2. **ETB / blink loops:** **Cloudstone Curio**, **Wirewood Symbiote**, **Eerie Interlude**, **Lae'zel's Acrobatics**, **Norin the Wary**-style chaos, **Panharmonicon** / **Preston, the Vanisher**.
3. **Damage payoffs:** **Purphoros**, **Impact Tremors**, **Warleader's Call**, **Mechanized Warfare** / **City on Fire**, **Solphim**, **Witty Roastmaster**, etc.
4. **Combo overlay:** **Food Chain** + **Squee, the Immortal** is a classic **infinite colored mana** engine that converts cleanly with Rocco / other outlets — this raises **ceiling** and **table expectations** independent of “fair” ETB plans.

## Synergy and alignment audit

- **Matrix summary:** Most nonlands **High** on commander synergy (cheap creatures, ETB bodies, burn payoffs). Interaction pieces (**Swords**, **Path**, **Chaos Warp**) are **Med** synergy but **High** role fit.
- **Misaligned / tension:** **Grand Abolisher** helps combo turns but can read “unfun” at casual tables; **Genesis Chamber** speeds **everyone** and can backfire vs go-wide. Not wrong, just **political** knobs.
- **Cluster gaps:** **Ramp** and **steady draw** are the main structural gaps versus EvalDragons defaults; the deck compensates with **treasure** (e.g. **Prosperous Innkeeper**, **Gala Greeters**, **Rose Room Treasurer**) and **fast mana**, which is powerful but **burstier** than land ramp.

## Build value — general sentiment

The list is **coherent and high-ceiling**: it reads like a **Bracket 4** Naya ETB shell with **explicit combo** (Food Chain) and **multiple game-changer-class cards**. Card quality is **strong** for speed and redundancy; the main question is whether the **social contract** at your table matches that ceiling.

## Strategic summary

You pressure life totals with **incremental damage** while **snowballing board presence** through ETBs and copy effects. Rocco gives you a **scalable tutor** that rewards sequencing: early **value bears**, midgame **Panharmonicon** / **Preston**, late **finishers** or **combo assembly**. The deck’s main risks are **sweepers** that strand your commitment, **rule-of-law** effects that turn off triggers, and **running out of cards** if engines are answered — your draw suite is **good but not deep** relative to the synergy load.

## Recommended play lines

1. **Early:** Prioritize **mana** (Sol Ring, dorks, cheap lands) then a **draw engine** or **damage multiplier** only when you can protect a turn or have redundancy.
2. **Rocco timing:** Cast Rocco when **X** lines up with a **tutor target that changes the math** (Panharmonicon, Preston, **Reclamation Sage** blowout, **Grand Abolisher** before a combo turn). Avoid telegraphing **Food Chain** without backup interaction or protection.
3. **Mid:** Use **Eerie Interlude** / **Lae'zel's Acrobatics** to **dodge wraths** or **double ETBs**; hold **Deflecting Swat** for the **stack fight** that actually loses you the game.
4. **Late / win-ready:** Convert **Food Chain** mana into **Rocco loops** or close with **Purphoros** / **City on Fire** style damage after a wide board. **Teferi's Protection** is for the **turn you go for it** or to survive an alpha strike.

**Example sequences (illustrative):**

- **T1–3:** Sol Ring → Birds of Paradise → Rocco for X=2 grabbing **Impact Tremors** (or **Welcoming Vampire** if you need cards more than damage).
- **Mid:** Panharmonicon on board → cheap creature → **Preston** triggers stack copies; follow with **Cloudstone Curio** only when you see a **safe line** (mana and life buffer).

## Tutor targets by game stage

| Stage | Best tutor targets (via **Rocco**, **Gamble**, **Sterling Grove**) | Why |
|-------|----------------------------------------------------------------------|-----|
| Early (1–4) | **Birds of Paradise**, **Bloom Tender**, **Heronblade Elite**, **Impact Tremors**, **Welcoming Vampire** | Fixes colors, accelerates X, or starts the damage clock / card flow |
| Mid | **Panharmonicon**, **Preston, the Vanisher**, **Aura Shards**, **Reclamation Sage**, **Grand Abolisher** | Doubles ETBs, enables copy chains, answers problematic types, protects combo |
| Late / win | **Food Chain**, **Squee, the Immortal**, **Purphoros, God of the Forge**, **City on Fire**, **Molten Echoes** | Assembles **infinite mana** or closes with **damage doublers** and ETB spam |

**Sterling Grove:** usually finds **Mechanized Warfare**, **Guardian Project**, **Food Chain**, or **Aura Shards** depending on what the table is playing.

## WOTC bracket fit

- **Game changers (Archidekt oracle flags on this list):** **Gamble**, **Aura Shards**, **Teferi's Protection** (three flagged in export — confirm on [Scryfall](https://scryfall.com) if your group uses printed lists).
- **Other flags:** **Food Chain** combo with **Squee**; **Blasphemous Act** as a cheap reset; no extra-turn spells detected in main + commander.
- **Current vs target:** The deck **plays above** a typical **Bracket 3** even if you pilot it “fairly,” because of **fast mana**, **tutors**, and **Food Chain** potential. **`target_bracket: 4`** in the deck file is a **reasonable self-label**; drop toward 3 only if you **remove combo** and some **free protection**.

Official bracket guidance: [Commander Brackets (Wizards)](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025).

## Outside-list candidates

| Add | Why | Suggested cut | Bracket note |
|-----|-----|---------------|--------------|
| [Smuggler's Share](https://scryfall.com/search?q=%21%22Smuggler%27s%20Share%22) | Steady cards / treasures on a **low curve** | **Genesis Chamber** (table symmetry) or a **marginal 3-drop** | Strong at 4; feels “value” not “combo” |
| [Esper Sentinel](https://scryfall.com/search?q=%21%22Esper%20Sentinel%22) | Early **card flow** without committing a full engine | **Mother of Runes** (overlap in protection role) or a **fifth** redundant pinger | Fine at 3–4 |
| [Garruk's Uprising](https://scryfall.com/search?q=%21%22Garruk%27s%20Uprising%22) | Triggers off **power ≥ 4** line you already hit with buffs / tokens | **Soul's Attendant** or **Soul Warden** if lifegain is **nice-not-needed** | Low bracket impact |
| [Toski, Bearer of Secrets](https://scryfall.com/search?q=%21%22Toski%2C%20Bearer%20of%20Secrets%22) | Combat **draw** in a go-wide shell | **Weftstalker Ardent** or another **medium-rate** beater | Fine at 3–4 |
| [March of Otherworldly Light](https://scryfall.com/search?q=%21%22March%20of%20Otherworldly%20Light%22) | Flexible **answer** using treasures / extra mana | **Aura Mutation** (narrower) | Slight uptick in interaction density |
| [Elesh Norn, Mother of Machines](https://scryfall.com/search?q=%21%22Elesh%20Norn%2C%20Mother%20of%20Machines%22) | Doubles ETBs symmetrically (high power) | Only if you want **Bracket 5** — swap a **mid** synergy piece | **Raises** bracket |

**Optional sideboard ideas:** The 10-card Archidekt sideboard is a **module swap** (adventure / Universes Beyond faces). Treat it as **house-rule** content, not Commander 99, unless your group explicitly allows it.

## Bracket tuning plan

1. **Stay at 4:** Keep **Food Chain** but add **clear pre-game** discussion; keep **Teferi's Protection** / **Swat** as “fair” emergency valves.
2. **Move toward 3:** Cut **Food Chain** + tune tutors toward **value** only; replace **Gamble** with **less swingy** selection; trim **Grand Abolisher** if tables dislike **combo shields**.
3. **Move toward 5 (not recommended without table buy-in):** Add **efficient tutors** (e.g. **Enlightened Tutor**-class effects where legal in your philosophy) and **Dockside**-tier acceleration — only if everyone is on that **power contract**.

## Organization audit

- Deck markdown follows [`deck-organization.md`](../deck-organization.md): **Commander → Lands → Ramp → Draw → Removal → Wipes → Synergy → Utility**.
- **Ojer** is correctly called out as **MDFC** in Utility; **Boseiju** removal is on the **land** card (not double-counted as a spell).

## Turns 1–4 (three scenarios)

Assumptions: **on the play**, no opposing interaction, reasonable shuffles.

### Hand A — fast mana + Rocco

- **T1:** **Sol Ring** (tap for 2 total with land) or **Birds** off a **Green** source; play a fetch or dual if available.
- **T2:** Deploy **Arcane Signet** / second land; set up **two** mana toward Rocco.
- **T3:** **Rocco** for **X = 2–3**, tutoring something that **accelerates damage or cards** (e.g. **Impact Tremors**, **Welcoming Vampire**). You are already **ahead on tempo**.
- **T4:** Deploy **Panharmonicon** or a **second engine**; start **closing** with ETBs.

### Hand B — medium setup (no fast mana)

- **T1–2:** Lands + **dork** or **2-mana** play (**Welcoming Vampire** / **Soul Warden**).
- **T3:** **Rocco** for small **X** to recover parity (**Reclamation Sage** if needed, else value).
- **T4:** **Guardian Project** or **Tocasia's Welcome** online; you are **stabilizing** toward a **card-positive** midgame.

### Hand C — flood / light action

- **T1–3:** Multiple lands, no engine; hold **Chaos Warp** / **Generous Gift** if someone runs away.
- **T4:** **Gamble** for a **high-impact** piece (risk) or deploy **Sterling Grove** setting up **next-turn** enchantment tutor. Without a draw spell, you are **vulnerable** — this is where **Smuggler's Share** / **Toski**-class cards help most.

## Prioritized changes

1. Add **2–4** pieces of **land-based ramp** or **2-mana ramp** if you want less **feast-or-famine** starts (keep **AMV** in mind — you already curve low).
2. Add **2–4** **steady card engines** that do not require a wide board (unless you deliberately accept **high variance**).
3. Decide whether **Food Chain** stays; if yes, **predeclare** combo lines and keep **interaction** tight so games end cleanly.
4. Revisit **Genesis Chamber** and **Grand Abolisher** for **table feel** — powerful, not strictly “wrong.”
