"""Meaning registry — provides fast lookup of card meanings by name."""
from __future__ import annotations

from functools import lru_cache
from typing import Optional

from tarot_tool.cards.deck import get_deck
from tarot_tool.models.card import TarotCard


@lru_cache(maxsize=1)
def _build_name_index() -> dict[str, TarotCard]:
    """Build a lowercased-name → TarotCard index (cached)."""
    return {card.name.lower(): card for card in get_deck()}


def get_meaning(
    card_name: str,
    orientation: str = "both",
) -> dict[str, str | list[str]]:
    """
    Look up upright/reversed meanings for a card by name.

    Args:
        card_name: Case-insensitive card name.
        orientation: 'upright', 'reversed', or 'both'.

    Returns:
        Dict with 'name' and requested meaning fields.

    Raises:
        KeyError: If card is not found.
        ValueError: If orientation is invalid.
    """
    if orientation not in ("upright", "reversed", "both"):
        raise ValueError(f"orientation must be 'upright', 'reversed', or 'both'")

    index = _build_name_index()
    card = index.get(card_name.lower())
    if card is None:
        raise KeyError(f"Card not found: {card_name!r}")

    result: dict = {"name": card.name}
    if orientation in ("upright", "both"):
        result["keywords_upright"] = card.keywords_upright
        result["meaning_upright"] = card.meaning_upright
    if orientation in ("reversed", "both"):
        result["keywords_reversed"] = card.keywords_reversed
        result["meaning_reversed"] = card.meaning_reversed
    return result


def list_card_names() -> list[str]:
    """Return all 78 card names in deck order."""
    return [card.name for card in get_deck()]
