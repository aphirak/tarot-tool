"""Full 78-card deck assembly and cached lookup."""
from __future__ import annotations

from functools import lru_cache

from tarot_tool.cards.major_arcana import MAJOR_ARCANA
from tarot_tool.cards.minor_arcana import MINOR_ARCANA
from tarot_tool.models.card import TarotCard


@lru_cache(maxsize=1)
def get_deck() -> list[TarotCard]:
    """
    Return the full 78-card tarot deck as validated TarotCard objects.

    The result is cached after the first call — same list object is returned
    on every subsequent call. The list itself must not be mutated by callers.

    Returns:
        Ordered list of 78 TarotCard instances (Major then Minor Arcana).
    """
    all_raw = MAJOR_ARCANA + MINOR_ARCANA
    return [TarotCard(**data) for data in all_raw]


def get_card_by_id(card_id: int) -> TarotCard:
    """
    Retrieve a single card from the deck by its ID (0–77).

    Args:
        card_id: Integer ID of the card.

    Returns:
        The matching TarotCard.

    Raises:
        IndexError: If card_id is not in range 0–77.
    """
    if not (0 <= card_id <= 77):
        raise IndexError(f"card_id must be 0–77, got {card_id}")
    deck = get_deck()
    # IDs are sequential 0–77 by construction; use direct index
    return deck[card_id]
