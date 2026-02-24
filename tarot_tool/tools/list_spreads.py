"""OpenClaw Tool: list_spread_formats."""
from __future__ import annotations

from typing import Any

from tarot_tool.spreads.registry import list_spreads

TOOL_DEFINITION = {
    "name": "list_spread_formats",
    "description": "List all available tarot spread formats with position descriptions.",
    "input_schema": {
        "type": "object",
        "properties": {
            "include_positions": {
                "type": "boolean",
                "description": "Include per-position labels and guidance in the response.",
                "default": True,
            },
        },
        "required": [],
    },
}


def list_spread_formats(include_positions: bool = True) -> list[dict]:
    """
    Return all registered spread formats.

    Args:
        include_positions: If True, include position details (label + guidance).

    Returns:
        List of dicts describing each spread format.
    """
    spreads = list_spreads()
    result: list[dict] = []

    for spread in spreads:
        entry: dict = {
            "id": spread.id,
            "name": spread.name,
            "description": spread.description,
            "card_count": spread.min_cards,
        }
        if include_positions:
            entry["positions"] = [
                {"index": p.index, "label": p.label, "guidance": p.guidance}
                for p in spread.positions
            ]
        result.append(entry)

    # Always include custom spread entry
    result.append({
        "id": "custom",
        "name": "Custom Spread",
        "description": "A dynamic spread with user-defined positions. Pass custom_positions list.",
        "card_count": "variable",
        **({"positions": []} if include_positions else {}),
    })

    return result


def tool_handler(params: dict[str, Any]) -> dict[str, Any]:
    """
    OpenClaw-compatible handler for list_spread_formats.

    Args:
        params: Dict with optional key 'include_positions' (bool).

    Returns:
        {"success": True, "data": [...]} or {"success": False, "error": "...", "error_type": "..."}
    """
    try:
        result = list_spread_formats(
            include_positions=bool(params.get("include_positions", True)),
        )
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e), "error_type": type(e).__name__}
