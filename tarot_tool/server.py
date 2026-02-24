"""OpenClaw skill server entry point for tarot_tool."""
from __future__ import annotations

import json
import sys
from typing import Any

from tarot_tool.tools.draw_cards import TOOL_DEFINITION as _DRAW_DEF
from tarot_tool.tools.draw_cards import tool_handler as _draw_handler
from tarot_tool.tools.get_meaning import TOOL_DEFINITION as _MEANING_DEF
from tarot_tool.tools.get_meaning import tool_handler as _meaning_handler
from tarot_tool.tools.list_spreads import TOOL_DEFINITION as _LIST_DEF
from tarot_tool.tools.list_spreads import tool_handler as _list_handler
from tarot_tool.tools.read_spread import TOOL_DEFINITION as _READ_DEF
from tarot_tool.tools.read_spread import tool_handler as _read_handler

# ── Registry ──────────────────────────────────────────────────────────────────

_DEFINITIONS: list[dict[str, Any]] = [
    _DRAW_DEF,
    _MEANING_DEF,
    _LIST_DEF,
    _READ_DEF,
]

_HANDLERS: dict[str, Any] = {
    "draw_tarot_cards": _draw_handler,
    "get_card_meaning": _meaning_handler,
    "list_spread_formats": _list_handler,
    "read_spread": _read_handler,
}


# ── Public API (called by OpenClaw) ───────────────────────────────────────────

def get_tool_definitions() -> list[dict[str, Any]]:
    """Return all tool definitions in OpenClaw input_schema format."""
    return _DEFINITIONS


def call_tool(name: str, params: dict[str, Any]) -> dict[str, Any]:
    """
    Dispatch a tool call by name.

    Args:
        name: Tool name (e.g. 'draw_tarot_cards').
        params: Raw parameter dict from the OpenClaw agent.

    Returns:
        {"success": True, "data": ...} or {"success": False, "error": ..., "error_type": ...}
    """
    handler = _HANDLERS.get(name)
    if handler is None:
        available = ", ".join(_HANDLERS.keys())
        return {
            "success": False,
            "error": f"Unknown tool '{name}'. Available: {available}",
            "error_type": "KeyError",
        }
    return handler(params)


# ── Stdio loop (OpenClaw subprocess protocol) ─────────────────────────────────

def main() -> None:
    """
    Run the tarot_tool skill as a line-delimited JSON server over stdio.

    OpenClaw sends newline-delimited JSON requests and expects newline-delimited
    JSON responses. Each request has the shape:
        {"id": "...", "method": "call_tool", "params": {"name": "...", "input": {...}}}
    or:
        {"id": "...", "method": "list_tools"}

    Each response has the shape:
        {"id": "...", "result": ...}
    or:
        {"id": "...", "error": {"message": "..."}}
    """
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        try:
            request: dict[str, Any] = json.loads(line)
        except json.JSONDecodeError as exc:
            _write({"id": None, "error": {"message": f"Invalid JSON: {exc}"}})
            continue

        req_id = request.get("id")
        method = request.get("method", "")

        try:
            if method == "list_tools":
                _write({"id": req_id, "result": get_tool_definitions()})

            elif method == "call_tool":
                tool_params = request.get("params", {})
                tool_name = tool_params.get("name", "")
                tool_input = tool_params.get("input", {})
                result = call_tool(tool_name, tool_input)
                _write({"id": req_id, "result": result})

            else:
                _write({
                    "id": req_id,
                    "error": {"message": f"Unknown method '{method}'. Use 'list_tools' or 'call_tool'."},
                })

        except Exception as exc:  # noqa: BLE001
            _write({"id": req_id, "error": {"message": str(exc)}})


def _write(obj: dict[str, Any]) -> None:
    """Write a JSON response line to stdout and flush immediately."""
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
