<div align="center">

# tarot-tool

**Production-grade Python tarot system for [OpenClaw](https://openclaw.ai) MCP integration**

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-127%20passing-brightgreen?style=flat-square)]()
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen?style=flat-square)]()
[![Pydantic v2](https://img.shields.io/badge/pydantic-v2-red?style=flat-square)](https://docs.pydantic.dev/latest/)

Give your AI agent the ability to draw tarot cards, look up rich card meanings, and deliver fully structured reading contexts — with cryptographically secure randomness and zero external dependencies.

</div>

---

## Highlights

| | |
|---|---|
| **78-card deck** | Complete Rider-Waite-Smith corpus — all Major and Minor Arcana with full upright/reversed meanings, keywords, elements, and astrology |
| **9 spread formats** | Single, Three-Card, Celtic Cross, Horseshoe, Relationship, Year Ahead, Chakra, Decision Making, and dynamic Custom spreads |
| **CSPRNG shuffle** | `secrets.SystemRandom()` + Fisher-Yates — cryptographically secure, no duplicates |
| **LLM-ready output** | `ReadingContext.system_prompt_injection` is a complete, self-contained system prompt with full card meanings, thematic context, numerology notes, and narrative guidance — ready to prepend to any LLM call. `SpreadResult.interpretation_prompt` provides the same for raw draws. |
| **OpenClaw-native** | 4 registered tools with `input_schema` definitions, `tool_handler()` wrappers, and a stdio skill server |

---

## Requirements

- Python >= 3.11
- `pydantic >= 2.0`

---

## Installation

```bash
git clone https://github.com/aphirak/tarot-tool.git
cd tarot-tool
pip install -e ".[dev]"
```

---

## OpenClaw Setup

### 1. Register the skill

Add the manifest path to your OpenClaw config:

```toml
[[skills]]
manifest = "/path/to/tarot-tool/tarot_tool.toml"
```

### 2. Protocol

The skill runs as a subprocess and speaks newline-delimited JSON over stdio:

```bash
# OpenClaw launches:
tarot-tool

# Sends over stdin:
{"id": "1", "method": "list_tools"}
{"id": "2", "method": "call_tool", "params": {"name": "read_spread", "input": {"spread_id": "celtic_cross", "question": "What do I need to know?"}}}

# Skill responds over stdout:
{"id": "1", "result": [ ...tool definitions... ]}
{"id": "2", "result": {"success": true, "data": { ...ReadingContext... }}}
```

### 3. Available tools

| Tool | Description |
|---|---|
| `draw_tarot_cards` | Draw cards for a spread — returns full card metadata and orientations |
| `get_card_meaning` | Look up upright/reversed meanings for any card by name |
| `list_spread_formats` | Enumerate all spread formats with per-position descriptions |
| `read_spread` | Full reading — draws cards and builds an LLM-ready `ReadingContext` |

---

## Tool Reference

### `draw_tarot_cards`

```json
{
  "spread_id": "celtic_cross",
  "question": "What do I need to know?",
  "reversal_probability": 0.35,
  "custom_positions": ["Mind", "Body", "Spirit"]
}
```

Returns a `SpreadResult` with drawn cards, positions, orientations, active meanings, and an `interpretation_prompt` string — a ready-to-use LLM context built from the full card meanings and positional labels.

---

### `get_card_meaning`

```json
{
  "card_name": "The Tower",
  "orientation": "both"
}
```

`orientation` accepts `"upright"`, `"reversed"`, or `"both"`. Supports partial, case-insensitive name matching.

---

### `list_spread_formats`

```json
{
  "include_positions": true
}
```

Returns all 9 spread definitions including per-position labels and guidance text.

---

### `read_spread`

```json
{
  "spread_id": "three_card",
  "question": "What path should I take?",
  "reversal_probability": 0.35,
  "reading_style": "psychological"
}
```

`reading_style` accepts `"psychological"`, `"spiritual"`, `"practical"`, or `"combined"`.

Returns a `ReadingContext` — see below.

---

## ReadingContext

`read_spread` returns a fully assembled payload for LLM interpretation:

```json
{
  "spread_name": "Past / Present / Future",
  "question": "What path should I take?",
  "reading_style": "psychological",
  "drawn_cards": [ "...DrawnCard objects..." ],
  "spread_narrative_hints": [ "...per-position guidance strings..." ],
  "thematic_summary": "Minor Arcana predominate, focusing on practical circumstances. The dominant energy is cups, highlighting emotion, intuition, and relationships.",
  "element_distribution": {"Water": 2, "Fire": 1},
  "numerology_notes": ["The Hermit (numerology 9): completion, wisdom, and humanitarianism"],
  "dominant_suit": "cups",
  "reading_timestamp": "2026-02-24T10:30:00+00:00",
  "system_prompt_injection": "..."
}
```

`system_prompt_injection` is a complete, self-contained system prompt ready to prepend to any LLM call. It includes:

```
You are an expert tarot reader performing a psychological reading.

## Spread: Past / Present / Future
## Question: "What path should I take?"

## Cards Drawn

### Position 1: Past
Card: The Hermit (upright)
Keywords: solitude, introspection, inner guidance, soul-searching, wisdom
Meaning: The Hermit suggests a period of withdrawal and inner reflection...

### Position 2: Present
Card: Five of Cups (reversed)
Keywords: acceptance, moving on, finding peace, healing, forgiveness
Meaning: The reversed Five of Cups indicates a turning point...

### Position 3: Future
Card: Ace of Wands (upright)
Keywords: inspiration, new beginnings, creative spark, potential, enthusiasm
Meaning: The Ace of Wands heralds a burst of creative energy...

## Thematic Context
Minor Arcana predominate, focusing on practical day-to-day circumstances.
The dominant energy is cups, highlighting emotion, intuition, and relationships.
Element distribution: Fire: 1, Water: 2
The Hermit (numerology 9): completion, wisdom, and humanitarianism

## Spread Narrative Guidance
- Position 1 (Past): The Hermit (upright) — reflect on the foundation of solitude...
- Position 2 (Present): Five of Cups (reversed) — examine current emotional recovery...
- Position 3 (Future): Ace of Wands (upright) — embrace the creative spark ahead...

## Your Task
Provide the seeker with a cohesive interpretation. Address each card in its positional
context, weave the cards into a unified narrative, and note any elemental or thematic
patterns across the spread.
```

## SpreadResult

`draw_tarot_cards` returns a `SpreadResult` that also carries an `interpretation_prompt` — the same structured format as above but without the reading-style framing and thematic analysis. Use it when you want to interpret a raw draw without calling `read_spread`.

```python
result = draw_tarot_cards("three_card", question="Where am I headed?")
print(result.interpretation_prompt)  # full card meanings + positional context
```

---

## Spreads

| ID | Name | Cards |
|---|---|:---:|
| `single` | Single Card | 1 |
| `three_card` | Past / Present / Future | 3 |
| `celtic_cross` | Celtic Cross | 10 |
| `horseshoe` | Horseshoe | 7 |
| `relationship` | Relationship | 6 |
| `year_ahead` | Year Ahead | 13 |
| `chakra` | Chakra Spread | 7 |
| `decision` | Decision Making | 5 |
| `custom` | Custom (dynamic) | n |

---

## Python Library Usage

```python
from tarot_tool.tools import read_spread, draw_tarot_cards, get_card_meaning

# Full LLM reading
ctx = read_spread("celtic_cross", question="What do I need to know?", reading_style="spiritual")
print(ctx.system_prompt_injection)

# Draw cards only — interpretation_prompt gives full context for the raw draw
result = draw_tarot_cards("three_card", question="Where am I headed?")
for card in result.drawn_cards:
    print(f"[{card.position_label}] {card.card.name} {'(R)' if card.is_reversed else ''}")
print(result.interpretation_prompt)  # full card meanings + positional context

# Look up a card
info = get_card_meaning("The Moon", orientation="both")
print(info["meaning_upright"])
```

### Programmatic tool calls (OpenClaw style)

```python
from tarot_tool.server import call_tool, get_tool_definitions

tools = get_tool_definitions()

result = call_tool("read_spread", {"spread_id": "horseshoe", "reading_style": "combined"})
if result["success"]:
    print(result["data"]["system_prompt_injection"])
else:
    print("Error:", result["error"])
```

---

## Project Structure

```
tarot-tool/
├── tarot_tool.toml              # OpenClaw skill manifest
├── pyproject.toml               # Python packaging + dev tools
└── tarot_tool/
    ├── server.py                # OpenClaw stdio skill server
    ├── cli.py                   # User CLI: tarot spreads/read/draw/meaning
    ├── models/
    │   ├── card.py              # TarotCard, DrawnCard, Suit
    │   ├── spread.py            # SpreadDefinition, SpreadResult
    │   └── reading.py           # ReadingContext
    ├── cards/
    │   ├── major_arcana.py      # 22 Major Arcana (full RWS corpus)
    │   ├── minor_arcana.py      # 56 Minor Arcana (all four suits)
    │   ├── deck.py              # get_deck() — cached 78-card list
    │   └── meanings.py          # Name-indexed meaning lookup
    ├── engine/
    │   ├── rng.py               # CSPRNG draw + Fisher-Yates shuffle
    │   ├── shuffle.py           # shuffle_deck()
    │   └── context_builder.py   # ReadingContext assembly
    ├── spreads/
    │   ├── registry.py          # get_spread(), list_spreads()
    │   ├── single.py
    │   ├── three_card.py
    │   ├── celtic_cross.py
    │   ├── horseshoe.py
    │   ├── relationship.py
    │   ├── year_ahead.py
    │   ├── chakra.py
    │   ├── decision.py
    │   └── custom.py
    ├── tools/
    │   ├── draw_cards.py        # draw_tarot_cards + tool_handler()
    │   ├── get_meaning.py       # get_card_meaning + tool_handler()
    │   ├── list_spreads.py      # list_spread_formats + tool_handler()
    │   └── read_spread.py       # read_spread + tool_handler()
    └── tests/
        ├── test_deck.py         # 14 tests
        ├── test_rng.py          # 13 tests
        ├── test_spreads.py      # 10 tests
        ├── test_context.py      # 31 tests
        ├── test_handlers.py     # 27 tests
        └── test_cli.py          # 32 tests
```

---

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run all tests
python3.11 -m pytest tarot_tool/tests/ -v

# Coverage report
python3.11 -m pytest tarot_tool/tests/ --cov=tarot_tool --cov-report=term-missing

# Lint / format / type check
ruff check tarot_tool/
black tarot_tool/
mypy tarot_tool/
```

**127 tests · 95% coverage**

---

## Design Notes

- **No shared mutable state** — all tool functions are pure with respect to side effects; safe for concurrent calls
- **No runtime I/O** — all 78 cards are embedded Python constants; no disk reads, no network calls
- **CSPRNG only** — `secrets.SystemRandom()` for all production draws; seeded `random.Random` exists only for deterministic testing
- **Never raises in handlers** — every `tool_handler()` catches all exceptions and returns `{"success": false, "error": "..."}` instead

---

## License

MIT — Aphirak JANSANG
