"""Dataclass models for tarot spreads."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from tarot_tool.models.card import DrawnCard


@dataclass
class PositionDefinition:
    """A single position in a spread layout."""

    index: int
    label: str
    guidance: str  # Interpretation guidance for this position


@dataclass
class SpreadDefinition:
    """Definition of a spread format."""

    id: str
    name: str
    description: str
    positions: list[PositionDefinition]
    min_cards: int
    max_cards: int


@dataclass
class SpreadResult:
    """Result of performing a spread draw."""

    spread: SpreadDefinition
    drawn_cards: list[DrawnCard]
    question: Optional[str] = None
    interpretation_prompt: str = ""  # Ready-to-use LLM context for interpreting this draw
