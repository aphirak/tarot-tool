# SKILL.md — OpenClaw Skill Integration Guide

**tarot_tool** exposes its four tools to OpenClaw in two modes:

| Mode | Entry point | How OpenClaw uses it |
|---|---|---|
| **Stdio subprocess** | `tarot-tool` command | Spawns a subprocess, sends line-delimited JSON |
| **Python direct import** | `tarot_tool.tool.TarotSkill` | Imports the class, calls methods in-process |

---

## 1. Stdio Subprocess Mode (existing `server.py`)

OpenClaw spawns `tarot-tool` as a subprocess and communicates via line-delimited JSON:

```bash
# Input (stdin) — one JSON object per line:
{"id": "1", "method": "list_tools"}
{"id": "2", "method": "call_tool", "params": {"name": "read_spread", "input": {"spread_id": "three_card"}}}

# Output (stdout) — one JSON object per line:
{"id": "1", "result": [...tool definitions...]}
{"id": "2", "result": {"success": true, "data": {...ReadingContext...}}}
```

**OpenClaw config** (`openclaw.toml`):
```toml
[[skills]]
manifest = "/path/to/tarot-tool/tarot_tool.toml"
```

**Manifest** (`tarot_tool.toml`):
```toml
[skill]
name        = "tarot_tool"
version     = "0.1.0"
entry_point = "tarot_tool.server:main"
python_skill = "tarot_tool.tool:TarotSkill"
```

---

## 2. Python Direct Import Mode (`tool.py`)

OpenClaw imports `TarotSkill` and calls tools in-process — no subprocess, no JSON serialization overhead.

```python
from tarot_tool.tool import TarotSkill

skill = TarotSkill()

# Discover available tools
definitions = skill.get_tool_definitions()

# Call any tool by name (generic)
result = skill.call_tool("read_spread", {"spread_id": "three_card"})

# Or use named methods (recommended)
result = skill.draw_tarot_cards(spread_id="three_card", question="What's next?")
result = skill.read_spread(spread_id="celtic_cross", reading_style="psychological")
result = skill.get_card_meaning("The Moon", orientation="both")
result = skill.list_spread_formats(include_positions=True)
```

All methods return a consistent dict:
```python
{"success": True,  "data": {...}}        # on success
{"success": False, "error": "...", "error_type": "ValueError"}  # on failure
```

---

## Tools Reference

### `draw_tarot_cards`

Draw cards for a spread. Returns full card metadata and an interpretation prompt.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `spread_id` | string | yes | — | Spread ID (see list below) |
| `question` | string | no | null | Reading question or context |
| `reversal_probability` | float | no | 0.35 | Probability each card is reversed |
| `custom_positions` | list[str] | no | null | Position labels (required for `custom` spread) |

```python
result = skill.draw_tarot_cards(
    spread_id="horseshoe",
    question="What obstacles face me?",
    reversal_probability=0.25,
)
cards = result["data"]["drawn_cards"]
```

---

### `read_spread`

Full reading with LLM context. Returns `ReadingContext` including `system_prompt_injection`.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `spread_id` | string | yes | — | Spread ID |
| `question` | string | no | null | Reading question |
| `reversal_probability` | float | no | 0.35 | Reversal probability |
| `reading_style` | string | no | `combined` | `psychological` \| `spiritual` \| `practical` \| `combined` |
| `custom_positions` | list[str] | no | null | For `custom` spread |

```python
result = skill.read_spread(
    spread_id="celtic_cross",
    question="How do I navigate this transition?",
    reading_style="psychological",
)
llm_prompt = result["data"]["system_prompt_injection"]
```

---

### `get_card_meaning`

Look up a card's meaning, keywords, and metadata by name.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `card_name` | string | yes | — | Exact or partial name (case-insensitive) |
| `orientation` | string | no | `both` | `upright` \| `reversed` \| `both` |

```python
result = skill.get_card_meaning("The High Priestess", orientation="upright")
meaning = result["data"]["meaning_upright"]
```

---

### `list_spread_formats`

Enumerate all available spreads.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `include_positions` | boolean | no | `true` | Include per-position labels |

```python
result = skill.list_spread_formats(include_positions=False)
spread_ids = [s["id"] for s in result["data"]]
```

---

## Available Spread IDs

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
| `custom` | Custom (user-defined) | n |

---

## Skill Metadata

```python
from tarot_tool.tool import TarotSkill

skill = TarotSkill()
print(skill.name)         # "tarot_tool"
print(skill.version)      # "0.1.0"
print(skill.description)  # "Tarot card reading tools for OpenClaw AI agents..."
```

---

## Installation

No third-party dependencies — requires Python 3.11+ only.

```bash
# Clone and install in editable mode
git clone <repo>
cd tarot-tool
python3.11 -m pip install -e ".[dev]"

# Verify skill loads
python3.11 -c "from tarot_tool.tool import TarotSkill; s = TarotSkill(); print(s.name, s.version)"
```
