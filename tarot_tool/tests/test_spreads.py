"""Tests for spread registry and spread definitions."""
from __future__ import annotations

import pytest

from tarot_tool.spreads.registry import get_spread, is_valid_spread_id, list_spreads


class TestSpreadRegistry:
    def test_all_named_spreads_resolve(self) -> None:
        spread_ids = [
            "single", "three_card", "celtic_cross", "horseshoe",
            "relationship", "year_ahead", "chakra", "decision",
        ]
        for sid in spread_ids:
            spread = get_spread(sid)
            assert spread.id == sid

    def test_unknown_spread_raises_key_error(self) -> None:
        with pytest.raises(KeyError, match="Unknown spread"):
            get_spread("nonexistent_spread")

    def test_custom_spread_requires_positions(self) -> None:
        with pytest.raises(ValueError, match="custom_positions"):
            get_spread("custom")

    def test_custom_spread_with_positions(self) -> None:
        positions = ["Mind", "Body", "Spirit"]
        spread = get_spread("custom", custom_positions=positions)
        assert spread.id == "custom"
        assert len(spread.positions) == 3
        assert spread.positions[0].label == "Mind"
        assert spread.positions[1].label == "Body"
        assert spread.positions[2].label == "Spirit"

    def test_list_spreads_returns_all_named(self) -> None:
        spreads = list_spreads()
        ids = {s.id for s in spreads}
        assert "single" in ids
        assert "three_card" in ids
        assert "celtic_cross" in ids
        assert "horseshoe" in ids
        assert "relationship" in ids
        assert "year_ahead" in ids
        assert "chakra" in ids
        assert "decision" in ids
        assert len(ids) == 8

    def test_is_valid_spread_id(self) -> None:
        assert is_valid_spread_id("single")
        assert is_valid_spread_id("celtic_cross")
        assert is_valid_spread_id("custom")
        assert not is_valid_spread_id("bogus")

    def test_spread_card_counts(self) -> None:
        expected = {
            "single": 1,
            "three_card": 3,
            "celtic_cross": 10,
            "horseshoe": 7,
            "relationship": 6,
            "year_ahead": 13,
            "chakra": 7,
            "decision": 5,
        }
        for sid, count in expected.items():
            spread = get_spread(sid)
            assert spread.min_cards == count, (
                f"{sid}: expected {count} cards, got {spread.min_cards}"
            )
            assert len(spread.positions) == count, (
                f"{sid}: position count {len(spread.positions)} != {count}"
            )

    def test_positions_have_unique_indices(self) -> None:
        for spread in list_spreads():
            indices = [p.index for p in spread.positions]
            assert len(indices) == len(set(indices)), (
                f"{spread.id}: duplicate position indices"
            )

    def test_positions_have_non_empty_labels(self) -> None:
        for spread in list_spreads():
            for pos in spread.positions:
                assert pos.label.strip(), f"{spread.id} pos {pos.index} has empty label"

    def test_positions_have_non_empty_guidance(self) -> None:
        for spread in list_spreads():
            for pos in spread.positions:
                assert pos.guidance.strip(), (
                    f"{spread.id} pos {pos.index} has empty guidance"
                )
