"""Single card spread definition."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

SINGLE_CARD = SpreadDefinition(
    id="single",
    name="Single Card",
    description="A one-card draw for a direct answer, daily guidance, or focused insight.",
    positions=[
        PositionDefinition(
            index=0,
            label="The Card",
            guidance=(
                "This card speaks directly to the question or situation at hand. "
                "Interpret it as the central message or energy surrounding the matter."
            ),
        )
    ],
    min_cards=1,
    max_cards=1,
)
