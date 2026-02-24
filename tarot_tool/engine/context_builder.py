"""LLM context payload assembler for tarot readings."""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from typing import Optional

from tarot_tool.models.card import DrawnCard, Suit
from tarot_tool.models.reading import ReadingContext
from tarot_tool.models.spread import SpreadDefinition

_ELEMENT_MAP: dict[str, str] = {
    Suit.WANDS: "Fire",
    Suit.CUPS: "Water",
    Suit.SWORDS: "Air",
    Suit.PENTACLES: "Earth",
}

_MAJOR_ELEMENTS: dict[str, str] = {
    "The Fool": "Air",
    "The Magician": "Air",
    "The High Priestess": "Water",
    "The Empress": "Earth",
    "The Emperor": "Fire",
    "The Hierophant": "Earth",
    "The Lovers": "Air",
    "The Chariot": "Water",
    "Strength": "Fire",
    "The Hermit": "Earth",
    "Wheel of Fortune": "Fire",
    "Justice": "Air",
    "The Hanged Man": "Water",
    "Death": "Water",
    "Temperance": "Fire",
    "The Devil": "Earth",
    "The Tower": "Fire",
    "The Star": "Air",
    "The Moon": "Water",
    "The Sun": "Fire",
    "Judgement": "Fire",
    "The World": "Earth",
}

_NUMEROLOGY_MEANINGS: dict[int, str] = {
    0: "infinite potential and new beginnings",
    1: "initiation, leadership, and willpower",
    2: "duality, balance, and partnership",
    3: "creativity, growth, and expression",
    4: "stability, structure, and foundation",
    5: "change, conflict, and freedom",
    6: "harmony, responsibility, and nurturing",
    7: "introspection, wisdom, and mystery",
    8: "power, ambition, and mastery",
    9: "completion, wisdom, and humanitarianism",
    10: "cycles, endings, and new beginnings",
    11: "illumination, intuition, and spiritual insight",
    12: "sacrifice, surrender, and new perspective",
    13: "transformation, death, and rebirth",
    14: "moderation, balance, and patience",
    15: "bondage, materialism, and shadow self",
    16: "sudden change, upheaval, and revelation",
    17: "hope, inspiration, and faith",
    18: "illusion, fear, and the subconscious",
    19: "joy, vitality, and success",
    20: "awakening, judgment, and renewal",
    21: "completion, integration, and wholeness",
}


def build_reading_context(
    spread: SpreadDefinition,
    drawn_cards: list[DrawnCard],
    question: Optional[str],
    reading_style: str,
) -> ReadingContext:
    """
    Assemble the full ReadingContext payload for LLM interpretation.

    Args:
        spread: The spread definition used for this reading.
        drawn_cards: List of DrawnCard objects with positional context.
        question: Optional user question for the reading.
        reading_style: One of 'psychological', 'spiritual', 'practical', 'combined'.

    Returns:
        A fully populated ReadingContext ready for LLM consumption.
    """
    element_distribution = _compute_element_distribution(drawn_cards)
    dominant_suit = _compute_dominant_suit(drawn_cards)
    numerology_notes = _compute_numerology_notes(drawn_cards)
    thematic_summary = _compute_thematic_summary(drawn_cards, dominant_suit)
    narrative_hints = _extract_narrative_hints(spread, drawn_cards)
    system_prompt = _build_system_prompt(
        spread, drawn_cards, question, reading_style,
        element_distribution, thematic_summary, numerology_notes, narrative_hints,
    )

    return ReadingContext(
        spread_name=spread.name,
        question=question,
        reading_style=reading_style,
        drawn_cards=drawn_cards,
        spread_narrative_hints=narrative_hints,
        thematic_summary=thematic_summary,
        element_distribution=element_distribution,
        numerology_notes=numerology_notes,
        dominant_suit=dominant_suit,
        reading_timestamp=datetime.now(timezone.utc).isoformat(),
        system_prompt_injection=system_prompt,
    )


def _get_element(card: DrawnCard) -> Optional[str]:
    """Resolve element for a card (minor or major arcana)."""
    if card.card.suit != Suit.MAJOR:
        return _ELEMENT_MAP.get(card.card.suit)
    return _MAJOR_ELEMENTS.get(card.card.name)


def _compute_element_distribution(drawn_cards: list[DrawnCard]) -> dict[str, int]:
    """Count elemental occurrences across drawn cards."""
    counts: Counter[str] = Counter()
    for dc in drawn_cards:
        elem = _get_element(dc)
        if elem:
            counts[elem] += 1
    return dict(counts)


def _compute_dominant_suit(drawn_cards: list[DrawnCard]) -> Optional[str]:
    """Return the most common suit/element, or None if tied."""
    suit_counts: Counter[str] = Counter()
    for dc in drawn_cards:
        suit_counts[dc.card.suit.value] += 1
    if not suit_counts:
        return None
    top = suit_counts.most_common(2)
    if len(top) == 1 or top[0][1] > top[1][1]:
        return top[0][0]
    return None


def _compute_numerology_notes(drawn_cards: list[DrawnCard]) -> list[str]:
    """Generate numerology notes for each card with a numerological value."""
    notes: list[str] = []
    for dc in drawn_cards:
        num = dc.card.numerology
        if num is not None and num in _NUMEROLOGY_MEANINGS:
            notes.append(
                f"{dc.card.name} (numerology {num}): {_NUMEROLOGY_MEANINGS[num]}"
            )
    return notes


def _compute_thematic_summary(
    drawn_cards: list[DrawnCard],
    dominant_suit: Optional[str],
) -> str:
    """Auto-generate a thematic summary from the drawn cards."""
    major_count = sum(1 for dc in drawn_cards if dc.card.arcana == "major")
    minor_count = len(drawn_cards) - major_count
    reversed_count = sum(1 for dc in drawn_cards if dc.is_reversed)

    parts: list[str] = []
    if major_count > minor_count:
        parts.append("Major Arcana dominate this reading, indicating significant life themes at play.")
    elif minor_count > major_count:
        parts.append("Minor Arcana predominate, focusing on practical day-to-day circumstances.")
    else:
        parts.append("A balanced mix of Major and Minor Arcana suggests both fate and free will are active.")

    if dominant_suit:
        suit_themes = {
            "wands": "creativity, passion, and ambition",
            "cups": "emotion, intuition, and relationships",
            "swords": "intellect, conflict, and communication",
            "pentacles": "material matters, work, and the body",
            "major_arcana": "universal forces and karmic lessons",
        }
        theme = suit_themes.get(dominant_suit, dominant_suit)
        parts.append(f"The dominant energy is {dominant_suit.replace('_', ' ')}, highlighting {theme}.")

    if reversed_count > len(drawn_cards) // 2:
        parts.append("Many reversed cards indicate internal blocks or energies in transition.")
    elif reversed_count == 0:
        parts.append("All cards are upright, suggesting clear and direct energetic flow.")

    return " ".join(parts)


def _extract_narrative_hints(
    spread: SpreadDefinition,
    drawn_cards: list[DrawnCard],
) -> list[str]:
    """Build per-position narrative hints combining position guidance and card energy."""
    hints: list[str] = []
    pos_map = {p.index: p for p in spread.positions}

    for dc in drawn_cards:
        pos_def = pos_map.get(dc.position)
        guidance = pos_def.guidance if pos_def else dc.position_label
        orientation = "reversed" if dc.is_reversed else "upright"
        hint = (
            f"Position {dc.position} ({dc.position_label}): "
            f"{dc.card.name} ({orientation}) — {guidance}"
        )
        hints.append(hint)
    return hints


def _build_system_prompt(
    spread: SpreadDefinition,
    drawn_cards: list[DrawnCard],
    question: Optional[str],
    reading_style: str,
    element_distribution: dict[str, int],
    thematic_summary: str,
    numerology_notes: list[str],
    narrative_hints: list[str],
) -> str:
    """Construct the ready-to-use LLM system prompt with full card meanings and context."""
    question_str = f'"{question}"' if question else "Open reading — no specific question"
    elem_str = ", ".join(f"{k}: {v}" for k, v in sorted(element_distribution.items())) or "undefined"

    card_sections: list[str] = []
    for i, dc in enumerate(drawn_cards):
        orientation = "reversed" if dc.is_reversed else "upright"
        keywords_str = ", ".join(dc.active_keywords)
        card_sections.append(
            f"### Position {i + 1}: {dc.position_label}\n"
            f"Card: {dc.card.name} ({orientation})\n"
            f"Keywords: {keywords_str}\n"
            f"Meaning: {dc.active_meaning}"
        )

    cards_block = "\n\n".join(card_sections)
    numerology_block = "\n".join(numerology_notes) if numerology_notes else "No significant numerology patterns."
    hints_block = "\n".join(f"- {h}" for h in narrative_hints)

    return (
        f"You are an expert tarot reader performing a {reading_style} reading.\n\n"
        f"## Spread: {spread.name}\n"
        f"## Question: {question_str}\n\n"
        f"## Cards Drawn\n\n"
        f"{cards_block}\n\n"
        f"## Thematic Context\n"
        f"{thematic_summary}\n"
        f"Element distribution: {elem_str}\n"
        f"{numerology_block}\n\n"
        f"## Spread Narrative Guidance\n"
        f"{hints_block}\n\n"
        f"## Your Task\n"
        f"Provide the seeker with a cohesive interpretation. Address each card in its positional "
        f"context, weave the cards into a unified narrative, and note any elemental or thematic "
        f"patterns across the spread."
    )


def build_draw_prompt(
    spread: SpreadDefinition,
    drawn_cards: list[DrawnCard],
    question: Optional[str],
) -> str:
    """Build a ready-to-use LLM context prompt for a raw card draw (no thematic analysis)."""
    question_str = f'"{question}"' if question else "Open reading"

    card_sections: list[str] = []
    for i, dc in enumerate(drawn_cards):
        orientation = "reversed" if dc.is_reversed else "upright"
        keywords_str = ", ".join(dc.active_keywords)
        card_sections.append(
            f"### Position {i + 1}: {dc.position_label}\n"
            f"Card: {dc.card.name} ({orientation})\n"
            f"Keywords: {keywords_str}\n"
            f"Meaning: {dc.active_meaning}"
        )

    cards_block = "\n\n".join(card_sections)

    return (
        f"You are an expert tarot reader.\n\n"
        f"## Spread: {spread.name}\n"
        f"## Question: {question_str}\n\n"
        f"## Cards Drawn\n\n"
        f"{cards_block}\n\n"
        f"## Your Task\n"
        f"Interpret each card in its positional context and provide a reading for the seeker."
    )
