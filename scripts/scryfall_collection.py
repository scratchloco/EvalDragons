#!/usr/bin/env python3
"""Resolve MTG card names via Scryfall (stdin: one name per line) -> JSON lines stdout."""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.scryfall.com"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "EvalDragons/1.0"})
    while True:
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
                return json.loads(data.decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                retry = e.headers.get("Retry-After")
                time.sleep(float(retry) if retry else 0.5)
                continue
            if e.code == 404:
                return {}
            raise


def resolve_name(name: str) -> dict | None:
    name = name.strip()
    if not name:
        return None
    q = urllib.parse.quote(name)
    # Exact match first
    card = fetch_json(f"{BASE}/cards/named?exact={q}")
    if card:
        return card
    # Fuzzy fallback
    card = fetch_json(f"{BASE}/cards/named?fuzzy={q}")
    return card or None


def main() -> int:
    for line in sys.stdin:
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        card = resolve_name(raw)
        if card is None:
            sys.stdout.write(json.dumps({"input": raw, "error": "not_found"}) + "\n")
        else:
            slim = {
                "input": raw,
                "name": card.get("name"),
                "type_line": card.get("type_line"),
                "mana_cost": card.get("mana_cost"),
                "cmc": card.get("cmc"),
                "oracle_text": card.get("oracle_text"),
                "color_identity": card.get("color_identity"),
                "legalities": card.get("legalities"),
                "game_changer": card.get("game_changer"),
                "scryfall_uri": card.get("scryfall_uri"),
            }
            sys.stdout.write(json.dumps(slim, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
