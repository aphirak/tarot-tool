"""Relationship spread — 6 positions."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

RELATIONSHIP = SpreadDefinition(
    id="relationship",
    name="Relationship",
    description=(
        "A six-card spread designed to illuminate the dynamics between two people—their "
        "individual energies, how they see each other, what connects them, and the relationship's direction."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="You",
            guidance="The energy, attitude, or role the querent brings to the relationship.",
        ),
        PositionDefinition(
            index=1,
            label="The Other Person",
            guidance="The energy, attitude, or role the other person brings to the relationship.",
        ),
        PositionDefinition(
            index=2,
            label="The Connection",
            guidance="What binds these two people together—shared values, karma, or circumstance.",
        ),
        PositionDefinition(
            index=3,
            label="What You Want",
            guidance="The querent's conscious or unconscious desires within this relationship.",
        ),
        PositionDefinition(
            index=4,
            label="What They Want",
            guidance="The other person's desires, needs, or expectations in the relationship.",
        ),
        PositionDefinition(
            index=5,
            label="The Path Forward",
            guidance=(
                "The likely trajectory of the relationship and what can guide it toward "
                "its highest potential."
            ),
        ),
    ],
    min_cards=6,
    max_cards=6,
)
