# EDH deck review — reference

## Moxfield

- **Deck JSON**: `GET https://api.moxfield.com/v2/decks/all/{publicId}`
- **publicId**: last path segment of `https://www.moxfield.com/decks/<publicId>`

Example:

```bash
curl -sS "https://api.moxfield.com/v2/decks/all/<PUBLIC_ID>" | head -c 2000
```

Response uses `mainboard`, `commanders`, etc. as maps of card keys → `{ quantity, card: { name, ... } }`.

## Archidekt

- **Deck JSON**: `GET https://archidekt.com/api/decks/{deckId}/`
- **deckId**: numeric id in the deck URL (path segment after `/decks/`).

Example:

```bash
curl -sS "https://archidekt.com/api/decks/<DECK_ID>/" | head -c 2000
```

Card arrays differ by API version; normalize to `{ name, quantity }`. If `curl` fails (auth, block), use exported JSON from the site UI into `decks/incoming/`.

## Scryfall — collection (bulk by name)

`POST https://api.scryfall.com/cards/collection`

```bash
curl -sS -X POST https://api.scryfall.com/cards/collection \
  -H "Content-Type: application/json" \
  -d '{"identifiers":[{"name":"Sol Ring"},{"name":"Arcane Signet"}]}'
```

Max **75** identifiers per request. Respect `429` — sleep per `Retry-After`.

## Scryfall — legality

- Per card: `legalities.commander` on card JSON.
- Banned list sweep: open in browser or use [card search](https://scryfall.com/docs/api/cards/search) with a documented query, e.g. cards banned in Commander (verify current syntax on Scryfall docs). Example pattern to verify live: `banned:commander` or `-legal:commander` searches — **always confirm** on [Scryfall syntax](https://scryfall.com/docs/reference/syntax).

## Scryfall — discovery queries (examples)

Always add `legal:commander` and restrict identity. Commander colors as letters WUBRGC.

- **Identity subset**: e.g. Boros → `id<=boros` is not valid Scryfall; use **`id:boros`** for “this exact identity” or combine `c:` / `id:` per [color docs](https://scryfall.com/docs/reference/colors). Practical pattern: `id:esper` for Esper-only cards; for “in Garza’s colors” use identity letters matching commander’s `color_identity` array.
- **Artifacts in Jeskai**: `legal:commander id:jeskai t:artifact -is:creature`
- **Enchantress hooks**: `legal:commander oracle:draws~a~card oracle:enchantment`

**Game changers** (count for WOTC brackets): on card JSON, `game_changer: true`. Search keyword may appear as `is:gamechanger` — verify on Scryfall before relying in scripts.

Encode spaces as `+` or `%20` in GET URLs.

## Wizards Commander Brackets

Official sources (summaries only; read articles for full rules):

- [Introducing Commander Brackets Beta](https://magic.wizards.com/en/news/announcements/introducing-commander-brackets-beta)
- [Commander Brackets Beta Update – October 21, 2025](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025)

**Bracket names (1–5)** — high level:

1. **Exhibition** — ultra-casual / theme; strictest on fast mana, game changers, MLD, extra turns, etc. (see WOTC).
2. **Core** — precon-like expectations.
3. **Upgraded** — stronger; limited game changers; some combo timing rules per WOTC.
4. **Optimized** — high power; effectively Commander-legal card pool for many restrictions.
5. **cEDH** — same card legality as 4 with competitive intent / metagame.

When advising, **cite the article** for any bracket-specific claim.

## Core ratio — counting edge cases

- **MDFC / modal lands**: If the deck plays a spell land as a land drop most games, count as **Land**; if primarily cast as spell, use that spell bucket.
- **Split / fuse**: One physical card = one slot; pick primary function.
- **Commander tax**: Commander not in the 99 counts.
- **Ramp vs rock that draws**: Primary job = bucket (`Mind Stone` ramp if mainly cracked for mana).
- **Flexible removal**: `Assassin’s Trophy` = targeted removal; `Cyclonic Rift` overload = often classified as **wipe** for ratio purposes (state choice).
- **Tutors**: If they exist to find combo pieces, usually **synergy**; generic `Demonic Tutor` often synergy unless the deck is pure goodstuff.

## Banlist note

Use Scryfall + official Commander banlist communications. Automated queries should be re-checked when sets release.
