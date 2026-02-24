# Example.md — tarot-tool Usage Examples

Practical, runnable examples for both the CLI and OpenClaw skill integration.

---

## Part 1 — CLI (`tarot` command)

### Install

```bash
git clone https://github.com/aphirak/tarot-tool.git
cd tarot-tool
python3.11 -m pip install -e .
```

---

### 1.1 List available spreads

```bash
tarot spreads
```

```
═══════════════════  AVAILABLE SPREADS  ════════════════════

  ID                 Name                       Cards
  ────────────────── ────────────────────────── ─────
  single             Single Card                1
  three_card         Past / Present / Future    3
  celtic_cross       Celtic Cross               10
  horseshoe          Horseshoe                  7
  relationship       Relationship               6
  year_ahead         Year Ahead                 13
  chakra             Chakra Spread              7
  decision           Decision Making            5
  custom             Custom Spread              variable
```

---

### 1.2 Daily card (single)

```bash
tarot read --spread single
```

```
═══════════════════════  SINGLE CARD READING  ═══════════════════════

  Question : —
  Style    : Combined
  Date     : 2026-02-24

  1. Card
     The Star
     Keywords : hope  · renewal  · serenity  · inspiration  · faith  · calm
     Meaning  : The Star follows the destruction of the Tower with a message of
                renewal and hope. Bathed in starlight, the figure pours water
                freely—replenishing both the unconscious and the earth...
```

---

### 1.3 Three-card reading with a question

```bash
tarot read --spread three_card --question "What do I need to focus on this week?"
```

```
═══════════════  PAST / PRESENT / FUTURE READING  ═══════════════

  Question : What do I need to focus on this week?
  Style    : Combined
  Date     : 2026-02-24

  1. Past
     The Hermit
     Keywords : solitude  · inner guidance  · introspection  · wisdom
     Meaning  : The Hermit holds his lantern aloft not to guide others...

  2. Present
     Five of Cups  ★ REVERSED
     Keywords : acceptance  · moving on  · forgiveness  · healing
     Meaning  : Reversed, the Five of Cups signals that healing is underway...

  3. Future
     Ace of Wands
     Keywords : inspiration  · new venture  · creativity  · spark
     Meaning  : The Ace of Wands bursts with raw creative energy...

────────────────────────────────────────────────────────────
  Elements : Air: 1  ·  Fire: 1  ·  Water: 1
  Theme    : A balanced mix of Major and Minor Arcana...
  Numerology:
    • The Hermit (numerology 9): completion, wisdom, and humanitarianism
```

---

### 1.4 Celtic Cross — psychological style

```bash
tarot read --spread celtic_cross --style psychological --question "Where am I blocking myself?"
```

---

### 1.5 Custom spread

```bash
tarot read --spread custom \
  --positions "Mind,Body,Spirit" \
  --question "Where am I out of balance?"
```

```bash
# Four-position custom
tarot read --spread custom \
  --positions "Situation,Challenge,Hidden Factor,Outcome" \
  --question "How do I approach this decision?"
```

---

### 1.6 Draw cards only (no thematic analysis)

```bash
tarot draw --spread three_card
```

```
══════════  PAST / PRESENT / FUTURE — CARD DRAW  ═══════════

  1. Past
     Three of Swords
     heartbreak  · grief  · sorrow  · rejection

  2. Present
     Ace of Cups
     love  · new feelings  · emotional beginning  · compassion

  3. Future
     Page of Swords
     curious  · talkative  · restless  · mental agility
```

---

### 1.7 Card meaning lookup

```bash
tarot meaning "The Tower"
```

```bash
tarot meaning "fool"                           # partial, case-insensitive
tarot meaning "queen of cups" --orientation upright
tarot meaning "ace of wands" --orientation reversed
```

```
════════════════════════  THE FOOL  ════════════════════════

  Arcana     : Major
  Element    : Air
  Astrology  : Uranus
  Numerology : 0

Upright
───────
  Keywords : beginnings  · innocence  · spontaneity  · free spirit  · adventure

  The Fool represents the beginning of a journey, a leap of faith into the
  unknown with an open heart and fresh eyes...

Reversed
────────
  Keywords : recklessness  · naivety  · foolishness  · risk  · negligence

  Reversed, the Fool warns of recklessness, poor judgment, or leaping before looking...
```

---

### 1.8 JSON output and scripting

```bash
# Emit raw JSON
tarot read --spread three_card --json

# Extract the LLM system prompt for piping into your own model call
tarot read --spread three_card --question "What's next?" --json \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['system_prompt_injection'])"

# Same for a raw draw (skips thematic analysis, still includes full card meanings)
tarot draw --spread horseshoe --json \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['interpretation_prompt'])"

# Save a reading to a file
tarot read --spread celtic_cross \
  --question "What does 2026 hold for me?" \
  > celtic_cross_reading.txt

# No reversed cards
tarot read --spread single --reversal 0.0
```

---

## Part 2 — OpenClaw Skill (stdio subprocess)

The skill runs as a subprocess (`tarot-tool`) and speaks line-delimited JSON over stdio.

### Register the skill

```toml
# openclaw.toml
[[skills]]
manifest = "/path/to/tarot-tool/tarot_tool.toml"
```

### 2.1 List available tools

```bash
echo '{"id":"1","method":"list_tools"}' | tarot-tool
```

```json
{
  "id": "1",
  "result": [
    {"name": "draw_tarot_cards", "description": "Draw tarot cards for a reading...", "input_schema": {...}},
    {"name": "get_card_meaning",  "description": "Retrieve full meaning...",          "input_schema": {...}},
    {"name": "list_spread_formats","description": "List all available spread formats...","input_schema": {...}},
    {"name": "read_spread",       "description": "Perform a complete tarot reading...", "input_schema": {...}}
  ]
}
```

### 2.2 Read a spread

```bash
echo '{"id":"2","method":"call_tool","params":{"name":"read_spread","input":{"spread_id":"three_card","question":"What path should I take?","reading_style":"psychological"}}}' \
  | tarot-tool
```

```json
{
  "id": "2",
  "result": {
    "success": true,
    "data": {
      "spread_name": "Past / Present / Future",
      "question": "What path should I take?",
      "reading_style": "psychological",
      "drawn_cards": [...],
      "thematic_summary": "...",
      "element_distribution": {"Water": 2, "Fire": 1},
      "numerology_notes": ["..."],
      "system_prompt_injection": "You are an expert tarot reader..."
    }
  }
}
```

### 2.3 Draw cards only

```bash
echo '{"id":"3","method":"call_tool","params":{"name":"draw_tarot_cards","input":{"spread_id":"celtic_cross"}}}' \
  | tarot-tool
```

### 2.4 Get a card meaning

```bash
echo '{"id":"4","method":"call_tool","params":{"name":"get_card_meaning","input":{"card_name":"The Moon","orientation":"both"}}}' \
  | tarot-tool
```

### 2.5 List spread formats

```bash
echo '{"id":"5","method":"call_tool","params":{"name":"list_spread_formats","input":{"include_positions":false}}}' \
  | tarot-tool
```

### 2.6 Custom spread via OpenClaw

```bash
echo '{"id":"6","method":"call_tool","params":{"name":"read_spread","input":{"spread_id":"custom","custom_positions":["Mind","Body","Spirit"],"question":"Where am I out of balance?"}}}' \
  | tarot-tool
```

---

## Part 3 — OpenClaw Python Skill (direct import)

`TarotSkill` lets OpenClaw call tools in-process — no subprocess, no JSON serialization.

```python
from tarot_tool.tool import TarotSkill

skill = TarotSkill()
```

### 3.1 Discover tools

```python
definitions = skill.get_tool_definitions()
for t in definitions:
    print(t["name"], "—", t["description"])
```

```
draw_tarot_cards — Draw tarot cards for a reading...
get_card_meaning — Retrieve full meaning, keywords, and metadata...
list_spread_formats — List all available tarot spread formats...
read_spread — Perform a complete tarot reading...
```

### 3.2 Full reading

```python
result = skill.read_spread(
    spread_id="three_card",
    question="What path should I take?",
    reading_style="psychological",
)

if result["success"]:
    ctx = result["data"]
    print("Spread :", ctx["spread_name"])
    print("Theme  :", ctx["thematic_summary"])
    print()
    print(ctx["system_prompt_injection"])   # ready to prepend to any LLM call
else:
    print("Error:", result["error"])
```

### 3.3 Draw cards only

```python
result = skill.draw_tarot_cards(
    spread_id="celtic_cross",
    question="What do I need to know?",
    reversal_probability=0.25,
)

for card in result["data"]["drawn_cards"]:
    orientation = "reversed" if card["is_reversed"] else "upright"
    print(f"[{card['position_label']}] {card['card']['name']} ({orientation})")
```

### 3.4 Card meaning

```python
result = skill.get_card_meaning("The High Priestess", orientation="upright")
print(result["data"]["meaning_upright"])
print(result["data"]["keywords_upright"])
```

### 3.5 List spreads

```python
result = skill.list_spread_formats(include_positions=True)
for spread in result["data"]:
    positions = [p["label"] for p in spread.get("positions", [])]
    print(f"{spread['id']:15s}  {spread['name']:25s}  {spread['card_count']} cards")
    if positions:
        print("  Positions:", " · ".join(positions))
```

### 3.6 Generic dispatcher

```python
# Call any tool by name — same as the named methods above
result = skill.call_tool("read_spread", {
    "spread_id": "horseshoe",
    "reading_style": "spiritual",
})
```

### 3.7 Custom spread

```python
result = skill.read_spread(
    spread_id="custom",
    custom_positions=["Situation", "Challenge", "Hidden Factor", "Advice", "Outcome"],
    question="How do I navigate this transition?",
    reading_style="combined",
)
```

### 3.8 Using the system prompt with an LLM

```python
from tarot_tool.tool import TarotSkill

skill = TarotSkill()

# 1. Perform the reading
result = skill.read_spread(
    spread_id="celtic_cross",
    question="What do I need to know about my career path?",
    reading_style="practical",
)
system_prompt = result["data"]["system_prompt_injection"]

# 2. Pass to your LLM (example using Anthropic SDK)
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": "Please give me the reading."}],
)
print(response.content[0].text)
```

---

## Quick Reference

| Task | CLI | Python skill |
|---|---|---|
| List spreads | `tarot spreads` | `skill.list_spread_formats()` |
| Full reading | `tarot read --spread three_card` | `skill.read_spread(spread_id="three_card")` |
| Draw only | `tarot draw --spread three_card` | `skill.draw_tarot_cards(spread_id="three_card")` |
| Card meaning | `tarot meaning "The Fool"` | `skill.get_card_meaning("The Fool")` |
| Custom spread | `tarot read --spread custom --positions "A,B,C"` | `skill.read_spread(spread_id="custom", custom_positions=["A","B","C"])` |
| JSON output | `tarot read --spread single --json` | *(all methods return dicts)* |
| LLM prompt | `tarot read --spread single --json \| ...` | `result["data"]["system_prompt_injection"]` |
