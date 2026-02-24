"""Year Ahead spread — 13 positions (12 months + theme card)."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

_MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

YEAR_AHEAD = SpreadDefinition(
    id="year_ahead",
    name="Year Ahead",
    description=(
        "A thirteen-card spread mapping energy and themes for each month of the coming year, "
        "plus an overarching theme card for the year as a whole."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="Year Theme",
            guidance=(
                "The overarching energy, lesson, or archetype guiding the entire year ahead."
            ),
        ),
        *[
            PositionDefinition(
                index=i + 1,
                label=month,
                guidance=f"The dominant energy and themes for {month}.",
            )
            for i, month in enumerate(_MONTHS)
        ],
    ],
    min_cards=13,
    max_cards=13,
)
