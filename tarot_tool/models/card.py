"""Dataclass models for tarot cards."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Suit(str, Enum):
    MAJOR = "major_arcana"
    WANDS = "wands"
    CUPS = "cups"
    SWORDS = "swords"
    PENTACLES = "pentacles"


@dataclass
class TarotCard:
    """A single tarot card with full metadata and meanings."""

    id: int  # 0–77
    name: str
    suit: Suit
    number: Optional[int]  # 0=Fool, 1–21 Major; 1–14 Minor
    arcana: str  # "major" | "minor"
    keywords_upright: list[str]
    keywords_reversed: list[str]
    meaning_upright: str  # Full paragraph
    meaning_reversed: str
    element: Optional[str]
    astrology: Optional[str]
    numerology: Optional[int]
    image_key: str  # slug for image lookup

    def __post_init__(self) -> None:
        if isinstance(self.suit, str):
            self.suit = Suit(self.suit)
        if self.arcana not in ("major", "minor"):
            raise ValueError("arcana must be 'major' or 'minor'")
        if not (0 <= self.id <= 77):
            raise ValueError("id must be between 0 and 77")


@dataclass
class DrawnCard:
    """A card drawn for a reading, with positional context."""

    card: TarotCard
    position: int
    position_label: str
    is_reversed: bool
    active_meaning: str  # Resolved based on is_reversed
    active_keywords: list[str]
