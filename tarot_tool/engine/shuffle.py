"""Fisher-Yates shuffle utilities for the tarot deck."""
from __future__ import annotations

import secrets

from tarot_tool.models.card import TarotCard


def shuffle_deck(deck: list[TarotCard]) -> list[TarotCard]:
    """
    Return a new shuffled copy of the deck using Fisher-Yates + CSPRNG.

    Args:
        deck: List of TarotCard objects to shuffle.

    Returns:
        A new list with cards in random order; original list is not mutated.
    """
    cards = list(deck)
    rng = secrets.SystemRandom()
    n = len(cards)
    for i in range(n - 1, 0, -1):
        j = rng.randint(0, i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards
