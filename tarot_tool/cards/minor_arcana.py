"""Minor Arcana card definitions — all 56 cards across four suits."""
from __future__ import annotations

MINOR_ARCANA: list[dict] = [
    # ── WANDS (Fire) ── ids 22–35
    {
        "id": 22, "name": "Ace of Wands", "suit": "wands", "number": 1, "arcana": "minor",
        "keywords_upright": ["inspiration", "new venture", "potential", "creativity", "enthusiasm", "spark"],
        "keywords_reversed": ["delays", "creative block", "lack of energy", "missed opportunity", "hesitation"],
        "meaning_upright": (
            "The Ace of Wands bursts with raw creative energy—a divine spark of inspiration landing in your hands. "
            "A new venture, project, or passion is calling to you with electric urgency. "
            "This is the moment to say yes to the idea that excites you most and channel that initial fire into purposeful action. "
            "The potential here is enormous; everything depends on your willingness to act on this inspiration before it fades."
        ),
        "meaning_reversed": (
            "Reversed, the Ace of Wands suggests that the creative spark is present but blocked, delayed, or misdirected. "
            "You may be hesitating to begin a project out of fear, or the timing may simply not be right yet. "
            "Frustration, low energy, or a string of false starts may be dampening your enthusiasm. "
            "Tend the spark carefully—the fire is still there, waiting for the right conditions to blaze."
        ),
        "element": "Fire", "astrology": "Fire signs (Aries, Leo, Sagittarius)", "numerology": 1,
        "image_key": "ace_of_wands",
    },
    {
        "id": 23, "name": "Two of Wands", "suit": "wands", "number": 2, "arcana": "minor",
        "keywords_upright": ["planning", "future vision", "progress", "decision", "discovery", "ambition"],
        "keywords_reversed": ["fear of change", "poor planning", "lack of foresight", "playing it safe", "indecision"],
        "meaning_upright": (
            "The Two of Wands represents the moment after the initial spark when the visionary stands at the threshold, surveying the vast territory ahead. "
            "You have established a foothold and now must plan the next steps with boldness and foresight. "
            "Big plans are in motion; this card encourages you to think expansively about your future and commit to the path that aligns with your deepest ambitions. "
            "The world is waiting for you—begin mapping your route."
        ),
        "meaning_reversed": (
            "Reversed, the Two of Wands points to fear of moving forward, poor planning, or an unwillingness to step outside familiar territory. "
            "You may be clinging to safety when a calculated risk is what growth demands. "
            "Alternatively, plans may feel scattered or goals unclear, leaving you stuck at the threshold without direction. "
            "Clarify your vision and commit to a path before the window of opportunity closes."
        ),
        "element": "Fire", "astrology": "Mars in Aries", "numerology": 2,
        "image_key": "two_of_wands",
    },
    {
        "id": 24, "name": "Three of Wands", "suit": "wands", "number": 3, "arcana": "minor",
        "keywords_upright": ["expansion", "foresight", "preparation", "enterprise", "overseas opportunities", "growth"],
        "keywords_reversed": ["obstacles", "delays", "frustration", "lack of progress", "short-sightedness"],
        "meaning_upright": (
            "The Three of Wands signals that your initial efforts have borne fruit and expansion is underway. "
            "Look to the horizon—opportunities are coming, perhaps from unexpected or distant sources. "
            "This is a time to think big, to broaden your perspective, and to prepare for the growth that your efforts have set in motion. "
            "Your ships are in the water; stay watchful and ready to receive what is coming toward you."
        ),
        "meaning_reversed": (
            "Reversed, the Three of Wands suggests delays, obstacles, or a frustrating lack of progress despite your best efforts. "
            "Expected opportunities may be slow to materialize, or plans may be encountering unforeseen resistance. "
            "Short-sightedness or a failure to plan adequately for expansion may be creating bottlenecks. "
            "Patience and a willingness to revise your strategy will carry you through."
        ),
        "element": "Fire", "astrology": "Sun in Aries", "numerology": 3,
        "image_key": "three_of_wands",
    },
    {
        "id": 25, "name": "Four of Wands", "suit": "wands", "number": 4, "arcana": "minor",
        "keywords_upright": ["celebration", "harmony", "homecoming", "community", "milestone", "joy"],
        "keywords_reversed": ["conflict at home", "transition", "incomplete celebration", "instability", "lack of support"],
        "meaning_upright": (
            "The Four of Wands is a joyful celebration—a milestone reached, a foundation established, and a community gathered to honor what has been achieved. "
            "This is a time of harmony, happiness, and the warm sense of belonging that comes when effort is rewarded. "
            "Celebrate freely; you have earned this moment of rest and joy before the next stage of your journey begins. "
            "Home, family, and community are highlighted as sources of strength and joy."
        ),
        "meaning_reversed": (
            "Reversed, the Four of Wands points to conflict at home, disruptions to harmony, or a celebration that feels incomplete or hollow. "
            "The foundation you have built may feel unstable, or family and community dynamics may be creating tension rather than support. "
            "Alternatively, this card reversed can simply indicate a transition—a completion of one phase before the celebration is fully acknowledged. "
            "Address the underlying discord so that true celebration can occur."
        ),
        "element": "Fire", "astrology": "Venus in Aries", "numerology": 4,
        "image_key": "four_of_wands",
    },
    {
        "id": 26, "name": "Five of Wands", "suit": "wands", "number": 5, "arcana": "minor",
        "keywords_upright": ["conflict", "competition", "tension", "diversity", "chaos", "disagreement"],
        "keywords_reversed": ["resolution", "avoiding conflict", "harmony restored", "internal struggle", "compromise"],
        "meaning_upright": (
            "The Five of Wands depicts the chaos of competition and conflict—a scramble of energies all pulling in different directions. "
            "Disagreements, rivalries, and conflicting agendas are creating friction. "
            "Not all conflict is destructive; this card can represent the healthy tension that arises when diverse perspectives clash and eventually forge something stronger. "
            "Engage with the competition honestly and don't shy away from the struggle—it is forging your resilience."
        ),
        "meaning_reversed": (
            "Reversed, the Five of Wands suggests that conflict is being avoided or suppressed rather than resolved, or that internal struggle is the real battleground. "
            "A period of friction may be coming to an end and harmony is being restored. "
            "Alternatively, you may be running from necessary confrontation, allowing tensions to simmer beneath the surface. "
            "Find the courage to address conflict openly; resolution requires that all voices be heard."
        ),
        "element": "Fire", "astrology": "Saturn in Leo", "numerology": 5,
        "image_key": "five_of_wands",
    },
    {
        "id": 27, "name": "Six of Wands", "suit": "wands", "number": 6, "arcana": "minor",
        "keywords_upright": ["victory", "recognition", "success", "public acclaim", "confidence", "achievement"],
        "keywords_reversed": ["ego", "arrogance", "fall from grace", "lack of recognition", "delayed success"],
        "meaning_upright": (
            "The Six of Wands is the victory parade—you have triumphed and the world is taking notice. "
            "Public recognition, awards, or the satisfaction of achieved goals is at hand. "
            "Walk confidently into the spotlight you have earned; this is a moment to celebrate success and allow yourself to be seen and applauded. "
            "Your confidence is well-founded—own your accomplishments fully."
        ),
        "meaning_reversed": (
            "Reversed, the Six of Wands warns of ego, arrogance, or a fall from the high position that success created. "
            "Recognition may be delayed, or you may be seeking validation from others rather than finding confidence within. "
            "Alternatively, success may have come at a cost—relationships damaged, or values compromised in the pursuit of victory. "
            "True success is built on integrity; ensure your win is one you can be proud of at every level."
        ),
        "element": "Fire", "astrology": "Jupiter in Leo", "numerology": 6,
        "image_key": "six_of_wands",
    },
    {
        "id": 28, "name": "Seven of Wands", "suit": "wands", "number": 7, "arcana": "minor",
        "keywords_upright": ["perseverance", "defensiveness", "challenge", "standing firm", "conviction", "competition"],
        "keywords_reversed": ["surrender", "giving up", "overwhelm", "yielding", "backing down", "worn out"],
        "meaning_upright": (
            "The Seven of Wands finds you at the top, defending your position against challengers who want what you have achieved. "
            "Stand your ground with conviction—you have the advantage of high ground and the righteousness of your cause. "
            "This is not the time to back down; perseverance and a clear sense of what you are defending will carry you through the onslaught. "
            "Know your values and hold them fiercely."
        ),
        "meaning_reversed": (
            "Reversed, the Seven of Wands signals exhaustion, overwhelm, or a growing temptation to surrender when holding on is what's needed. "
            "You may be giving up territory you have worked hard to gain, or backing down from a position that still deserves to be defended. "
            "Alternatively, the battle may truly be over and it is time to lay down your weapon—know the difference between strategic retreat and cowardly capitulation. "
            "Assess whether what you are fighting for is still worth the cost."
        ),
        "element": "Fire", "astrology": "Mars in Leo", "numerology": 7,
        "image_key": "seven_of_wands",
    },
    {
        "id": 29, "name": "Eight of Wands", "suit": "wands", "number": 8, "arcana": "minor",
        "keywords_upright": ["speed", "swift action", "movement", "air travel", "communication", "momentum"],
        "keywords_reversed": ["delays", "frustration", "miscommunication", "slow progress", "waiting", "resisting change"],
        "meaning_upright": (
            "The Eight of Wands is pure velocity—everything is moving rapidly, events are accelerating, and the time for action is now. "
            "Communications arrive quickly; decisions must be made with confidence and without delay. "
            "Travel, rapid developments in a project, or a flurry of activity characterize this card. "
            "Go with the flow of this accelerated energy and act decisively; hesitation now will cause you to miss the wave."
        ),
        "meaning_reversed": (
            "Reversed, the Eight of Wands signals frustrating delays, miscommunication, or a situation that is moving far too slowly for your patience. "
            "Plans are stalling; messages are going astray; the momentum you counted on has evaporated. "
            "Resist the urge to force progress—understand the delay, address the miscommunication, and be prepared to act when the blockage clears. "
            "Patience is the medicine for this reversed card."
        ),
        "element": "Fire", "astrology": "Mercury in Sagittarius", "numerology": 8,
        "image_key": "eight_of_wands",
    },
    {
        "id": 30, "name": "Nine of Wands", "suit": "wands", "number": 9, "arcana": "minor",
        "keywords_upright": ["resilience", "last stand", "persistence", "test of faith", "boundaries", "stamina"],
        "keywords_reversed": ["exhaustion", "giving up", "paranoia", "rigid defensiveness", "burnout", "unable to continue"],
        "meaning_upright": (
            "The Nine of Wands is the battle-worn warrior who has fought long and hard and is nearly there. "
            "Wounded but unbroken, you are being asked to draw on the last reserves of your resilience for one final push. "
            "You have the strength to see this through, even when you feel you cannot take another step. "
            "Set firm boundaries, trust your experience, and hold on—victory is closer than it appears."
        ),
        "meaning_reversed": (
            "Reversed, the Nine of Wands indicates burnout, exhaustion so complete that continuing feels impossible, or a defensive posture so rigid it is now a prison. "
            "You may be so battle-scarred that you trust no one and see threats where none exist. "
            "Sometimes the bravest act is to lay down your weapon and accept help. "
            "Examine whether you are truly facing a threat or whether old wounds are distorting your perception of the present."
        ),
        "element": "Fire", "astrology": "Moon in Sagittarius", "numerology": 9,
        "image_key": "nine_of_wands",
    },
    {
        "id": 31, "name": "Ten of Wands", "suit": "wands", "number": 10, "arcana": "minor",
        "keywords_upright": ["burden", "responsibility", "overextension", "duty", "hard work", "overwhelm"],
        "keywords_reversed": ["releasing burden", "delegating", "avoiding responsibility", "burnout", "breakdown"],
        "meaning_upright": (
            "The Ten of Wands depicts a figure bent under the weight of ten heavy staves—a powerful image of overextension and the burden of too many responsibilities. "
            "You may have taken on more than one person can reasonably carry, or perhaps success itself has created an overwhelming list of obligations. "
            "The destination is in sight, but the weight is enormous. "
            "Consider what can be delegated, released, or renegotiated before the burden breaks you."
        ),
        "meaning_reversed": (
            "Reversed, the Ten of Wands signals that you are releasing a heavy burden, delegating effectively, or finally setting down what was never yours to carry. "
            "A period of excessive work or responsibility is coming to an end. "
            "Alternatively, this card reversed can indicate a complete avoidance of responsibility—refusing to do your fair share or collapsing entirely under the weight. "
            "Find the balance between doing too much and doing nothing at all."
        ),
        "element": "Fire", "astrology": "Saturn in Sagittarius", "numerology": 10,
        "image_key": "ten_of_wands",
    },
    {
        "id": 32, "name": "Page of Wands", "suit": "wands", "number": 11, "arcana": "minor",
        "keywords_upright": ["enthusiasm", "exploration", "discovery", "free spirit", "youthful energy", "new idea"],
        "keywords_reversed": ["immaturity", "hastiness", "lack of direction", "scattered energy", "naive"],
        "meaning_upright": (
            "The Page of Wands is the eager explorer—bursting with enthusiasm, curiosity, and an infectious love of new ideas and adventures. "
            "A new creative project, passion, or direction is calling to you with playful energy. "
            "Approach this with the Page's openness and willingness to experiment without the need for guaranteed outcomes. "
            "Let your enthusiasm be your guide and don't be afraid to begin before you feel fully ready."
        ),
        "meaning_reversed": (
            "Reversed, the Page of Wands suggests that enthusiasm has become scattered, immature, or misdirected. "
            "There may be a tendency to rush into things without adequate preparation, or to abandon projects at the first sign of difficulty. "
            "Creative ideas are abundant but follow-through is lacking. "
            "Ground your enthusiasm in a practical plan and commit to seeing at least one of your ideas through to completion."
        ),
        "element": "Fire", "astrology": None, "numerology": None,
        "image_key": "page_of_wands",
    },
    {
        "id": 33, "name": "Knight of Wands", "suit": "wands", "number": 12, "arcana": "minor",
        "keywords_upright": ["action", "adventure", "impulsiveness", "passion", "courage", "energy", "fearlessness"],
        "keywords_reversed": ["recklessness", "arrogance", "anger", "volatility", "scattered energy", "impatience"],
        "meaning_upright": (
            "The Knight of Wands charges forward with fearless, passionate energy—he is the embodiment of bold action, adventure, and the pursuit of excitement. "
            "When this knight appears, action is required; waiting is not an option. "
            "Channel your passion into bold moves, take the calculated risk, and move forward with confidence and flair. "
            "This is a time for adventure, for saying yes to the exciting and the unknown."
        ),
        "meaning_reversed": (
            "Reversed, the Knight of Wands becomes reckless, arrogant, and volatile—charging forward without wisdom, burning bridges, or igniting unnecessary conflict. "
            "Impulsiveness may be leading to poor decisions or unintended harm. "
            "Channel this fiery energy constructively; direct the passion into purposeful action rather than letting it scatter into chaos or aggression. "
            "Slow down enough to ensure your boldness is guided by wisdom."
        ),
        "element": "Fire", "astrology": "Sagittarius/Scorpio", "numerology": None,
        "image_key": "knight_of_wands",
    },
    {
        "id": 34, "name": "Queen of Wands", "suit": "wands", "number": 13, "arcana": "minor",
        "keywords_upright": ["confidence", "charisma", "passion", "determination", "warmth", "independence", "vibrancy"],
        "keywords_reversed": ["jealousy", "demanding", "self-centeredness", "controlling", "insecurity", "burnout"],
        "meaning_upright": (
            "The Queen of Wands radiates a magnetic confidence and warmth that draws people naturally to her. "
            "She is passionate, creative, and fiercely independent, yet generous in sharing her light with those she loves. "
            "This queen knows who she is and pursues her goals with assured, joyful determination. "
            "Embody her energy—lead with charisma, act with confidence, and inspire others through the sheer force of your authentic passion."
        ),
        "meaning_reversed": (
            "Reversed, the Queen of Wands loses her radiant confidence and becomes jealous, controlling, or driven by insecurity rather than genuine passion. "
            "Competitiveness may turn toxic, or the warmth of leadership may curdle into demanding, self-centered behavior. "
            "Burnout from overextending her fiery energy may be taking its toll. "
            "Return to the source of your genuine passion and confidence rather than performing them for external validation."
        ),
        "element": "Fire", "astrology": "Pisces/Aries", "numerology": None,
        "image_key": "queen_of_wands",
    },
    {
        "id": 35, "name": "King of Wands", "suit": "wands", "number": 14, "arcana": "minor",
        "keywords_upright": ["visionary", "leadership", "entrepreneur", "honor", "bold", "inspirational", "mastery"],
        "keywords_reversed": ["forceful", "vain", "tyrannical", "impulsive leadership", "ruthlessness", "ego-driven"],
        "meaning_upright": (
            "The King of Wands is the master entrepreneur and visionary leader—commanding, inspiring, and fiercely creative. "
            "He leads through the power of his passion and vision, motivating others not through fear but through the infectious energy of his purpose. "
            "This king acts with integrity, boldness, and a long-range view that transforms ideas into empires. "
            "Step into this energy—lead with vision, act with courage, and inspire those around you through the example of your own burning purpose."
        ),
        "meaning_reversed": (
            "Reversed, the King of Wands becomes domineering, impulsive, or ruled by ego rather than genuine vision. "
            "Leadership may turn tyrannical; the passion that once inspired now controls and demeans. "
            "Vanity, ruthlessness, or an inability to delegate may be undermining the very vision this king seeks to build. "
            "True leadership requires listening as much as leading; recalibrate before the force of your will drives away those who make your vision possible."
        ),
        "element": "Fire", "astrology": "Scorpio/Sagittarius", "numerology": None,
        "image_key": "king_of_wands",
    },

    # ── CUPS (Water) ── ids 36–49
    {
        "id": 36, "name": "Ace of Cups", "suit": "cups", "number": 1, "arcana": "minor",
        "keywords_upright": ["love", "new feelings", "emotional beginning", "compassion", "creativity", "intuition"],
        "keywords_reversed": ["emotional block", "repressed feelings", "emptiness", "creative drought", "self-love deficit"],
        "meaning_upright": (
            "The Ace of Cups is the overflowing vessel of divine love—an outpouring of emotional richness, new relationships, and creative inspiration. "
            "The heart is opening; love in its many forms is being offered to you. "
            "This is the beginning of a deeply meaningful emotional experience: a new relationship, a creative burst, or a profound spiritual awakening of the heart. "
            "Receive this love gratefully and let it flow through you and outward to the world."
        ),
        "meaning_reversed": (
            "Reversed, the Ace of Cups points to an emotional block—feelings are being suppressed, love is being withheld, or the heart has closed in self-protection. "
            "A creative or spiritual drought may be leaving you feeling emotionally empty. "
            "You may be struggling to give or receive love, or to open to new emotional beginnings because of past wounds. "
            "Tend gently to your heart; the love that feels unavailable is still there, waiting beneath the block."
        ),
        "element": "Water", "astrology": "Water signs (Cancer, Scorpio, Pisces)", "numerology": 1,
        "image_key": "ace_of_cups",
    },
    {
        "id": 37, "name": "Two of Cups", "suit": "cups", "number": 2, "arcana": "minor",
        "keywords_upright": ["partnership", "mutual attraction", "connection", "harmony", "unity", "love"],
        "keywords_reversed": ["disharmony", "imbalance in relationship", "broken bonds", "miscommunication", "separation"],
        "meaning_upright": (
            "The Two of Cups is the card of genuine partnership—the sacred exchange of love and energy between two people who truly see and honor each other. "
            "Whether romantic or platonic, this connection is characterized by mutual respect, attraction, and a deep sense of harmony and recognition. "
            "A partnership is forming or deepening; this is a moment of beautiful union and the beginning of something meaningful between equals. "
            "Honor this bond and the love it represents."
        ),
        "meaning_reversed": (
            "Reversed, the Two of Cups signals disharmony, imbalance, or a breakdown in communication within a close partnership. "
            "A relationship that was once characterized by mutual love and understanding may be experiencing friction, jealousy, or a loss of connection. "
            "Alternatively, this card reversed can indicate the difficult but necessary ending of a partnership that has run its natural course. "
            "Address the imbalance directly; honest communication is the bridge back to harmony."
        ),
        "element": "Water", "astrology": "Venus in Cancer", "numerology": 2,
        "image_key": "two_of_cups",
    },
    {
        "id": 38, "name": "Three of Cups", "suit": "cups", "number": 3, "arcana": "minor",
        "keywords_upright": ["celebration", "friendship", "community", "joy", "sisterhood", "abundance", "reunion"],
        "keywords_reversed": ["overindulgence", "gossip", "isolation", "superficial connections", "excess"],
        "meaning_upright": (
            "The Three of Cups is pure celebration—friends gathered to honor each other, raising their cups in joyful recognition of shared abundance and love. "
            "Community, friendship, and the warmth of genuine human connection are highlighted now. "
            "Celebrate with the people you love; allow yourself to receive the nourishment of community and the particular joy that comes from feeling truly seen and celebrated. "
            "This is a time for reunions, parties, and the deep pleasure of belonging."
        ),
        "meaning_reversed": (
            "Reversed, the Three of Cups warns of overindulgence, superficial connections, or a social circle that has become toxic with gossip and competition. "
            "You may be isolated from community when you need connection, or drowning in social obligations that leave you feeling emptier than before. "
            "Alternatively, excess in pleasure—whether food, drink, or the company of others—may be taking a toll. "
            "Seek genuine connection over social performance."
        ),
        "element": "Water", "astrology": "Mercury in Cancer", "numerology": 3,
        "image_key": "three_of_cups",
    },
    {
        "id": 39, "name": "Four of Cups", "suit": "cups", "number": 4, "arcana": "minor",
        "keywords_upright": ["contemplation", "apathy", "reevaluation", "disconnection", "meditation", "boredom"],
        "keywords_reversed": ["clarity emerging", "new motivation", "accepting opportunity", "ending withdrawal"],
        "meaning_upright": (
            "The Four of Cups depicts a figure so absorbed in contemplation—or apathy—that a new cup being offered by a divine hand goes unnoticed. "
            "You may be so focused on what you lack or what has disappointed you that you are missing the opportunities and blessings being offered right now. "
            "This card invites honest self-examination: is your contemplation productive soul-searching, or has it become comfortable avoidance of life? "
            "Look up from your inner world and notice what is being extended to you."
        ),
        "meaning_reversed": (
            "Reversed, the Four of Cups indicates that a period of withdrawal, apathy, or inner focus is ending. "
            "You are emerging from your shell of contemplation with renewed clarity and motivation. "
            "An opportunity that was previously overlooked is now being seen and seized. "
            "The fog of dissatisfaction is lifting; you are ready to re-engage with life and its offerings."
        ),
        "element": "Water", "astrology": "Moon in Cancer", "numerology": 4,
        "image_key": "four_of_cups",
    },
    {
        "id": 40, "name": "Five of Cups", "suit": "cups", "number": 5, "arcana": "minor",
        "keywords_upright": ["grief", "loss", "disappointment", "regret", "focusing on the negative", "mourning"],
        "keywords_reversed": ["acceptance", "moving on", "forgiveness", "finding silver lining", "emotional recovery"],
        "meaning_upright": (
            "The Five of Cups shows a figure mourning over three spilled cups while two full ones stand behind them, unseen. "
            "Loss, disappointment, and grief are real—the pain deserves to be honored, not rushed past. "
            "Yet this card also reminds you that not everything has been lost; what remains is significant if you can turn your gaze toward it. "
            "Allow yourself to grieve, but do not let mourning become a permanent residence."
        ),
        "meaning_reversed": (
            "Reversed, the Five of Cups signals that healing is underway—you are beginning to accept loss, turn toward what remains, and take tentative steps toward recovery. "
            "Forgiveness—of others or yourself—may be freeing you from emotional bondage. "
            "The perspective shift from focusing on what was lost to appreciating what remains marks the beginning of genuine emotional renewal. "
            "Let yourself move forward."
        ),
        "element": "Water", "astrology": "Mars in Scorpio", "numerology": 5,
        "image_key": "five_of_cups",
    },
    {
        "id": 41, "name": "Six of Cups", "suit": "cups", "number": 6, "arcana": "minor",
        "keywords_upright": ["nostalgia", "childhood", "innocence", "reunion", "past influences", "giving"],
        "keywords_reversed": ["living in the past", "stuck in nostalgia", "naivety", "moving forward", "leaving childhood behind"],
        "meaning_upright": (
            "The Six of Cups is a gentle return to the past—a time of nostalgia, reunion with old friends or places, and the innocent joy of childhood revisited. "
            "Old connections may be revived; gifts from the past—talents, memories, or relationships—are coming forward to offer their sweetness. "
            "There is healing available in honoring where you came from. "
            "Receive the gifts of the past with gratitude while remaining rooted in the present."
        ),
        "meaning_reversed": (
            "Reversed, the Six of Cups warns of being trapped in nostalgia—romanticizing the past to the extent that it prevents full engagement with the present. "
            "You may be comparing current relationships to idealized memories, or refusing to grow beyond the patterns of your early conditioning. "
            "Alternatively, this card reversed can indicate a necessary break from the past—a move away from old haunts or the liberation from childhood wounds. "
            "Honor the past without being imprisoned by it."
        ),
        "element": "Water", "astrology": "Sun in Scorpio", "numerology": 6,
        "image_key": "six_of_cups",
    },
    {
        "id": 42, "name": "Seven of Cups", "suit": "cups", "number": 7, "arcana": "minor",
        "keywords_upright": ["fantasy", "illusion", "wishful thinking", "choices", "temptation", "daydreaming"],
        "keywords_reversed": ["clarity", "chosen path", "realistic goals", "emerging from illusion", "decisiveness"],
        "meaning_upright": (
            "The Seven of Cups presents a dreamlike array of tempting visions—every desire seems equally attainable, every fantasy equally real. "
            "But beware: not all that glitters is gold, and wishful thinking divorced from practical action produces nothing. "
            "Important choices are before you, and the danger is being seduced by what looks appealing without discerning what is truly valuable. "
            "Get out of the clouds and ground your dreams in honest evaluation before choosing."
        ),
        "meaning_reversed": (
            "Reversed, the Seven of Cups brings welcome clarity after a period of confusion and fantasy. "
            "The fog of illusion is lifting; you are beginning to see which of your many dreams is genuinely worth pursuing. "
            "A decisive commitment to a clear path is available now. "
            "Use this moment of clarity to make concrete plans and take tangible steps toward what truly matters."
        ),
        "element": "Water", "astrology": "Venus in Scorpio", "numerology": 7,
        "image_key": "seven_of_cups",
    },
    {
        "id": 43, "name": "Eight of Cups", "suit": "cups", "number": 8, "arcana": "minor",
        "keywords_upright": ["walking away", "disillusionment", "abandonment", "seeking deeper meaning", "withdrawal"],
        "keywords_reversed": ["fear of moving on", "stagnation", "aimlessness", "returning to old situations"],
        "meaning_upright": (
            "The Eight of Cups shows a figure walking away under cover of night, leaving behind a carefully arranged stack of cups—all that was once valued—in search of something more meaningful. "
            "Something that once satisfied no longer does; the emotional investment has been depleted and the soul is calling you onward. "
            "This is a courageous and melancholy departure from what is safe and known in pursuit of deeper meaning. "
            "Trust the pull toward something more authentic, even if the path ahead is uncertain."
        ),
        "meaning_reversed": (
            "Reversed, the Eight of Cups suggests a fear of walking away, a return to a situation that no longer serves you, or aimless wandering without a clear sense of what you are seeking. "
            "You may know on some level that a situation needs to be left behind but cannot bring yourself to go. "
            "Alternatively, you may be in a period of searching without direction, unsure what the next cup even looks like. "
            "Clarify what you are truly seeking before taking the next step."
        ),
        "element": "Water", "astrology": "Saturn in Pisces", "numerology": 8,
        "image_key": "eight_of_cups",
    },
    {
        "id": 44, "name": "Nine of Cups", "suit": "cups", "number": 9, "arcana": "minor",
        "keywords_upright": ["contentment", "satisfaction", "gratitude", "wish fulfilled", "emotional well-being", "pleasure"],
        "keywords_reversed": ["greed", "dissatisfaction", "materialism", "overindulgence", "inner happiness lacking"],
        "meaning_upright": (
            "The Nine of Cups is the classic 'wish card'—a moment of genuine contentment where you can look at your life and feel deeply satisfied with what you have created. "
            "Your emotional needs are being met; the things you have wished for are manifesting or have already arrived. "
            "Allow yourself to fully enjoy this satisfaction without guilt or anxiety. "
            "Gratitude for what is amplifies the abundance that surrounds you."
        ),
        "meaning_reversed": (
            "Reversed, the Nine of Cups reveals that despite apparent material success or the fulfillment of surface wishes, a deeper dissatisfaction persists. "
            "Overindulgence, greed, or the pursuit of the wrong goals may have left you hollow. "
            "The things you thought would make you happy have not delivered the contentment you expected. "
            "Look inward; the fulfillment you seek is not found in acquiring more but in deepening your relationship with what truly matters."
        ),
        "element": "Water", "astrology": "Jupiter in Pisces", "numerology": 9,
        "image_key": "nine_of_cups",
    },
    {
        "id": 45, "name": "Ten of Cups", "suit": "cups", "number": 10, "arcana": "minor",
        "keywords_upright": ["divine love", "happy family", "harmony", "alignment", "fulfillment", "bliss", "abundance"],
        "keywords_reversed": ["broken family", "misalignment of values", "unhappy home", "disrupted harmony"],
        "meaning_upright": (
            "The Ten of Cups is a vision of complete emotional fulfillment—the rainbow family, the loving home, the sense that all is right with the world and with those you love. "
            "This is the culmination of the emotional journey: deep belonging, shared joy, and the quiet certainty that you are exactly where you are meant to be. "
            "Cherish what you have built with the people you love; this is the heart's truest wealth. "
            "Genuine happiness in relationship and home is available now."
        ),
        "meaning_reversed": (
            "Reversed, the Ten of Cups points to disruptions in family harmony, misaligned values in close relationships, or an inability to experience the happiness that should be present. "
            "The ideal of the loving home may be clashing painfully with reality. "
            "There may be rifts in family, a misalignment between your inner emotional state and your outer circumstances, or a deep longing for the belonging that feels just out of reach. "
            "Address the source of the discord; true harmony is built through honest love, not performed perfection."
        ),
        "element": "Water", "astrology": "Mars in Pisces", "numerology": 10,
        "image_key": "ten_of_cups",
    },
    {
        "id": 46, "name": "Page of Cups", "suit": "cups", "number": 11, "arcana": "minor",
        "keywords_upright": ["creative opportunities", "intuitive messages", "curiosity", "sensitivity", "playfulness"],
        "keywords_reversed": ["emotional immaturity", "blocked creativity", "escapism", "moodiness", "unrealistic"],
        "meaning_upright": (
            "The Page of Cups is the dreamy, sensitive, creative soul—open to intuitive messages, unexpected inspiration, and the magic of emotional curiosity. "
            "A surprising emotional or creative message may arrive; be open to the unusual and the whimsical. "
            "This page invites you to approach life with the openness of a child who still believes in magic. "
            "Trust your intuitive hits and don't dismiss the creative impulses that arise from the depths of feeling."
        ),
        "meaning_reversed": (
            "Reversed, the Page of Cups becomes emotionally immature, prone to escapism, or blocked in their creative and intuitive channels. "
            "Moodiness, unrealistic fantasies, or a tendency to let feelings rule all decisions without grounding in reality may be creating problems. "
            "Alternatively, the rich inner world of intuition and creativity may be suppressed by fear or shame. "
            "Find a safe, structured way to honor your emotional sensitivity while developing the maturity to navigate the world with it."
        ),
        "element": "Water", "astrology": None, "numerology": None,
        "image_key": "page_of_cups",
    },
    {
        "id": 47, "name": "Knight of Cups", "suit": "cups", "number": 12, "arcana": "minor",
        "keywords_upright": ["romantic", "idealistic", "charm", "following the heart", "artistic", "graceful"],
        "keywords_reversed": ["moodiness", "unrealistic", "jealousy", "emotional manipulation", "escapism"],
        "meaning_upright": (
            "The Knight of Cups rides forward with romantic idealism and artistic grace—he is the poet, the lover, the dreamer who follows his heart wherever it leads. "
            "This knight brings an invitation: to a new romance, a creative project, or a vision worth pursuing with passion and imagination. "
            "Approach life and love with an open heart, leading with feeling and trusting that beauty and meaning can be found in the journey. "
            "Follow the heart's call."
        ),
        "meaning_reversed": (
            "Reversed, the Knight of Cups loses his grace and becomes moody, manipulative, or lost in escapist fantasies. "
            "The romantic idealism that was charming now tips into jealousy, neediness, or an inability to function when reality doesn't match the dream. "
            "There may be a tendency to manipulate emotions—yours or others'—to create the feeling of romance rather than the real thing. "
            "Ground your feelings in honesty and ensure your heart's guidance is trustworthy before following it blindly."
        ),
        "element": "Water", "astrology": "Pisces/Aquarius", "numerology": None,
        "image_key": "knight_of_cups",
    },
    {
        "id": 48, "name": "Queen of Cups", "suit": "cups", "number": 13, "arcana": "minor",
        "keywords_upright": ["compassion", "intuition", "emotional intelligence", "nurturing", "empathy", "wisdom"],
        "keywords_reversed": ["emotional insecurity", "co-dependency", "martyrdom", "manipulation", "over-emotional"],
        "meaning_upright": (
            "The Queen of Cups is the embodiment of emotional intelligence and compassionate wisdom—she feels deeply, intuits accurately, and nurtures with profound understanding. "
            "She is a gifted healer and counselor because she has made peace with her own depths. "
            "Approach your relationships and emotional life with this queen's grace—listen with full presence, trust your intuition, and offer care that truly nourishes. "
            "Your empathy is a gift; use it wisely."
        ),
        "meaning_reversed": (
            "Reversed, the Queen of Cups becomes enmeshed in emotional dependency, martyrdom, or the use of empathy as manipulation. "
            "Boundaries may have dissolved in relationships, leaving you drained and resentful. "
            "Emotional insecurity may be driving you to seek constant validation or to play the victim role. "
            "Reconnect with your own emotional truth and establish healthy boundaries that allow you to care without losing yourself."
        ),
        "element": "Water", "astrology": "Gemini/Cancer", "numerology": None,
        "image_key": "queen_of_cups",
    },
    {
        "id": 49, "name": "King of Cups", "suit": "cups", "number": 14, "arcana": "minor",
        "keywords_upright": ["emotional maturity", "compassionate leadership", "wisdom", "balance", "diplomacy", "calm"],
        "keywords_reversed": ["emotional manipulation", "moodiness", "repression", "coldness", "cruelty", "volatility"],
        "meaning_upright": (
            "The King of Cups has mastered his emotional world—he feels deeply but is not ruled by feeling, maintaining dignity and calm even in the stormiest of circumstances. "
            "He leads with compassion, diplomacy, and a wisdom born from genuine emotional experience. "
            "Embody this king's balanced authority—let your decisions be informed by both feeling and reason, and lead others with the kind of steady care that creates lasting trust. "
            "Emotional mastery is your superpower."
        ),
        "meaning_reversed": (
            "Reversed, the King of Cups loses his mastery and becomes emotionally manipulative, volatile, or completely shut down. "
            "Repression of deep feelings may explode into dramatic emotional outbursts or manifest as a cold, calculating cruelty. "
            "Someone in your life—or a part of yourself—may be using emotional intelligence not to connect but to control. "
            "True emotional mastery requires the courage to feel honestly; reconnect with your genuine emotional experience before you can lead from a place of wisdom."
        ),
        "element": "Water", "astrology": "Libra/Scorpio", "numerology": None,
        "image_key": "king_of_cups",
    },

    # ── SWORDS (Air) ── ids 50–63
    {
        "id": 50, "name": "Ace of Swords", "suit": "swords", "number": 1, "arcana": "minor",
        "keywords_upright": ["breakthrough", "clarity", "truth", "sharp mind", "new idea", "justice", "communication"],
        "keywords_reversed": ["confusion", "false truth", "miscommunication", "brutality", "mental block"],
        "meaning_upright": (
            "The Ace of Swords is the flash of pure clarity—a mental breakthrough, a truth that cuts through confusion with brilliant precision. "
            "A new idea, a powerful decision, or a moment of honest reckoning is available to you. "
            "The mind is at its sharpest; use this clarity to cut through illusion, speak your truth, and act with intellectual conviction. "
            "This sword is a tool of liberation when wielded with integrity."
        ),
        "meaning_reversed": (
            "Reversed, the Ace of Swords indicates confusion, mental fog, or a truth that is being distorted or weaponized. "
            "Communication may be sharp but dishonest—cutting with cruelty rather than clarity. "
            "A mental block is preventing the breakthrough that is needed. "
            "Slow down, question your assumptions, and ensure that the truth you are wielding is genuinely in service of understanding rather than destruction."
        ),
        "element": "Air", "astrology": "Air signs (Gemini, Libra, Aquarius)", "numerology": 1,
        "image_key": "ace_of_swords",
    },
    {
        "id": 51, "name": "Two of Swords", "suit": "swords", "number": 2, "arcana": "minor",
        "keywords_upright": ["indecision", "stalemate", "avoidance", "difficult choices", "blocked information"],
        "keywords_reversed": ["indecision resolved", "information revealed", "confusion", "lesser of evils", "making a choice"],
        "meaning_upright": (
            "The Two of Swords depicts a blindfolded figure holding two balanced swords—a classic stalemate of indecision, where both options feel equally weighted and the choice is paralyzed. "
            "You may be avoiding a necessary decision, keeping yourself deliberately in the dark rather than facing uncomfortable information. "
            "The impasse will not resolve itself; you must be willing to remove the blindfold and see the situation clearly. "
            "Choose, even if imperfectly—staying suspended is the most costly option."
        ),
        "meaning_reversed": (
            "Reversed, the Two of Swords indicates that a long period of indecision is resolving—perhaps because new information has emerged or the stakes of not choosing have become undeniable. "
            "The blindfold is coming off; clarity, though uncomfortable, is available. "
            "Make the choice that your honest assessment demands, even if both options carry costs. "
            "Action, however imperfect, is better than continued paralysis."
        ),
        "element": "Air", "astrology": "Moon in Libra", "numerology": 2,
        "image_key": "two_of_swords",
    },
    {
        "id": 52, "name": "Three of Swords", "suit": "swords", "number": 3, "arcana": "minor",
        "keywords_upright": ["heartbreak", "grief", "sorrow", "rejection", "loss", "pain", "separation"],
        "keywords_reversed": ["recovery", "forgiveness", "healing grief", "releasing pain", "moving on"],
        "meaning_upright": (
            "The Three of Swords is one of the tarot's most direct expressions of pain: three swords piercing a heart, rain falling, storm clouds gathered. "
            "Heartbreak, loss, betrayal, or deep sorrow are present; there is no sugarcoating this card's message. "
            "Allow yourself to feel the grief fully—healing requires acknowledgment, not avoidance. "
            "This storm will pass, but only if you do not fight the rain."
        ),
        "meaning_reversed": (
            "Reversed, the Three of Swords signals that the acute phase of pain is beginning to ease. "
            "Healing is underway; the swords are slowly being removed from the heart. "
            "Forgiveness—of yourself or another—is opening the door to genuine recovery. "
            "You are not yet fully healed, but the turning point has been reached. "
            "Allow the healing to proceed at its own pace without forcing closure before it's ready."
        ),
        "element": "Air", "astrology": "Saturn in Libra", "numerology": 3,
        "image_key": "three_of_swords",
    },
    {
        "id": 53, "name": "Four of Swords", "suit": "swords", "number": 4, "arcana": "minor",
        "keywords_upright": ["rest", "recuperation", "contemplation", "passive healing", "peace", "sanctuary"],
        "keywords_reversed": ["restlessness", "returning to activity", "burnout", "refusal to rest", "awakening"],
        "meaning_upright": (
            "The Four of Swords is a welcome pause after battle—a deliberate retreat into rest, recuperation, and quiet contemplation. "
            "Your nervous system, body, and mind need genuine restoration before the next engagement. "
            "This is not laziness but strategic recovery: the warrior who rests between battles fights better and lasts longer. "
            "Give yourself permission to stop, to be still, to let the body and mind heal."
        ),
        "meaning_reversed": (
            "Reversed, the Four of Swords suggests restlessness in rest—an inability to settle, a refusal to honor the need for recovery, or an impulsive return to activity before healing is complete. "
            "Alternatively, this card reversed can indicate an awakening from a period of necessary retreat—you are ready to re-engage with life. "
            "Ensure the rest was sufficient before stepping back into the fray; half-healed warriors make poor soldiers."
        ),
        "element": "Air", "astrology": "Jupiter in Libra", "numerology": 4,
        "image_key": "four_of_swords",
    },
    {
        "id": 54, "name": "Five of Swords", "suit": "swords", "number": 5, "arcana": "minor",
        "keywords_upright": ["conflict", "defeat", "winning at all costs", "hollow victory", "betrayal", "tension"],
        "keywords_reversed": ["reconciliation", "moving past conflict", "letting go", "desire for peace", "consequences"],
        "meaning_upright": (
            "The Five of Swords shows the aftermath of a conflict where someone has won, but at great cost—the victory is hollow because it came through betrayal, cruelty, or the defeat of those who mattered. "
            "Not every battle is worth fighting, and winning at all costs may cost you more than losing would have. "
            "Examine your role in current conflicts: are you engaging with honor or resorting to tactics that compromise your integrity? "
            "Even victory can be a form of loss."
        ),
        "meaning_reversed": (
            "Reversed, the Five of Swords suggests a desire for reconciliation after conflict, a willingness to let go of the need to win, or facing the consequences of past aggressive actions. "
            "Peace is possible, but it requires someone to make the first move toward genuine understanding rather than victory. "
            "The conflict may also be winding down on its own as both parties exhaust their fighting energy. "
            "Choose reconciliation over revenge."
        ),
        "element": "Air", "astrology": "Venus in Aquarius", "numerology": 5,
        "image_key": "five_of_swords",
    },
    {
        "id": 55, "name": "Six of Swords", "suit": "swords", "number": 6, "arcana": "minor",
        "keywords_upright": ["transition", "moving on", "healing journey", "travel", "change of scene", "recovery"],
        "keywords_reversed": ["resistance to change", "unable to move on", "returning to trouble", "unfinished business"],
        "meaning_upright": (
            "The Six of Swords is the gentle transit across troubled waters to calmer shores—a transition away from difficulty and toward healing, even if the destination is not yet fully visible. "
            "This card signals that things are getting better, even if slowly; you are moving in the right direction. "
            "Travel, change of environment, or a necessary departure from a difficult situation is supported now. "
            "Trust the journey; the waters are calming ahead."
        ),
        "meaning_reversed": (
            "Reversed, the Six of Swords indicates resistance to the necessary transition, an inability to leave the troubled waters behind, or a return to a difficult situation after having briefly escaped it. "
            "Unfinished business may be pulling you back to where you came from. "
            "Alternatively, the turbulence of transition itself may feel overwhelming, even though forward is the only direction that leads to peace. "
            "Release what you are clutching and allow yourself to be carried forward."
        ),
        "element": "Air", "astrology": "Mercury in Aquarius", "numerology": 6,
        "image_key": "six_of_swords",
    },
    {
        "id": 56, "name": "Seven of Swords", "suit": "swords", "number": 7, "arcana": "minor",
        "keywords_upright": ["deception", "betrayal", "strategy", "getting away with something", "cunning", "stealth"],
        "keywords_reversed": ["confession", "coming clean", "conscience", "recklessness", "caught out"],
        "meaning_upright": (
            "The Seven of Swords is the card of the fox—clever, strategic, but not always operating with full integrity. "
            "Someone may be deceiving you, cutting corners, or getting away with something that won't hold. "
            "Alternatively, you yourself may be tempted to use cunning over honesty—to take what you want covertly rather than asking openly. "
            "The short-term gain of deception rarely outweighs the long-term cost when the truth inevitably surfaces. "
            "Act with strategic intelligence, but not at the expense of your integrity."
        ),
        "meaning_reversed": (
            "Reversed, the Seven of Swords indicates that a deception is coming to light—someone is being caught out, or a guilty conscience is compelling a confession. "
            "Alternatively, reckless behavior that lacks even the Seven's cunning is creating unnecessary chaos. "
            "If you have been operating with less than full honesty, now is the time to come clean before the truth is exposed on someone else's terms. "
            "Integrity now will cost less than the eventual price of continued deception."
        ),
        "element": "Air", "astrology": "Moon in Aquarius", "numerology": 7,
        "image_key": "seven_of_swords",
    },
    {
        "id": 57, "name": "Eight of Swords", "suit": "swords", "number": 8, "arcana": "minor",
        "keywords_upright": ["restriction", "imprisonment", "self-doubt", "victim mentality", "helplessness", "trapped"],
        "keywords_reversed": ["release", "freedom", "new perspective", "taking control", "empowerment", "clarity"],
        "meaning_upright": (
            "The Eight of Swords depicts a bound and blindfolded figure surrounded by swords—yet none of the swords actually touch her, and she could walk away if she removed the blindfold. "
            "The prison is largely mental: self-doubt, limiting beliefs, or a victim mentality has convinced you that you are trapped when you are not. "
            "The constraints you feel are real in your experience, but they are not as absolute as they appear. "
            "Question the beliefs that are keeping you bound; freedom begins in the mind."
        ),
        "meaning_reversed": (
            "Reversed, the Eight of Swords signals liberation—the blindfold is coming off, the mental prison is dissolving, and you are beginning to see the ways out that were always there. "
            "Self-awareness is empowering you to take responsibility for your situation and make choices that were previously invisible to you. "
            "Step out of the victim story and into your genuine agency. "
            "Freedom is available now; claim it."
        ),
        "element": "Air", "astrology": "Jupiter in Gemini", "numerology": 8,
        "image_key": "eight_of_swords",
    },
    {
        "id": 58, "name": "Nine of Swords", "suit": "swords", "number": 9, "arcana": "minor",
        "keywords_upright": ["anxiety", "nightmares", "worry", "fear", "despair", "dread", "mental anguish"],
        "keywords_reversed": ["hope after despair", "releasing anxiety", "seeking help", "healing nightmares", "dawn breaking"],
        "meaning_upright": (
            "The Nine of Swords is the 3 AM panic—the dark thoughts that spiral in the sleepless night, the anxiety that magnifies every fear into catastrophe. "
            "The mind has turned on itself; worry and dread have taken up residence in your head and are running the show. "
            "While the fears feel absolutely real, this card reminds you that the mind's nighttime stories are not always reliable narrators of reality. "
            "Seek support, break the cycle of rumination, and remember that daylight will come."
        ),
        "meaning_reversed": (
            "Reversed, the Nine of Swords signals that the worst of the mental anguish is passing—the grip of anxiety is loosening, and hope is beginning to flicker through. "
            "You may be reaching out for help, challenging the catastrophic narratives your mind has been telling, or finding the courage to face rather than avoid your fears. "
            "The darkest hour is before the dawn; hold on. "
            "Dawn is breaking."
        ),
        "element": "Air", "astrology": "Mars in Gemini", "numerology": 9,
        "image_key": "nine_of_swords",
    },
    {
        "id": 59, "name": "Ten of Swords", "suit": "swords", "number": 10, "arcana": "minor",
        "keywords_upright": ["painful ending", "betrayal", "collapse", "defeat", "hitting rock bottom", "loss"],
        "keywords_reversed": ["recovery", "regeneration", "resisting inevitable end", "fear of ruin", "surviving crisis"],
        "meaning_upright": (
            "The Ten of Swords depicts the most dramatic ending in the tarot—a figure lying face down, ten swords in their back, yet the sky above shows the first light of dawn. "
            "A painful ending, betrayal, or collapse is complete; there is nowhere further to fall. "
            "As devastating as this is, the Ten of Swords marks the absolute bottom—which means the only direction from here is up. "
            "Something has ended irrevocably; let it be over, grieve it, and prepare for the sunrise that is already beginning."
        ),
        "meaning_reversed": (
            "Reversed, the Ten of Swords suggests either a recovery from a devastating blow—the swords being slowly removed and healing beginning—or a resistance to the inevitable ending that is still coming. "
            "You may be refusing to acknowledge that something is truly over, prolonging your suffering by fighting what cannot be changed. "
            "Alternatively, you have survived the worst and are beginning the long road back. "
            "Accept the ending; the dawn is already breaking beyond what you can currently see."
        ),
        "element": "Air", "astrology": "Sun in Gemini", "numerology": 10,
        "image_key": "ten_of_swords",
    },
    {
        "id": 60, "name": "Page of Swords", "suit": "swords", "number": 11, "arcana": "minor",
        "keywords_upright": ["curious", "talkative", "restless", "mental agility", "news", "vigilance", "ideas"],
        "keywords_reversed": ["gossip", "hasty words", "scattered thinking", "all talk no action", "deceptive"],
        "meaning_upright": (
            "The Page of Swords is the keen-eyed scout—alert, curious, and quick to communicate what they observe. "
            "New information or a message that requires careful attention may arrive. "
            "This page has a razor-sharp mind and an eagerness to learn that is admirable; the challenge is channeling that mental energy into focused thought rather than scattered analysis. "
            "Stay alert, gather information, and think before you speak."
        ),
        "meaning_reversed": (
            "Reversed, the Page of Swords becomes the gossip—all talk and no action, spreading half-truths or using information as a weapon. "
            "Scattered, restless thinking that never lands on anything solid may be creating confusion. "
            "Guard against speaking before you have thought carefully; words are powerful and this page's tongue can cut. "
            "Slow down, verify information, and commit to communicating with genuine honesty."
        ),
        "element": "Air", "astrology": None, "numerology": None,
        "image_key": "page_of_swords",
    },
    {
        "id": 61, "name": "Knight of Swords", "suit": "swords", "number": 12, "arcana": "minor",
        "keywords_upright": ["ambitious", "action-oriented", "driven", "fast-moving", "assertive", "courageous"],
        "keywords_reversed": ["reckless", "ruthless", "scattered energy", "argumentative", "burning bridges"],
        "meaning_upright": (
            "The Knight of Swords charges forward with breathtaking speed and single-minded conviction—nothing will stop this knight from reaching his objective. "
            "Decisive action, bold communication, and a willingness to cut through obstacles with intellectual precision are all available to you now. "
            "The momentum this knight brings is tremendous; use it to advance your goals with courage and clarity. "
            "Act swiftly and decisively before the window closes."
        ),
        "meaning_reversed": (
            "Reversed, the Knight of Swords becomes reckless, argumentative, and destructive—charging into battles that don't need to be fought and leaving wreckage in the wake of his speed. "
            "Words may be weaponized; bridges may be burned in the pursuit of being right. "
            "Slow the charge enough to ensure your actions are guided by wisdom and not just adrenaline. "
            "Speed without direction creates chaos, not progress."
        ),
        "element": "Air", "astrology": "Taurus/Gemini", "numerology": None,
        "image_key": "knight_of_swords",
    },
    {
        "id": 62, "name": "Queen of Swords", "suit": "swords", "number": 13, "arcana": "minor",
        "keywords_upright": ["sharp mind", "honest", "direct", "perceptive", "independent", "clear boundaries"],
        "keywords_reversed": ["cold", "cruel", "bitter", "overly critical", "manipulation through intellect"],
        "meaning_upright": (
            "The Queen of Swords has earned her clear-eyed wisdom through experience, loss, and the hard work of facing truth without flinching. "
            "She is direct, perceptive, and unapologetically honest—not to wound, but because she knows that truth is ultimately more merciful than comfortable illusions. "
            "Embody her energy: cut through the noise with clarity, enforce your boundaries with dignity, and trust the intelligence of your own perception. "
            "Her wisdom is yours to claim."
        ),
        "meaning_reversed": (
            "Reversed, the Queen of Swords becomes cold, bitter, or uses her sharp intelligence as a weapon of cruelty rather than truth. "
            "Past pain may have calcified into a bitterness that now distorts her perception and poisons her communication. "
            "Alternatively, overly critical judgment—of yourself or others—may be shutting down genuine connection. "
            "The sword of the mind should serve understanding, not isolation; reconnect with the compassion that makes truth bearable."
        ),
        "element": "Air", "astrology": "Virgo/Libra", "numerology": None,
        "image_key": "queen_of_swords",
    },
    {
        "id": 63, "name": "King of Swords", "suit": "swords", "number": 14, "arcana": "minor",
        "keywords_upright": ["intellectual authority", "truth", "ethics", "reason", "structure", "judgment", "clear communication"],
        "keywords_reversed": ["tyranny", "manipulation", "abuse of power", "coldness", "dishonesty", "cruelty"],
        "meaning_upright": (
            "The King of Swords sits in judgment with a mind as sharp as his blade and a commitment to truth and justice that never wavers. "
            "He represents the highest expression of intellect: clear, ethical, decisive, and utterly reliable. "
            "Lead with reason and integrity; communicate with clarity and directness; let your decisions be guided by principle rather than emotion or personal gain. "
            "His authority is earned through the consistent exercise of honest, disciplined thought."
        ),
        "meaning_reversed": (
            "Reversed, the King of Swords becomes a tyrant of the intellect—using his analytical power to manipulate, control, or destroy rather than to serve truth. "
            "Dishonesty dressed in the language of reason, or the weaponization of logic against those who cannot match his intellectual resources, marks this king at his worst. "
            "Cold, calculating cruelty is possible here. "
            "Examine whether your intellect is serving justice or your ego; the sword of reason must always be wielded in service of truth."
        ),
        "element": "Air", "astrology": "Capricorn/Aquarius", "numerology": None,
        "image_key": "king_of_swords",
    },

    # ── PENTACLES (Earth) ── ids 64–77
    {
        "id": 64, "name": "Ace of Pentacles", "suit": "pentacles", "number": 1, "arcana": "minor",
        "keywords_upright": ["new financial opportunity", "manifestation", "abundance", "security", "prosperity", "potential"],
        "keywords_reversed": ["lost opportunity", "poor planning", "greed", "financial insecurity", "instability"],
        "meaning_upright": (
            "The Ace of Pentacles is the golden coin dropped into an outstretched hand—an opportunity for material prosperity, financial growth, or a new beginning in the physical realm. "
            "A new job, business venture, investment, or physical project is calling to you with the promise of real, tangible results. "
            "The seeds of abundance are being planted; tend them with practical wisdom and consistent effort. "
            "The potential for genuine material security and prosperity is present."
        ),
        "meaning_reversed": (
            "Reversed, the Ace of Pentacles warns of a missed or mismanaged financial opportunity, poor planning, or a tendency to pursue wealth through greed rather than genuine value creation. "
            "Material instability may be present; the foundation you thought you were building is less secure than it appears. "
            "Examine your relationship with money and resources; are you approaching material matters with the care and practicality they require?"
        ),
        "element": "Earth", "astrology": "Earth signs (Taurus, Virgo, Capricorn)", "numerology": 1,
        "image_key": "ace_of_pentacles",
    },
    {
        "id": 65, "name": "Two of Pentacles", "suit": "pentacles", "number": 2, "arcana": "minor",
        "keywords_upright": ["balance", "adaptability", "juggling priorities", "time management", "flexibility"],
        "keywords_reversed": ["imbalance", "disorganized", "overwhelmed", "financial difficulties", "poor priorities"],
        "meaning_upright": (
            "The Two of Pentacles depicts a figure skillfully juggling two coins while ships navigate turbulent waters behind him—the art of maintaining balance amid constant motion and competing demands. "
            "You are managing multiple responsibilities or financial considerations simultaneously; the key is to stay light on your feet and adapt as circumstances change. "
            "Flexibility and a sense of humor about life's inevitable juggling act will carry you through. "
            "Keep the balls in the air without gripping too tightly."
        ),
        "meaning_reversed": (
            "Reversed, the Two of Pentacles signals that the juggling act is becoming unsustainable—things are being dropped, priorities are unclear, and the balancing act is causing stress rather than demonstrating skill. "
            "Financial disorganization or an inability to manage competing demands effectively may be creating real problems. "
            "Simplify, prioritize ruthlessly, and seek practical help before the overwhelm becomes a crisis."
        ),
        "element": "Earth", "astrology": "Jupiter in Capricorn", "numerology": 2,
        "image_key": "two_of_pentacles",
    },
    {
        "id": 66, "name": "Three of Pentacles", "suit": "pentacles", "number": 3, "arcana": "minor",
        "keywords_upright": ["teamwork", "collaboration", "craftsmanship", "skill", "planning", "building"],
        "keywords_reversed": ["disharmony in team", "poor teamwork", "lack of skill", "mediocrity", "conflict"],
        "meaning_upright": (
            "The Three of Pentacles celebrates the power of skillful collaboration—the architect, the master craftsman, and the patron working together, each contributing their unique expertise to create something greater than any individual could achieve alone. "
            "Teamwork, the application of genuine skill, and pride in quality craftsmanship are the themes here. "
            "Embrace collaboration; your skills are recognized and valued, and working with others will produce results that honor everyone's contribution."
        ),
        "meaning_reversed": (
            "Reversed, the Three of Pentacles signals a breakdown in collaboration—team dynamics are fractured, skills are not being applied effectively, or quality is being sacrificed for speed or cost. "
            "Conflict within a working group or a refusal to collaborate with those who have different approaches may be limiting what can be achieved. "
            "Recommit to the shared vision and the standard of excellence that comes when everyone is rowing in the same direction."
        ),
        "element": "Earth", "astrology": "Mars in Capricorn", "numerology": 3,
        "image_key": "three_of_pentacles",
    },
    {
        "id": 67, "name": "Four of Pentacles", "suit": "pentacles", "number": 4, "arcana": "minor",
        "keywords_upright": ["security", "control", "conservatism", "scarcity mindset", "stability", "possessiveness"],
        "keywords_reversed": ["generosity", "releasing control", "financial insecurity", "reckless spending", "letting go"],
        "meaning_upright": (
            "The Four of Pentacles shows a figure clutching his coins possessively—one on his crown, one under each foot, one gripped in his hands—blocking himself from the flow of life in his determination to hold on to what he has. "
            "Financial security and careful stewardship of resources is wise; excessive hoarding, a scarcity mindset, or using money as a form of control is a limitation. "
            "Examine whether your relationship with money and security is one of healthy prudence or fearful constriction."
        ),
        "meaning_reversed": (
            "Reversed, the Four of Pentacles can indicate either a welcome release from a miserly grip on resources—generosity emerging—or a reckless swinging to the opposite extreme of uncontrolled spending. "
            "Financial insecurity may be causing anxiety, or you may be loosening your grip in a healthy way as security increases. "
            "Find the generous middle ground between holding too tightly and giving too freely."
        ),
        "element": "Earth", "astrology": "Sun in Capricorn", "numerology": 4,
        "image_key": "four_of_pentacles",
    },
    {
        "id": 68, "name": "Five of Pentacles", "suit": "pentacles", "number": 5, "arcana": "minor",
        "keywords_upright": ["hardship", "poverty", "insecurity", "isolation", "worry", "financial loss", "adversity"],
        "keywords_reversed": ["recovery", "finding support", "spiritual poverty", "improving finances", "renewed hope"],
        "meaning_upright": (
            "The Five of Pentacles depicts two figures huddled in the cold, passing a warmly lit church window—outside of the warmth and community that could offer them shelter. "
            "Financial hardship, material insecurity, or a sense of profound lack is present. "
            "Yet the card also asks: are you so focused on your suffering that you cannot see the help that is available nearby? "
            "Reach out; support exists, but you must be willing to accept it."
        ),
        "meaning_reversed": (
            "Reversed, the Five of Pentacles signals recovery from hardship—finances are beginning to stabilize, support has been found and accepted, and the worst of the material difficulty may be passing. "
            "Alternatively, this card reversed can point to a spiritual poverty that persists even when material needs are met. "
            "Reconnect with community, seek the help that is available, and allow yourself to receive."
        ),
        "element": "Earth", "astrology": "Mercury in Taurus", "numerology": 5,
        "image_key": "five_of_pentacles",
    },
    {
        "id": 69, "name": "Six of Pentacles", "suit": "pentacles", "number": 6, "arcana": "minor",
        "keywords_upright": ["generosity", "sharing wealth", "charity", "gratitude", "giving and receiving", "fairness"],
        "keywords_reversed": ["strings attached", "inequality", "power imbalance", "debt", "selfishness"],
        "meaning_upright": (
            "The Six of Pentacles depicts a prosperous merchant weighing coins before distributing them to those in need—the balanced flow of generosity and gratitude. "
            "Give what you have in abundance; receive what is offered with grace. "
            "The healthy circulation of resources—whether financial, emotional, or material—creates a generative loop of prosperity. "
            "This card affirms that generosity is both ethical and energetically sound."
        ),
        "meaning_reversed": (
            "Reversed, the Six of Pentacles warns of generosity with strings attached, a power imbalance in giving and receiving, or the use of charity as a means of control. "
            "Someone may be giving in order to hold power over the recipient, or there may be a sense that gifts come with unspoken obligations. "
            "Examine the dynamics of exchange in your life; true generosity is given freely, without expectation of control or return."
        ),
        "element": "Earth", "astrology": "Moon in Taurus", "numerology": 6,
        "image_key": "six_of_pentacles",
    },
    {
        "id": 70, "name": "Seven of Pentacles", "suit": "pentacles", "number": 7, "arcana": "minor",
        "keywords_upright": ["assessment", "patience", "long-term vision", "investment", "perseverance", "harvest"],
        "keywords_reversed": ["lack of growth", "impatience", "missed opportunities", "poor investment", "scattered effort"],
        "meaning_upright": (
            "The Seven of Pentacles shows a farmer pausing to assess his growing crop—a moment of honest evaluation of what his sustained effort has produced. "
            "You have put in real work, and the results are beginning to materialize; now is the time to step back and assess whether your investment of time, energy, or money is yielding the returns you hoped for. "
            "Patience is required; meaningful results take time. "
            "Stay the course if the growth is promising, or redirect if honest assessment reveals the investment is not bearing fruit."
        ),
        "meaning_reversed": (
            "Reversed, the Seven of Pentacles signals frustration with slow progress, a poor investment that is not yielding returns, or impatience that is leading to premature abandonment of a promising endeavor. "
            "Scattered effort without focused commitment may be preventing the harvest. "
            "Honestly assess whether to persist or pivot, then commit fully to the chosen course."
        ),
        "element": "Earth", "astrology": "Saturn in Taurus", "numerology": 7,
        "image_key": "seven_of_pentacles",
    },
    {
        "id": 71, "name": "Eight of Pentacles", "suit": "pentacles", "number": 8, "arcana": "minor",
        "keywords_upright": ["diligence", "skill development", "craftsmanship", "dedication", "mastery", "apprenticeship"],
        "keywords_reversed": ["perfectionism", "lack of ambition", "mediocrity", "no passion", "shortcuts"],
        "meaning_upright": (
            "The Eight of Pentacles is the dedicated apprentice—head down, hands busy, utterly absorbed in the work of mastering a craft through patient, repetitive practice. "
            "Excellence is achieved not through talent alone but through the commitment to show up and do the work, day after day, until mastery is yours. "
            "This is a time to invest seriously in your skills, to learn from masters, and to take genuine pride in the quality of your work. "
            "Diligence is its own reward—and it eventually yields mastery."
        ),
        "meaning_reversed": (
            "Reversed, the Eight of Pentacles warns of perfectionism that paralyzes, a lack of genuine ambition or passion for the work, or a tendency to cut corners in ways that undermine the quality of your output. "
            "You may be going through the motions without the inner fire that transforms effort into mastery. "
            "Reconnect with why this work matters to you; genuine passion is the fuel that transforms diligence into excellence."
        ),
        "element": "Earth", "astrology": "Sun in Virgo", "numerology": 8,
        "image_key": "eight_of_pentacles",
    },
    {
        "id": 72, "name": "Nine of Pentacles", "suit": "pentacles", "number": 9, "arcana": "minor",
        "keywords_upright": ["abundance", "luxury", "self-sufficiency", "financial independence", "refinement", "achievement"],
        "keywords_reversed": ["financial dependence", "working too hard", "materialism", "hollow success", "financial setback"],
        "meaning_upright": (
            "The Nine of Pentacles is the self-made woman—walking through her abundant garden, falcon on her wrist, at complete ease in the world she has created through her own effort and discernment. "
            "Financial independence, refined taste, and the quiet satisfaction of genuine self-sufficiency are yours. "
            "Enjoy what you have built; you have earned this abundance. "
            "This is a time to savor the fruits of your labor without apology."
        ),
        "meaning_reversed": (
            "Reversed, the Nine of Pentacles indicates that the appearance of abundance masks a financial dependence, a hollow success built on unstable foundations, or a workaholic approach that is sacrificing genuine enjoyment of life for the accumulation of more. "
            "Alternatively, a financial setback may be threatening the security you have worked hard to establish. "
            "Examine whether your relationship with material success is genuinely fulfilling or merely an accumulation that leaves you empty."
        ),
        "element": "Earth", "astrology": "Venus in Virgo", "numerology": 9,
        "image_key": "nine_of_pentacles",
    },
    {
        "id": 73, "name": "Ten of Pentacles", "suit": "pentacles", "number": 10, "arcana": "minor",
        "keywords_upright": ["legacy", "wealth", "family", "long-term success", "tradition", "security", "inheritance"],
        "keywords_reversed": ["family dysfunction", "financial failure", "lack of stability", "conflict over inheritance"],
        "meaning_upright": (
            "The Ten of Pentacles represents the fulfillment of the material journey—generational wealth, a thriving family lineage, and the deep satisfaction of knowing that your efforts will endure beyond your own lifetime. "
            "This is the card of legacy: the home, the business, the family, the tradition that you are building for those who come after you. "
            "Celebrate the abundance you have created and the community of loved ones who share in it. "
            "You are building something that will last."
        ),
        "meaning_reversed": (
            "Reversed, the Ten of Pentacles points to dysfunction within the family system, financial instability threatening long-term security, or conflicts around inheritance and the passing of wealth and tradition. "
            "The solid structure that should be passing down through generations may be crumbling due to old grievances, poor financial management, or a breakdown in family values. "
            "Address the source of the dysfunction before the legacy is lost."
        ),
        "element": "Earth", "astrology": "Mercury in Virgo", "numerology": 10,
        "image_key": "ten_of_pentacles",
    },
    {
        "id": 74, "name": "Page of Pentacles", "suit": "pentacles", "number": 11, "arcana": "minor",
        "keywords_upright": ["ambition", "desire to learn", "practical", "diligent", "grounded", "manifestation", "new opportunity"],
        "keywords_reversed": ["laziness", "lack of focus", "procrastination", "wasted potential", "poor planning"],
        "meaning_upright": (
            "The Page of Pentacles is the earnest student of the material world—grounded, curious, and deeply motivated by the desire to learn how things work and to build something real. "
            "A practical new opportunity or the beginning of a skill-building journey is available. "
            "Approach this with the page's diligence and openness to learning; real mastery begins with willing apprenticeship. "
            "Be patient with the process and trust that consistent practical effort will yield tangible results."
        ),
        "meaning_reversed": (
            "Reversed, the Page of Pentacles becomes lazy, unfocused, or prone to procrastination that squanders genuine potential. "
            "There may be an inability to commit to the sustained effort that material success requires, or a tendency to plan endlessly without taking the practical first steps. "
            "Ground your ambitions in a concrete daily practice; dreams without action are just wishes."
        ),
        "element": "Earth", "astrology": None, "numerology": None,
        "image_key": "page_of_pentacles",
    },
    {
        "id": 75, "name": "Knight of Pentacles", "suit": "pentacles", "number": 12, "arcana": "minor",
        "keywords_upright": ["hard work", "reliability", "methodical", "patience", "conservative", "committed"],
        "keywords_reversed": ["laziness", "boredom", "obsessive routine", "stubbornness", "stagnation"],
        "meaning_upright": (
            "The Knight of Pentacles is the most methodical and reliable of all the knights—he doesn't charge forward recklessly but advances with steady, deliberate purpose, trusting the process more than the sprint. "
            "He is committed to the long game, willing to do the unglamorous work day after day because he understands that lasting results are built through sustained effort. "
            "Embrace his dependable energy: show up consistently, do the work with care, and trust that patience will be rewarded."
        ),
        "meaning_reversed": (
            "Reversed, the Knight of Pentacles loses his admirable steadiness and becomes stuck in routine to the point of stagnation, or swings to the opposite extreme of laziness and avoidance. "
            "An obsessive adherence to method may be preventing necessary adaptation and growth. "
            "Alternatively, boredom with the slow pace of real progress may be leading to shortcuts or abandonment of important long-term commitments. "
            "Find the balance between healthy consistency and life-giving flexibility."
        ),
        "element": "Earth", "astrology": "Leo/Virgo", "numerology": None,
        "image_key": "knight_of_pentacles",
    },
    {
        "id": 76, "name": "Queen of Pentacles", "suit": "pentacles", "number": 13, "arcana": "minor",
        "keywords_upright": ["nurturing", "practical", "providing", "down-to-earth", "financial security", "abundant"],
        "keywords_reversed": ["financial insecurity", "smothering", "neglect of self", "work-life imbalance", "gold digger"],
        "meaning_upright": (
            "The Queen of Pentacles is the practical nurturer—she creates an environment of warmth, abundance, and genuine comfort through her steady, competent care. "
            "She is equally at home in the garden and the boardroom, capable of nurturing both living things and financial resources with equal grace. "
            "Embody her energy: create the material and emotional conditions that allow the people and projects you love to flourish. "
            "Her gift is making abundance feel like home."
        ),
        "meaning_reversed": (
            "Reversed, the Queen of Pentacles may become so focused on providing materially that she neglects her own needs or those of the people she loves at a deeper emotional level. "
            "Financial insecurity may be driving an anxious, controlling approach to resources. "
            "Alternatively, smothering behavior—controlling through material provision—may be stifling those in her care. "
            "True nurturing honors both the material and the emotional; ensure your care nourishes rather than controls."
        ),
        "element": "Earth", "astrology": "Sagittarius/Capricorn", "numerology": None,
        "image_key": "queen_of_pentacles",
    },
    {
        "id": 77, "name": "King of Pentacles", "suit": "pentacles", "number": 14, "arcana": "minor",
        "keywords_upright": ["abundance", "security", "ambition", "enterprising", "sensual", "reliable", "mastery of wealth"],
        "keywords_reversed": ["materialism", "greed", "corruption", "financial instability", "stubbornness", "misuse of power"],
        "meaning_upright": (
            "The King of Pentacles has achieved mastery of the material world—he sits on his throne of accumulated wealth and wisdom with the comfortable authority of one who has earned everything he possesses through patience, discipline, and genuine enterprise. "
            "He is generous, reliable, and deeply practical, leading through the example of sustained prosperity and material security. "
            "Embody this king's mastery: build with patience, give generously, and lead through the example of honest, sustained achievement. "
            "Material success and true security are yours to claim."
        ),
        "meaning_reversed": (
            "Reversed, the King of Pentacles becomes corrupted by the very wealth he has accumulated—greedy, materialistic, and willing to compromise his integrity for financial gain. "
            "The stability and security he prizes above all may be used as a means of control rather than a gift to share. "
            "Financial instability or a misuse of material power may be creating serious consequences. "
            "Return to the values that create genuine, lasting abundance: honest effort, practical wisdom, and generous stewardship of what you have been given."
        ),
        "element": "Earth", "astrology": "Aries/Taurus", "numerology": None,
        "image_key": "king_of_pentacles",
    },
]
