"""User-facing command-line interface for tarot-tool."""
from __future__ import annotations

import argparse
import json
import sys
from typing import Optional

from tarot_tool import __version__
from tarot_tool.server import call_tool, get_tool_definitions
from tarot_tool.spreads.registry import list_spreads

# ── Formatting helpers ─────────────────────────────────────────────────────────

_WIDTH = 60
_SEP = "─" * _WIDTH
_THICK = "═" * _WIDTH


def _header(title: str) -> str:
    padded = f"  {title.upper()}  "
    side = (_WIDTH - len(padded)) // 2
    return f"\n{'═' * side}{padded}{'═' * (_WIDTH - side - len(padded))}\n"


def _section(title: str) -> str:
    return f"\n{title}\n{'─' * len(title)}"


def _keywords(kws: list[str]) -> str:
    return "  · ".join(kws)


# ── Command: tarot spreads ─────────────────────────────────────────────────────

def cmd_spreads(as_json: bool = False) -> int:
    """List all available spread formats."""
    result = call_tool("list_spread_formats", {"include_positions": False})
    if not result["success"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps(result["data"], indent=2))
        return 0

    spreads = result["data"]
    print(_header("Available Spreads"))
    print(f"  {'ID':<18} {'Name':<26} {'Cards'}")
    print(f"  {'─'*18} {'─'*26} {'─'*5}")
    for s in spreads:
        count = str(s["card_count"])
        print(f"  {s['id']:<18} {s['name']:<26} {count}")
    print()
    return 0


# ── Command: tarot read ────────────────────────────────────────────────────────

def cmd_read(
    spread_id: str,
    question: Optional[str] = None,
    style: str = "combined",
    positions: Optional[str] = None,
    reversal: float = 0.35,
    as_json: bool = False,
) -> int:
    """Perform a full tarot reading."""
    params: dict = {
        "spread_id": spread_id,
        "reading_style": style,
        "reversal_probability": reversal,
    }
    if question:
        params["question"] = question
    if positions:
        params["custom_positions"] = [p.strip() for p in positions.split(",")]

    result = call_tool("read_spread", params)
    if not result["success"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps(result["data"], indent=2))
        return 0

    data = result["data"]
    _print_reading(data)
    return 0


def _print_reading(data: dict) -> None:
    print(_header(f"{data['spread_name']} Reading"))

    if data.get("question"):
        print(f"  Question : {data['question']}")
    print(f"  Style    : {data['reading_style'].title()}")
    print(f"  Date     : {data['reading_timestamp'][:10]}")
    print()

    for card in data["drawn_cards"]:
        c = card["card"]
        orientation = "reversed" if card["is_reversed"] else "upright"
        rev_marker = "  ★ REVERSED" if card["is_reversed"] else ""
        print(f"  {card['position'] + 1}. {card['position_label']}")
        print(f"     {c['name']}{rev_marker}")
        print(f"     Keywords : {_keywords(card['active_keywords'][:5])}")
        print(f"     Meaning  : {card['active_meaning'][:120].rstrip()}...")
        print()

    print(_SEP)
    elems = data.get("element_distribution", {})
    if elems:
        elem_str = "  ·  ".join(f"{k}: {v}" for k, v in sorted(elems.items()))
        print(f"  Elements : {elem_str}")
    if data.get("dominant_suit"):
        print(f"  Dominant : {data['dominant_suit'].replace('_', ' ').title()}")
    if data.get("thematic_summary"):
        print(f"  Theme    : {data['thematic_summary']}")
    print()

    if data.get("numerology_notes"):
        print("  Numerology:")
        for note in data["numerology_notes"]:
            print(f"    • {note}")
        print()

    print(_SEP)
    print("  LLM Prompt Injection")
    print(_SEP)
    for line in data["system_prompt_injection"].splitlines():
        print(f"  {line}")
    print()


# ── Command: tarot draw ────────────────────────────────────────────────────────

def cmd_draw(
    spread_id: str,
    question: Optional[str] = None,
    positions: Optional[str] = None,
    reversal: float = 0.35,
    as_json: bool = False,
) -> int:
    """Draw cards for a spread and show a concise card list."""
    params: dict = {
        "spread_id": spread_id,
        "reversal_probability": reversal,
    }
    if question:
        params["question"] = question
    if positions:
        params["custom_positions"] = [p.strip() for p in positions.split(",")]

    result = call_tool("draw_tarot_cards", params)
    if not result["success"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps(result["data"], indent=2))
        return 0

    data = result["data"]
    spread_name = data["spread"]["name"]
    print(_header(f"{spread_name} — Card Draw"))
    if data.get("question"):
        print(f"  Question: {data['question']}\n")

    for card in data["drawn_cards"]:
        c = card["card"]
        rev = "  (reversed)" if card["is_reversed"] else ""
        print(f"  {card['position'] + 1}. {card['position_label']}")
        print(f"     {c['name']}{rev}")
        print(f"     {_keywords(card['active_keywords'][:4])}")
        print()
    return 0


# ── Command: tarot meaning ─────────────────────────────────────────────────────

def cmd_meaning(
    card_name: str,
    orientation: str = "both",
    as_json: bool = False,
) -> int:
    """Look up a card's meaning."""
    result = call_tool("get_card_meaning", {"card_name": card_name, "orientation": orientation})
    if not result["success"]:
        print(f"Error: {result['error']}", file=sys.stderr)
        return 1

    if as_json:
        print(json.dumps(result["data"], indent=2))
        return 0

    data = result["data"]
    _print_meaning(data, orientation)
    return 0


def _print_meaning(data: dict, orientation: str) -> None:
    suit = data.get("suit", "").replace("_", " ").title()
    elem = data.get("element") or "—"
    astro = data.get("astrology") or "—"
    num = data.get("numerology")
    num_str = str(num) if num is not None else "—"

    print(_header(data["name"]))
    print(f"  Arcana     : {data.get('arcana', '').title()}")
    print(f"  Suit       : {suit}")
    print(f"  Element    : {elem}")
    print(f"  Astrology  : {astro}")
    print(f"  Numerology : {num_str}")
    print()

    if orientation in ("upright", "both") and "keywords_upright" in data:
        print(_section("Upright"))
        print(f"  Keywords : {_keywords(data['keywords_upright'])}")
        print(f"\n  {data['meaning_upright']}\n")

    if orientation in ("reversed", "both") and "keywords_reversed" in data:
        print(_section("Reversed"))
        print(f"  Keywords : {_keywords(data['keywords_reversed'])}")
        print(f"\n  {data['meaning_reversed']}\n")


# ── Argument parser ────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tarot",
        description="Tarot card readings from the command line.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  tarot spreads\n"
            "  tarot read --spread celtic_cross --question \"What do I need to know?\"\n"
            "  tarot read --spread three_card --style psychological\n"
            "  tarot read --spread custom --positions \"Mind,Body,Spirit\"\n"
            "  tarot draw --spread horseshoe\n"
            "  tarot meaning \"The Tower\"\n"
            "  tarot meaning \"Queen of Cups\" --orientation upright\n"
        ),
    )
    parser.add_argument("--version", action="version", version=f"tarot-tool {__version__}")

    sub = parser.add_subparsers(dest="command", metavar="<command>")

    # spreads
    sp = sub.add_parser("spreads", help="List all available spread formats")
    sp.add_argument("--json", action="store_true", help="Output raw JSON")

    # read
    rp = sub.add_parser("read", help="Perform a full tarot reading")
    rp.add_argument("--spread", "-s", required=True, metavar="ID",
                    help="Spread ID (see: tarot spreads)")
    rp.add_argument("--question", "-q", metavar="TEXT",
                    help="Your question for the reading")
    rp.add_argument("--style", choices=["psychological", "spiritual", "practical", "combined"],
                    default="combined", metavar="STYLE",
                    help="Reading style: psychological | spiritual | practical | combined  (default: combined)")
    rp.add_argument("--positions", metavar="\"A,B,C\"",
                    help="Comma-separated position labels (required for --spread custom)")
    rp.add_argument("--reversal", type=float, default=0.35, metavar="PROB",
                    help="Reversal probability 0.0–1.0  (default: 0.35)")
    rp.add_argument("--json", action="store_true", help="Output raw JSON")

    # draw
    dp = sub.add_parser("draw", help="Draw cards for a spread (no interpretation)")
    dp.add_argument("--spread", "-s", required=True, metavar="ID",
                    help="Spread ID (see: tarot spreads)")
    dp.add_argument("--question", "-q", metavar="TEXT",
                    help="Optional question for context")
    dp.add_argument("--positions", metavar="\"A,B,C\"",
                    help="Comma-separated position labels (required for --spread custom)")
    dp.add_argument("--reversal", type=float, default=0.35, metavar="PROB",
                    help="Reversal probability 0.0–1.0  (default: 0.35)")
    dp.add_argument("--json", action="store_true", help="Output raw JSON")

    # meaning
    mp = sub.add_parser("meaning", help="Look up a card's meaning")
    mp.add_argument("card", nargs="+", metavar="CARD",
                    help="Card name (e.g. \"The Tower\" or \"Queen of Cups\")")
    mp.add_argument("--orientation", "-o",
                    choices=["upright", "reversed", "both"], default="both",
                    help="Which meaning to show  (default: both)")
    mp.add_argument("--json", action="store_true", help="Output raw JSON")

    return parser


# ── Entry point ────────────────────────────────────────────────────────────────

def main() -> None:
    """Entry point for the `tarot` CLI command."""
    parser = _build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    as_json = getattr(args, "json", False)

    if args.command == "spreads":
        sys.exit(cmd_spreads(as_json=as_json))

    elif args.command == "read":
        sys.exit(cmd_read(
            spread_id=args.spread,
            question=getattr(args, "question", None),
            style=args.style,
            positions=getattr(args, "positions", None),
            reversal=args.reversal,
            as_json=as_json,
        ))

    elif args.command == "draw":
        sys.exit(cmd_draw(
            spread_id=args.spread,
            question=getattr(args, "question", None),
            positions=getattr(args, "positions", None),
            reversal=args.reversal,
            as_json=as_json,
        ))

    elif args.command == "meaning":
        card_name = " ".join(args.card)
        sys.exit(cmd_meaning(
            card_name=card_name,
            orientation=args.orientation,
            as_json=as_json,
        ))

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
