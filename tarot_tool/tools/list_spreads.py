"""OpenClaw Tool: list_spread_formats."""
from __future__ import annotations

from tarot_tool.spreads.registry import list_spreads

TOOL_DEFINITION = {
    "name": "list_spread_formats",
    "description": "List all available tarot spread formats with position descriptions.",
    "parameters": {
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
