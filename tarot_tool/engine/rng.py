"""Cryptographically secure RNG engine for tarot card draws."""
from __future__ import annotations

import secrets
from typing import Optional

from tarot_tool.models.card import TarotCard

_system_rng = secrets.SystemRandom()


def draw_cards(
    deck: list[TarotCard],
    count: int,
    reversal_probability: float = 0.35,
    seed: Optional[int] = None,
) -> list[tuple[TarotCard, bool]]:
    """
    Draw `count` unique cards from `deck` using Fisher-Yates shuffle.

    Args:
        deck: Full list of TarotCard objects to draw from.
        count: Number of cards to draw.
        reversal_probability: Probability each card is reversed (0.0–1.0).
        seed: Optional integer seed for reproducible testing only.
              Uses secrets.SystemRandom in production (seed=None).

    Returns:
        List of (TarotCard, is_reversed) tuples, length == count.

    Raises:
        ValueError: If count exceeds deck size or is non-positive.
    """
    if count <= 0:
        raise ValueError(f"count must be positive, got {count}")
    if count > len(deck):
        raise ValueError(f"count {count} exceeds deck size {len(deck)}")

    rng = secrets.SystemRandom() if seed is None else _SeededRandom(seed)
    shuffled = _fisher_yates(list(deck), rng)
    drawn = shuffled[:count]

    return [
        (card, rng.random() < reversal_probability)
        for card in drawn
    ]


def _fisher_yates(cards: list[TarotCard], rng: secrets.SystemRandom) -> list[TarotCard]:
    """In-place Fisher-Yates shuffle, returns the list."""
    n = len(cards)
    for i in range(n - 1, 0, -1):
        j = rng.randint(0, i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards


class _SeededRandom:
    """Thin wrapper for seeded random — testing only, not cryptographically secure."""

    def __init__(self, seed: int) -> None:
        import random
        self._rng = random.Random(seed)

    def random(self) -> float:
        return self._rng.random()

    def randint(self, a: int, b: int) -> int:
        return self._rng.randint(a, b)
