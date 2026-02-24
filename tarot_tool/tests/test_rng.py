"""Tests for the RNG draw engine."""
from __future__ import annotations

import pytest

from tarot_tool.cards.deck import get_deck
from tarot_tool.engine.rng import draw_cards


class TestDrawCards:
    def test_draw_returns_correct_count(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=10)
        assert len(result) == 10

    def test_draw_returns_unique_cards(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=20)
        ids = [card.id for card, _ in result]
        assert len(ids) == len(set(ids)), "Duplicate cards drawn"

    def test_draw_single_card(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=1)
        assert len(result) == 1
        card, is_reversed = result[0]
        assert isinstance(is_reversed, bool)

    def test_draw_full_deck(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=78)
        assert len(result) == 78
        ids = {card.id for card, _ in result}
        assert ids == set(range(78))

    def test_draw_raises_on_zero_count(self) -> None:
        deck = get_deck()
        with pytest.raises(ValueError, match="count must be positive"):
            draw_cards(deck, count=0)

    def test_draw_raises_on_negative_count(self) -> None:
        deck = get_deck()
        with pytest.raises(ValueError):
            draw_cards(deck, count=-1)

    def test_draw_raises_when_count_exceeds_deck(self) -> None:
        deck = get_deck()
        with pytest.raises(ValueError, match="exceeds deck size"):
            draw_cards(deck, count=79)

    def test_seeded_draw_is_deterministic(self) -> None:
        deck = get_deck()
        result1 = draw_cards(deck, count=10, seed=42)
        result2 = draw_cards(deck, count=10, seed=42)
        ids1 = [card.id for card, _ in result1]
        ids2 = [card.id for card, _ in result2]
        assert ids1 == ids2, "Seeded draws should be deterministic"

    def test_seeded_draw_different_seeds_differ(self) -> None:
        deck = get_deck()
        result1 = draw_cards(deck, count=10, seed=1)
        result2 = draw_cards(deck, count=10, seed=2)
        ids1 = [card.id for card, _ in result1]
        ids2 = [card.id for card, _ in result2]
        assert ids1 != ids2, "Different seeds should produce different draws"

    def test_reversal_probability_zero(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=20, reversal_probability=0.0, seed=99)
        reversed_cards = [r for _, r in result if r]
        assert len(reversed_cards) == 0, "No cards should be reversed at probability 0"

    def test_reversal_probability_one(self) -> None:
        deck = get_deck()
        result = draw_cards(deck, count=20, reversal_probability=1.0, seed=99)
        reversed_cards = [r for _, r in result if r]
        assert len(reversed_cards) == 20, "All cards should be reversed at probability 1"

    def test_reversal_distribution_is_reasonable(self) -> None:
        """At 0.35 probability over 1000 draws, expect roughly 30–40% reversed."""
        deck = get_deck()
        total = 0
        reversed_count = 0
        for seed in range(50):
            draws = draw_cards(deck, count=20, reversal_probability=0.35, seed=seed)
            for _, is_rev in draws:
                total += 1
                if is_rev:
                    reversed_count += 1
        ratio = reversed_count / total
        assert 0.20 <= ratio <= 0.55, f"Reversal ratio {ratio:.2f} is outside expected range"

    def test_original_deck_not_mutated(self) -> None:
        """draw_cards should not mutate the input deck."""
        deck = get_deck()
        original_order = [card.id for card in deck]
        draw_cards(deck, count=10, seed=7)
        after_order = [card.id for card in deck]
        assert original_order == after_order, "draw_cards mutated the input deck"
