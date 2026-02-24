# CLAUDE.md — Tarot Tool System for OpenClaw

## Project Status

**Fully implemented and tested.** This document reflects the current state of the codebase as of 2026-02-24.

- 78-card Rider-Waite-Smith deck with full meanings
- 9 spread formats
- OpenClaw skill interface — stdio JSON protocol (`server.py`) and Python direct import (`tool.py`)
- `TarotSkill` class for in-process OpenClaw calls without a subprocess
- User-facing CLI (`tarot` command)
- 127 tests, ~95% coverage

---

## Project Structure

```
tarot-tool/
├── tarot_tool.toml              # OpenClaw skill manifest (entry_point + python_skill)
├── pyproject.toml               # Python packaging, dev tools, CLI entry points
├── README.md                    # Developer & OpenClaw integration docs
├── SKILL.md                     # OpenClaw skill integration guide (both modes)
├── User.md                      # End-user CLI guide
├── .gitignore
└── tarot_tool/
    ├── __init__.py              # Package version + TarotSkill export
    ├── server.py                # OpenClaw stdio skill server + call_tool()
    ├── tool.py                  # TarotSkill class — Python direct import mode
    ├── cli.py                   # User CLI: tarot spreads/read/draw/meaning
    ├── models/
    │   ├── card.py              # TarotCard, DrawnCard, Suit
    │   ├── spread.py            # SpreadDefinition, SpreadResult, PositionDefinition
    │   └── reading.py           # ReadingContext (LLM payload)
    ├── cards/
    │   ├── major_arcana.py      # 22 Major Arcana (ids 0–21, full RWS corpus)
    │   ├── minor_arcana.py      # 56 Minor Arcana (ids 22–77, all four suits)
    │   ├── deck.py              # get_deck() — lru_cache'd 78-card list
    │   └── meanings.py          # Name-indexed meaning lookup (partial match)
    ├── engine/
    │   ├── rng.py               # CSPRNG draw + Fisher-Yates shuffle
    │   ├── shuffle.py           # shuffle_deck()
    │   └── context_builder.py   # ReadingContext assembly + build_draw_prompt()
    ├── spreads/
    │   ├── registry.py          # get_spread(), list_spreads()
    │   ├── single.py            # 1-card
    │   ├── three_card.py        # Past / Present / Future (3)
    │   ├── celtic_cross.py      # Celtic Cross (10)
    │   ├── horseshoe.py         # Horseshoe (7)
    │   ├── relationship.py      # Relationship (6)
    │   ├── year_ahead.py        # Year Ahead (13)
    │   ├── chakra.py            # Chakra Spread (7)
    │   ├── decision.py          # Decision Making (5)
    │   └── custom.py            # Custom n-position spread
    ├── tools/
    │   ├── __init__.py          # ALL_TOOLS, TOOL_HANDLERS exports
    │   ├── draw_cards.py        # draw_tarot_cards + tool_handler()
    │   ├── get_meaning.py       # get_card_meaning + tool_handler()
    │   ├── list_spreads.py      # list_spread_formats + tool_handler()
    │   └── read_spread.py       # read_spread + tool_handler()
    └── tests/
        ├── test_deck.py         # 14 tests — deck completeness, no duplicates
        ├── test_rng.py          # 13 tests — CSPRNG, seeding, reversal distribution
        ├── test_spreads.py      # 10 tests — registry, custom spread, positions
        ├── test_context.py      # 31 tests — ReadingContext, all tool functions
        ├── test_handlers.py     # 27 tests — tool_handler() shapes, call_tool()
        └── test_cli.py          # 32 tests — all CLI subcommands, --json, error exits
```

---

## CLI Entry Points

Two registered entry points in `pyproject.toml`:

| Command | Module | Purpose |
|---|---|---|
| `tarot` | `tarot_tool.cli:main` | Human-readable CLI for end users |
| `tarot-tool` | `tarot_tool.server:main` | OpenClaw stdio skill server (JSON protocol) |

### User CLI (`tarot`)

```bash
tarot spreads                          # List all spread IDs
tarot read --spread <ID> [OPTIONS]     # Full reading with LLM context
tarot draw --spread <ID> [OPTIONS]     # Draw cards only (no interpretation)
tarot meaning "Card Name" [OPTIONS]    # Card meaning lookup
```

All commands support `--json` for raw JSON output. See `User.md` for complete reference.

### OpenClaw Skill Server (`tarot-tool`)

Runs as a subprocess, communicates via line-delimited JSON over stdio:

```bash
# Input (stdin):
{"id": "1", "method": "list_tools"}
{"id": "2", "method": "call_tool", "params": {"name": "read_spread", "input": {"spread_id": "three_card"}}}

# Output (stdout):
{"id": "1", "result": [...tool definitions...]}
{"id": "2", "result": {"success": true, "data": {...ReadingContext...}}}
```

### OpenClaw Python Skill (`TarotSkill`)

Import and call directly — no subprocess, no JSON serialization:

```python
from tarot_tool.tool import TarotSkill

skill = TarotSkill()
skill.get_tool_definitions()          # list[dict] — all 4 tool schemas
skill.call_tool(name, params)         # generic dispatcher
skill.draw_tarot_cards(spread_id=...) # named method
skill.read_spread(spread_id=...)      # named method
skill.get_card_meaning(card_name=...) # named method
skill.list_spread_formats()           # named method
```

`tarot_tool.toml` declares both modes:
```toml
entry_point  = "tarot_tool.server:main"     # stdio subprocess
python_skill = "tarot_tool.tool:TarotSkill" # Python direct import
```

See `SKILL.md` for the full integration reference.

---

## OpenClaw Tool Definitions

Tools use `input_schema` (not `parameters`). Each tool file exposes:
- `TOOL_DEFINITION: dict` — name, description, input_schema
- `tool_handler(params: dict) -> dict` — returns `{"success": bool, "data"/"error": ...}`

### `draw_tarot_cards`
```json
{
  "name": "draw_tarot_cards",
  "description": "Draw tarot cards for a reading.",
  "input_schema": {
    "type": "object",
    "properties": {
      "spread_id": {"type": "string"},
      "question": {"type": "string"},
      "reversal_probability": {"type": "number", "default": 0.35},
      "custom_positions": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["spread_id"]
  }
}
```

### `get_card_meaning`
```json
{
  "name": "get_card_meaning",
  "description": "Retrieve full meaning, keywords, and metadata for a tarot card.",
  "input_schema": {
    "type": "object",
    "properties": {
      "card_name": {"type": "string"},
      "orientation": {"type": "string", "enum": ["upright", "reversed", "both"]}
    },
    "required": ["card_name"]
  }
}
```

### `list_spread_formats`
```json
{
  "name": "list_spread_formats",
  "description": "List all available tarot spread formats.",
  "input_schema": {
    "type": "object",
    "properties": {
      "include_positions": {"type": "boolean", "default": true}
    }
  }
}
```

### `read_spread`
```json
{
  "name": "read_spread",
  "description": "Perform a complete tarot reading. Returns a ReadingContext for LLM interpretation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "spread_id": {"type": "string"},
      "question": {"type": "string"},
      "reversal_probability": {"type": "number", "default": 0.35},
      "reading_style": {"type": "string", "enum": ["psychological", "spiritual", "practical", "combined"]}
    },
    "required": ["spread_id"]
  }
}
```

---

## Key Data Models

### `TarotCard` (Pydantic v2)
```python
class TarotCard(BaseModel):
    id: int                        # 0–77
    name: str
    suit: Suit                     # Suit enum
    number: Optional[int]
    arcana: str                    # "major" | "minor"
    keywords_upright: list[str]
    keywords_reversed: list[str]
    meaning_upright: str
    meaning_reversed: str
    element: Optional[str]
    astrology: Optional[str]
    numerology: Optional[int]
    image_key: str
```

### `SpreadResult` (draw output)
```python
class SpreadResult(BaseModel):
    spread: SpreadDefinition
    drawn_cards: list[DrawnCard]
    question: Optional[str] = None
    interpretation_prompt: str = ""  # Ready-to-use LLM context for this draw
```

### `ReadingContext` (LLM payload)
```python
class ReadingContext(BaseModel):
    spread_name: str
    question: Optional[str]
    reading_style: str
    drawn_cards: list[DrawnCard]
    spread_narrative_hints: list[str]
    thematic_summary: str
    element_distribution: dict[str, int]
    numerology_notes: list[str]
    dominant_suit: Optional[str]
    reading_timestamp: str          # ISO 8601
    system_prompt_injection: str    # Complete LLM system prompt: full card meanings,
                                    # thematic context, numerology, narrative guidance
```

---

## Spreads

| ID | Name | Cards |
|---|---|---|
| `single` | Single Card | 1 |
| `three_card` | Past / Present / Future | 3 |
| `celtic_cross` | Celtic Cross | 10 |
| `horseshoe` | Horseshoe | 7 |
| `relationship` | Relationship | 6 |
| `year_ahead` | Year Ahead | 13 |
| `chakra` | Chakra Spread | 7 |
| `decision` | Decision Making | 5 |
| `custom` | Custom (dynamic) | n (user-defined) |

---

## RNG Design

- **Production**: `secrets.SystemRandom()` — CSPRNG, no seed
- **Testing**: `random.Random(seed)` — deterministic, seeded only in tests
- **Shuffle**: Fisher-Yates on full 78-card deck copy
- **Reversal**: Per-card Bernoulli trial at `reversal_probability` (default 0.35)
- **No duplicates**: Cards drawn from shuffled deck without replacement

---

## Development

```bash
# Requires Python 3.11+ (system Python may be older)
python3.11 -m pip install -e ".[dev]"

# Run all tests
python3.11 -m pytest tarot_tool/tests/ -v

# With coverage
python3.11 -m pytest tarot_tool/tests/ --cov=tarot_tool --cov-report=term-missing

# Lint / format / type check
ruff check tarot_tool/
black tarot_tool/
mypy tarot_tool/
```

**Test results**: 127 tests, ~95% coverage.

---

## Design Constraints

- No external API calls — all 78 cards embedded as Python constants
- No file I/O at runtime — data loaded from module-level dicts
- No shared mutable state — all tool functions are pure with respect to side effects
- `get_deck()` uses `@lru_cache` — callers must not mutate the returned list
- Every `tool_handler()` catches all exceptions; never raises to the caller
- Thread-safe for concurrent OpenClaw calls

---

## OpenClaw Skill Manifest

`tarot_tool.toml` registers the skill:

```toml
[skill]
name = "tarot_tool"
version = "0.1.0"
entry_point = "tarot_tool.server:main"

[[skill.tools]]
name = "draw_tarot_cards"
# ... (four tools registered)
```

Point your OpenClaw config at this file:
```toml
[[skills]]
manifest = "/path/to/tarot-tool/tarot_tool.toml"
```
