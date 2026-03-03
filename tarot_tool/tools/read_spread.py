"""OpenClaw Tool: read_spread — full reading context for LLM interpretation."""
from __future__ import annotations

import dataclasses
from typing import Any, Literal, Optional

from tarot_tool.cards.deck import get_deck
from tarot_tool.engine.context_builder import build_reading_context
from tarot_tool.engine.rng import draw_cards as rng_draw
from tarot_tool.models.card import DrawnCard
from tarot_tool.models.reading import ReadingContext
from tarot_tool.spreads.registry import get_spread

TOOL_DEFINITION = {
    "name": "read_spread",
    "description": (
        "Perform a complete tarot reading. Returns a structured ReadingContext with "
        "all card meanings, elemental analysis, numerology, and a ready-to-use LLM system prompt."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "spread_id": {
                "type": "string",
                "description": "Spread format ID.",
            },
            "question": {
                "type": "string",
                "description": "Optional question or focus for the reading.",
            },
            "reversal_probability": {
                "type": "number",
                "description": "Probability each card is reversed (0.0–1.0, default 0.35).",
                "default": 0.35,
            },
            "reading_style": {
                "type": "string",
                "enum": ["psychological", "spiritual", "practical", "combined"],
                "description": "Interpretive lens for the reading.",
                "default": "combined",
            },
            "custom_positions": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Position labels for a custom spread.",
            },
        },
        "required": ["spread_id"],
    },
}

ReadingStyle = Literal["psychological", "spiritual", "practical", "combined"]


def read_spread(
    spread_id: str,
    question: Optional[str] = None,
    reversal_probability: float = 0.35,
    reading_style: ReadingStyle = "combined",
    custom_positions: Optional[list[str]] = None,
) -> ReadingContext:
    """
    Perform a complete tarot reading and return a fully-assembled ReadingContext.

    Args:
        spread_id: The spread format to use.
        question: Optional question or focus for the reading.
        reversal_probability: Probability of each card being reversed.
        reading_style: Interpretive style for the LLM system prompt.
        custom_positions: Required for custom spread.

    Returns:
        A ReadingContext ready for LLM consumption.

    Raises:
        ValueError: If reading_style is invalid.
    """
    valid_styles = ("psychological", "spiritual", "practical", "combined")
    if reading_style not in valid_styles:
        raise ValueError(
            f"reading_style must be one of {valid_styles}, got '{reading_style}'"
        )

    spread = get_spread(spread_id, custom_positions=custom_positions)
    deck = get_deck()
    raw_draws = rng_draw(deck, count=spread.min_cards, reversal_probability=reversal_probability)

    drawn_cards: list[DrawnCard] = []
    for pos_def, (card, is_reversed) in zip(spread.positions, raw_draws):
        drawn_cards.append(
            DrawnCard(
                card=card,
                position=pos_def.index,
                position_label=pos_def.label,
                is_reversed=is_reversed,
                active_meaning=card.meaning_reversed if is_reversed else card.meaning_upright,
                active_keywords=card.keywords_reversed if is_reversed else card.keywords_upright,
            )
        )

    return build_reading_context(
        spread=spread,
        drawn_cards=drawn_cards,
        question=question,
        reading_style=reading_style,
    )


def tool_handler(params: dict[str, Any]) -> dict[str, Any]:
    """
    OpenClaw-compatible handler for read_spread.

    Args:
        params: Dict with keys matching read_spread() signature.

    Returns:
        {"success": True, "data": {...}} or {"success": False, "error": "...", "error_type": "..."}
    """
    try:
        result = read_spread(
            spread_id=params["spread_id"],
            question=params.get("question"),
            reversal_probability=float(params.get("reversal_probability", 0.35)),
            reading_style=params.get("reading_style", "combined"),  # type: ignore[arg-type]
            custom_positions=params.get("custom_positions"),
        )
        return {"success": True, "data": dataclasses.asdict(result)}
    except Exception as e:
        return {"success": False, "error": str(e), "error_type": type(e).__name__}
