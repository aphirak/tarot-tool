"""Three-card spread — Past / Present / Future."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

THREE_CARD = SpreadDefinition(
    id="three_card",
    name="Past / Present / Future",
    description=(
        "A classic three-card spread revealing the timeline of a situation: "
        "the past influences shaping it, the present moment, and likely future outcome."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="Past",
            guidance=(
                "Influences, events, or energies from the past that have led to the current situation. "
                "What foundation—positive or challenging—has been laid?"
            ),
        ),
        PositionDefinition(
            index=1,
            label="Present",
            guidance=(
                "The current state of affairs, the energy surrounding the querent right now. "
                "What is actively at work in this moment?"
            ),
        ),
        PositionDefinition(
            index=2,
            label="Future",
            guidance=(
                "The likely outcome or direction if the current path continues. "
                "This is potential, not certainty—free will can alter this trajectory."
            ),
        ),
    ],
    min_cards=3,
    max_cards=3,
)
