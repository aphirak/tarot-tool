"""Tests for OpenClaw tool_handler() interface and server dispatch."""
from __future__ import annotations

import pytest

from tarot_tool.server import call_tool, get_tool_definitions
from tarot_tool.tools import TOOL_HANDLERS


class TestToolDefinitions:
    def test_all_four_definitions_present(self) -> None:
        defs = get_tool_definitions()
        names = {d["name"] for d in defs}
        assert names == {"draw_tarot_cards", "get_card_meaning", "list_spread_formats", "read_spread"}

    def test_definitions_use_input_schema_not_parameters(self) -> None:
        for defn in get_tool_definitions():
            assert "input_schema" in defn, f"{defn['name']} uses 'parameters' instead of 'input_schema'"
            assert "parameters" not in defn

    def test_all_definitions_have_required_fields(self) -> None:
        for defn in get_tool_definitions():
            assert "name" in defn
            assert "description" in defn
            assert "input_schema" in defn


class TestToolHandlers:
    def test_all_four_handlers_registered(self) -> None:
        assert set(TOOL_HANDLERS.keys()) == {
            "draw_tarot_cards", "get_card_meaning", "list_spread_formats", "read_spread"
        }

    # draw_tarot_cards
    def test_draw_handler_success(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({"spread_id": "single"})
        assert result["success"] is True
        assert "data" in result
        data = result["data"]
        assert "drawn_cards" in data
        assert len(data["drawn_cards"]) == 1

    def test_draw_handler_with_question(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({
            "spread_id": "three_card",
            "question": "What should I focus on?",
        })
        assert result["success"] is True
        assert result["data"]["question"] == "What should I focus on?"

    def test_draw_handler_has_interpretation_prompt(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({"spread_id": "three_card"})
        assert result["success"] is True
        data = result["data"]
        assert "interpretation_prompt" in data
        assert data["interpretation_prompt"].strip(), "interpretation_prompt is empty"

    def test_draw_handler_interpretation_prompt_contains_card_names(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({"spread_id": "three_card"})
        assert result["success"] is True
        prompt = result["data"]["interpretation_prompt"]
        for dc in result["data"]["drawn_cards"]:
            assert dc["card"]["name"] in prompt, (
                f"Card name {dc['card']['name']!r} missing from interpretation_prompt"
            )

    def test_draw_handler_interpretation_prompt_contains_position_labels(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({"spread_id": "three_card"})
        assert result["success"] is True
        prompt = result["data"]["interpretation_prompt"]
        for dc in result["data"]["drawn_cards"]:
            assert dc["position_label"] in prompt, (
                f"Position label {dc['position_label']!r} missing from interpretation_prompt"
            )

    def test_draw_handler_bad_spread_returns_error(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({"spread_id": "nonexistent"})
        assert result["success"] is False
        assert "error" in result
        assert "error_type" in result

    def test_draw_handler_missing_required_param(self) -> None:
        result = TOOL_HANDLERS["draw_tarot_cards"]({})
        assert result["success"] is False

    # get_card_meaning
    def test_meaning_handler_success(self) -> None:
        result = TOOL_HANDLERS["get_card_meaning"]({"card_name": "The Fool"})
        assert result["success"] is True
        assert result["data"]["name"] == "The Fool"

    def test_meaning_handler_upright_only(self) -> None:
        result = TOOL_HANDLERS["get_card_meaning"]({
            "card_name": "The Moon",
            "orientation": "upright",
        })
        assert result["success"] is True
        assert "meaning_upright" in result["data"]
        assert "meaning_reversed" not in result["data"]

    def test_meaning_handler_unknown_card(self) -> None:
        result = TOOL_HANDLERS["get_card_meaning"]({"card_name": "Card of Doom"})
        assert result["success"] is False
        assert result["error_type"] == "LookupError"

    def test_meaning_handler_bad_orientation(self) -> None:
        result = TOOL_HANDLERS["get_card_meaning"]({
            "card_name": "The Sun",
            "orientation": "sideways",
        })
        assert result["success"] is False
        assert result["error_type"] == "ValueError"

    # list_spread_formats
    def test_list_handler_success(self) -> None:
        result = TOOL_HANDLERS["list_spread_formats"]({})
        assert result["success"] is True
        assert isinstance(result["data"], list)
        assert len(result["data"]) == 9

    def test_list_handler_without_positions(self) -> None:
        result = TOOL_HANDLERS["list_spread_formats"]({"include_positions": False})
        assert result["success"] is True
        for spread in result["data"]:
            assert "positions" not in spread

    # read_spread
    def test_read_handler_success(self) -> None:
        result = TOOL_HANDLERS["read_spread"]({"spread_id": "single"})
        assert result["success"] is True
        data = result["data"]
        assert "system_prompt_injection" in data
        assert data["system_prompt_injection"].strip()

    def test_read_handler_with_style(self) -> None:
        result = TOOL_HANDLERS["read_spread"]({
            "spread_id": "three_card",
            "reading_style": "spiritual",
        })
        assert result["success"] is True
        assert "spiritual" in result["data"]["system_prompt_injection"]

    def test_read_handler_bad_style_returns_error(self) -> None:
        result = TOOL_HANDLERS["read_spread"]({
            "spread_id": "single",
            "reading_style": "mystical",
        })
        assert result["success"] is False
        assert result["error_type"] == "ValueError"

    def test_read_handler_custom_spread(self) -> None:
        result = TOOL_HANDLERS["read_spread"]({
            "spread_id": "custom",
            "custom_positions": ["Past", "Present", "Future"],
        })
        assert result["success"] is True
        assert len(result["data"]["drawn_cards"]) == 3

    def test_handler_data_is_json_serialisable(self) -> None:
        """Ensure all handler outputs can be round-tripped through JSON."""
        import json
        for name, handler in TOOL_HANDLERS.items():
            params = {"spread_id": "single"} if name != "get_card_meaning" else {"card_name": "The Star"}
            result = handler(params)
            assert result["success"] is True
            serialised = json.dumps(result)  # must not raise
            assert serialised


class TestCallTool:
    def test_call_tool_dispatches_correctly(self) -> None:
        result = call_tool("list_spread_formats", {})
        assert result["success"] is True

    def test_call_tool_unknown_name_returns_error(self) -> None:
        result = call_tool("nonexistent_tool", {})
        assert result["success"] is False
        assert "Unknown tool" in result["error"]
        assert result["error_type"] == "KeyError"

    def test_call_tool_draw(self) -> None:
        result = call_tool("draw_tarot_cards", {"spread_id": "celtic_cross"})
        assert result["success"] is True
        assert len(result["data"]["drawn_cards"]) == 10

    def test_call_tool_read(self) -> None:
        result = call_tool("read_spread", {"spread_id": "horseshoe"})
        assert result["success"] is True
        assert len(result["data"]["drawn_cards"]) == 7

    def test_call_tool_meaning(self) -> None:
        result = call_tool("get_card_meaning", {"card_name": "Death"})
        assert result["success"] is True
        assert result["data"]["name"] == "Death"
