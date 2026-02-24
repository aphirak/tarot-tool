"""OpenClaw Tool: draw_tarot_cards."""
from __future__ import annotations

from typing import Optional

from tarot_tool.cards.deck import get_deck
from tarot_tool.engine.rng import draw_cards as rng_draw
from tarot_tool.models.card import DrawnCard
from tarot_tool.models.spread import SpreadResult
from tarot_tool.spreads.registry import get_spread

TOOL_DEFINITION = {
    "name": "draw_tarot_cards",
    "description": (
        "Draw tarot cards for a reading. Returns drawn cards with full metadata and meanings. "
        "Use list_spread_formats to enumerate available spread IDs."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "spread_id": {
                "type": "string",
                "description": "Spread format ID (use list_spread_formats to enumerate).",
            },
            "question": {
                "type": "string",
                "description": "Optional question or context for the reading.",
            },
            "reversal_probability": {
                "type": "number",
                "description": "Probability each card is reversed (0.0–1.0, default 0.35).",
                "default": 0.35,
            },
            "custom_positions": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Position labels for a custom spread (required when spread_id='custom').",
            },
        },
        "required": ["spread_id"],
    },
}


def draw_tarot_cards(
    spread_id: str,
    question: Optional[str] = None,
    reversal_probability: float = 0.35,
    custom_positions: Optional[list[str]] = None,
) -> SpreadResult:
    """
    Draw tarot cards for the specified spread.

    Args:
        spread_id: The spread format to use.
        question: Optional question for the reading.
        reversal_probability: Probability of each card being reversed.
        custom_positions: Required for custom spread; list of position labels.

    Returns:
        A SpreadResult containing the spread definition and drawn cards.
    """
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

    return SpreadResult(
        spread=spread,
        drawn_cards=drawn_cards,
        question=question,
    )
