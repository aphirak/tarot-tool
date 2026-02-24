"""Tarot card data — deck, meanings, Major and Minor Arcana definitions."""
from tarot_tool.cards.deck import get_deck
from tarot_tool.cards.meanings import get_meaning, list_card_names

__all__ = ["get_deck", "get_meaning", "list_card_names"]
