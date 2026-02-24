"""Custom dynamic n-position spread."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition


def build_custom_spread(position_labels: list[str]) -> SpreadDefinition:
    """
    Build a custom spread from a list of position labels.

    Args:
        position_labels: List of strings naming each position.
                         Length determines the number of cards drawn.

    Returns:
        A SpreadDefinition configured for the given positions.

    Raises:
        ValueError: If position_labels is empty.
    """
    if not position_labels:
        raise ValueError("Custom spread requires at least one position label.")

    positions = [
        PositionDefinition(
            index=i,
            label=label,
            guidance=f"Interpret this card in the context of: {label}",
        )
        for i, label in enumerate(position_labels)
    ]
    n = len(position_labels)

    return SpreadDefinition(
        id="custom",
        name="Custom Spread",
        description=f"A custom {n}-card spread with user-defined positions.",
        positions=positions,
        min_cards=n,
        max_cards=n,
    )
