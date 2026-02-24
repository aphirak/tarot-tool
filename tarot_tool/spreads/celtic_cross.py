"""Celtic Cross — 10-position spread."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

CELTIC_CROSS = SpreadDefinition(
    id="celtic_cross",
    name="Celtic Cross",
    description=(
        "The most comprehensive traditional tarot spread. Ten positions explore the situation "
        "from every angle: the core issue, crossing energies, past, future, internal and external "
        "forces, hopes, fears, and final outcome."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="The Heart of the Matter",
            guidance="The central issue, the core energy of what is being asked about.",
        ),
        PositionDefinition(
            index=1,
            label="The Crossing Card",
            guidance=(
                "What crosses or challenges the central card. "
                "Can be an obstacle, a complementary force, or a complicating factor."
            ),
        ),
        PositionDefinition(
            index=2,
            label="The Root / Foundation",
            guidance=(
                "The underlying foundation of the situation—unconscious influences, "
                "past events, or root causes driving the matter."
            ),
        ),
        PositionDefinition(
            index=3,
            label="The Recent Past",
            guidance=(
                "Events or energies that have recently passed and are passing out of influence, "
                "but still relevant to the current situation."
            ),
        ),
        PositionDefinition(
            index=4,
            label="The Crown / Possible Outcome",
            guidance=(
                "The best possible outcome, or what the querent is consciously aiming for. "
                "What could be achieved."
            ),
        ),
        PositionDefinition(
            index=5,
            label="The Near Future",
            guidance=(
                "What is moving toward the querent in the near future—events or energies "
                "about to manifest."
            ),
        ),
        PositionDefinition(
            index=6,
            label="The Querent",
            guidance=(
                "How the querent sees themselves, their attitude, or their role in this situation."
            ),
        ),
        PositionDefinition(
            index=7,
            label="External Influences",
            guidance=(
                "How others see the querent, or the external environment and other people's "
                "influence on the situation."
            ),
        ),
        PositionDefinition(
            index=8,
            label="Hopes and Fears",
            guidance=(
                "The querent's deepest hopes or fears around this situation—often these are "
                "two sides of the same coin."
            ),
        ),
        PositionDefinition(
            index=9,
            label="Final Outcome",
            guidance=(
                "The ultimate outcome or resolution if the current path is followed. "
                "The culmination of all surrounding energies."
            ),
        ),
    ],
    min_cards=10,
    max_cards=10,
)
