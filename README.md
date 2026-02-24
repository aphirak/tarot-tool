# tarot-tool

A production-grade Python tarot card tool system built for **OpenClaw MCP** (Model Context Protocol) integration. Enables LLMs to draw cards with cryptographically secure randomness, retrieve rich card meanings, and compose structured reading contexts for any spread format.

---

## Features

- **78-card deck** — Full Rider-Waite-Smith corpus: all 22 Major Arcana and 56 Minor Arcana with upright/reversed meanings, keywords, elements, astrology, and numerology
- **Cryptographically secure draws** — Uses `secrets.SystemRandom()` + Fisher-Yates shuffle; no `random.Random` in production paths
- **9 built-in spreads** — Single, Three-Card, Celtic Cross, Horseshoe, Relationship, Year Ahead, Chakra, Decision, and fully dynamic Custom spreads
- **4 OpenClaw tools** — Drop-in tool definitions with JSON schemas ready for MCP registration
- **LLM-ready context** — `ReadingContext` payload includes elemental analysis, numerology notes, thematic summary, and a pre-built `system_prompt_injection` string
- **Pydantic v2 models** — Fully validated, type-safe data throughout
- **Zero external dependencies at runtime** — All card data embedded in Python; no file I/O, no network calls

---

## Requirements

- Python ≥ 3.11
- `pydantic >= 2.0`

---

## Installation

```bash
# Standard install
pip install tarot-tool

# From source (recommended for development)
git clone https://github.com/your-org/tarot-tool.git
cd tarot-tool
pip install -e ".[dev]"
```

---

## Quick Start

### Draw cards for a spread

```python
from tarot_tool.tools import draw_tarot_cards

result = draw_tarot_cards("celtic_cross", question="What do I need to know right now?")

for card in result.drawn_cards:
    orientation = "reversed" if card.is_reversed else "upright"
    print(f"[{card.position_label}] {card.card.name} ({orientation})")
    print(f"  → {', '.join(card.active_keywords)}")
```

### Perform a full LLM reading

```python
from tarot_tool.tools import read_spread

ctx = read_spread(
    "three_card",
    question="What path should I take?",
    reading_style="psychological",
)

# Ready-to-use system prompt for any LLM
print(ctx.system_prompt_injection)

# Elemental balance of the draw
print(ctx.element_distribution)  # e.g. {"Fire": 2, "Water": 1}

# Thematic summary auto-generated from drawn cards
print(ctx.thematic_summary)
```

### Look up a card's meaning

```python
from tarot_tool.tools import get_card_meaning

info = get_card_meaning("The Tower", orientation="both")
print(info["meaning_upright"])
print(info["meaning_reversed"])
print(info["keywords_upright"])
```

### List available spreads

```python
from tarot_tool.tools import list_spread_formats

spreads = list_spread_formats(include_positions=True)
for s in spreads:
    print(f"{s['id']:15} — {s['name']} ({s['card_count']} cards)")
```

### Custom spread

```python
from tarot_tool.tools import read_spread

ctx = read_spread(
    "custom",
    custom_positions=["Mind", "Body", "Spirit", "Shadow"],
    question="Where am I out of balance?",
    reading_style="spiritual",
)
```

---

## OpenClaw MCP Integration

Register all four tools with your OpenClaw server in one line:

```python
from tarot_tool.tools import ALL_TOOLS
# ALL_TOOLS is a list of JSON-schema tool definitions ready for MCP registration
```

### Available tools

| Tool name | Description |
|---|---|
| `draw_tarot_cards` | Draw cards for a spread; returns `SpreadResult` with full card metadata |
| `get_card_meaning` | Look up upright/reversed meanings for any card by name |
| `list_spread_formats` | Enumerate all available spread formats with position descriptions |
| `read_spread` | Full reading: draws cards + assembles `ReadingContext` for LLM interpretation |

#### `draw_tarot_cards`

```json
{
  "spread_id": "string",
  "question": "string (optional)",
  "reversal_probability": 0.35,
  "custom_positions": ["label1", "label2"]
}
```

#### `get_card_meaning`

```json
{
  "card_name": "The Moon",
  "orientation": "upright | reversed | both"
}
```

#### `list_spread_formats`

```json
{
  "include_positions": true
}
```

#### `read_spread`

```json
{
  "spread_id": "celtic_cross",
  "question": "string (optional)",
  "reversal_probability": 0.35,
  "reading_style": "psychological | spiritual | practical | combined"
}
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

## ReadingContext payload

The `read_spread` tool returns a `ReadingContext` object containing:

```python
class ReadingContext(BaseModel):
    spread_name: str
    question: Optional[str]
    reading_style: str
    drawn_cards: list[DrawnCard]          # Full card data + positional context
    spread_narrative_hints: list[str]     # Per-position interpretation guidance
    thematic_summary: str                 # Auto-generated from card composition
    element_distribution: dict[str, int]  # Fire/Water/Air/Earth counts
    numerology_notes: list[str]           # Numerological significance per card
    dominant_suit: Optional[str]          # Most represented suit/element
    reading_timestamp: str                # ISO 8601
    system_prompt_injection: str          # Ready-to-use LLM system prompt fragment
```

The `system_prompt_injection` field is fully formatted and ready to prepend to any LLM conversation:

```
You are reading a psychological tarot spread (Celtic Cross).
The seeker asks: "What do I need to know right now?"
Cards drawn:
  1. The Heart of the Matter: The Tower — sudden change, upheaval, revelation
  2. The Crossing Card: Nine of Cups — contentment, satisfaction, wish fulfilled
  ...
Elemental balance: Air: 3, Fire: 2, Water: 4, Earth: 1
Dominant theme: Cups
Interpret each card in its positional context. Note interactions between cards.
```

---

## Project Structure

```
tarot_tool/
├── models/
│   ├── card.py           # TarotCard, DrawnCard, Suit
│   ├── spread.py         # SpreadDefinition, SpreadResult, PositionDefinition
│   └── reading.py        # ReadingContext
├── cards/
│   ├── major_arcana.py   # 22 Major Arcana data
│   ├── minor_arcana.py   # 56 Minor Arcana data (all four suits)
│   ├── deck.py           # get_deck() — cached full 78-card deck
│   └── meanings.py       # Name-indexed meaning lookup
├── engine/
│   ├── rng.py            # draw_cards() — CSPRNG + Fisher-Yates
│   ├── shuffle.py        # shuffle_deck()
│   └── context_builder.py # build_reading_context()
├── spreads/
│   ├── registry.py       # get_spread(), list_spreads()
│   ├── single.py
│   ├── three_card.py
│   ├── celtic_cross.py
│   ├── horseshoe.py
│   ├── relationship.py
│   ├── year_ahead.py
│   ├── chakra.py
│   ├── decision.py
│   └── custom.py         # build_custom_spread()
├── tools/
│   ├── draw_cards.py     # draw_tarot_cards()
│   ├── get_meaning.py    # get_card_meaning()
│   ├── list_spreads.py   # list_spread_formats()
│   └── read_spread.py    # read_spread()
└── tests/
    ├── test_deck.py
    ├── test_rng.py
    ├── test_spreads.py
    └── test_context.py
```

---

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
python3.11 -m pytest tarot_tool/tests/ -v

# Run tests with coverage report
python3.11 -m pytest tarot_tool/tests/ --cov=tarot_tool --cov-report=term-missing

# Lint
ruff check tarot_tool/

# Format
black tarot_tool/

# Type check
mypy tarot_tool/
```

### Test coverage

```
TOTAL    728 stmts    95% coverage
64 tests passing
```

### Adding a new spread

1. Create `tarot_tool/spreads/my_spread.py` defining a `SpreadDefinition`
2. Import and add it to `_REGISTRY` in `tarot_tool/spreads/registry.py`
3. Add a card count entry to the test in `test_spreads.py`

### Adding or editing card meanings

Card data lives in plain Python dicts — no database, no files to load:

- **Major Arcana**: `tarot_tool/cards/major_arcana.py` — `MAJOR_ARCANA: list[dict]`
- **Minor Arcana**: `tarot_tool/cards/minor_arcana.py` — `MINOR_ARCANA: list[dict]`

After editing, the `get_deck()` LRU cache will reflect changes on the next process start.

---

## Design principles

- **No shared mutable state** — all tool functions are pure with respect to side effects; safe for concurrent use
- **No runtime I/O** — card data is embedded in Python constants; no disk reads, no network calls
- **CSPRNG only** — `secrets.SystemRandom()` for all production draws; the seeded path (`seed=int`) exists only for deterministic testing
- **Fail loudly** — invalid spread IDs, unknown card names, and bad orientation values raise immediately with clear messages

---

## License

MIT
