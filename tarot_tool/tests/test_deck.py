"""Tests for deck integrity — all 78 cards, no duplicates, valid data."""
from __future__ import annotations

import pytest

from tarot_tool.cards.deck import get_deck
from tarot_tool.models.card import Suit, TarotCard


class TestDeckCompleteness:
    def test_deck_has_78_cards(self) -> None:
        deck = get_deck()
        assert len(deck) == 78, f"Expected 78 cards, got {len(deck)}"

    def test_no_duplicate_ids(self) -> None:
        deck = get_deck()
        ids = [card.id for card in deck]
        assert len(ids) == len(set(ids)), "Duplicate card IDs found"

    def test_no_duplicate_names(self) -> None:
        deck = get_deck()
        names = [card.name for card in deck]
        assert len(names) == len(set(names)), "Duplicate card names found"

    def test_ids_sequential_0_to_77(self) -> None:
        deck = get_deck()
        ids = sorted(card.id for card in deck)
        assert ids == list(range(78)), "Card IDs are not 0–77 sequential"

    def test_major_arcana_count(self) -> None:
        deck = get_deck()
        major = [c for c in deck if c.arcana == "major"]
        assert len(major) == 22, f"Expected 22 Major Arcana, got {len(major)}"

    def test_minor_arcana_count(self) -> None:
        deck = get_deck()
        minor = [c for c in deck if c.arcana == "minor"]
        assert len(minor) == 56, f"Expected 56 Minor Arcana, got {len(minor)}"

    def test_each_suit_has_14_cards(self) -> None:
        deck = get_deck()
        for suit in (Suit.WANDS, Suit.CUPS, Suit.SWORDS, Suit.PENTACLES):
            cards = [c for c in deck if c.suit == suit]
            assert len(cards) == 14, f"Expected 14 {suit.value} cards, got {len(cards)}"

    def test_all_cards_are_tarot_card_instances(self) -> None:
        deck = get_deck()
        for card in deck:
            assert isinstance(card, TarotCard)


class TestCardDataIntegrity:
    def test_all_cards_have_non_empty_meanings(self) -> None:
        deck = get_deck()
        for card in deck:
            assert card.meaning_upright.strip(), f"{card.name} has empty meaning_upright"
            assert card.meaning_reversed.strip(), f"{card.name} has empty meaning_reversed"

    def test_all_cards_have_keywords(self) -> None:
        deck = get_deck()
        for card in deck:
            assert len(card.keywords_upright) >= 3, (
                f"{card.name} has fewer than 3 upright keywords"
            )
            assert len(card.keywords_reversed) >= 3, (
                f"{card.name} has fewer than 3 reversed keywords"
            )

    def test_all_cards_have_image_keys(self) -> None:
        deck = get_deck()
        for card in deck:
            assert card.image_key.strip(), f"{card.name} has empty image_key"

    def test_major_arcana_have_elements(self) -> None:
        deck = get_deck()
        for card in deck:
            if card.arcana == "major":
                assert card.element is not None, f"{card.name} is missing element"

    def test_minor_arcana_elements_match_suit(self) -> None:
        expected = {
            Suit.WANDS: "Fire",
            Suit.CUPS: "Water",
            Suit.SWORDS: "Air",
            Suit.PENTACLES: "Earth",
        }
        deck = get_deck()
        for card in deck:
            if card.arcana == "minor":
                assert card.element == expected[card.suit], (
                    f"{card.name}: expected element {expected[card.suit]}, got {card.element}"
                )

    def test_get_deck_returns_consistent_result(self) -> None:
        """get_deck() should return the same objects on repeated calls (cached)."""
        deck1 = get_deck()
        deck2 = get_deck()
        assert deck1 is deck2, "get_deck() should return a cached list"
