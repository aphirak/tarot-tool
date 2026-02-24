"""
tarot_tool — Production-grade tarot card system for OpenClaw MCP integration.

Quick start (function API):
    from tarot_tool.tools import read_spread
    context = read_spread("celtic_cross", question="What do I need to know?")
    print(context.system_prompt_injection)

Quick start (Python skill class):
    from tarot_tool.tool import TarotSkill
    skill = TarotSkill()
    result = skill.read_spread(spread_id="celtic_cross", question="What do I need to know?")
"""
from tarot_tool.tool import TarotSkill
from tarot_tool.tools import (
    ALL_TOOLS,
    draw_tarot_cards,
    get_card_meaning,
    list_spread_formats,
    read_spread,
)

__version__ = "0.1.0"
__all__ = [
    "TarotSkill",
    "draw_tarot_cards",
    "get_card_meaning",
    "list_spread_formats",
    "read_spread",
    "ALL_TOOLS",
]
