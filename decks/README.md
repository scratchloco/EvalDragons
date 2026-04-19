# Deck sources

Store one deck per file under `decks/`, for example `decks/my-deck.md`.

## Recommended content

- **Source URL**: Moxfield or Archidekt link on its own line: `Source: https://...`  
  Reviews use **main deck + commander** from that URL only (not sideboard / maybeboard for core counts). SB/MB may be cited optionally as add ideas; suggestions are **not** limited to those zones—see the **edh-deck-review** skill.
- **Target bracket** (optional): in frontmatter, `target_bracket: 3` (Wizards 1–5).
- **Sections**: follow [`../deck-organization.md`](../deck-organization.md).

## Fallback when APIs fail

If the agent cannot fetch a URL, export **raw JSON** from the deck builder and save as `decks/incoming/<name>.json`, then point the review at that file.

## JSON policy

Small exports may be committed for reproducibility. Large caches should stay local (see root `README` / `.gitignore`).
