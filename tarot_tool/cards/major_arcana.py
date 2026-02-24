"""Major Arcana card definitions — all 22 cards."""
from __future__ import annotations

MAJOR_ARCANA: list[dict] = [
    {
        "id": 0,
        "name": "The Fool",
        "suit": "major_arcana",
        "number": 0,
        "arcana": "major",
        "keywords_upright": ["beginnings", "innocence", "spontaneity", "free spirit", "adventure", "potential"],
        "keywords_reversed": ["recklessness", "naivety", "foolishness", "risk", "negligence", "chaos"],
        "meaning_upright": (
            "The Fool represents the beginning of a journey, a leap of faith into the unknown with an open heart and fresh eyes. "
            "This card embodies pure potential, the excitement of new beginnings, and the trust that the universe will provide. "
            "The Fool urges you to embrace spontaneity, take a risk, and step off the edge of the familiar into uncharted territory. "
            "This is a time of unlimited possibility, where you are unburdened by past experience and free to explore life with childlike wonder. "
            "Trust your instincts and begin the adventure—the journey itself is the destination."
        ),
        "meaning_reversed": (
            "Reversed, the Fool warns of recklessness, poor judgment, or leaping before looking. "
            "You may be ignoring sensible advice or taking unnecessary risks without considering the consequences. "
            "There could be a tendency toward naivety or an unwillingness to grow up and take responsibility. "
            "Alternatively, it may indicate that fear is holding you back from taking the very leap of faith you need. "
            "Examine whether you are being foolishly impulsive or whether fear is disguising itself as caution."
        ),
        "element": "Air",
        "astrology": "Uranus",
        "numerology": 0,
        "image_key": "the_fool",
    },
    {
        "id": 1,
        "name": "The Magician",
        "suit": "major_arcana",
        "number": 1,
        "arcana": "major",
        "keywords_upright": ["willpower", "manifestation", "resourcefulness", "skill", "concentration", "power"],
        "keywords_reversed": ["manipulation", "trickery", "wasted talent", "illusion", "deception", "blocked potential"],
        "meaning_upright": (
            "The Magician is the master of manifestation, possessing all four elemental tools—wand, cup, sword, and pentacle—representing "
            "the full spectrum of resources at your disposal. This card signals that you have everything you need to achieve your goals; "
            "the question is whether you will channel your willpower and focus into purposeful action. "
            "The Magician connects the spiritual to the physical, translating divine inspiration into earthly reality through concentrated intent. "
            "This is a powerful time to set clear intentions, develop your skills, and act with confidence—for the universe responds to those who act with conviction."
        ),
        "meaning_reversed": (
            "Reversed, the Magician points to manipulation, deception, or using power for selfish ends. "
            "There may be someone in your life—or within yourself—who is not operating with integrity, twisting facts or using skill to mislead. "
            "Alternatively, you may be experiencing a block in your ability to manifest, feeling that your talents are wasted or untapped. "
            "Scattered focus, poor planning, or a lack of commitment are preventing the magic from flowing. "
            "Reassess your intentions and ensure you are working in alignment with your highest good."
        ),
        "element": "Air",
        "astrology": "Mercury",
        "numerology": 1,
        "image_key": "the_magician",
    },
    {
        "id": 2,
        "name": "The High Priestess",
        "suit": "major_arcana",
        "number": 2,
        "arcana": "major",
        "keywords_upright": ["intuition", "sacred knowledge", "mystery", "stillness", "subconscious", "inner voice"],
        "keywords_reversed": ["secrets", "disconnected intuition", "withdrawal", "hidden motives", "repressed feelings"],
        "meaning_upright": (
            "The High Priestess sits at the threshold between the conscious and unconscious, guarding the mysteries of the inner world. "
            "She represents deep intuition, psychic knowing, and the wisdom that comes from silence and contemplation rather than outward action. "
            "When she appears, the time calls for stillness—listen to your dreams, your gut feelings, and the subtle signals your body and soul are sending. "
            "Knowledge that cannot be learned from books is available to you now; trust the wisdom that arises from within. "
            "The High Priestess asks you to trust the unseen and to wait before acting."
        ),
        "meaning_reversed": (
            "Reversed, the High Priestess indicates that you are ignoring your intuition or suppressing your inner voice in favor of external noise. "
            "Important information or feelings are being repressed, and secrets—either yours or others'—may be affecting the situation. "
            "You may be overthinking things or allowing others to override the wisdom of your gut. "
            "Alternatively, this card reversed can indicate a withdrawal from the world that has become unhealthy isolation. "
            "Reconnect with your inner world and let your intuition guide you back to clarity."
        ),
        "element": "Water",
        "astrology": "Moon",
        "numerology": 2,
        "image_key": "the_high_priestess",
    },
    {
        "id": 3,
        "name": "The Empress",
        "suit": "major_arcana",
        "number": 3,
        "arcana": "major",
        "keywords_upright": ["fertility", "abundance", "nurturing", "nature", "creativity", "sensuality", "growth"],
        "keywords_reversed": ["creative block", "dependence", "smothering", "neglect", "stagnation", "emptiness"],
        "meaning_upright": (
            "The Empress is the great mother archetype, embodying fertility, abundance, and the creative life force that flows through all living things. "
            "She represents a deep connection to nature, sensuality, and the pleasure of physical existence. "
            "In her presence, things grow—ideas bloom into projects, relationships deepen, and material prosperity increases. "
            "She invites you to honor your body, immerse yourself in beauty, and allow creative energy to flow freely and abundantly. "
            "This is a time for nurturing yourself and others, for tending to what you love and watching it flourish."
        ),
        "meaning_reversed": (
            "Reversed, the Empress suggests creative blocks, neglect of self-care, or an unhealthy dependency or smothering dynamic in relationships. "
            "The natural flow of abundance may be disrupted by a tendency to control, to withhold, or to place conditions on love and care. "
            "You may be neglecting your own needs or the needs of a creative project, or alternatively overindulging in the physical world at the expense of growth. "
            "Reconnect with nature, your creative instincts, and the simple joys of physical existence. "
            "Let yourself receive as well as give."
        ),
        "element": "Earth",
        "astrology": "Venus",
        "numerology": 3,
        "image_key": "the_empress",
    },
    {
        "id": 4,
        "name": "The Emperor",
        "suit": "major_arcana",
        "number": 4,
        "arcana": "major",
        "keywords_upright": ["authority", "structure", "stability", "leadership", "discipline", "protection"],
        "keywords_reversed": ["tyranny", "rigidity", "domination", "loss of control", "inflexibility", "abuse of power"],
        "meaning_upright": (
            "The Emperor represents authority, structure, and the power to create order from chaos through discipline and leadership. "
            "He is the archetypal father figure who establishes rules, boundaries, and systems that allow others to thrive in safety. "
            "This card calls you to take charge of your life with confidence and to build a stable foundation through careful planning and consistent effort. "
            "Success comes through discipline, responsibility, and clear-headed logic rather than emotion or impulse. "
            "The Emperor reminds you that true power is exercised with integrity and in service of those who depend on you."
        ),
        "meaning_reversed": (
            "Reversed, the Emperor warns of the misuse of power—tyranny, domination, or rigid control that stifles freedom and growth. "
            "There may be an authority figure in your life who is abusing their position, or you yourself may be holding on too tightly to control. "
            "Excessive rigidity, an inability to adapt, or a refusal to consider others' perspectives can lead to isolation and conflict. "
            "Alternatively, the reversed Emperor can indicate a lack of structure, discipline, or self-authority, leaving you feeling scattered and unable to establish order. "
            "Examine where power is being misused or where more structure is needed."
        ),
        "element": "Fire",
        "astrology": "Aries",
        "numerology": 4,
        "image_key": "the_emperor",
    },
    {
        "id": 5,
        "name": "The Hierophant",
        "suit": "major_arcana",
        "number": 5,
        "arcana": "major",
        "keywords_upright": ["tradition", "conformity", "spiritual guidance", "institutions", "belief", "ritual"],
        "keywords_reversed": ["rebellion", "subversiveness", "unconventional", "dogma", "restriction", "challenge to norms"],
        "meaning_upright": (
            "The Hierophant is the keeper of sacred traditions, spiritual wisdom, and established systems of belief. "
            "He represents the value of learning from those who came before, of finding guidance within established institutions—religion, philosophy, or education. "
            "This card suggests that the conventional path, the tried-and-true method, or seeking counsel from a trusted mentor or institution may be the wisest course of action. "
            "There is wisdom in ritual, in community, and in the accumulated knowledge of tradition. "
            "Honor the structures and teachings that have proven their worth, and consider seeking guidance from a teacher or spiritual community."
        ),
        "meaning_reversed": (
            "Reversed, the Hierophant challenges you to question the rules, to break free from dogma and rigid conformity that no longer serves your growth. "
            "You may be feeling constrained by social conventions, institutional expectations, or the pressure to follow a path that isn't authentically yours. "
            "This card reversed encourages you to forge your own spiritual path, trust your unorthodox approach, and challenge systems that have become oppressive. "
            "Alternatively, it may warn against rebellion for its own sake, or against rejecting all guidance and structure out of defiance. "
            "Find the balance between honoring wisdom and blazing your own authentic trail."
        ),
        "element": "Earth",
        "astrology": "Taurus",
        "numerology": 5,
        "image_key": "the_hierophant",
    },
    {
        "id": 6,
        "name": "The Lovers",
        "suit": "major_arcana",
        "number": 6,
        "arcana": "major",
        "keywords_upright": ["love", "harmony", "relationships", "values alignment", "choices", "partnership", "union"],
        "keywords_reversed": ["disharmony", "imbalance", "misalignment", "bad choices", "conflict", "broken relationships"],
        "meaning_upright": (
            "The Lovers represents the deepest form of union—not just romantic love but the alignment of values, the harmony of opposites, and the sacred choice to commit. "
            "This card often appears at a crossroads where a significant decision must be made, one that will define your path forward. "
            "The choice presented by the Lovers is not merely between two people or two options, but between two different versions of yourself and the values each embodies. "
            "When the Lovers appears, authentic connection—to another person or to your deepest self—is available to you. "
            "Choose with your heart aligned with your highest values."
        ),
        "meaning_reversed": (
            "Reversed, the Lovers indicates disharmony, imbalanced relationships, or a failure to honor your true values when making important choices. "
            "You may be in a relationship marked by conflict, incompatibility, or a fundamental misalignment of values and desires. "
            "There is also the possibility of making choices from a place of fear, neediness, or external pressure rather than authentic desire. "
            "This card reversed can also speak to an internal conflict—the warring factions within yourself that prevent you from committing fully to any path. "
            "Reconnect with your core values before making decisions that will define your future."
        ),
        "element": "Air",
        "astrology": "Gemini",
        "numerology": 6,
        "image_key": "the_lovers",
    },
    {
        "id": 7,
        "name": "The Chariot",
        "suit": "major_arcana",
        "number": 7,
        "arcana": "major",
        "keywords_upright": ["determination", "willpower", "victory", "control", "ambition", "direction", "success"],
        "keywords_reversed": ["aggression", "lack of direction", "scattered energy", "defeat", "out of control", "opposition"],
        "meaning_upright": (
            "The Chariot represents the triumphant harnessing of opposing forces—the will to succeed and the discipline to direct that energy toward a single goal. "
            "Victory is assured when you maintain focus, overcome internal contradictions, and move forward with confidence and decisive action. "
            "This is a card of hard-won success through sheer determination, of mastering the tensions within yourself and the obstacles in your path. "
            "The Charioteer does not merely react to circumstances; he commands them, using both intellect and instinct to navigate toward his destination. "
            "Claim your power, set your course, and push through every challenge with unwavering resolve."
        ),
        "meaning_reversed": (
            "Reversed, the Chariot warns of a loss of control, aggression without direction, or forces pulling you in conflicting directions with no resolution. "
            "You may be trying to force an outcome through sheer willpower when a subtler approach is needed. "
            "Alternatively, you may be feeling directionless, unable to marshal your energy into focused action, scattered and overwhelmed. "
            "There may also be a tendency toward aggression, control issues, or steamrolling others in pursuit of your goals. "
            "Regain your sense of direction and ensure your determination serves your highest purpose."
        ),
        "element": "Water",
        "astrology": "Cancer",
        "numerology": 7,
        "image_key": "the_chariot",
    },
    {
        "id": 8,
        "name": "Strength",
        "suit": "major_arcana",
        "number": 8,
        "arcana": "major",
        "keywords_upright": ["inner strength", "courage", "patience", "compassion", "soft power", "fortitude", "confidence"],
        "keywords_reversed": ["self-doubt", "weakness", "fear", "raw emotion", "insecurity", "cowardice", "lack of confidence"],
        "meaning_upright": (
            "Strength does not roar—it whispers with quiet certainty. This card represents the power that comes from compassion, patience, and inner resolve. "
            "The figure in the card tames the lion not through force but through gentle courage, showing that the fiercest battles are often won with love and endurance. "
            "This is a time to face your fears, doubts, and primal instincts with calm grace rather than brute force. "
            "Your inner resources—your faith in yourself, your capacity for compassion, your willingness to endure—are your greatest weapons. "
            "Trust that quiet confidence and loving persistence will carry you through any challenge."
        ),
        "meaning_reversed": (
            "Reversed, Strength signals self-doubt, a loss of courage, or allowing fear and insecurity to dictate your actions. "
            "You may be doubting your ability to cope, giving your power away to others, or being overwhelmed by raw emotion and instinct. "
            "There may also be a tendency toward weakness disguised as niceness—giving in to avoid conflict when standing firm is what's needed. "
            "Alternatively, this card reversed can indicate that you are being too forceful, relying on aggression rather than inner strength. "
            "Reconnect with your genuine inner power and let it guide you with compassion and courage."
        ),
        "element": "Fire",
        "astrology": "Leo",
        "numerology": 8,
        "image_key": "strength",
    },
    {
        "id": 9,
        "name": "The Hermit",
        "suit": "major_arcana",
        "number": 9,
        "arcana": "major",
        "keywords_upright": ["solitude", "inner guidance", "introspection", "wisdom", "soul-searching", "contemplation"],
        "keywords_reversed": ["isolation", "loneliness", "withdrawal", "exile", "lost", "anti-social", "refusing guidance"],
        "meaning_upright": (
            "The Hermit holds his lantern aloft not to guide others, but to illuminate the path for himself—and in doing so, light the way for those who follow. "
            "This is a card of deliberate solitude, of withdrawing from the noise of the world to hear the voice of wisdom within. "
            "Soul-searching, contemplation, and deep inner work are called for now; the answers you seek will not come from external sources but from honest self-examination. "
            "This may be a time of spiritual study, mentorship, or simply taking a step back from daily activity to integrate what you have learned. "
            "The Hermit trusts that the light he carries within is sufficient to guide him home."
        ),
        "meaning_reversed": (
            "Reversed, the Hermit speaks of unhealthy isolation, loneliness that comes from fear rather than choice, or refusing the guidance of a wise mentor. "
            "You may have withdrawn too deeply from the world, cutting yourself off from the connection and support you actually need. "
            "Alternatively, there may be a resistance to introspection—keeping yourself constantly busy to avoid confronting uncomfortable truths. "
            "This card reversed can also indicate returning from a period of solitude and rejoining the world. "
            "Examine whether your current state of aloneness is nourishing or depleting you."
        ),
        "element": "Earth",
        "astrology": "Virgo",
        "numerology": 9,
        "image_key": "the_hermit",
    },
    {
        "id": 10,
        "name": "Wheel of Fortune",
        "suit": "major_arcana",
        "number": 10,
        "arcana": "major",
        "keywords_upright": ["luck", "fate", "turning points", "cycles", "opportunity", "destiny", "change"],
        "keywords_reversed": ["bad luck", "resistance to change", "broken cycle", "stagnation", "no control", "misfortune"],
        "meaning_upright": (
            "The Wheel of Fortune turns ceaselessly—what is at the bottom rises to the top, and what is at the top descends again. "
            "This card speaks of fate, of the grand cycles of life, and of the unpredictable turns of fortune that no human will can fully control. "
            "A significant turning point is at hand—a change that may feel sudden but has long been in motion at the level of fate. "
            "This is an auspicious time when luck, opportunity, and divine timing are on your side; be alert to synchronicities and be ready to act when the wheel turns in your favor. "
            "Trust the larger cycles of your life and know that whatever position you are in now is temporary."
        ),
        "meaning_reversed": (
            "Reversed, the Wheel of Fortune suggests bad luck, resistance to change, or feeling trapped in an endless negative cycle. "
            "You may be fighting against forces far larger than yourself, or clinging to circumstances that fate is already moving to change. "
            "There is a sense of being at the mercy of forces beyond your control, of misfortune seemingly arriving without cause. "
            "This card reversed asks you to examine whether your own choices have contributed to your circumstances, and whether resistance to change is prolonging your difficulties. "
            "Sometimes the wheel must fall before it can rise again; trust the process even when fortune seems to have turned against you."
        ),
        "element": "Fire",
        "astrology": "Jupiter",
        "numerology": 10,
        "image_key": "wheel_of_fortune",
    },
    {
        "id": 11,
        "name": "Justice",
        "suit": "major_arcana",
        "number": 11,
        "arcana": "major",
        "keywords_upright": ["fairness", "truth", "cause and effect", "law", "balance", "accountability", "integrity"],
        "keywords_reversed": ["injustice", "dishonesty", "bias", "avoidance", "corruption", "imbalance", "lack of accountability"],
        "meaning_upright": (
            "Justice holds the scales level and the sword sharp—representing the unwavering principle that actions have consequences and truth will prevail. "
            "This card calls for clear-eyed objectivity, honesty, and the courage to take full accountability for your choices and their effects on others. "
            "Legal matters, contracts, and formal agreements are highlighted; whatever is fair and truthful will be upheld. "
            "Justice also invites you to examine the balance in your own life—are you giving and receiving in equal measure? "
            "The sword of Justice cuts through illusion; be prepared to face the truth, even when it is uncomfortable."
        ),
        "meaning_reversed": (
            "Reversed, Justice warns of injustice, dishonesty, bias, or the avoidance of accountability. "
            "Someone—perhaps you, perhaps another—is refusing to take responsibility for their actions or is manipulating the truth to serve their own interests. "
            "Legal matters may not resolve fairly, or the system may be failing those it was meant to protect. "
            "This card reversed can also indicate an imbalance in how you weigh your choices, applying different standards to yourself than to others. "
            "Integrity demands that you face the truth about your own role in any difficult situation, even when it is painful to do so."
        ),
        "element": "Air",
        "astrology": "Libra",
        "numerology": 11,
        "image_key": "justice",
    },
    {
        "id": 12,
        "name": "The Hanged Man",
        "suit": "major_arcana",
        "number": 12,
        "arcana": "major",
        "keywords_upright": ["suspension", "surrender", "new perspective", "pause", "sacrifice", "letting go", "contemplation"],
        "keywords_reversed": ["resistance", "stalling", "delay", "martyrdom", "indecision", "useless sacrifice"],
        "meaning_upright": (
            "The Hanged Man has willingly surrendered, choosing to pause and view the world from an entirely different angle. "
            "What appears to be a position of helplessness is actually one of profound wisdom—by releasing the need to act, to control, or to force outcomes, "
            "he gains insight that cannot be achieved through ordinary means. "
            "This card calls for a voluntary pause, a period of waiting and contemplation before moving forward. "
            "You may need to sacrifice a particular outcome, belief, or pattern in order to receive the deeper understanding that awaits. "
            "The enlightenment of the Hanged Man comes not from doing, but from the courage to stop and see clearly."
        ),
        "meaning_reversed": (
            "Reversed, the Hanged Man indicates resistance to the pause that is needed, or a sacrifice that is made in martyrdom rather than wisdom. "
            "You may be stalling—neither surrendering nor moving forward—caught in indecision or delay that serves no purpose. "
            "Alternatively, you may be clinging to unnecessary suffering, believing that self-sacrifice is noble when it is actually self-defeating. "
            "This card reversed can also indicate a readiness to emerge from a period of suspension and re-engage with the world. "
            "Examine whether your waiting serves a higher purpose or is simply fear wearing the mask of contemplation."
        ),
        "element": "Water",
        "astrology": "Neptune",
        "numerology": 12,
        "image_key": "the_hanged_man",
    },
    {
        "id": 13,
        "name": "Death",
        "suit": "major_arcana",
        "number": 13,
        "arcana": "major",
        "keywords_upright": ["transformation", "endings", "transition", "letting go", "change", "release", "rebirth"],
        "keywords_reversed": ["resistance to change", "stagnation", "decay", "fear of endings", "clinging to the past", "inability to move on"],
        "meaning_upright": (
            "Death rarely signals physical death—instead, it announces the end of one chapter and the inevitable beginning of another. "
            "This is the card of profound transformation, of releasing what has served its purpose so that something entirely new can emerge. "
            "Like the seasons, life moves in cycles, and Death reminds us that endings are necessary and even sacred. "
            "What must be released—a relationship, a belief, an identity, a phase of life—must be allowed to die so that you can be reborn into your next form. "
            "The Death card asks you to grieve what is ending with grace and to trust that transformation, though painful, is the doorway to growth."
        ),
        "meaning_reversed": (
            "Reversed, Death indicates a desperate clinging to what has already ended, a refusal to let go that results in stagnation and decay. "
            "You may be trapped in a situation, relationship, or identity that is no longer alive, yet you cannot bring yourself to release it. "
            "This resistance to necessary endings prolongs suffering and prevents the new life that is waiting to emerge. "
            "Alternatively, this card reversed can speak of a near-death experience—physical, psychological, or spiritual—from which you have narrowly escaped. "
            "The universe is asking you to trust the process of transformation; what feels like destruction is actually the ground being cleared for new growth."
        ),
        "element": "Water",
        "astrology": "Scorpio",
        "numerology": 13,
        "image_key": "death",
    },
    {
        "id": 14,
        "name": "Temperance",
        "suit": "major_arcana",
        "number": 14,
        "arcana": "major",
        "keywords_upright": ["balance", "moderation", "patience", "purpose", "alchemy", "harmony", "integration"],
        "keywords_reversed": ["imbalance", "excess", "discord", "impatience", "lack of moderation", "extremes", "misalignment"],
        "meaning_upright": (
            "Temperance is the master alchemist, patiently and skillfully blending seemingly opposite elements into a harmonious whole. "
            "This card speaks of the virtue of moderation—the middle path that avoids the excesses of either extreme. "
            "Balance is achieved not through passivity but through the conscious and artful integration of all parts of yourself. "
            "There is a higher purpose at work; trust the process of gradual transformation that unfolds when you work patiently and in alignment with your values. "
            "Temperance asks you to flow—to adapt, to mix, to combine—and to find the harmony that exists when all elements are in right relationship."
        ),
        "meaning_reversed": (
            "Reversed, Temperance signals imbalance, excess, or a fundamental misalignment between your actions and your deeper purpose. "
            "You may be swinging between extremes—working too hard then burning out, loving too intensely then withdrawing, spending too freely then scrambling. "
            "Impatience may be pushing you to rush a process that requires time and careful tending. "
            "Relationships, projects, or even your own inner life may be suffering from a lack of the moderate, steady care they require. "
            "Return to the middle path; examine where excess or deficiency is creating discord and restore the equilibrium."
        ),
        "element": "Fire",
        "astrology": "Sagittarius",
        "numerology": 14,
        "image_key": "temperance",
    },
    {
        "id": 15,
        "name": "The Devil",
        "suit": "major_arcana",
        "number": 15,
        "arcana": "major",
        "keywords_upright": ["bondage", "addiction", "shadow self", "materialism", "restriction", "illusion", "temptation"],
        "keywords_reversed": ["release", "freedom", "breaking free", "reclaiming power", "overcoming addiction", "detachment"],
        "meaning_upright": (
            "The Devil does not imprison anyone—the chains in the card hang loosely around the necks of the figures, who could remove them at any time. "
            "This card represents the ways we enslave ourselves: to addictions, to toxic relationships, to materialism, to our own shadow impulses. "
            "The Devil is the master of illusion, convincing us that we have no choice when in fact we always do. "
            "Shadow work is called for—an honest examination of where you are giving your power away and what beliefs, behaviors, or relationships are keeping you in bondage. "
            "To be liberated, you must first acknowledge that you are chained and that you hold the key."
        ),
        "meaning_reversed": (
            "Reversed, the Devil heralds a powerful breaking free from bondage, addiction, or a toxic situation that has held you captive. "
            "You are reclaiming your power, seeing through the illusions that kept you trapped, and making the brave choice to live more authentically. "
            "This is an incredibly positive sign if you have been struggling with addiction, dependency, or a destructive relationship. "
            "Alternatively, this card reversed may indicate that you are becoming aware of your shadow patterns but have not yet taken action to change them. "
            "The freedom is available; it awaits only your decision to reach for it."
        ),
        "element": "Earth",
        "astrology": "Capricorn",
        "numerology": 15,
        "image_key": "the_devil",
    },
    {
        "id": 16,
        "name": "The Tower",
        "suit": "major_arcana",
        "number": 16,
        "arcana": "major",
        "keywords_upright": ["sudden change", "upheaval", "revelation", "chaos", "destruction", "awakening", "crisis"],
        "keywords_reversed": ["avoidance", "fear of change", "delayed disaster", "resisting upheaval", "personal transformation"],
        "meaning_upright": (
            "The Tower strikes without warning, shattering structures that were built on false foundations—pride, illusion, or avoidance of truth. "
            "This is the card of crisis and catastrophe, of the lightning bolt of sudden revelation that demolishes what seemed solid. "
            "Though deeply uncomfortable, the Tower's destruction is ultimately liberating: only that which was false is destroyed; what is true survives the fire. "
            "This upheaval—whether in relationships, career, beliefs, or circumstances—is clearing the ground for something more authentic to be built. "
            "Do not fight the Tower's truth; allow the demolition of what no longer serves so that something truer can rise."
        ),
        "meaning_reversed": (
            "Reversed, the Tower indicates that you are resisting the inevitable upheaval that is trying to occur, delaying but not preventing the necessary destruction. "
            "You may be clinging to a false structure out of fear—knowing it is unsound but unwilling to face the fall. "
            "Alternatively, the reversed Tower can indicate that a crisis has been narrowly averted, or that the destruction is happening on an internal, personal level rather than in external circumstances. "
            "The tower must eventually fall; the only question is whether you will allow the collapse to happen with grace. "
            "Examine what you are refusing to see and what you are working so hard to preserve that perhaps needs to crumble."
        ),
        "element": "Fire",
        "astrology": "Mars",
        "numerology": 16,
        "image_key": "the_tower",
    },
    {
        "id": 17,
        "name": "The Star",
        "suit": "major_arcana",
        "number": 17,
        "arcana": "major",
        "keywords_upright": ["hope", "faith", "renewal", "inspiration", "serenity", "healing", "optimism"],
        "keywords_reversed": ["despair", "hopelessness", "disconnection", "lack of faith", "disillusionment", "negativity"],
        "meaning_upright": (
            "After the Tower's destruction comes the Star—a shining beacon of hope, healing, and renewal in the aftermath of crisis. "
            "The Star pours its waters freely, replenishing what has been depleted and offering faith that the universe is fundamentally benevolent. "
            "This is a card of calm restoration, of reconnecting with your sense of purpose and the quiet certainty that everything will be all right. "
            "Creativity, inspiration, and spiritual renewal are available to you now; open yourself to receive the healing that the universe is offering. "
            "Allow yourself to dream and to trust—the Star reminds you that you are guided, that you are part of something vast and beautiful."
        ),
        "meaning_reversed": (
            "Reversed, the Star signals despair, hopelessness, or a profound disconnection from faith in yourself or the universe. "
            "You may be struggling to find meaning after a period of loss or difficulty, unable to access the inner well of optimism and hope. "
            "This card reversed can also indicate a failure to receive the healing that is available—refusing comfort, isolating yourself, or denying your need for renewal. "
            "Alternatively, overly idealistic expectations may be setting you up for disillusionment. "
            "Reconnect with what gives you hope, even in small doses—let the star's light, however dim it seems, guide you back toward faith."
        ),
        "element": "Air",
        "astrology": "Aquarius",
        "numerology": 17,
        "image_key": "the_star",
    },
    {
        "id": 18,
        "name": "The Moon",
        "suit": "major_arcana",
        "number": 18,
        "arcana": "major",
        "keywords_upright": ["illusion", "fear", "subconscious", "confusion", "dreams", "anxiety", "the unknown"],
        "keywords_reversed": ["release of fear", "repressed emotion", "clarity returning", "confusion lifting", "deception revealed"],
        "meaning_upright": (
            "The Moon illuminates only partially, casting deep shadows and distorting what it touches—it is the realm of dreams, illusions, and the primal fears that lurk in the unconscious. "
            "Under the Moon's light, nothing is quite as it appears; anxiety, confusion, and a sense of disorientation may be pervasive. "
            "Pay close attention to your dreams, your gut feelings, and the irrational fears that surface in the night, for they carry important messages. "
            "Deception—from within or without—may be at work; trust slowly and verify before committing. "
            "The Moon asks you to navigate the darkness with intuition rather than logic, honoring the wisdom of your depths even when the path is unclear."
        ),
        "meaning_reversed": (
            "Reversed, the Moon suggests that the fog of confusion and fear is beginning to lift, bringing clarity after a period of disorientation. "
            "Illusions that have obscured the truth are dissolving, and repressed emotions or unconscious fears are finally surfacing where they can be acknowledged and healed. "
            "Alternatively, this card reversed can indicate that deception is being uncovered or that you are beginning to see through a situation that was previously unclear. "
            "The darkness is passing; the irrational fears that gripped you are losing their power. "
            "Trust the gradual return of clarity and allow the light of consciousness to illuminate what the shadows had concealed."
        ),
        "element": "Water",
        "astrology": "Pisces",
        "numerology": 18,
        "image_key": "the_moon",
    },
    {
        "id": 19,
        "name": "The Sun",
        "suit": "major_arcana",
        "number": 19,
        "arcana": "major",
        "keywords_upright": ["joy", "success", "positivity", "vitality", "confidence", "clarity", "abundance"],
        "keywords_reversed": ["inner child", "overconfidence", "pessimism", "blocked joy", "dimmed light", "delayed success"],
        "meaning_upright": (
            "The Sun shines without reservation, pouring warmth and light on everything it touches—this is the card of joy, success, and the exuberant celebration of being alive. "
            "Whatever you have been working toward, the Sun brings clarity, confidence, and the warmth of achievement. "
            "This is a time of vitality, optimism, and abundance—everything is illuminated, and there is nothing to fear because truth and light prevail. "
            "Allow yourself to be fully present, to enjoy life without apology, and to share your brightness generously with those around you. "
            "The Sun is the universe's wholehearted 'yes' to you and your path."
        ),
        "meaning_reversed": (
            "Reversed, the Sun's light is partially blocked—joy feels out of reach, pessimism clouds what should be a time of celebration, or overconfidence creates blind spots. "
            "You may be struggling to access your natural vitality and enthusiasm, feeling low even in objectively positive circumstances. "
            "Alternatively, the reversed Sun can indicate an inner child wound—a difficulty in allowing yourself to be playful, joyful, or confident without guilt. "
            "Success may be delayed rather than denied; the light is there, but something—internal blocks, circumstances, or timing—is dimming it temporarily. "
            "Look for what is obscuring your natural joy and gently move it aside."
        ),
        "element": "Fire",
        "astrology": "Sun",
        "numerology": 19,
        "image_key": "the_sun",
    },
    {
        "id": 20,
        "name": "Judgement",
        "suit": "major_arcana",
        "number": 20,
        "arcana": "major",
        "keywords_upright": ["rebirth", "absolution", "awakening", "renewal", "calling", "reflection", "reckoning"],
        "keywords_reversed": ["self-doubt", "refusing the call", "ignoring inner voice", "failure to learn", "stagnation", "self-judgment"],
        "meaning_upright": (
            "Judgement is the great awakening—the trumpet call that summons the dead to rise and be transformed. "
            "This card represents a profound moment of reckoning: a time to honestly assess your past, take account of where you have been, and hear the call to become something greater. "
            "You are being invited to shed an old identity and rise into a new, more evolved version of yourself—one that integrates all you have been through into wisdom. "
            "Absolution is available; forgive yourself and others, release the past, and answer the call of your highest purpose. "
            "This is a moment of awakening that cannot be ignored—you are being asked to rise."
        ),
        "meaning_reversed": (
            "Reversed, Judgement indicates a refusal to answer the call, a resistance to the awakening that is trying to occur within you. "
            "You may be paralyzed by self-judgment—holding yourself to an impossible standard and refusing to forgive yourself for past mistakes. "
            "Alternatively, you may be ignoring clear inner guidance, suppressing the voice of your higher self that is urging a profound change. "
            "The reckoning is being avoided, but it cannot be permanently escaped—the longer you resist, the louder the call will become. "
            "Examine where self-doubt or a fear of change is preventing the transformation that your soul is ready for."
        ),
        "element": "Fire",
        "astrology": "Pluto",
        "numerology": 20,
        "image_key": "judgement",
    },
    {
        "id": 21,
        "name": "The World",
        "suit": "major_arcana",
        "number": 21,
        "arcana": "major",
        "keywords_upright": ["completion", "integration", "accomplishment", "wholeness", "fulfillment", "success", "travel"],
        "keywords_reversed": ["incompleteness", "shortcuts", "delays", "loose ends", "stagnation", "lack of closure"],
        "meaning_upright": (
            "The World is the final card of the Major Arcana and the culmination of the Fool's long journey—a triumphant declaration of completion, wholeness, and achieved mastery. "
            "A cycle is complete; you have earned this moment through all the lessons, trials, and transformations of the journey. "
            "Celebrate what has been accomplished, for this is the result of genuine, hard-won integration of all you have experienced. "
            "The World also heralds a readiness to begin the next great cycle—completion is not an ending but the threshold of the next adventure. "
            "Step into the world with the confidence of one who has truly arrived at themselves."
        ),
        "meaning_reversed": (
            "Reversed, the World indicates incompleteness, loose ends, or shortcuts that have prevented the full experience of achievement and integration. "
            "A cycle is not quite finished; something remains unresolved or unacknowledged that must be addressed before true completion can be celebrated. "
            "There may also be a fear of completion itself—an unconscious resistance to finishing that keeps you perpetually in process without arrival. "
            "Delays in a major life goal or project may be testing your patience. "
            "Examine what still needs to be completed, integrated, or released before you can cross this threshold with your whole self."
        ),
        "element": "Earth",
        "astrology": "Saturn",
        "numerology": 21,
        "image_key": "the_world",
    },
]
