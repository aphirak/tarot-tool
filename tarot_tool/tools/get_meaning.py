"""OpenClaw Tool: get_card_meaning."""
from __future__ import annotations

from typing import Literal, Optional

from tarot_tool.cards.deck import get_deck
from tarot_tool.models.card import TarotCard

TOOL_DEFINITION = {
    "name": "get_card_meaning",
    "description": (
        "Retrieve full meaning, keywords, and metadata for a specific tarot card. "
        "Supports exact name match or partial/case-insensitive search."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "card_name": {
                "type": "string",
                "description": "Exact card name or partial match (case-insensitive).",
            },
            "orientation": {
                "type": "string",
                "enum": ["upright", "reversed", "both"],
                "description": "Which orientation meaning(s) to return.",
                "default": "both",
            },
        },
        "required": ["card_name"],
    },
}


def get_card_meaning(
    card_name: str,
    orientation: Literal["upright", "reversed", "both"] = "both",
) -> dict:
    """
    Retrieve meaning and metadata for a tarot card by name.

    Args:
        card_name: Exact or partial card name (case-insensitive).
        orientation: Which meaning(s) to include in the result.

    Returns:
        Dict with card metadata and requested meaning(s).

    Raises:
        ValueError: If orientation is invalid.
        LookupError: If no card matches the given name.
    """
    if orientation not in ("upright", "reversed", "both"):
        raise ValueError(f"orientation must be 'upright', 'reversed', or 'both', got '{orientation}'")

    card = _find_card(card_name)

    result: dict = {
        "id": card.id,
        "name": card.name,
        "suit": card.suit.value,
        "arcana": card.arcana,
        "number": card.number,
        "element": card.element,
        "astrology": card.astrology,
        "numerology": card.numerology,
        "image_key": card.image_key,
    }

    if orientation in ("upright", "both"):
        result["keywords_upright"] = card.keywords_upright
        result["meaning_upright"] = card.meaning_upright

    if orientation in ("reversed", "both"):
        result["keywords_reversed"] = card.keywords_reversed
        result["meaning_reversed"] = card.meaning_reversed

    return result


def _find_card(card_name: str) -> TarotCard:
    """Find a card by exact or partial case-insensitive name match."""
    deck = get_deck()
    needle = card_name.lower().strip()

    # Exact match first
    for card in deck:
        if card.name.lower() == needle:
            return card

    # Partial match
    matches = [card for card in deck if needle in card.name.lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = ", ".join(c.name for c in matches)
        raise LookupError(f"Multiple cards match '{card_name}': {names}. Please be more specific.")

    raise LookupError(f"No card found matching '{card_name}'.")
