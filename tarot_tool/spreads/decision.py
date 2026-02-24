"""Decision Making spread — 5 positions."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

DECISION = SpreadDefinition(
    id="decision",
    name="Decision Making",
    description=(
        "A five-card spread for navigating a choice or fork in the road. "
        "Illuminates the current situation, pros and cons of each path, "
        "and the guiding advice."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="The Situation",
            guidance="The core of the decision at hand—what is actually being decided.",
        ),
        PositionDefinition(
            index=1,
            label="Option A — Pros",
            guidance="The benefits, advantages, or positive energy of choosing Option A.",
        ),
        PositionDefinition(
            index=2,
            label="Option A — Cons",
            guidance="The challenges, risks, or shadow aspects of choosing Option A.",
        ),
        PositionDefinition(
            index=3,
            label="Option B — Pros",
            guidance="The benefits, advantages, or positive energy of choosing Option B.",
        ),
        PositionDefinition(
            index=4,
            label="Option B — Cons",
            guidance="The challenges, risks, or shadow aspects of choosing Option B.",
        ),
    ],
    min_cards=5,
    max_cards=5,
)
