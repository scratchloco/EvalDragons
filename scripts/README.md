# Scripts

## `scryfall_collection.py`

Reads **one card name per line** from stdin (UTF-8), resolves each via Scryfall’s **named** endpoint (exact then fuzzy), and prints **JSON lines** (one object per input card).

```bash
python3 scripts/scryfall_collection.py < names.txt > resolved.jsonl
```

Requires **network**. Honors HTTP 429 `Retry-After` when present.

For deck-sized lists prefer the official **Cards Collection** API in batches of 75 (see `reference.md`); this script is a lightweight fallback for small lists or quick checks.
