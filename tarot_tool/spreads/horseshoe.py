"""Horseshoe spread — 7 positions."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

HORSESHOE = SpreadDefinition(
    id="horseshoe",
    name="Horseshoe",
    description=(
        "A seven-card spread arranged in a horseshoe arc, providing a thorough view of "
        "a situation's past, present, future, advice, external influences, hopes/fears, and outcome."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="The Past",
            guidance="Past events and influences that have shaped the current situation.",
        ),
        PositionDefinition(
            index=1,
            label="The Present",
            guidance="The current state of affairs and active energies in the situation.",
        ),
        PositionDefinition(
            index=2,
            label="Hidden Influences",
            guidance=(
                "Unseen or unconscious forces at work—what may be operating beneath the surface."
            ),
        ),
        PositionDefinition(
            index=3,
            label="Obstacles",
            guidance="Challenges or blocks that must be acknowledged and addressed.",
        ),
        PositionDefinition(
            index=4,
            label="External Influences",
            guidance="Outside forces, other people, or environmental factors affecting the outcome.",
        ),
        PositionDefinition(
            index=5,
            label="Advice",
            guidance="The recommended course of action or attitude to adopt.",
        ),
        PositionDefinition(
            index=6,
            label="Outcome",
            guidance="The most likely resolution if present energies continue on their current path.",
        ),
    ],
    min_cards=7,
    max_cards=7,
)
