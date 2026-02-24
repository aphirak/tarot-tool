"""Chakra spread — 7 positions."""
from __future__ import annotations

from tarot_tool.models.spread import PositionDefinition, SpreadDefinition

CHAKRA = SpreadDefinition(
    id="chakra",
    name="Chakra Spread",
    description=(
        "A seven-card spread aligned with the seven major chakras. "
        "Reveals energetic blocks, strengths, and areas for healing in the body-mind-spirit system."
    ),
    positions=[
        PositionDefinition(
            index=0,
            label="Root Chakra (Muladhara)",
            guidance=(
                "Security, survival, grounding, and physical needs. "
                "How is the querent's sense of safety and foundation?"
            ),
        ),
        PositionDefinition(
            index=1,
            label="Sacral Chakra (Svadhisthana)",
            guidance=(
                "Creativity, pleasure, sexuality, and emotional flow. "
                "What is the state of creative and sensual energy?"
            ),
        ),
        PositionDefinition(
            index=2,
            label="Solar Plexus (Manipura)",
            guidance=(
                "Personal power, confidence, willpower, and identity. "
                "How strong is the querent's sense of self?"
            ),
        ),
        PositionDefinition(
            index=3,
            label="Heart Chakra (Anahata)",
            guidance=(
                "Love, compassion, forgiveness, and connection. "
                "How open is the querent's heart to giving and receiving love?"
            ),
        ),
        PositionDefinition(
            index=4,
            label="Throat Chakra (Vishuddha)",
            guidance=(
                "Communication, truth, expression, and authenticity. "
                "Is the querent speaking and living their truth?"
            ),
        ),
        PositionDefinition(
            index=5,
            label="Third Eye (Ajna)",
            guidance=(
                "Intuition, insight, wisdom, and inner vision. "
                "What is the clarity of the querent's inner knowing?"
            ),
        ),
        PositionDefinition(
            index=6,
            label="Crown Chakra (Sahasrara)",
            guidance=(
                "Spiritual connection, higher purpose, and universal consciousness. "
                "How is the querent's relationship with the divine or higher self?"
            ),
        ),
    ],
    min_cards=7,
    max_cards=7,
)
