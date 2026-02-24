"""CLI smoke tests — verify all commands run and produce valid output."""
from __future__ import annotations

import json
import sys
from io import StringIO
from unittest.mock import patch

import pytest

from tarot_tool.cli import cmd_draw, cmd_meaning, cmd_read, cmd_spreads


class TestCmdSpreads:
    def test_spreads_exits_zero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_spreads()
        assert code == 0

    def test_spreads_lists_all_ids(self, capsys: pytest.CaptureFixture) -> None:
        cmd_spreads()
        out = capsys.readouterr().out
        for sid in ["single", "three_card", "celtic_cross", "horseshoe",
                    "relationship", "year_ahead", "chakra", "decision", "custom"]:
            assert sid in out

    def test_spreads_json_is_parseable(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_spreads(as_json=True)
        assert code == 0
        data = json.loads(capsys.readouterr().out)
        assert isinstance(data, list)
        assert len(data) == 9


class TestCmdRead:
    def test_read_single_exits_zero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_read("single")
        assert code == 0

    def test_read_three_card_shows_three_cards(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("three_card")
        out = capsys.readouterr().out
        # positions 1, 2, 3 should appear
        assert "1. Past" in out
        assert "2. Present" in out
        assert "3. Future" in out

    def test_read_with_question(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("single", question="What do I need?")
        out = capsys.readouterr().out
        assert "What do I need?" in out

    def test_read_with_style(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("single", style="spiritual")
        out = capsys.readouterr().out
        assert "spiritual" in out.lower()

    def test_read_celtic_cross_shows_ten_cards(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("celtic_cross")
        out = capsys.readouterr().out
        assert "10." in out

    def test_read_custom_spread(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_read("custom", positions="Mind,Body,Spirit")
        assert code == 0
        out = capsys.readouterr().out
        assert "Mind" in out
        assert "Body" in out
        assert "Spirit" in out

    def test_read_bad_spread_exits_nonzero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_read("nonexistent_spread")
        assert code != 0

    def test_read_json_flag(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_read("single", as_json=True)
        assert code == 0
        data = json.loads(capsys.readouterr().out)
        assert "drawn_cards" in data
        assert "system_prompt_injection" in data

    def test_read_reversal_zero(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("three_card", reversal=0.0)
        out = capsys.readouterr().out
        assert "reversed" not in out.lower()

    def test_read_reversal_one(self, capsys: pytest.CaptureFixture) -> None:
        cmd_read("three_card", reversal=1.0)
        out = capsys.readouterr().out
        assert "reversed" in out.lower()


class TestCmdDraw:
    def test_draw_single_exits_zero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_draw("single")
        assert code == 0

    def test_draw_shows_card_count(self, capsys: pytest.CaptureFixture) -> None:
        cmd_draw("three_card")
        out = capsys.readouterr().out
        assert "1." in out
        assert "2." in out
        assert "3." in out

    def test_draw_custom(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_draw("custom", positions="Alpha,Beta")
        assert code == 0
        out = capsys.readouterr().out
        assert "Alpha" in out
        assert "Beta" in out

    def test_draw_bad_spread_exits_nonzero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_draw("bogus")
        assert code != 0

    def test_draw_json_flag(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_draw("single", as_json=True)
        assert code == 0
        data = json.loads(capsys.readouterr().out)
        assert "drawn_cards" in data


class TestCmdMeaning:
    def test_meaning_major_arcana(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_meaning("The Fool")
        assert code == 0
        out = capsys.readouterr().out
        assert "THE FOOL" in out

    def test_meaning_upright_only(self, capsys: pytest.CaptureFixture) -> None:
        cmd_meaning("The Moon", orientation="upright")
        out = capsys.readouterr().out
        assert "Upright" in out
        assert "Reversed" not in out

    def test_meaning_reversed_only(self, capsys: pytest.CaptureFixture) -> None:
        cmd_meaning("The Moon", orientation="reversed")
        out = capsys.readouterr().out
        assert "Reversed" in out
        assert "Upright" not in out

    def test_meaning_minor_arcana(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_meaning("Ace of Wands")
        assert code == 0
        out = capsys.readouterr().out
        assert "ACE OF WANDS" in out

    def test_meaning_unknown_card_exits_nonzero(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_meaning("The Nonexistent")
        assert code != 0

    def test_meaning_json_flag(self, capsys: pytest.CaptureFixture) -> None:
        code = cmd_meaning("The Star", as_json=True)
        assert code == 0
        data = json.loads(capsys.readouterr().out)
        assert data["name"] == "The Star"

    def test_meaning_shows_element(self, capsys: pytest.CaptureFixture) -> None:
        cmd_meaning("The Tower")
        out = capsys.readouterr().out
        assert "Fire" in out

    def test_meaning_shows_keywords(self, capsys: pytest.CaptureFixture) -> None:
        cmd_meaning("The Star")
        out = capsys.readouterr().out
        assert "Keywords" in out


class TestMainEntryPoint:
    def test_no_args_prints_help(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot"]):
            with pytest.raises(SystemExit) as exc:
                main()
        assert exc.value.code == 0

    def test_version_flag(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot", "--version"]):
            with pytest.raises(SystemExit):
                main()

    def test_spreads_command(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot", "spreads"]):
            with pytest.raises(SystemExit) as exc:
                main()
        assert exc.value.code == 0

    def test_read_command(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot", "read", "--spread", "single"]):
            with pytest.raises(SystemExit) as exc:
                main()
        assert exc.value.code == 0

    def test_draw_command(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot", "draw", "--spread", "single"]):
            with pytest.raises(SystemExit) as exc:
                main()
        assert exc.value.code == 0

    def test_meaning_command(self, capsys: pytest.CaptureFixture) -> None:
        from tarot_tool.cli import main
        with patch("sys.argv", ["tarot", "meaning", "The", "Fool"]):
            with pytest.raises(SystemExit) as exc:
                main()
        assert exc.value.code == 0
