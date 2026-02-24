"""OpenClaw tool implementations for the tarot system."""
from tarot_tool.tools.draw_cards import TOOL_DEFINITION as DRAW_TOOL, draw_tarot_cards
from tarot_tool.tools.get_meaning import TOOL_DEFINITION as MEANING_TOOL, get_card_meaning
from tarot_tool.tools.list_spreads import TOOL_DEFINITION as LIST_TOOL, list_spread_formats
from tarot_tool.tools.read_spread import TOOL_DEFINITION as READ_TOOL, read_spread

ALL_TOOLS = [DRAW_TOOL, MEANING_TOOL, LIST_TOOL, READ_TOOL]

__all__ = [
    "draw_tarot_cards",
    "get_card_meaning",
    "list_spread_formats",
    "read_spread",
    "ALL_TOOLS",
]
