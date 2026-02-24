# GEMINI.md — Tarot Tool System for OpenClaw

## Mission

You are implementing a **production-ready Python tarot card tool system** for the **OpenClaw** framework (Model Context Protocol). This system provides structured tarot card drawing, rich card meaning lookup, and LLM-ready reading context generation.

**Read this file completely before writing any code.**

---

## Primary Objectives

1. Build a complete 78-card tarot deck with full meaning corpus (upright + reversed)
2. Implement cryptographically secure randomization using `secrets.SystemRandom()`
3. Register all spread formats (Celtic Cross, Three-Card, Horseshoe, etc.)
4. Expose 4 OpenClaw tools: `draw_tarot_cards`, `get_card_meaning`, `list_spread_formats`, `read_spread`
5. Generate `ReadingContext` — a structured payload that gives any LLM full context to perform a reading

---

## Step-by-Step Build Order

Follow this exact order to avoid dependency issues:

```
Step 1 → models/card.py          (TarotCard, DrawnCard — Pydantic v2)
Step 2 → models/spread.py        (SpreadDefinition, SpreadResult)
Step 3 → models/reading.py       (ReadingContext)
Step 4 → cards/major_arcana.py   (22 cards with full meanings)
Step 5 → cards/minor_arcana.py   (56 cards — all 4 suits × 14 ranks)
Step 6 → cards/deck.py           (Assemble full 78-card deck list)
Step 7 → engine/rng.py           (Fisher-Yates + CSPRNG)
Step 8 → spreads/registry.py     (All spread definitions)
Step 9 → engine/context_builder.py (ReadingContext assembly)
Step 10 → tools/*.py             (4 OpenClaw tool wrappers)
Step 11 → tests/                 (pytest suite)
```

---

## File Structure

```
tarot_tool/
├── __init__.py
├── cards/
│   ├── __init__.py
│   ├── major_arcana.py
│   ├── minor_arcana.py
│   └── deck.py
├── spreads/
│   ├── __init__.py
│   └── registry.py
├── engine/
│   ├── __init__.py
│   ├── rng.py
│   └── context_builder.py
├── tools/
│   ├── __init__.py
│   ├── draw_cards.py
│   ├── get_meaning.py
│   ├── list_spreads.py
│   └── read_spread.py
├── models/
│   ├── card.py
│   ├── spread.py
│   └── reading.py
├── tests/
│   ├── test_deck.py
│   ├── test_rng.py
│   ├── test_spreads.py
│   └── test_context.py
└── pyproject.toml
```

---

## Data Specifications

### Major Arcana — Required Cards (0–21)

You must implement ALL 22 cards with complete fields:

| # | Name | Element | Astrology | Numerology |
|---|------|---------|-----------|------------|
| 0 | The Fool | Air | Uranus | 0 |
| 1 | The Magician | Air | Mercury | 1 |
| 2 | The High Priestess | Water | Moon | 2 |
| 3 | The Empress | Earth | Venus | 3 |
| 4 | The Emperor | Fire | Aries | 4 |
| 5 | The Hierophant | Earth | Taurus | 5 |
| 6 | The Lovers | Air | Gemini | 6 |
| 7 | The Chariot | Water | Cancer | 7 |
| 8 | Strength | Fire | Leo | 8 |
| 9 | The Hermit | Earth | Virgo | 9 |
| 10 | Wheel of Fortune | Fire | Jupiter | 10 |
| 11 | Justice | Air | Libra | 11 |
| 12 | The Hanged Man | Water | Neptune | 12 |
| 13 | Death | Water | Scorpio | 13 |
| 14 | Temperance | Fire | Sagittarius | 14 |
| 15 | The Devil | Earth | Capricorn | 15 |
| 16 | The Tower | Fire | Mars | 16 |
| 17 | The Star | Air | Aquarius | 17 |
| 18 | The Moon | Water | Pisces | 18 |
| 19 | The Sun | Fire | Sun | 19 |
| 20 | Judgement | Fire | Pluto | 20 |
| 21 | The World | Earth | Saturn | 21 |

### Minor Arcana — Required Suits & Ranks

Each suit must have 14 cards: Ace, 2–10, Page, Knight, Queen, King.

| Suit | Element | Domain |
|------|---------|--------|
| Wands | Fire | Creativity, Will, Passion, Career |
| Cups | Water | Emotions, Relationships, Intuition |
| Swords | Air | Mind, Conflict, Truth, Communication |
| Pentacles | Earth | Material, Finance, Health, Work |

---

## Core Class Contracts

### `TarotCard` (Pydantic v2)

```python
class TarotCard(BaseModel):
    id: int                          # Unique 0–77
    name: str
    suit: Suit                       # Enum: major_arcana | wands | cups | swords | pentacles
    number: int | None               # Rank within suit
    arcana: Literal["major", "minor"]
    keywords_upright: list[str]      # 5–8 items
    keywords_reversed: list[str]     # 5–8 items
    meaning_upright: str             # Full paragraph, ≥3 sentences
    meaning_reversed: str            # Full paragraph, ≥3 sentences
    element: str | None
    astrology: str | None
    numerology: int | None
    image_key: str                   # e.g. "major_00_fool"
```

### `ReadingContext` (LLM Payload)

```python
class ReadingContext(BaseModel):
    spread_name: str
    question: str | None
    reading_style: str
    drawn_cards: list[DrawnCard]
    spread_narrative_hints: list[str]
    thematic_summary: str
    element_distribution: dict[str, int]
    numerology_notes: list[str]
    dominant_suit: str | None
    reading_timestamp: str
    system_prompt_injection: str     # ← Critical: ready-to-inject LLM context
```

**`system_prompt_injection` must be generated as a formatted string:**

```python
def build_system_prompt(ctx: ReadingContext) -> str:
    cards_text = "\n".join([
        f"  [{i+1}] {c.position_label}: {c.card.name} "
        f"({'Reversed' if c.is_reversed else 'Upright'}) — {c.active_keywords}"
        for i, c in enumerate(ctx.drawn_cards)
    ])
    return f"""You are performing a {ctx.reading_style} tarot reading using the {ctx.spread_name} spread.
{'Question: ' + ctx.question if ctx.question else 'No specific question — general reading.'}

Cards drawn:
{cards_text}

Elemental balance: {ctx.element_distribution}
Dominant suit: {ctx.dominant_suit or 'balanced'}
Thematic summary: {ctx.thematic_summary}

Instructions:
- Interpret each card within its positional meaning
- Note elemental interactions and numerological patterns
- Provide cohesive narrative connecting all positions
- Honor reversed cards as blocked, internalized, or shadow energy
"""
```

---

## RNG Requirements (CRITICAL)

```python
# CORRECT — use this
import secrets
_rng = secrets.SystemRandom()

def shuffle_deck(deck: list[TarotCard]) -> list[TarotCard]:
    """Fisher-Yates shuffle using CSPRNG."""
    deck = list(deck)
    for i in range(len(deck) - 1, 0, -1):
        j = _rng.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

# WRONG — do NOT use
import random
random.shuffle(deck)  # ← Not cryptographically secure, do not use
```

**Reversal**: For each drawn card, call `_rng.random() < reversal_probability` to determine if reversed.

---

## Spread Definitions

Implement these spreads in `spreads/registry.py`:

### three_card
```
Position 1: "Past"         — Influences from the past shaping the situation
Position 2: "Present"      — Current state and active energies
Position 3: "Future"       — Potential outcome if current path continues
```

### celtic_cross (10 positions)
```
Position 1:  "Present"          — The current situation
Position 2:  "Challenge"        — What crosses or challenges you
Position 3:  "Foundation"       — Root cause or unconscious influence
Position 4:  "Recent Past"      — What is passing away
Position 5:  "Higher Potential" — Best possible outcome
Position 6:  "Near Future"      — What approaches next
Position 7:  "Your Influence"   — How you see yourself
Position 8:  "Environment"      — How others see you / external forces
Position 9:  "Hopes and Fears"  — Inner hopes or hidden fears
Position 10: "Outcome"          — Final result
```

### horseshoe (7 positions)
```
Position 1: "Past"
Position 2: "Present"
Position 3: "Hidden Influences"
Position 4: "Obstacles"
Position 5: "External Influences"
Position 6: "Guidance"
Position 7: "Outcome"
```

### relationship (6 positions)
```
Position 1: "You"
Position 2: "Them"
Position 3: "Relationship Dynamic"
Position 4: "Strengths"
Position 5: "Challenges"
Position 6: "Advice"
```

### single (1 position)
```
Position 1: "Card of the Day / Focus"
```

### decision (5 positions)
```
Position 1: "Situation"
Position 2: "Option A"
Position 3: "Option B"
Position 4: "Hidden Factor"
Position 5: "Recommended Path"
```

### year_ahead (13 positions)
```
Positions 1–12: "Month 1" through "Month 12"
Position 13: "Year Theme"
```

### chakra (7 positions)
```
Position 1: "Root Chakra — Security"
Position 2: "Sacral Chakra — Creativity"
Position 3: "Solar Plexus — Power"
Position 4: "Heart Chakra — Love"
Position 5: "Throat Chakra — Expression"
Position 6: "Third Eye — Intuition"
Position 7: "Crown Chakra — Spirituality"
```

### custom (dynamic)
- Accept `custom_positions: list[str]` parameter
- Validate: 1 ≤ len(custom_positions) ≤ 78
- Generate SpreadDefinition dynamically from provided position labels

---

## Tool Interface Pattern

Each tool in `tools/` must follow this pattern for OpenClaw compatibility:

```python
from typing import Any

def tool_definition() -> dict[str, Any]:
    """Returns OpenClaw-compatible tool JSON schema."""
    return {
        "name": "tool_name",
        "description": "...",
        "input_schema": {
            "type": "object",
            "properties": { ... },
            "required": [...]
        }
    }

def tool_handler(params: dict[str, Any]) -> dict[str, Any]:
    """
    Validates input, executes logic, returns serializable dict.
    Must never raise unhandled exceptions — catch and return error dict.
    """
    try:
        # validate params
        # execute
        return {"success": True, "data": result.model_dump()}
    except Exception as e:
        return {"success": False, "error": str(e), "error_type": type(e).__name__}
```

---

## Validation Rules

Enforce these via Pydantic validators:

```python
@field_validator("reversal_probability")
def validate_reversal(cls, v: float) -> float:
    if not 0.0 <= v <= 1.0:
        raise ValueError("reversal_probability must be between 0.0 and 1.0")
    return v

@field_validator("spread_id")
def validate_spread(cls, v: str) -> str:
    from tarot_tool.spreads.registry import SPREAD_REGISTRY
    if v not in SPREAD_REGISTRY and v != "custom":
        raise ValueError(f"Unknown spread_id: {v}. Use list_spread_formats to enumerate valid IDs.")
    return v
```

---

## Testing Requirements

### `tests/test_deck.py`
```python
def test_deck_has_78_cards(): ...
def test_no_duplicate_ids(): ...
def test_no_duplicate_names(): ...
def test_all_major_arcana_present(): ...
def test_all_suits_have_14_cards(): ...
def test_all_cards_have_meanings(): ...
```

### `tests/test_rng.py`
```python
def test_draw_returns_exact_count(): ...
def test_draw_no_duplicates(): ...
def test_reversal_rate_within_tolerance(): ...  # ±5% over 10,000 draws
def test_full_deck_draw(): ...  # draw all 78
```

### `tests/test_spreads.py`
```python
def test_all_spreads_registered(): ...
def test_celtic_cross_positions(): ...
def test_custom_spread_dynamic(): ...
def test_year_ahead_13_cards(): ...
```

### `tests/test_context.py`
```python
def test_reading_context_complete(): ...
def test_system_prompt_injection_nonempty(): ...
def test_element_distribution_sums_to_card_count(): ...
def test_dominant_suit_logic(): ...
```

---

## pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "tarot-tool"
version = "1.0.0"
description = "OpenClaw tarot card tools with full 78-card corpus"
requires-python = ">=3.11"
dependencies = [
    "pydantic>=2.0,<3.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov",
    "ruff",
    "black",
    "mypy",
]

[tool.ruff]
target-version = "py311"
select = ["E", "F", "I", "N", "UP"]

[tool.mypy]
python_version = "3.11"
strict = true
```

---

## Do Not Do

- ❌ Do NOT use `import random` for production draws
- ❌ Do NOT truncate card meanings — every card needs full text
- ❌ Do NOT use `dict` as mutable default argument
- ❌ Do NOT raise bare `Exception` — use specific types
- ❌ Do NOT skip any of the 78 cards with placeholder text
- ❌ Do NOT use global mutable state in tool handlers
- ❌ Do NOT write async code unless OpenClaw SDK requires it

---

## Deliverables Checklist

- [ ] All 78 cards implemented with complete meaning corpus
- [ ] `secrets.SystemRandom()` used exclusively for draws
- [ ] All 9 spread formats registered and functional
- [ ] All 4 OpenClaw tools implemented with schema + handler
- [ ] `ReadingContext.system_prompt_injection` generated for all spreads
- [ ] Full pytest suite with ≥90% coverage
- [ ] `pyproject.toml` complete
- [ ] No `mypy --strict` errors
- [ ] `ruff check .` passes with zero violations
