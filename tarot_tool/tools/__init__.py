"""OpenClaw tool implementations for the tarot system."""
from typing import Any, Callable

from tarot_tool.tools.draw_cards import TOOL_DEFINITION as DRAW_TOOL
from tarot_tool.tools.draw_cards import draw_tarot_cards
from tarot_tool.tools.draw_cards import tool_handler as draw_handler
from tarot_tool.tools.get_meaning import TOOL_DEFINITION as MEANING_TOOL
from tarot_tool.tools.get_meaning import get_card_meaning
from tarot_tool.tools.get_meaning import tool_handler as meaning_handler
from tarot_tool.tools.list_spreads import TOOL_DEFINITION as LIST_TOOL
from tarot_tool.tools.list_spreads import list_spread_formats
from tarot_tool.tools.list_spreads import tool_handler as list_handler
from tarot_tool.tools.read_spread import TOOL_DEFINITION as READ_TOOL
from tarot_tool.tools.read_spread import read_spread
from tarot_tool.tools.read_spread import tool_handler as read_handler

ALL_TOOLS: list[dict[str, Any]] = [DRAW_TOOL, MEANING_TOOL, LIST_TOOL, READ_TOOL]

TOOL_HANDLERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "draw_tarot_cards": draw_handler,
    "get_card_meaning": meaning_handler,
    "list_spread_formats": list_handler,
    "read_spread": read_handler,
}

__all__ = [
    "draw_tarot_cards",
    "get_card_meaning",
    "list_spread_formats",
    "read_spread",
    "ALL_TOOLS",
    "TOOL_HANDLERS",
    "draw_handler",
    "meaning_handler",
    "list_handler",
    "read_handler",
]
