# tarot-tool — User Guide

> How to use tarot-tool from the command line.

---

## Requirements

- Python 3.11 or higher
- pip

Check your Python version:

```bash
python3 --version
# Python 3.11.x or higher required
```

---

## Installation

```bash
git clone https://github.com/aphirak/tarot-tool.git
cd tarot-tool
pip install -e .
```

Verify the install:

```bash
tarot --version
# tarot-tool 0.1.0
```

---

## Commands at a glance

```
tarot spreads                    List all available spread formats
tarot read   --spread <ID>       Perform a full reading with interpretation context
tarot draw   --spread <ID>       Draw cards only (no interpretation)
tarot meaning <Card Name>        Look up a card's meaning
```

Every command supports `--json` to output raw JSON instead of formatted text.

---

## `tarot spreads` — List spread formats

Shows every available spread ID, name, and card count.

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

Use the `ID` column as the value for `--spread` in the other commands.

---

## `tarot read` — Full reading

Draws cards, assigns them to positions, and produces a complete reading context including elemental analysis, numerology notes, thematic summary, and a ready-to-use LLM prompt injection.

### Syntax

```bash
tarot read --spread <ID> [OPTIONS]
```

### Options

| Option | Short | Description | Default |
|---|---|---|---|
| `--spread <ID>` | `-s` | Spread format ID | *(required)* |
| `--question "..."` | `-q` | Your question for the reading | none |
| `--style <STYLE>` | | Reading style (see below) | `combined` |
| `--positions "A,B,C"` | | Position labels for `custom` spread | none |
| `--reversal <0.0–1.0>` | | Probability each card is reversed | `0.35` |
| `--json` | | Output raw JSON instead of formatted text | off |

### Reading styles

| Style | Lens |
|---|---|
| `combined` | Balanced interpretation (default) |
| `psychological` | Jungian / inner-world focus |
| `spiritual` | Soul journey and higher purpose |
| `practical` | Day-to-day decisions and actions |

### Examples

**Simple single-card reading:**
```bash
tarot read --spread single
```

**Three-card reading with a question:**
```bash
tarot read --spread three_card --question "What do I need to focus on this week?"
```

**Celtic Cross with psychological style:**
```bash
tarot read --spread celtic_cross --style psychological
```

**Custom 3-position spread:**
```bash
tarot read --spread custom --positions "Mind,Body,Spirit" --question "Where am I out of balance?"
```

**No reversed cards:**
```bash
tarot read --spread horseshoe --reversal 0.0
```

**Output as JSON (for scripting):**
```bash
tarot read --spread single --json
```

### Sample output

```
═══════════════  PAST / PRESENT / FUTURE READING  ═══════════════

  Question : What do I need to focus on this week?
  Style    : Combined
  Date     : 2026-02-24

  1. Past
     The Hermit
     Keywords : solitude  · inner guidance  · introspection  · wisdom  · soul-searching
     Meaning  : The Hermit holds his lantern aloft not to guide others, but to illuminate...

  2. Present
     Five of Cups  ★ REVERSED
     Keywords : acceptance  · moving on  · forgiveness  · finding silver lining  · recovery
     Meaning  : Reversed, the Five of Cups signals that healing is underway—you are beginning...

  3. Future
     Ace of Wands
     Keywords : inspiration  · new venture  · potential  · creativity  · enthusiasm  · spark
     Meaning  : The Ace of Wands bursts with raw creative energy—a divine spark of inspiration...

────────────────────────────────────────────────────────────
  Elements : Air: 1  ·  Fire: 1  ·  Water: 1
  Dominant : Balanced
  Theme    : A balanced mix of Major and Minor Arcana suggests both fate and free will are active.

  Numerology:
    • The Hermit (numerology 9): completion, wisdom, and humanitarianism

────────────────────────────────────────────────────────────
  LLM Prompt Injection
────────────────────────────────────────────────────────────
  You are an expert tarot reader performing a combined reading.

  ## Spread: Past / Present / Future
  ## Question: "What do I need to focus on this week?"

  ## Cards Drawn

  ### Position 1: Past
  Card: The Hermit (upright)
  Keywords: solitude, introspection, inner guidance, soul-searching, wisdom
  Meaning: The Hermit holds his lantern aloft not to guide others, but to
  illuminate his own path inward...

  ### Position 2: Present
  Card: Five of Cups (reversed)
  Keywords: acceptance, moving on, forgiveness, finding silver lining, recovery
  Meaning: Reversed, the Five of Cups signals that healing is underway—you are
  beginning to turn away from grief and toward what remains...

  ### Position 3: Future
  Card: Ace of Wands (upright)
  Keywords: inspiration, new venture, potential, creativity, enthusiasm, spark
  Meaning: The Ace of Wands bursts with raw creative energy—a divine spark of
  inspiration that heralds bold new beginnings...

  ## Thematic Context
  A balanced mix of Major and Minor Arcana suggests both fate and free will are active.
  Element distribution: Air: 1, Fire: 1, Water: 1
  The Hermit (numerology 9): completion, wisdom, and humanitarianism

  ## Spread Narrative Guidance
  - Position 1 (Past): The Hermit (upright) — reflect on what wisdom solitude has built
  - Position 2 (Present): Five of Cups (reversed) — examine what you are releasing
  - Position 3 (Future): Ace of Wands (upright) — step toward the creative spark ahead

  ## Your Task
  Provide the seeker with a cohesive interpretation. Address each card in its
  positional context, weave the cards into a unified narrative, and note any
  elemental or thematic patterns across the spread.
```

---

## `tarot draw` — Draw cards only

Draws cards and shows their names and keywords. Useful for a quick look at what cards came up. When used with `--json`, the output also includes an `interpretation_prompt` field containing full card meanings and positional context — ready to feed to an LLM without running a full `read`.

### Syntax

```bash
tarot draw --spread <ID> [OPTIONS]
```

Supports the same `--question`, `--positions`, `--reversal`, and `--json` options as `tarot read`.

### Example

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

## `tarot meaning` — Look up a card

Shows the full upright and/or reversed meaning, keywords, and metadata for any card.

### Syntax

```bash
tarot meaning "Card Name" [--orientation upright|reversed|both]
```

Card names are **case-insensitive** and support partial matching.

### Options

| Option | Short | Description | Default |
|---|---|---|---|
| `--orientation` | `-o` | `upright`, `reversed`, or `both` | `both` |
| `--json` | | Output raw JSON | off |

### Examples

**Full meaning (upright + reversed):**
```bash
tarot meaning "The Tower"
```

**Upright only:**
```bash
tarot meaning "The Moon" --orientation upright
```

**Minor Arcana:**
```bash
tarot meaning "Queen of Cups"
```

**Partial match (case-insensitive):**
```bash
tarot meaning "fool"
tarot meaning "ace of wands"
```

### Sample output

```
════════════════════════  THE FOOL  ════════════════════════

  Arcana     : Major
  Suit       : Major Arcana
  Element    : Air
  Astrology  : Uranus
  Numerology : 0

Upright
───────
  Keywords : beginnings  · innocence  · spontaneity  · free spirit  · adventure  · potential

  The Fool represents the beginning of a journey, a leap of faith into the unknown
  with an open heart and fresh eyes. This card embodies pure potential, the excitement
  of new beginnings, and the trust that the universe will provide...

Reversed
────────
  Keywords : recklessness  · naivety  · foolishness  · risk  · negligence  · chaos

  Reversed, the Fool warns of recklessness, poor judgment, or leaping before looking...
```

---

## Spreads reference

| ID | Name | Cards | Best used for |
|---|---|---|---|
| `single` | Single Card | 1 | Daily card, quick answer |
| `three_card` | Past / Present / Future | 3 | Situation timeline |
| `celtic_cross` | Celtic Cross | 10 | Deep, comprehensive reading |
| `horseshoe` | Horseshoe | 7 | General situation overview |
| `relationship` | Relationship | 6 | Two-person dynamics |
| `year_ahead` | Year Ahead | 13 | Monthly energy for the coming year |
| `chakra` | Chakra Spread | 7 | Energy body and healing |
| `decision` | Decision Making | 5 | Choosing between two paths |
| `custom` | Custom | n | Any layout you define |

### Custom spread

Pass your own position labels as a comma-separated string:

```bash
tarot read --spread custom --positions "Career,Finances,Health,Relationships"
tarot read --spread custom --positions "Option A,Option B,Outcome"
```

---

## Tips

**Pipe output to a file:**
```bash
tarot read --spread celtic_cross --question "What does 2026 hold for me?" > my_reading.txt
```

**Feed the full LLM prompt from a complete reading:**
```bash
tarot read --spread three_card --json | python3 -c "
import json, sys
ctx = json.load(sys.stdin)
print(ctx['system_prompt_injection'])
"
```

**Feed the LLM prompt from a raw draw (skips thematic analysis):**
```bash
tarot draw --spread three_card --json | python3 -c "
import json, sys
ctx = json.load(sys.stdin)
print(ctx['interpretation_prompt'])
"
```

**Set no reversals for a purely upright reading:**
```bash
tarot read --spread single --reversal 0.0
```

**Set all reversals (fully reversed deck):**
```bash
tarot read --spread single --reversal 1.0
```

---

## Troubleshooting

**`tarot: command not found`**
The install did not register the entry point. Run:
```bash
pip install -e .
# then retry
tarot --version
```

**`Error: Unknown spread 'xxx'`**
Run `tarot spreads` to see valid IDs. Spread IDs use underscores, not hyphens (`three_card`, not `three-card`).

**`Error: Multiple cards match '...'`**
Your search matched more than one card. Be more specific:
```bash
tarot meaning "ace of wands"    # not just "ace"
tarot meaning "The Star"        # not just "star"
```

**`Error: custom spread requires custom_positions list`**
When using `--spread custom` you must also pass `--positions`:
```bash
tarot read --spread custom --positions "Past,Present,Future"
```

**Python version error**
This tool requires Python 3.11+. Check with `python3 --version` and install a newer version if needed.
