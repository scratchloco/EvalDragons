# EDH review: Merieke Ri Berit

**Generated:** 2026-04-19  
**Deck file:** [decks/merieke-ri-berit.md](../decks/merieke-ri-berit.md)  
**Data:** Archidekt API export + embedded oracle legality; run [Scryfall](https://scryfall.com/docs/api) `cards/collection` before tournaments.

---

## Deck source

- **URL / file:** [https://archidekt.com/decks/21722664/merieke_ri_berit](https://archidekt.com/decks/21722664/merieke_ri_berit)  
- **Commander:** **Merieke Ri Berit**  
- **Core list scope:** Main + commander only for counts, ratios, synergy, brackets, and goldfish. Sideboard (5) and maybeboard (14) are **excluded** from core math; they may appear under optional add hints.

---

## Deck zones (from URL) — Archidekt `cards[].categories`

| Zone | Total cards (sum of qty) | Notes |
|------|---------------------------|--------|
| Main + commander | 100 | 99 + commander; row-level `Maybeboard` / `Sideboard` / `Commander` tags |
| Sideboard | 5 | Agent of Treachery, Akroma's Will, Anguished Unmaking, High Market, Mindcrank |
| Maybeboard | 14 | See deck file |

---

## Target Commander Bracket

- **Goal (1–5):** **3** (from [`decks/merieke-ri-berit.md`](../decks/merieke-ri-berit.md) frontmatter)  
- **Stated intent:** Esper **combo-control** — Merieke **tap/steal** with **untap** engines, **Isochron Scepter + Dramatic Reversal**, **Freed from the Real**, **Intruder Alarm** lines, plus **premium counters** and **Rise of the Dark Realms** / **Bribery** closers.

---

## Legality table

| Scope | Commander legal | Notes |
|-------|-----------------|-------|
| **Main 99 + commander** | **Yes** (embedded `oracleCard.legalities.commander` in export) | No `not_legal` entries detected. **Re-verify** every name via Scryfall before competitive play. |
| Color identity | Esper (WUB) | Duals and pips align with commander. |

---

## Cleaned list delta

- **None** — no cards removed for illegal or identity errors in this export.

---

## Core ratio table

| Bucket | Target | Actual | Delta | Notes |
|--------|--------|--------|-------|-------|
| Lands | 36–38 | **36** | 0 | Nonland **AMV ~2.48** → 34–35 also defensible per EvalDragons guidelines. |
| Ramp | 10–12 | **~5–6** | **−4 to −6** | Sol Ring, Arcane Signet, Chromatic Lantern, Patriar's Seal, Fellwar Stone. **Below** guideline. |
| Card draw | ~10 | **~4–6** | **−4 to −6** | Mystic Remora, Brainstorm, Ponder, Skullclamp; Sensei's Divining Top as partial selection. **Below** steady + burst mix. |
| Targeted removal | 7–10 | **~15+** | **+5+** | Dense **counters** + **Swords**, **Path**, **Swan Song**, **Void Rend**, **Vindicate**, **Pongify**, etc. **Damn** is flexible (creature / overload). |
| Board wipes | 2–4 | **1–2** | **0 to −1** | **Austere Command**; **Damn** overload as optional second reset. |
| Synergy / strategy | 25–30 | **remainder** | ✓ | Large **combo** package (Scepter, Reversal, Freed, Alarm, Aphetto, Fatestitcher, Pemmin's, Elixir, Sakashima, Staff, Key, etc.). |

---

## Mana and curve

- **Nonland AMV:** ~**2.48** (63 nonlands).  
- **CMC buckets (nonland qty):** 1 MV: 17 · 2 MV: 18 · 3 MV: 18 · 4 MV: 6 · 5 MV: 2 · 6 MV: 1 · 9 MV: 1 — **curve is low and interaction-dense**; you spend many turns **holding mana** for counters while setting up **artifacts**.

---

## Role density

- **Interaction:** Very high — multiple **hard counters**, **Mana Drain**, **Deadly Rollick**, flexible removal.  
- **Creatures:** Mix of **combo creatures** (Fatestitcher, Aphetto, Vizier, Marvin, Kelpie Guide), **protection** (Mother, Giver), and **value** (Thassa, Robaran, Royal Assassin).  
- **Artifacts / enchantments:** Core **combo** and **protection** (Greaves, Boots, Scepter, Bracers, Propaganda, Ghostly Prison).  
- **Finishers:** **Rise of the Dark Realms**, **Bribery**, **Austere Command**.

---

## Commander axes

1. **Tap / steal** — Merieke **controls** creatures; **untap** breaks **summoning sickness** and **combat** parity.  
2. **Untap / combo** — **Intruder Alarm**, **Aphetto Alchemist**, **Fatestitcher**, **Pemmin's Aura**, **Thousand-Year Elixir**, **Magewright's Stone**, **Illusionist's Bracers**, **Manifold Key**, **Staff of Domination**.  
3. **Isochron + Reversal** — **Infinite mana** with sufficient rocks / **blue** for **Walking Ballista**-style wins (Ballista not in main; closers are mostly **Rise** / **Bribery** / **beats**).  
4. **Control shell** — **Teferi's Protection**, **Propaganda**, **Ghostly Prison**, **counter suite**.  
5. **Grave / theft** — **Reanimate**, **Rise**, **Bribery**, **Nightmare Shepherd**.

---

## Synergy and alignment audit

- **Matrix summary:** **High** commander synergy on **untap** pieces and **blue** enchantments; **high** internal synergy between **artifacts**, **Isochron**, and **mana rocks** (but **rock count is low** for Reversal lines).  
- **Misaligned / tension:** Deck wants **both** **tap-out** setup turns and **hold-up** countermagic — sequencing discipline matters. **Skullclamp** needs **1-toughness** bodies you are happy to trade.  
- **Cluster gaps:** **Ramp** and **card flow** are the clearest gaps vs EvalDragons targets; **wipes** are slightly thin if meta is go-wide without you having **Merieke** online.

---

## Build value — general sentiment

- **Strong card quality** for a **combo Esper** table (premium interaction, tutor, theft finishers).  
- **Coherent** for **Merieke combo** — not a scattershot goodstuff pile.  
- **Undersupported** on **velocity** (ramp/draw) for how many **moving parts** you must assemble **before** opponents pressure **life / tempo**.

---

## Strategic summary

You are a **combo-control** deck that ideally **stabilizes** on **rocks + land**, **protects** or **blinks** Merieke, then **assembles** either **Scepter + Dramatic Reversal** mana or **Freed from the Real** + **tap/untap** loop, while **countering** the most dangerous stack or board interaction. Wins often go through **Rise of the Dark Realms**, **Bribery**, or **incremental** value once the table is **locked**.  
**Risks:** fast **aggro**, **stax** that taxes **artifacts** and **noncreature spells**, **grave hate** on **Rise**, and **Rule of Law** effects that strand **Reversal** lines. **Mulligans** that lack **lands + early interaction** are punishing.

---

## Recommended play lines

1. **Opening:** Keep **2 lands + cheap interaction** or **2 lands + Sol Ring** over **greedy** keeps with **5 MV** air and no **U** up.  
2. **Merieke timing:** Cast when you can **protect** (Greaves / boots / **Deadly Rollick** / **Mana Drain**) and when **stealing** a **real** threat or **stopping** an attack—not only as a **3/4** for three.  
3. **Combo turn:** Sequence **Isochron imprint** → **Reversal** with **enough** **net mana** from rocks; or **Freed** on Merieke with **permanent** untap — **practice** on [Archidekt playtester](https://archidekt.com/decks/21722664/merieke_ri_berit).  
4. **Example (mid):** **T3** Merieke + **hold** **Mana Drain**; **T4** **Arcane Signet** + **Ponder** setup; **T5+** threaten **Sakashima** / **Thassa** value or **tutor** for **Scepter**.

---

## Tutor targets by game stage

*Deck includes **Vampiric Tutor**.*

| Stage | Efficient targets | Why | Tutor |
|-------|-------------------|-----|--------|
| Early (1–4) | **Sol Ring**, **Isochron Scepter**, **Swan Song** / **Swords to Plowshares** | Speed or **answer** to **artifact hate** / early **creature** | Vampiric |
| Mid | **Dramatic Reversal**, **Freed from the Real**, **Intruder Alarm** | **Combo assembly** before shields drop | Vampiric |
| Late / win-ready | **Rise of the Dark Realms**, **Bribery**, **Austere Command** | **Close** after **yards** are full or **boards** are wide | Vampiric |

---

## WOTC bracket fit

- **Game changers (verify on Scryfall):** Deck runs **Mana Drain**, **Deadly Rollick**, **Vampiric Tutor** — treat as **likely Game Changers** under [Wizards Oct 2025 bracket guidance](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025); confirm with `game_changer` on each printing.  
- **Other flags:** **Two-card combo** heuristics (**Scepter + Reversal** with mana); **no** obvious **mass land denial** or **extra turn** chain in main 99 from list review.  
- **Current vs target (3):** Deck **leans** toward **Bracket 4** power at spirier tables; for strict **Bracket 3**, consider **swapping** one of **Drain / Rollick / Vampiric** for lower-impact analogs or **adding** **precon-speed** pieces if you need to **downshift**.

---

## Outside-list candidates

| Add | Why | Cut | Bracket note |
|-----|-----|-----|---------------|
| **Azorius Signet** | On-color **2 MV** ramp | Weakest **counter** or **Pongify** if meta allows | Low |
| **Dimir Signet** | Same | Same | Low |
| **Orzhov Signet** | Same | Same | Low |
| **Mind Stone** | Ramp **or** cycle late | marginal **1 MV** spell if any | Low |
| **Night's Whisper** | **Burst draw** | low-impact **creature** if slots tight | Low |
| **Secrets of the Golden City** | **Draw 2** with **ascend** late | Same | Low |
| **Talisman of Dominance** | **Efficient** rock | — | Low |
| **Rhystic Study** | **Steady draw** (if bracket OK) | — | Raises bracket feel |
| **Finale of Revelation** | Already in **maybe** — strong **refill** | **Brainstorm** if redundant with Top | Medium |
| **Supreme Verdict** | In **maybe** — **uncounterable** wipe | **Austere** if redundant | Medium |

- **Primary pool:** Scryfall-driven rows above (not limited to builder zones).  
- **Optional — sideboard / maybe:** **Supreme Verdict**, **Finale**, **Blue Sun's Zenith**, **Spark Double**, **Rings of Brighthearth** are strong **on-theme** pulls from your **maybe** list; still use **Scryfall** for cards **not** already listed.

---

## Bracket tuning plan

1. **Stay at Bracket 3:** Replace or downgrade **one** of **Mana Drain / Deadly Rollick / Vampiric**; add **precon-style** **ramp** and **draw**.  
2. **Accept Bracket 4:** Keep suite; add **Fierce Guardianship**-style only if you want **maximum** protection (meta call).  
3. **Either:** Add **2+ wraths** if **creature** metas are **faster** than your **Merieke** setup.

---

## Organization audit

- [decks/merieke-ri-berit.md](../decks/merieke-ri-berit.md) follows **deck-organization.md** headers. **Fellwar Stone** is noted in **Ramp** with a **ratio** note (also artifact). **Sideboard** and **maybe** are **separated** from core sections.

---

## Turns 1–4 (three scenarios)

*No opponents; London mulligan assumed; **maindeck cards only**.*

### Hand A — fast (Sol Ring, Swords, 2 lands, Island, Swamp, Plains)

- **T1:** **Plains**, tap **Sol Ring**.  
- **T2:** **Island**, **Arcane Signet** (or hold **Swords** if creature threat).  
- **T3:** **Swamp**, play **Merieke** if safe; else develop second rock.  
- **T4:** **Hold Mana Drain** + tap Merieke on best creature — **floating** UWB.

### Hand B — medium (3 lands, Counterspell, Ponder, Fellwar, random 3-drop)

- **T1–2:** **Lands**, **Fellwar**.  
- **T3:** **Ponder** — **shuffle** or keep based on **interaction** density.  
- **T4:** **Hold Counterspell** for **first** noncreature threat or **combo** piece; **develop** land **four** if **curve** allows **Merieke** next.

### Hand C — flood-screw (6 lands, no rocks, expensive spells)

- **Mulligan** aggressively — this list **needs** early **U** and **interaction** or **rocks**; **six lands** with no **1–2 MV** play is a **loss** vs **aggro**.

---

## Prioritized changes

1. **Add 4–6** real **2 MV** ramp pieces (signets / talismans / **Mind Stone**).  
2. **Add 3–5** **card advantage** spells (**Night's Whisper**, **Secrets**, etc.).  
3. **Consider** **second wipe** or promote **Supreme Verdict** from **maybe** if **go-wide** meta.  
4. **Sideboard:** **Akroma's Will** / **Agent** are strong **meta** swaps — integrate with **bracket** goal.  
5. **Bracket:** consciously choose **3 vs 4** and tune **Game Changers** accordingly.
