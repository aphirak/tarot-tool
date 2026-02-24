# CLAUDE.md — Tarot Tool System for OpenClaw

## Project Overview

Build a **production-grade Python tarot card tool system** designed for OpenClaw MCP (Model Context Protocol) integration. The system enables LLMs to draw cards with cryptographically secure randomization, retrieve rich card meanings, and compose structured reading contexts for any spread format.

---

## Architecture

```
tarot_tool/
├── __init__.py
├── cards/
│   ├── __init__.py
│   ├── deck.py           # Full 78-card deck definition + metadata
│   ├── major_arcana.py   # 22 Major Arcana with full meaning maps
│   ├── minor_arcana.py   # 56 Minor Arcana (Wands/Cups/Swords/Pentacles)
│   └── meanings.py       # Upright / Reversed meaning registry
├── spreads/
│   ├── __init__.py
│   ├── registry.py       # Spread format registry
│   ├── single.py         # Single card
│   ├── three_card.py     # Past / Present / Future
│   ├── celtic_cross.py   # 10-position Celtic Cross
│   ├── horseshoe.py      # 7-card Horseshoe
│   ├── relationship.py   # Relationship spread
│   └── custom.py         # Dynamic n-position spread
├── engine/
│   ├── __init__.py
│   ├── rng.py            # CSPRNG draw engine (secrets module)
│   ├── shuffle.py        # Fisher-Yates on full deck
│   └── context_builder.py # LLM context payload assembler
├── tools/
│   ├── __init__.py
│   ├── draw_cards.py     # OpenClaw Tool: draw_tarot_cards
│   ├── get_meaning.py    # OpenClaw Tool: get_card_meaning
│   ├── list_spreads.py   # OpenClaw Tool: list_spread_formats
│   └── read_spread.py    # OpenClaw Tool: read_spread (full reading context)
├── models/
│   ├── card.py           # Pydantic: TarotCard, DrawnCard
│   ├── spread.py         # Pydantic: SpreadResult, SpreadDefinition
│   └── reading.py        # Pydantic: ReadingContext (LLM payload)
├── tests/
│   ├── test_deck.py
│   ├── test_rng.py
│   ├── test_spreads.py
│   └── test_context.py
├── pyproject.toml
└── README.md
```

---

## Implementation Requirements

### 1. Card Data Model (`models/card.py`)

```python
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Suit(str, Enum):
    MAJOR = "major_arcana"
    WANDS = "wands"
    CUPS = "cups"
    SWORDS = "swords"
    PENTACLES = "pentacles"

class TarotCard(BaseModel):
    id: int                        # 0–77
    name: str
    suit: Suit
    number: Optional[int]          # 0=Fool, 1–21 Major; 1–14 Minor
    arcana: str                    # "major" | "minor"
    keywords_upright: list[str]
    keywords_reversed: list[str]
    meaning_upright: str           # Full paragraph
    meaning_reversed: str
    element: Optional[str]
    astrology: Optional[str]
    numerology: Optional[int]
    image_key: str                 # slug for image lookup

class DrawnCard(BaseModel):
    card: TarotCard
    position: int
    position_label: str
    is_reversed: bool
    active_meaning: str            # Resolved based on is_reversed
    active_keywords: list[str]
```

### 2. RNG Engine (`engine/rng.py`)

- **Must use `secrets.SystemRandom()`** — not `random.Random()`.
- Implement **Fisher-Yates shuffle** on the full 78-card list.
- Support **reversal probability** (default: 0.35).
- No card duplication within a single draw session.

```python
import secrets
from typing import Optional

_system_rng = secrets.SystemRandom()

def draw_cards(
    deck: list[TarotCard],
    count: int,
    reversal_probability: float = 0.35,
    seed: Optional[int] = None,       # For reproducible testing only
) -> list[tuple[TarotCard, bool]]:
    """
    Fisher-Yates shuffle + draw `count` unique cards.
    Returns list of (card, is_reversed) tuples.
    """
    ...
```

### 3. Spread Registry (`spreads/registry.py`)

Register all spreads as `SpreadDefinition` objects:

| Spread ID | Name | Positions |
|---|---|---|
| `single` | Single Card | 1 |
| `three_card` | Past / Present / Future | 3 |
| `celtic_cross` | Celtic Cross | 10 |
| `horseshoe` | Horseshoe | 7 |
| `relationship` | Relationship | 6 |
| `year_ahead` | Year Ahead | 13 |
| `chakra` | Chakra Spread | 7 |
| `decision` | Decision Making | 5 |
| `custom` | Custom (n positions) | n (dynamic) |

```python
class SpreadDefinition(BaseModel):
    id: str
    name: str
    description: str
    positions: list[PositionDefinition]   # label + guidance per position
    min_cards: int
    max_cards: int
```

### 4. OpenClaw Tool Definitions

Each tool must implement the OpenClaw `Tool` interface:

#### `draw_tarot_cards`
```json
{
  "name": "draw_tarot_cards",
  "description": "Draw tarot cards for a reading. Returns drawn cards with full metadata and meanings.",
  "parameters": {
    "spread_id": "string — spread format ID (use list_spread_formats to enumerate)",
    "question": "string (optional) — user's question for context",
    "reversal_probability": "float (optional, default 0.35)",
    "custom_positions": "list[string] (optional) — labels for custom spread"
  }
}
```

#### `get_card_meaning`
```json
{
  "name": "get_card_meaning",
  "description": "Retrieve full meaning, keywords, and metadata for a specific tarot card.",
  "parameters": {
    "card_name": "string — exact card name or partial match",
    "orientation": "string — 'upright' | 'reversed' | 'both'"
  }
}
```

#### `list_spread_formats`
```json
{
  "name": "list_spread_formats",
  "description": "List all available tarot spread formats with position descriptions.",
  "parameters": {
    "include_positions": "bool (default true)"
  }
}
```

#### `read_spread`
```json
{
  "name": "read_spread",
  "description": "Perform a complete tarot reading. Returns a structured ReadingContext for LLM interpretation.",
  "parameters": {
    "spread_id": "string",
    "question": "string (optional)",
    "reversal_probability": "float (optional)",
    "reading_style": "string — 'psychological' | 'spiritual' | 'practical' | 'combined'"
  }
}
```

### 5. LLM Context Payload (`models/reading.py`)

`read_spread` must return a `ReadingContext` that gives the LLM everything needed to generate a coherent reading:

```python
class ReadingContext(BaseModel):
    spread_name: str
    question: Optional[str]
    reading_style: str
    drawn_cards: list[DrawnCard]
    spread_narrative_hints: list[str]   # Per-position interpretation guidance
    thematic_summary: str               # Auto-generated card theme summary
    element_distribution: dict[str, int]  # Fire/Water/Air/Earth counts
    numerology_notes: list[str]
    dominant_suit: Optional[str]
    reading_timestamp: str              # ISO 8601
    system_prompt_injection: str        # Ready-to-use LLM system prompt fragment
```

The `system_prompt_injection` field must be a fully formed string like:

```
You are reading a {reading_style} tarot spread ({spread_name}).
{question_context}
Cards drawn:
{card_list_formatted}
Elemental balance: {element_distribution}
Dominant theme: {dominant_suit}
Interpret each card in its positional context. Note interactions between cards.
```

---

## Card Meaning Corpus Requirements

All 78 cards must be populated with:

- **Major Arcana (0–21)**: Full Rider-Waite-Smith meanings. Each card needs:
  - `meaning_upright`: 3–5 sentence paragraph
  - `meaning_reversed`: 3–5 sentence paragraph
  - 5–8 upright keywords, 5–8 reversed keywords
  - Element, astrological correspondence, numerology

- **Minor Arcana (56 cards)**: All four suits × 14 ranks (Ace–10 + Page/Knight/Queen/King)
  - Each with upright/reversed meanings
  - Suit element mapping: Wands=Fire, Cups=Water, Swords=Air, Pentacles=Earth

---

## Code Quality Requirements

- Python ≥ 3.11
- **Pydantic v2** for all data models
- Type hints on all functions (strict mode compatible)
- `pyproject.toml` with `[project.optional-dependencies]` for dev/test
- 90%+ test coverage target
- All public functions have docstrings
- No mutable default arguments
- `ruff` for linting, `black` for formatting

---

## Dependencies

```toml
[project]
requires-python = ">=3.11"
dependencies = [
    "pydantic>=2.0",
    "secrets",   # stdlib
]

[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "ruff", "black", "mypy"]
openclaw = ["openclaw-sdk>=0.1"]  # Adjust to actual package name
```

---

## Testing Checklist

- [ ] All 78 cards present and no duplicates in deck
- [ ] `draw_cards(count=10)` returns exactly 10 unique cards
- [ ] `draw_cards` with fixed seed produces deterministic output
- [ ] Celtic Cross always returns exactly 10 cards
- [ ] `is_reversed` distribution is statistically consistent with `reversal_probability`
- [ ] `ReadingContext.system_prompt_injection` is non-empty for all spread types
- [ ] All spread IDs resolve via registry without KeyError
- [ ] Pydantic validation rejects invalid `orientation` values

---

## Constraints

- No external API calls — all card data is embedded in source
- No file I/O at runtime — data loaded from Python dicts/constants
- Thread-safe (no shared mutable state between tool calls)
- All tool functions must be **pure functions** with respect to side effects (no DB, no disk)
