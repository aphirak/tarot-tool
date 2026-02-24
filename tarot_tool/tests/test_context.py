"""Tests for ReadingContext assembly and tool integrations."""
from __future__ import annotations

import pytest

from tarot_tool.tools.draw_cards import draw_tarot_cards
from tarot_tool.tools.get_meaning import get_card_meaning
from tarot_tool.tools.list_spreads import list_spread_formats
from tarot_tool.tools.read_spread import read_spread


class TestReadSpread:
    def test_read_spread_returns_reading_context(self) -> None:
        from tarot_tool.models.reading import ReadingContext
        ctx = read_spread("single")
        assert isinstance(ctx, ReadingContext)

    def test_system_prompt_non_empty_for_all_spreads(self) -> None:
        spread_ids = [
            "single", "three_card", "celtic_cross", "horseshoe",
            "relationship", "chakra", "decision",
        ]
        for sid in spread_ids:
            ctx = read_spread(sid)
            assert ctx.system_prompt_injection.strip(), (
                f"{sid}: system_prompt_injection is empty"
            )

    def test_reading_context_fields_present(self) -> None:
        ctx = read_spread("three_card", question="What path should I take?")
        assert ctx.spread_name == "Past / Present / Future"
        assert ctx.question == "What path should I take?"
        assert ctx.reading_style == "combined"
        assert len(ctx.drawn_cards) == 3
        assert ctx.reading_timestamp  # ISO 8601 non-empty
        assert isinstance(ctx.element_distribution, dict)
        assert isinstance(ctx.numerology_notes, list)

    def test_reading_style_psychological(self) -> None:
        ctx = read_spread("single", reading_style="psychological")
        assert "psychological" in ctx.system_prompt_injection

    def test_reading_style_spiritual(self) -> None:
        ctx = read_spread("single", reading_style="spiritual")
        assert "spiritual" in ctx.system_prompt_injection

    def test_reading_style_practical(self) -> None:
        ctx = read_spread("single", reading_style="practical")
        assert "practical" in ctx.system_prompt_injection

    def test_invalid_reading_style_raises(self) -> None:
        with pytest.raises(ValueError, match="reading_style"):
            read_spread("single", reading_style="cosmic")  # type: ignore

    def test_drawn_cards_have_active_meanings(self) -> None:
        ctx = read_spread("three_card")
        for dc in ctx.drawn_cards:
            assert dc.active_meaning.strip(), f"Card {dc.card.name} has empty active_meaning"
            assert dc.active_keywords, f"Card {dc.card.name} has no active_keywords"

    def test_celtic_cross_returns_10_cards(self) -> None:
        ctx = read_spread("celtic_cross")
        assert len(ctx.drawn_cards) == 10

    def test_custom_spread_reading(self) -> None:
        ctx = read_spread("custom", custom_positions=["Career", "Finances", "Relationships"])
        assert len(ctx.drawn_cards) == 3
        labels = [dc.position_label for dc in ctx.drawn_cards]
        assert labels == ["Career", "Finances", "Relationships"]

    def test_spread_narrative_hints_match_card_count(self) -> None:
        ctx = read_spread("horseshoe")
        assert len(ctx.spread_narrative_hints) == 7

    def test_thematic_summary_non_empty(self) -> None:
        ctx = read_spread("three_card")
        assert ctx.thematic_summary.strip()

    def test_system_prompt_contains_full_meanings(self) -> None:
        ctx = read_spread("three_card")
        for dc in ctx.drawn_cards:
            assert dc.active_meaning in ctx.system_prompt_injection, (
                f"active_meaning for {dc.card.name} missing from system_prompt_injection"
            )

    def test_system_prompt_contains_thematic_summary(self) -> None:
        ctx = read_spread("single")
        assert ctx.thematic_summary in ctx.system_prompt_injection

    def test_system_prompt_contains_narrative_hints(self) -> None:
        ctx = read_spread("three_card")
        for hint in ctx.spread_narrative_hints:
            assert hint in ctx.system_prompt_injection, (
                f"Narrative hint missing from system_prompt_injection: {hint!r}"
            )

    def test_system_prompt_contains_numerology_notes(self) -> None:
        ctx = read_spread("celtic_cross")
        for note in ctx.numerology_notes:
            assert note in ctx.system_prompt_injection, (
                f"Numerology note missing from system_prompt_injection: {note!r}"
            )

    def test_reading_timestamp_is_iso8601(self) -> None:
        from datetime import datetime
        ctx = read_spread("single")
        # Should parse without error
        dt = datetime.fromisoformat(ctx.reading_timestamp)
        assert dt is not None


class TestDrawTarotCards:
    def test_draw_returns_spread_result(self) -> None:
        from tarot_tool.models.spread import SpreadResult
        result = draw_tarot_cards("three_card")
        assert isinstance(result, SpreadResult)
        assert len(result.drawn_cards) == 3

    def test_draw_with_question(self) -> None:
        result = draw_tarot_cards("single", question="What do I need today?")
        assert result.question == "What do I need today?"

    def test_draw_custom_spread(self) -> None:
        result = draw_tarot_cards("custom", custom_positions=["A", "B"])
        assert len(result.drawn_cards) == 2


class TestGetCardMeaning:
    def test_get_meaning_exact_name(self) -> None:
        result = get_card_meaning("The Fool")
        assert result["name"] == "The Fool"
        assert "meaning_upright" in result
        assert "meaning_reversed" in result

    def test_get_meaning_case_insensitive(self) -> None:
        result = get_card_meaning("the fool")
        assert result["name"] == "The Fool"

    def test_get_meaning_upright_only(self) -> None:
        result = get_card_meaning("The Magician", orientation="upright")
        assert "meaning_upright" in result
        assert "meaning_reversed" not in result

    def test_get_meaning_reversed_only(self) -> None:
        result = get_card_meaning("The Magician", orientation="reversed")
        assert "meaning_reversed" in result
        assert "meaning_upright" not in result

    def test_invalid_orientation_raises(self) -> None:
        with pytest.raises(ValueError, match="orientation"):
            get_card_meaning("The Fool", orientation="sideways")  # type: ignore

    def test_unknown_card_raises(self) -> None:
        with pytest.raises(LookupError):
            get_card_meaning("The Nonexistent Card")

    def test_minor_arcana_lookup(self) -> None:
        result = get_card_meaning("Ace of Wands")
        assert result["name"] == "Ace of Wands"
        assert result["suit"] == "wands"

    def test_court_card_lookup(self) -> None:
        result = get_card_meaning("Queen of Cups")
        assert result["name"] == "Queen of Cups"


class TestListSpreadFormats:
    def test_list_returns_all_spreads(self) -> None:
        spreads = list_spread_formats()
        ids = {s["id"] for s in spreads}
        assert "single" in ids
        assert "celtic_cross" in ids
        assert "custom" in ids
        assert len(spreads) == 9  # 8 named + custom

    def test_list_without_positions(self) -> None:
        spreads = list_spread_formats(include_positions=False)
        for s in spreads:
            assert "positions" not in s

    def test_list_with_positions(self) -> None:
        spreads = list_spread_formats(include_positions=True)
        named = [s for s in spreads if s["id"] != "custom"]
        for s in named:
            assert "positions" in s
            assert len(s["positions"]) > 0
