"""
OpenClaw Python skill interface for tarot_tool.

Import and instantiate TarotSkill to call tools directly without a subprocess:

    from tarot_tool.tool import TarotSkill

    skill = TarotSkill()
    result = skill.draw_tarot_cards(spread_id="three_card")
    result = skill.read_spread(spread_id="celtic_cross", question="What's next?")
    result = skill.get_card_meaning("The Moon")
    result = skill.list_spread_formats()

Each method returns {"success": True, "data": ...} or {"success": False, "error": ..., "error_type": ...}.
"""
from __future__ import annotations

from typing import Any, Literal, Optional

from tarot_tool.tools import ALL_TOOLS, TOOL_HANDLERS


class TarotSkill:
    """
    OpenClaw Python skill — import and call directly without a subprocess.

    OpenClaw can instantiate this class and invoke tools as Python method calls
    instead of spawning a stdio subprocess. All methods delegate to the same
    tool_handler functions used by the server, so error handling is identical.
    """

    name: str = "tarot_tool"
    version: str = "0.1.0"
    description: str = (
        "Tarot card reading tools for OpenClaw AI agents. "
        "Provides cryptographically secure card draws, rich RWS card meanings, "
        "9 spread formats, and fully assembled LLM reading contexts."
    )

    # ── Tool discovery ─────────────────────────────────────────────────────────

    def get_tool_definitions(self) -> list[dict[str, Any]]:
        """Return all tool definitions in OpenClaw input_schema format."""
        return ALL_TOOLS

    def call_tool(self, name: str, params: dict[str, Any]) -> dict[str, Any]:
        """
        Call any registered tool by name.

        Args:
            name: Tool name — one of draw_tarot_cards, get_card_meaning,
                  list_spread_formats, read_spread.
            params: Parameter dict matching the tool's input_schema.

        Returns:
            {"success": True, "data": ...}
            or {"success": False, "error": "...", "error_type": "..."}
        """
        handler = TOOL_HANDLERS.get(name)
        if handler is None:
            available = ", ".join(TOOL_HANDLERS.keys())
            return {
                "success": False,
                "error": f"Unknown tool '{name}'. Available: {available}",
                "error_type": "KeyError",
            }
        return handler(params)

    # ── Named tool methods ─────────────────────────────────────────────────────

    def draw_tarot_cards(
        self,
        spread_id: str,
        question: Optional[str] = None,
        reversal_probability: float = 0.35,
        custom_positions: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """
        Draw tarot cards for a reading.

        Args:
            spread_id: Spread format ID (use list_spread_formats to enumerate).
            question: Optional question or context for the reading.
            reversal_probability: Probability each card is reversed (0.0–1.0).
            custom_positions: Position labels when spread_id='custom'.

        Returns:
            {"success": True, "data": SpreadResult} or error dict.
        """
        return self.call_tool("draw_tarot_cards", {
            "spread_id": spread_id,
            "question": question,
            "reversal_probability": reversal_probability,
            "custom_positions": custom_positions,
        })

    def get_card_meaning(
        self,
        card_name: str,
        orientation: Literal["upright", "reversed", "both"] = "both",
    ) -> dict[str, Any]:
        """
        Retrieve full meaning, keywords, and metadata for a tarot card.

        Args:
            card_name: Exact or partial card name (case-insensitive).
            orientation: Which meanings to include — upright, reversed, or both.

        Returns:
            {"success": True, "data": card_dict} or error dict.
        """
        return self.call_tool("get_card_meaning", {
            "card_name": card_name,
            "orientation": orientation,
        })

    def list_spread_formats(self, include_positions: bool = True) -> dict[str, Any]:
        """
        List all available tarot spread formats.

        Args:
            include_positions: Include per-position labels and guidance.

        Returns:
            {"success": True, "data": [spread, ...]} or error dict.
        """
        return self.call_tool("list_spread_formats", {
            "include_positions": include_positions,
        })

    def read_spread(
        self,
        spread_id: str,
        question: Optional[str] = None,
        reversal_probability: float = 0.35,
        reading_style: Literal["psychological", "spiritual", "practical", "combined"] = "combined",
        custom_positions: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """
        Perform a complete tarot reading.

        Args:
            spread_id: Spread format ID.
            question: Optional question or focus for the reading.
            reversal_probability: Probability each card is reversed (0.0–1.0).
            reading_style: Interpretive lens — psychological, spiritual, practical, or combined.
            custom_positions: Position labels when spread_id='custom'.

        Returns:
            {"success": True, "data": ReadingContext} or error dict.
            ReadingContext includes system_prompt_injection ready for LLM use.
        """
        return self.call_tool("read_spread", {
            "spread_id": spread_id,
            "question": question,
            "reversal_probability": reversal_probability,
            "reading_style": reading_style,
            "custom_positions": custom_positions,
        })
