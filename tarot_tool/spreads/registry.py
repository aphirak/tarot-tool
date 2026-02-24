"""Spread format registry — central lookup for all available spreads."""
from __future__ import annotations

from typing import Optional

from tarot_tool.models.spread import SpreadDefinition
from tarot_tool.spreads.celtic_cross import CELTIC_CROSS
from tarot_tool.spreads.chakra import CHAKRA
from tarot_tool.spreads.custom import build_custom_spread
from tarot_tool.spreads.decision import DECISION
from tarot_tool.spreads.horseshoe import HORSESHOE
from tarot_tool.spreads.relationship import RELATIONSHIP
from tarot_tool.spreads.single import SINGLE_CARD
from tarot_tool.spreads.three_card import THREE_CARD
from tarot_tool.spreads.year_ahead import YEAR_AHEAD

_REGISTRY: dict[str, SpreadDefinition] = {
    "single": SINGLE_CARD,
    "three_card": THREE_CARD,
    "celtic_cross": CELTIC_CROSS,
    "horseshoe": HORSESHOE,
    "relationship": RELATIONSHIP,
    "year_ahead": YEAR_AHEAD,
    "chakra": CHAKRA,
    "decision": DECISION,
}


def get_spread(
    spread_id: str,
    custom_positions: Optional[list[str]] = None,
) -> SpreadDefinition:
    """
    Retrieve a spread definition by ID.

    Args:
        spread_id: The spread identifier string.
        custom_positions: Required when spread_id == 'custom'.
                          List of position labels for the custom spread.

    Returns:
        The corresponding SpreadDefinition.

    Raises:
        KeyError: If spread_id is not registered and not 'custom'.
        ValueError: If spread_id is 'custom' but no positions provided.
    """
    if spread_id == "custom":
        if not custom_positions:
            raise ValueError("custom spread requires custom_positions list")
        return build_custom_spread(custom_positions)

    if spread_id not in _REGISTRY:
        available = ", ".join(sorted(_REGISTRY.keys()))
        raise KeyError(f"Unknown spread '{spread_id}'. Available: {available}, custom")

    return _REGISTRY[spread_id]


def list_spreads() -> list[SpreadDefinition]:
    """Return all registered (non-custom) spread definitions."""
    return list(_REGISTRY.values())


def is_valid_spread_id(spread_id: str) -> bool:
    """Check whether a spread_id is valid (includes 'custom')."""
    return spread_id in _REGISTRY or spread_id == "custom"
