"""Dataclass model for the full LLM reading context payload."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from tarot_tool.models.card import DrawnCard


@dataclass
class ReadingContext:
    """Complete reading context payload for LLM interpretation."""

    spread_name: str
    question: Optional[str]
    reading_style: str
    drawn_cards: list[DrawnCard]
    spread_narrative_hints: list[str]  # Per-position interpretation guidance
    thematic_summary: str  # Auto-generated card theme summary
    element_distribution: dict[str, int]  # Fire/Water/Air/Earth counts
    numerology_notes: list[str]
    dominant_suit: Optional[str]
    reading_timestamp: str  # ISO 8601
    system_prompt_injection: str  # Ready-to-use LLM system prompt fragment
