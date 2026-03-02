"""Fisher-Yates shuffle and cut utilities for the tarot deck."""
from __future__ import annotations

import secrets
from typing import Optional

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


def cut_deck(deck: list[TarotCard], cut_point: Optional[int] = None) -> list[TarotCard]:
    """
    Cut the deck at a random position, placing the bottom portion on top.

    Mirrors the physical querent cut step (ตัดไพ่) that follows shuffling:
    the deck is split at cut_point and reassembled as deck[cut_point:] + deck[:cut_point].

    Args:
        deck: List of TarotCard objects to cut (not mutated).
        cut_point: Explicit cut index in [1, len-1] for deterministic testing.
                   When None (default), a CSPRNG value in [1, len-1] is chosen.

    Returns:
        A new list with the cut applied; original list is not mutated.
        Returns a plain copy when len(deck) < 2.
    """
    n = len(deck)
    if n < 2:
        return list(deck)
    if cut_point is None:
        cut_point = secrets.randbelow(n - 1) + 1  # uniform in [1, n-1]
    cut_point = max(1, min(cut_point, n - 1))
    return deck[cut_point:] + deck[:cut_point]
