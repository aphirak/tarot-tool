"""Pydantic models for tarot spreads."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from tarot_tool.models.card import DrawnCard


class PositionDefinition(BaseModel):
    """A single position in a spread layout."""

    index: int
    label: str
    guidance: str  # Interpretation guidance for this position


class SpreadDefinition(BaseModel):
    """Definition of a spread format."""

    id: str
    name: str
    description: str
    positions: list[PositionDefinition]
    min_cards: int
    max_cards: int


class SpreadResult(BaseModel):
    """Result of performing a spread draw."""

    spread: SpreadDefinition
    drawn_cards: list[DrawnCard]
    question: Optional[str] = None
    interpretation_prompt: str = ""  # Ready-to-use LLM context for interpreting this draw
