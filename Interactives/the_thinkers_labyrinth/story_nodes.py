"""
The Thinker's Labyrinth
A Choose Your Own Adventure through cognitive biases, thought experiments, and decision-making.

Protagonist: Theodore Ernest O'Hare ("Theo"), 17
Setting: A surreal labyrinth where each chamber manifests a famous thought experiment
Course: The Thinking Toolkit

Design: Hub-and-spoke architecture
  Frame (1 node): start — Theo enters the labyrinth, arrives at crossroads
  Hub (1 node): hub_crossroads — central chamber with 4 wing passages
  Mirror Wing (5 nodes): Cognitive biases — anchoring, sunk-cost, confirmation bias, etc.
  Ethics Wing (5 nodes): Moral philosophy — trolley problem, drowning child, veil of ignorance, etc.
  Game Wing (5 nodes): Game theory — prisoner's dilemma, stag hunt, tragedy of the commons, etc.
  Paradox Garden (4 nodes): Logical paradoxes — sorites, barber paradox, Russell's paradox, etc.
  Decision Chamber (2 nodes): Pre-mortem + regret minimization, leading to endings
  Endings (7 nodes): 1 best, 3 good, 1 neutral, 2 bad

The player explores 4 independent wings from the central crossroads in ANY order.
Each wing's exit node offers direct passage to the other 3 wings OR the Decision Chamber.
This creates path variety: Mirror→Ethics→Decision is completely different from
Game→Paradox→Decision. The hub is implicit in the exit-node choice structure.

Eras map to labyrinth zones for graph metrics:
  frame, biases, ethics, game_theory, paradox, decisions

40 vocabulary terms distributed across nodes.
7 endings: end_intellectual_humility (best), end_humble_exit (good),
  end_courageous_exit (good), end_clarity_exit (good),
  end_escalation_trap (neutral), end_commons_collapse (bad), end_one_model (bad)
"""

START_NODE = "start"

NODES = {
    # ============================================================
    # FRAME — ENTRY
    # ============================================================
    "start": {
        "title": "The Map Is Not the Territory",
        "text": (
            "Theo slumps over his desk at 11:47 PM, cheek pressed against page 42 of "
            "*The Thinking Toolkit*. The chapter heading blurs: **The Map Is Not the Territory**. "
            "He'd been trying to memorize the difference between the **availability heuristic** "
            "and the **representativeness heuristic** for tomorrow's exam, but the words have "
            "started swimming.\n\n"
            "He blinks. The desk is gone.\n\n"
            "He's standing in a vast stone antechamber, lit by torches that burn without heat. "
            "The air tastes of old libraries and copper pennies. Carved symbols cover every surface "
            "— a trolley on tracks, a prisoner's chain, an infinite staircase, a heap of sand "
            "that seems to grow as he watches. A bronze plaque above the inner archway reads:\n\n"
            "*Every model illuminates and every model obscures. The danger is not ignorance "
            "but the illusion of knowledge.*\n\n"
            "Beyond the archway, a passage descends into flickering blue light. "
            "Something down there hums — not a sound exactly, but a vibration in his thoughts, "
            "as if the labyrinth is already thinking about him."
        ),
        "choices": [
            {"text": "Descend into the labyrinth", "target": "hub_crossroads"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "frame",
        "vocabulary": [
            {"term": "availability heuristic", "definition": "Judging how likely something is based on how easily examples come to mind, rather than actual statistics."},
            {"term": "representativeness heuristic", "definition": "Judging probability by how closely something matches a stereotype or mental prototype."},
            {"term": "The Map Is Not the Territory", "definition": "The idea that our mental models of reality are simplifications, not reality itself. A map can be useful without being complete."}
        ],
        "figures": [],
        "tags": ["intro", "frame_story", "mental_models"]
    },

    # ============================================================
    # HUB — THE CROSSROADS
    # ============================================================
    "hub_crossroads": {
        "title": "The Crossroads of Four Winds",
        "text": (
            "The passage opens into a chamber so vast Theo can't see the ceiling. Four colossal "
            "archways stand at the cardinal points, each carved from a different material and "
            "radiating a different quality of light.\n\n"
            "To the NORTH, an arch of polished obsidian reflects Theo's face back at him in "
            "warped, multiplied fragments — a dozen versions of himself, each slightly wrong. "
            "A whisper drifts from it: *Do you trust what you see?*\n\n"
            "To the EAST, an arch of white marble hums with tension. Theo can hear faint voices "
            "arguing — not angrily, but desperately, as if lives hang on the outcome of a "
            "philosophical debate.\n\n"
            "To the SOUTH, an arch of iron and steel gleams coldly. Behind it, the sound of "
            "coins clinking, dice rolling, chains rattling — the mathematics of cooperation "
            "and betrayal.\n\n"
            "To the WEST, an arch of living wood, its surface covered in moss and paradoxical "
            "carvings — staircases that climb downward, doors that open onto themselves. "
            "The air through it smells of rain and impossibility.\n\n"
            "A mosaic on the floor depicts all four archways converging on a single point: "
            "a golden door at the heart of the labyrinth. The inscription reads: "
            "*Explore. Return. Choose again. The door opens only for those who have looked "
            "through more than one lens.*"
        ),
        "choices": [
            {"text": "Enter the Hall of Mirrors (north — obsidian arch)", "target": "mirror_entry"},
            {"text": "Enter the Moral Crossroads (east — marble arch)", "target": "ethics_entry"},
            {"text": "Enter the Game Room (south — iron arch)", "target": "game_entry"},
            {"text": "Enter the Paradox Garden (west — living wood arch)", "target": "paradox_entry"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["hub", "crossroads", "four_way_branch"]
    },

    # ============================================================
    # MIRROR WING — COGNITIVE BIASES (5 nodes)
    # ============================================================
    "mirror_entry": {
        "title": "The Hall of Mirrors",
        "text": (
            "The obsidian arch swallows Theo whole. He stumbles into a corridor of mirrors — "
            "but these aren't ordinary mirrors. Each one shows a version of himself that's "
            "almost right but subtly distorted. In one, he looks taller and more confident. "
            "In another, he's making a decision he's certain about — too certain.\n\n"
            "A merchant materializes at the center of the hall, standing behind a table piled "
            "with impossible objects: a compass that points sideways, a book with pages that "
            "rewrite themselves, a key made of glass.\n\n"
            "'Name your price for the glass key,' the merchant says. 'But know this: the last "
            "customer offered ten thousand gold coins.'\n\n"
            "Ten thousand. It's absurd for a glass key, but the number has lodged in Theo's "
            "mind like a splinter. He recognizes the trick: **anchoring** — the first number "
            "you hear distorts every number that follows, pulling your judgment toward it "
            "like gravity.\n\n"
            "The merchant watches him with ancient, amused eyes."
        ),
        "choices": [
            {"text": "Offer one coin — resist the anchor entirely", "target": "mirror_sunk_cost"},
            {"text": "Ask what the key actually does before naming a price", "target": "mirror_confirmation"},
            {"text": "Offer five hundred — a 'reasonable' compromise", "target": "mirror_anchoring"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "biases",
        "vocabulary": [
            {"term": "anchoring", "definition": "A cognitive bias where the first piece of information you encounter (the 'anchor') disproportionately influences your subsequent judgments and decisions."}
        ],
        "figures": ["Daniel Kahneman", "Amos Tversky"],
        "tags": ["anchoring", "negotiation", "cognitive_bias"]
    },

    "mirror_anchoring": {
        "title": "The Anchor Holds",
        "text": (
            "Theo offers five hundred gold coins. The merchant's eyes gleam. 'Sold!'\n\n"
            "As Theo picks up the glass key, one of his mirror reflections shakes its head. "
            "'You split the difference,' it says, voice muffled behind the glass. 'Classic "
            "anchoring. He invented the number, and you negotiated against it as if it meant "
            "something.'\n\n"
            "The key feels heavier than glass should. Theo realizes with a sinking feeling "
            "that he's already fallen for the **sunk-cost fallacy**: having paid 500 coins, "
            "he'll now feel compelled to use the key regardless of whether it's useful. "
            "The investment has become its own justification.\n\n"
            "But the key is doing something. Its surface clouds, then clears, showing "
            "Theo a vision: a comfortable room with a fireplace. Warm. Safe. Familiar. "
            "The mirror beside him whispers: *Why go further? You've already learned something. "
            "Isn't that enough?*\n\n"
            "Theo recognizes **status quo bias** — the seductive preference for staying "
            "exactly where you are, even when the labyrinth has so much more to teach."
        ),
        "choices": [
            {"text": "Use the key and keep exploring — you came here to learn", "target": "mirror_confirmation"},
            {"text": "Stay in the comfortable vision — you've learned enough", "target": "end_one_model"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "biases",
        "vocabulary": [
            {"term": "sunk-cost fallacy", "definition": "Continuing to invest in something because of what you've already spent, rather than evaluating it on its future value alone."},
            {"term": "status quo bias", "definition": "The preference for the current state of affairs. People tend to resist change even when the alternative is objectively better, because change feels like loss."}
        ],
        "figures": [],
        "tags": ["sunk_cost", "status_quo_bias", "bias_cascade"]
    },

    "mirror_sunk_cost": {
        "title": "The Weight of What You've Spent",
        "text": (
            "Theo offers a single coin. The merchant's face falls — then contorts with rage. "
            "'Fool! You'll pay for that insult!' The mirrors around them crack. The merchant "
            "vanishes, and the hall rearranges itself into a narrowing corridor.\n\n"
            "The walls are covered with tallies — hundreds of them, scratched into obsidian by "
            "previous visitors. Each tally represents a step deeper. A voice from the walls "
            "whispers: 'You've come this far. Turning back now would waste everything. "
            "Keep going.'\n\n"
            "Theo recognizes the trap: the **sunk-cost fallacy**. The steps he's already "
            "taken can't be recovered. The only question that matters is: what lies ahead?\n\n"
            "But his gut fights his brain. The corridor slopes downward, the tallies growing "
            "denser, and he feels the weight of imagined investment pressing him forward. "
            "Then he remembers: **loss aversion** — the fear of losing what you've already "
            "gained hurts roughly twice as much as gaining something new feels good. "
            "Kahneman and Tversky proved it. His emotions are lying to him.\n\n"
            "Two paths appear: one descends further into darkness; the other climbs toward "
            "a cold, clear light."
        ),
        "choices": [
            {"text": "Climb toward the light — cut your losses", "target": "mirror_confirmation"},
            {"text": "Keep descending — the answer must be down here", "target": "mirror_anchoring"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "biases",
        "vocabulary": [
            {"term": "sunk-cost fallacy", "definition": "Continuing a course of action because of past investment (time, money, effort) rather than future value. What's spent is spent — only future costs and benefits should guide your decision."},
            {"term": "loss aversion", "definition": "The psychological tendency to prefer avoiding losses over acquiring equivalent gains. Losing $100 feels roughly twice as painful as gaining $100 feels pleasurable."}
        ],
        "figures": ["Daniel Kahneman", "Amos Tversky"],
        "tags": ["sunk_cost", "loss_aversion", "prospect_theory"]
    },

    "mirror_confirmation": {
        "title": "The Echo Chamber",
        "text": (
            "Theo emerges into a circular room where every wall is a mirror — but these "
            "mirrors don't reflect light. They reflect *beliefs*. Each one shows a version of "
            "an argument he's already inclined to agree with, ignoring counterevidence, "
            "amplifying what he already thinks.\n\n"
            "A plaque on the floor reads: **Confirmation bias — the tendency to search for, "
            "interpret, and recall information in a way that confirms what you already believe.**\n\n"
            "Theo watches himself in the mirrors. In one, he's certain the merchant was "
            "dishonest. In another, he's certain the merchant was testing him. Each mirror "
            "shows the evidence that supports one interpretation and hides the rest.\n\n"
            "'The trick,' a voice says — it's his own reflection, speaking independently — "
            "'is **first principles thinking**. Don't start with what you believe. Start with "
            "what you can actually verify. Strip away assumptions. Build from the ground up.'\n\n"
            "The mirrors shatter simultaneously, revealing the exit."
        ),
        "choices": [
            {"text": "Apply first principles — question everything you've assumed", "target": "mirror_reflection"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "biases",
        "vocabulary": [
            {"term": "confirmation bias", "definition": "The tendency to seek out, favor, and remember information that confirms your existing beliefs while ignoring or discounting contradictory evidence."},
            {"term": "first principles thinking", "definition": "Breaking a problem down to its most basic, foundational truths and reasoning up from there, rather than reasoning by analogy or convention."}
        ],
        "figures": [],
        "tags": ["confirmation_bias", "first_principles", "critical_thinking"]
    },

    "mirror_reflection": {
        "title": "Through the Looking Glass",
        "text": (
            "The shattered mirrors reform into a single, enormous glass wall — and for the "
            "first time in the Hall of Mirrors, Theo sees himself clearly. Not distorted. "
            "Not flattering. Just... himself. A seventeen-year-old kid in a labyrinth, "
            "trying to think straight in a world designed to make thinking crooked.\n\n"
            "He reviews what the mirrors taught him: anchoring pulls your judgment toward "
            "the first number you hear. Sunk costs chain you to bad decisions. Loss aversion "
            "makes you cling to what you have rather than reach for what's better. "
            "Confirmation bias wraps you in a cocoon of comfortable agreement. And first "
            "principles thinking is the scalpel that cuts through all of it.\n\n"
            "The clear mirror shows four passages behind him — the crossroads reconstituted "
            "in glass. He can go anywhere from here."
        ),
        "choices": [
            {"text": "Enter the Moral Crossroads — face the ethical dilemmas", "target": "ethics_entry"},
            {"text": "Enter the Game Room — study cooperation and betrayal", "target": "game_entry"},
            {"text": "Enter the Paradox Garden — confront the limits of logic", "target": "paradox_entry"},
            {"text": "Enter the Decision Chamber — you've seen enough", "target": "decision_premortem"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "biases",
        "vocabulary": [],
        "figures": [],
        "tags": ["wing_exit", "reflection", "hub_return"]
    },

    # ============================================================
    # ETHICS WING — MORAL PHILOSOPHY (5 nodes)
    # ============================================================
    "ethics_entry": {
        "title": "The Trolley Problem",
        "text": (
            "The marble arch delivers Theo onto a raised platform overlooking a set of "
            "train tracks that stretch into the dark in both directions. Below, a runaway "
            "trolley hurtles toward five people tied to the rails. They strain against "
            "their ropes. One of them sees Theo and screams.\n\n"
            "A lever stands beside him. If he pulls it, the trolley diverts to a side "
            "track — but one person is tied there.\n\n"
            "This is the **trolley problem**, first posed by Philippa Foot in 1967. "
            "A **consequentialist** would say: pull the lever. Five saved is better than one. "
            "A **deontologist** would say: pulling the lever makes you the *cause* of "
            "someone's death. There's a moral difference between letting harm happen and "
            "actively causing it.\n\n"
            "The trolley is getting closer. Theo's hand hovers over the lever."
        ),
        "choices": [
            {"text": "Pull the lever — save the five", "target": "ethics_footbridge"},
            {"text": "Don't pull — you can't choose who dies", "target": "ethics_drowning"},
            {"text": "Look for a third option — yell a warning", "target": "ethics_trolley"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "ethics",
        "vocabulary": [
            {"term": "trolley problem", "definition": "A thought experiment in ethics: should you divert a runaway trolley to kill one person instead of five? Tests the boundary between consequentialist and deontological moral reasoning."},
            {"term": "consequentialism", "definition": "The moral theory that the rightness of an action depends entirely on its outcomes. The best action produces the most good (or least harm) for the most people."},
            {"term": "deontology", "definition": "The moral theory that some actions are inherently right or wrong, regardless of their consequences. Duties and rules matter, not just outcomes."}
        ],
        "figures": ["Philippa Foot", "Immanuel Kant", "Jeremy Bentham"],
        "tags": ["trolley_problem", "ethics", "opening_dilemma"]
    },

    "ethics_trolley": {
        "title": "Thinking Outside the Tracks",
        "text": (
            "Theo shouts at the top of his lungs. The five people look up — one wiggles "
            "free just as the trolley arrives. Four die instead of five.\n\n"
            "A voice echoes through the chamber: 'Interesting. You tried **inversion** — "
            "instead of accepting the binary, you questioned the framing itself. "
            "Instead of asking *which of two terrible options is better*, you asked "
            "*is the question wrong?*'\n\n"
            "But the voice grows somber: 'Four still died. Creative thinking doesn't "
            "always solve moral dilemmas. Sometimes the choices really are terrible.'\n\n"
            "The tracks dissolve. Theo finds himself in a hospital bed, connected by "
            "tubes to a stranger — a famous violinist, unconscious, with a rare blood disease. "
            "A nurse explains: 'The Society of Music Lovers connected you. If you disconnect, "
            "he dies. Stay connected for nine months, and he recovers.'\n\n"
            "This is Thomson's **violinist argument**: even if someone has a right to life, "
            "does that right extend to *your body* without your consent?"
        ),
        "choices": [
            {"text": "Stay connected — a life is a life", "target": "ethics_drowning"},
            {"text": "Disconnect — no one can conscript your body", "target": "ethics_reflection"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "ethics",
        "vocabulary": [
            {"term": "inversion", "definition": "A thinking tool: instead of asking how to achieve success, ask what would guarantee failure and avoid that. Instead of accepting a framing, question whether the framing itself is the problem."},
            {"term": "violinist argument", "definition": "Judith Jarvis Thomson's thought experiment: if you wake up connected to a dying violinist, are you morally obligated to stay connected? Tests whether the right to life entails a right to use another person's body."}
        ],
        "figures": ["Charlie Munger", "Judith Jarvis Thomson"],
        "tags": ["inversion", "violinist", "reframing"]
    },

    "ethics_footbridge": {
        "title": "The Footbridge Variant",
        "text": (
            "The lever worked. The trolley diverted. One person died instead of five.\n\n"
            "But the labyrinth isn't finished with Theo. He finds himself on a footbridge "
            "over another set of tracks. Another runaway trolley. Another five people. "
            "No lever this time. Instead, a very large man stands beside Theo on the bridge. "
            "If Theo pushes him off, his body would stop the trolley.\n\n"
            "Same math: one death to save five. But this feels *completely different*.\n\n"
            "This is the **doctrine of double effect**: there's a moral distinction between "
            "harm as a *side effect* of saving lives (pulling the lever) and harm as the "
            "*means* to saving lives (pushing the man). The outcome is identical. "
            "The moral weight is not.\n\n"
            "Theo's hands are shaking."
        ),
        "choices": [
            {"text": "Push the man — the math is the same", "target": "ethics_drowning"},
            {"text": "Refuse — using someone as a means is wrong", "target": "ethics_trolley"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "ethics",
        "vocabulary": [
            {"term": "doctrine of double effect", "definition": "The principle that it can be morally permissible to cause harm as a foreseen side effect of a good action, but not to cause harm as a deliberate means to a good end."}
        ],
        "figures": ["Judith Jarvis Thomson"],
        "tags": ["footbridge", "doctrine_double_effect", "moral_intuition"]
    },

    "ethics_drowning": {
        "title": "The Shallow Pond",
        "text": (
            "The labyrinth shifts. Theo stands in a garden with a shallow ornamental pond. "
            "A small child is face-down in the water, drowning. Theo is wearing his favorite "
            "shoes — the ones he saved up for all summer.\n\n"
            "He splashes in without thinking and pulls the child out. Of course he does. "
            "It would be monstrous not to.\n\n"
            "Peter Singer's voice fills the garden like a cathedral organ: 'Good. Now — if "
            "you'd ruin your shoes to save a child five feet away, are you obligated to donate "
            "the cost of those shoes to save a child dying of malaria five thousand miles away? "
            "The distance doesn't change the child's suffering.'\n\n"
            "This is the **drowning child argument**: if we can prevent something bad from "
            "happening without sacrificing anything of comparable moral importance, we ought "
            "to do it.\n\n"
            "Then the garden walls reform into a white room. Shadowy figures sit around a "
            "long table, designing the rules of a society that doesn't exist yet. A figure "
            "at the head speaks: 'You will choose the laws. But from behind a **veil of "
            "ignorance** — you won't know your position in the society you create. Rich or "
            "poor? Talented or disabled? Majority or minority?'\n\n"
            "John Rawls argued you'd protect the worst-off — because you might *be* them.\n\n"
            "A monstrous shape stirs in the corner. It pulses with pleasure, absorbing "
            "happiness like a sponge. Robert Nozick's **utility monster** — a being that "
            "derives so much more happiness from any resource that pure consequentialism "
            "demands you give it *everything*. 'Feed me,' it purrs. 'I'll enjoy it more "
            "than you ever could.'"
        ),
        "choices": [
            {"text": "Refuse the monster — happiness isn't the only thing that matters", "target": "ethics_reflection"},
            {"text": "Feed the monster — if total happiness increases, isn't that good?", "target": "ethics_reflection"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "ethics",
        "vocabulary": [
            {"term": "drowning child argument", "definition": "Peter Singer's thought experiment: if you would save a drowning child at minor personal cost, consistency demands you also help distant strangers in equivalent peril."},
            {"term": "veil of ignorance", "definition": "John Rawls's thought experiment: design a just society without knowing what position you'll occupy in it. Removes self-interest from the design of social institutions."},
            {"term": "utility monster", "definition": "Robert Nozick's objection to utilitarianism: a being that derives enormously more utility from resources than anyone else. Maximizing total utility would require giving it everything."}
        ],
        "figures": ["Peter Singer", "John Rawls", "Robert Nozick"],
        "tags": ["singer", "rawls", "nozick", "utility_monster"]
    },

    "ethics_reflection": {
        "title": "The Weight of Moral Reasoning",
        "text": (
            "The white room dissolves. Theo stands alone in a quiet marble corridor, "
            "breathing hard. The echoes of the thought experiments ring in his skull — "
            "trolleys and footbridges, drowning children and utility monsters, violinists "
            "and veils.\n\n"
            "He realizes something that both comforts and unsettles him: there is no master "
            "key to ethics. Consequentialism gives clean answers but monstrous edge cases. "
            "Deontology protects dignity but can be paralyzingly rigid. Every framework "
            "illuminates one thing by casting shadows on another.\n\n"
            "The marble walls show him four passages — the crossroads refracting through "
            "white stone. He can feel the labyrinth's other wings pulling at him like "
            "compass needles."
        ),
        "choices": [
            {"text": "Enter the Hall of Mirrors — confront your cognitive biases", "target": "mirror_entry"},
            {"text": "Enter the Game Room — study the mathematics of cooperation", "target": "game_entry"},
            {"text": "Enter the Paradox Garden — test the limits of logic itself", "target": "paradox_entry"},
            {"text": "Enter the Decision Chamber — you've wrestled enough with theory", "target": "decision_premortem"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "ethics",
        "vocabulary": [],
        "figures": [],
        "tags": ["wing_exit", "reflection", "hub_return"]
    },

    # ============================================================
    # GAME WING — GAME THEORY (5 nodes)
    # ============================================================
    "game_entry": {
        "title": "The Prisoner's Choice",
        "text": (
            "The iron arch clangs shut behind Theo. He's in a stark concrete cell, "
            "sitting across a bolted table from a stranger — another lost traveler in "
            "the labyrinth. Her eyes are wary. A guard reads the rules from a card:\n\n"
            "'Each of you will choose: cooperate or defect. Both cooperate — one year each. "
            "Both defect — three years each. One cooperates while the other defects — the "
            "defector goes free, the cooperator gets five years.'\n\n"
            "This is the **prisoner's dilemma**. The rational move is to defect — no matter "
            "what the other person does, you're better off betraying them. But if both "
            "players reason this way, they both get three years instead of one. Individual "
            "rationality creates collective disaster.\n\n"
            "The stranger looks at Theo with desperate eyes. 'I'll cooperate if you will,' "
            "she whispers. But Theo knows: that's exactly what a defector would say."
        ),
        "choices": [
            {"text": "Cooperate — trust the stranger", "target": "game_stag_chicken"},
            {"text": "Defect — protect yourself", "target": "game_stag_chicken"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "game_theory",
        "vocabulary": [
            {"term": "prisoner's dilemma", "definition": "A game theory scenario where two rational players each have an incentive to defect, but mutual cooperation would make both better off. Individual rationality leads to collective irrationality."}
        ],
        "figures": ["John Nash"],
        "tags": ["prisoners_dilemma", "game_theory", "trust"]
    },

    "game_stag_chicken": {
        "title": "The Hunt and the Highway",
        "text": (
            "The cell dissolves. Theo stands in a forest clearing with three other "
            "travelers. In the distance, a magnificent stag grazes — enough to feed all "
            "four for a week. But catching a stag requires all four hunters working together.\n\n"
            "Small hares hop nearby. Any one person could catch a hare alone — enough for "
            "a single meal.\n\n"
            "This is the **stag hunt**: cooperation yields a far larger reward, but only if "
            "everyone commits. If even one person breaks off to chase a hare, the stag "
            "escapes and the cooperators get nothing. One of the hunters is already "
            "eyeing a hare.\n\n"
            "Before Theo can decide, the forest flattens into a long, straight corridor. "
            "Another traveler walks toward him. The walls are closing in — slowly, steadily. "
            "If neither steps aside, they'll both be crushed. If one yields, the other "
            "passes safely.\n\n"
            "This is the **game of chicken**: the worst outcome is mutual stubbornness. "
            "In Cold War nuclear strategy, this logic governed the arms race. "
            "The walls inch closer. The other traveler shows no sign of stopping."
        ),
        "choices": [
            {"text": "Step aside — survival beats pride", "target": "game_commons"},
            {"text": "Keep walking — call their bluff", "target": "game_prisoners"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "game_theory",
        "vocabulary": [
            {"term": "stag hunt", "definition": "A coordination game: cooperating yields the highest payoff for everyone, but only if all players cooperate. If anyone defects to chase a small, guaranteed reward, the cooperators get nothing."},
            {"term": "game of chicken", "definition": "A game where two players head toward mutual destruction. Each benefits from the other swerving, but if neither swerves, both lose catastrophically."}
        ],
        "figures": ["Jean-Jacques Rousseau", "Bertrand Russell"],
        "tags": ["stag_hunt", "chicken", "coordination"]
    },

    "game_prisoners": {
        "title": "The Dollar Auction",
        "text": (
            "Neither blinked. The walls stopped just short of crushing them — it was "
            "a test — but now Theo is bruised and breathing hard.\n\n"
            "He stumbles into an auction hall. An auctioneer holds up a single gold coin. "
            "'Bidding starts at one copper piece. Highest bidder wins. But here's the rule: "
            "the *second-highest* bidder also pays their bid and gets nothing.'\n\n"
            "This is the **dollar auction**, invented by Martin Shubik. Rational bidding "
            "quickly turns irrational: once you're the second-highest bidder, you'd rather "
            "bid *more* than lose what you've already bid. **Escalation of commitment** "
            "becomes self-reinforcing — each step deeper makes walking away feel more "
            "costly, even though staying is always worse.\n\n"
            "Bidding has reached 80 copper pieces. Theo is second at 75. The other bidder "
            "grins, daring him to continue."
        ),
        "choices": [
            {"text": "Bid 85 — you're in too deep to stop now", "target": "end_escalation_trap"},
            {"text": "Walk away — recognize the trap for what it is", "target": "game_commons"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "game_theory",
        "vocabulary": [
            {"term": "dollar auction", "definition": "A game designed by Martin Shubik: auction off a dollar, but the second-highest bidder also pays their bid. Rational players escalate past the value of the prize because walking away means losing their investment."},
            {"term": "escalation of commitment", "definition": "The tendency to increase investment in a failing course of action because of what's already been invested. Also called the 'sunk-cost trap.'"}
        ],
        "figures": ["Martin Shubik"],
        "tags": ["dollar_auction", "escalation", "sunk_cost_strategic"]
    },

    "game_commons": {
        "title": "The Shared Pasture",
        "text": (
            "Theo enters a lush valley shared by a dozen farmers — other labyrinth "
            "travelers who've settled here. Each farmer grazes animals on the common "
            "pasture. The grass is green and thick... for now.\n\n"
            "But each farmer is adding more animals. Individually rational — one more "
            "animal costs the farmer nothing extra but earns a profit. Collectively "
            "catastrophic — the pasture is being overgrazed.\n\n"
            "This is the **tragedy of the commons**: when a shared resource has no rules, "
            "each person's rational self-interest destroys what belongs to everyone. "
            "Overfishing. Climate change. Antibiotic resistance. The pattern repeats "
            "everywhere.\n\n"
            "A farmer approaches Theo. 'We need someone to propose rules. Or we could "
            "divide the land. Or...' She trails off, looking at the yellowing grass."
        ),
        "choices": [
            {"text": "Propose shared rules — collective governance", "target": "game_reflection"},
            {"text": "Do nothing — maybe the pasture will recover on its own", "target": "end_commons_collapse"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "game_theory",
        "vocabulary": [
            {"term": "tragedy of the commons", "definition": "When individuals acting in rational self-interest deplete a shared resource, even though it's in everyone's long-term interest to preserve it. Named by Garrett Hardin in 1968."}
        ],
        "figures": ["Garrett Hardin", "Elinor Ostrom"],
        "tags": ["tragedy_commons", "collective_action", "governance"]
    },

    "game_reflection": {
        "title": "The Rules of the Game",
        "text": (
            "The farmers vote. Rules are set: grazing limits, rotation schedules, fines "
            "for overuse. It's not elegant, but it works. The pasture slowly greens again.\n\n"
            "Theo sits on a hillside overlooking the valley and thinks about what the "
            "Game Room taught him. The prisoner's dilemma shows why cooperation is hard. "
            "The stag hunt shows why it's fragile. The game of chicken shows the "
            "catastrophe of mutual stubbornness. The dollar auction shows how escalation "
            "traps rational minds. And the tragedy of the commons shows what happens "
            "when no one takes responsibility for the shared.\n\n"
            "The iron walls of the Game Room soften, revealing four passages."
        ),
        "choices": [
            {"text": "Enter the Hall of Mirrors — examine your cognitive biases", "target": "mirror_entry"},
            {"text": "Enter the Moral Crossroads — wrestle with ethical dilemmas", "target": "ethics_entry"},
            {"text": "Enter the Paradox Garden — explore the limits of logic", "target": "paradox_entry"},
            {"text": "Enter the Decision Chamber — time to choose your way out", "target": "decision_premortem"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "game_theory",
        "vocabulary": [],
        "figures": [],
        "tags": ["wing_exit", "reflection", "hub_return"]
    },

    # ============================================================
    # PARADOX GARDEN (4 nodes)
    # ============================================================
    "paradox_entry": {
        "title": "The Garden of Forking Paths",
        "text": (
            "The arch of living wood opens onto a garden unlike anything Theo has seen. "
            "The paths don't just branch — they loop back on themselves, dead-end into "
            "walls that weren't there a moment ago, and occasionally deposit him in places "
            "he's already been. The air smells of rain on hot stone, and every leaf seems "
            "to be debating itself.\n\n"
            "A sign carved into a living tree reads:\n\n"
            "*Welcome to the Paradox Garden. In this place, logic eats itself. "
            "The only way out is through.*\n\n"
            "Three structures stand in the garden: a growing heap of sand attended by "
            "a robed figure, a sturdy wooden fence across a garden path with faint claw "
            "marks on its far side, and a barber's shop with a paradoxical sign."
        ),
        "choices": [
            {"text": "Approach the heap of sand", "target": "paradox_sorites"},
            {"text": "Examine the fence across the path", "target": "paradox_sorites"},
            {"text": "Visit the barber's shop", "target": "paradox_barber"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "paradox",
        "vocabulary": [],
        "figures": [],
        "tags": ["paradox_entry", "three_way_branch"]
    },

    "paradox_sorites": {
        "title": "The Heap and the Fence",
        "text": (
            "A robed figure stands beside a pile of sand, adding one grain at a time. "
            "'One grain isn't a heap,' it says. 'Two grains aren't a heap. Three grains "
            "aren't. When does it *become* a heap?'\n\n"
            "This is the **sorites paradox**, from the Greek *soros* (heap). If adding "
            "one grain never turns a non-heap into a heap, then no amount of sand is a "
            "heap. But obviously, a million grains is a heap. The boundary is real but "
            "the line is nowhere.\n\n"
            "Theo thinks about the **Overton window** — how acceptable ideas shift "
            "gradually, one grain at a time, until what was unthinkable becomes mainstream.\n\n"
            "Nearby, a sturdy fence blocks a garden path. It seems pointless — nothing "
            "obvious it's protecting. Theo's instinct is to tear it down. But a plaque "
            "reads: **Chesterton's Fence — Do not remove a fence until you understand "
            "why it was built.**\n\n"
            "G.K. Chesterton argued that if a rule seems pointless, the fact that someone "
            "built it means they had a reason. Understand the reason before you destroy "
            "the rule — the consequences you can't see might be the ones that matter most.\n\n"
            "Theo examines the fence more carefully. There are faint claw marks on the "
            "far side."
        ),
        "choices": [
            {"text": "Leave the fence — respect what you don't understand", "target": "paradox_reflection"},
            {"text": "Tear it down — deal with consequences as they come", "target": "paradox_barber"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "paradox",
        "vocabulary": [
            {"term": "sorites paradox", "definition": "The paradox of the heap: if one grain of sand isn't a heap, and adding one grain never makes a non-heap a heap, then no number of grains is a heap. Challenges the precision of vague concepts."},
            {"term": "Overton window", "definition": "The range of ideas considered politically acceptable at any given time. It shifts gradually as public opinion changes, often without anyone noticing until the shift is complete."},
            {"term": "Chesterton's Fence", "definition": "The principle that you should not remove a rule, institution, or practice until you understand why it exists. If you can't explain the reason for the fence, you don't have enough information to decide it should go."}
        ],
        "figures": ["Eubulides of Miletus", "G.K. Chesterton"],
        "tags": ["sorites", "overton_window", "chestertons_fence"]
    },

    "paradox_barber": {
        "title": "The Barber and the Cascade",
        "text": (
            "The barber's shop has a sign: *The barber shaves all and only those who do "
            "not shave themselves.*\n\n"
            "The barber — a thoughtful man with a perfectly groomed beard — asks: "
            "'Do I shave myself?'\n\n"
            "If the barber shaves himself, then by the rule, he shouldn't (he only shaves "
            "those who *don't* shave themselves). But if he doesn't shave himself, then "
            "by the rule, he should.\n\n"
            "This is the **barber paradox**, a version of **Russell's paradox**: some "
            "self-referential definitions create contradictions that can't be resolved. "
            "Bertrand Russell showed that the set of all sets that don't contain themselves "
            "both must and must not contain itself. It shook the foundations of mathematics "
            "in 1901.\n\n"
            "Outside the shop, strange creatures are pouring through a gap where "
            "someone tore down the fence. The garden paths rearrange chaotically. "
            "This is **second-order effects** — the consequences of consequences. "
            "First-order thinking asks 'what happens if I do this?' Second-order "
            "thinking asks 'and then what?'\n\n"
            "The **law of unintended consequences** isn't about failure of imagination. "
            "It's about the fundamental complexity of interconnected systems."
        ),
        "choices": [
            {"text": "Accept that some questions have no clean answer — move on", "target": "paradox_reflection"},
            {"text": "Try to dissolve the paradox by reframing the question", "target": "paradox_reflection"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "paradox",
        "vocabulary": [
            {"term": "barber paradox", "definition": "If a barber shaves all and only those who don't shave themselves, does the barber shave himself? A self-referential paradox with no consistent answer."},
            {"term": "Russell's paradox", "definition": "Does the set of all sets that don't contain themselves contain itself? If yes, it shouldn't. If no, it should. Bertrand Russell's paradox shook the foundations of mathematics in 1901."},
            {"term": "second-order effects", "definition": "The consequences of consequences. First-order effects are direct and obvious; second-order effects are indirect and often surprising. Good decision-making requires thinking at least two steps ahead."},
            {"term": "law of unintended consequences", "definition": "Actions always have effects that are unanticipated or unintended. The more complex the system, the harder it is to predict all the ripples of any single change."}
        ],
        "figures": ["Bertrand Russell"],
        "tags": ["russells_paradox", "barber_paradox", "second_order", "unintended_consequences"]
    },

    "paradox_reflection": {
        "title": "The Limits of Logic",
        "text": (
            "Theo finds a bench at the center of the Paradox Garden — a still point amid "
            "the looping paths. The garden has settled, mostly. The creatures from behind "
            "the fence wander harmlessly now, having found their own equilibrium.\n\n"
            "He sits and thinks. The sorites paradox showed that precision has limits — "
            "some boundaries are real but uncapturable. Chesterton's Fence taught humility "
            "before destruction. Russell's paradox demonstrated that even logic can eat "
            "itself. And second-order effects proved that every action ripples further "
            "than you can see.\n\n"
            "The garden's living-wood walls part, revealing passages to the other wings. "
            "The moss on each archway glows faintly, beckoning."
        ),
        "choices": [
            {"text": "Enter the Hall of Mirrors — study how your mind distorts reality", "target": "mirror_entry"},
            {"text": "Enter the Moral Crossroads — grapple with right and wrong", "target": "ethics_entry"},
            {"text": "Enter the Game Room — learn the architecture of cooperation", "target": "game_entry"},
            {"text": "Enter the Decision Chamber — carry your paradoxes to the final door", "target": "decision_premortem"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "paradox",
        "vocabulary": [],
        "figures": [],
        "tags": ["wing_exit", "reflection", "hub_return"]
    },

    # ============================================================
    # DECISION CHAMBER (2 nodes)
    # ============================================================
    "decision_premortem": {
        "title": "The Decision Chamber",
        "text": (
            "Theo arrives at the heart of the labyrinth: a circular chamber with a single "
            "exit — a massive door that will take him home. But the door has a combination "
            "lock with three dials.\n\n"
            "A final inscription glows above the door: *Before you choose, imagine you've "
            "already failed. What went wrong?*\n\n"
            "This is the **pre-mortem**: instead of planning for success, assume failure "
            "and work backward to find the vulnerabilities. Gary Klein designed it as "
            "the antidote to **planning fallacy** — our persistent tendency to "
            "underestimate time, cost, and difficulty, the optimistic delusion that "
            "Kahneman called 'the engine of capitalism.'\n\n"
            "The three dials are labeled: HUMILITY, COURAGE, CLARITY.\n\n"
            "Theo thinks about everything the labyrinth has taught him. The biases that "
            "warp perception. The ethical dilemmas with no clean answers. The games where "
            "individual rationality destroys collective welfare. The paradoxes that show "
            "logic's own limits."
        ),
        "choices": [
            {"text": "Set all three dials to maximum — you need everything", "target": "end_intellectual_humility"},
            {"text": "Prioritize HUMILITY — knowing what you don't know", "target": "end_humble_exit"},
            {"text": "Prioritize COURAGE — acting despite uncertainty", "target": "end_courageous_exit"},
            {"text": "Prioritize CLARITY — cutting through confusion", "target": "end_clarity_exit"},
            {"text": "Wait — consult the Regret Machine first", "target": "decision_regret"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "decisions",
        "vocabulary": [
            {"term": "pre-mortem", "definition": "A decision-making technique: before starting a project, imagine it has failed spectacularly, then work backward to identify what went wrong. Counters overconfidence and planning fallacy."},
            {"term": "planning fallacy", "definition": "The systematic tendency to underestimate the time, cost, and risk of future actions while overestimating their benefits. First identified by Kahneman and Tversky."}
        ],
        "figures": ["Gary Klein", "Daniel Kahneman"],
        "tags": ["pre_mortem", "planning_fallacy", "decision_chamber"]
    },

    "decision_regret": {
        "title": "The Regret Machine",
        "text": (
            "Before setting the dials, Theo discovers a device in an alcove beside the "
            "door: a machine that shows him three possible futures.\n\n"
            "Jeff Bezos's **regret minimization framework**: project yourself to age 80 "
            "and ask which choice you'd regret *least*. Not which is safest. Not which "
            "is most profitable. Which lets you live without 'what if?'\n\n"
            "The machine also offers the **10/10/10 rule**: how will you feel about this "
            "decision in 10 minutes? 10 months? 10 years?\n\n"
            "Future 1 shows Theo playing it safe — comfortable but bored, haunted by "
            "the labyrinth he never fully explored.\n"
            "Future 2 shows him taking risks — sometimes failing, always learning, the "
            "labyrinth's lessons alive in every decision.\n"
            "Future 3 shows him paralyzed by analysis — standing at this very door forever, "
            "never choosing at all.\n\n"
            "The machine hums, waiting for his answer."
        ),
        "choices": [
            {"text": "Choose the learning path — regret comes from inaction", "target": "end_intellectual_humility"},
            {"text": "Choose comfort — not every life needs to be an adventure", "target": "end_humble_exit"},
            {"text": "Return to the dials — decide with your own hands", "target": "decision_premortem"}
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "decisions",
        "vocabulary": [
            {"term": "regret minimization framework", "definition": "A decision-making tool: imagine yourself at 80 years old looking back. Which choice would you regret least? Designed to cut through short-term noise and focus on what actually matters over a lifetime."},
            {"term": "10/10/10 rule", "definition": "Before making a decision, ask: how will I feel about this in 10 minutes, 10 months, and 10 years? Helps separate emotional reactions from lasting consequences."}
        ],
        "figures": ["Jeff Bezos", "Suzy Welch"],
        "tags": ["regret_minimization", "decision_tools", "time_horizon"]
    },

    # ============================================================
    # ENDINGS (7 nodes)
    # ============================================================
    "end_intellectual_humility": {
        "title": "The Examined Thinker",
        "text": (
            "Theo sets all three dials to maximum. The door doesn't just open — it "
            "dissolves. Behind it is not a corridor but a vast library that extends in "
            "every direction, infinite and luminous. Each book is a mental model, "
            "a framework, a way of seeing. And between the shelves, other doors — "
            "leading to labyrinths he hasn't visited yet.\n\n"
            "A voice — warm, amused — says: 'The most dangerous thinker isn't the one "
            "who knows no models. It's the one who knows one model very well. You've "
            "learned to hold many models at once without mistaking any of them for the "
            "territory itself.'\n\n"
            "Theo understands: **intellectual humility** isn't about doubting everything. "
            "It's about knowing which tool to use when, and knowing that every tool has "
            "limits. It's the meta-skill — the skill that makes all other skills useful.\n\n"
            "He wakes up at his desk. The exam tomorrow doesn't seem so scary anymore. "
            "He doesn't need to memorize every bias — he needs to think clearly about "
            "which ones apply to each question.\n\n"
            "The map is not the territory. But a good map, held lightly, can guide you home."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "best",
        "era": "decisions",
        "vocabulary": [
            {"term": "intellectual humility", "definition": "The recognition that your knowledge is always limited and your models are always incomplete. Not self-doubt, but accurate self-assessment — knowing what you know and what you don't."}
        ],
        "figures": ["Charlie Munger"],
        "tags": ["best_ending", "intellectual_humility", "synthesis"]
    },

    "end_humble_exit": {
        "title": "The Wisdom of Uncertainty",
        "text": (
            "Theo sets HUMILITY to maximum. The door opens onto a quiet garden — not "
            "the Paradox Garden, but a real one. Flowers grow in neat rows, but weeds "
            "grow too, and Theo understands that both belong.\n\n"
            "He learned something in the labyrinth that most people never grasp: "
            "the **Dunning-Kruger effect** works both ways. Beginners overestimate "
            "their knowledge — they don't know enough to see how much they don't know. "
            "But experts sometimes underestimate what beginners can see. Fresh eyes "
            "catch what habit hides.\n\n"
            "Theo wakes up knowing he'll never be the smartest person in any room. "
            "But he might be the person most willing to say: 'I don't know — yet.'\n\n"
            "He writes it in the margin of his textbook, right next to the definition "
            "of the availability heuristic: *The goal isn't to know everything. "
            "The goal is to know what you don't know.*"
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "decisions",
        "vocabulary": [
            {"term": "Dunning-Kruger effect", "definition": "A cognitive bias where people with limited knowledge overestimate their competence, while experts tend to underestimate theirs. The less you know, the less you realize how much you don't know."}
        ],
        "figures": ["David Dunning", "Justin Kruger"],
        "tags": ["good_ending", "humility", "dunning_kruger"]
    },

    "end_courageous_exit": {
        "title": "The One-Way Door",
        "text": (
            "Theo sets COURAGE to maximum. The door opens onto a cliff edge. Below, "
            "a river rushes through a canyon, white water churning over black rock. "
            "On the far side, the labyrinth continues — but transformed. The walls are "
            "transparent. He can see the whole structure from here: the Hall of Mirrors, "
            "the Moral Crossroads, the Game Room, the Paradox Garden — all connected, "
            "all part of a single design.\n\n"
            "He understands Jeff Bezos's distinction: **two-way doors** — reversible "
            "decisions — should be made quickly. One-way doors — irreversible decisions — "
            "deserve careful thought. But too many people treat every decision like a "
            "one-way door and end up paralyzed at every threshold.\n\n"
            "Theo jumps. The river catches him, cold and alive. He wakes up with his "
            "heart pounding and a new clarity: most of the things he was afraid of "
            "were two-way doors all along."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "decisions",
        "vocabulary": [
            {"term": "two-way door", "definition": "A reversible decision — if it doesn't work out, you can walk back through the door. These should be made quickly and delegated. Contrast with one-way doors (irreversible decisions) that deserve careful analysis."}
        ],
        "figures": ["Jeff Bezos"],
        "tags": ["good_ending", "courage", "reversibility"]
    },

    "end_clarity_exit": {
        "title": "Occam's Razor",
        "text": (
            "Theo sets CLARITY to maximum. The door opens onto a path so simple it "
            "almost seems wrong: a straight line through open countryside, no branches, "
            "no tricks, no mirrors or trolleys or paradoxes. After the labyrinth's "
            "complexity, the simplicity feels like a revelation.\n\n"
            "**Occam's razor**: among competing explanations, the simplest one that "
            "accounts for the evidence is usually correct. Not because the universe is "
            "simple — but because unnecessary complexity usually means you're making "
            "things up.\n\n"
            "Theo wakes up and writes one line in the margin of his textbook: "
            "*When confused, simplify. When sure, question.*\n\n"
            "It's not the deepest lesson the labyrinth had to offer. But it's the one "
            "he needed most."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "decisions",
        "vocabulary": [
            {"term": "Occam's razor", "definition": "The principle that among competing hypotheses, the one making the fewest assumptions should be preferred. Named for William of Ockham (c. 1287-1347). Not a law of nature, but a useful heuristic for cutting through complexity."}
        ],
        "figures": ["William of Ockham"],
        "tags": ["good_ending", "simplicity", "occams_razor"]
    },

    "end_escalation_trap": {
        "title": "The Sunk-Cost Spiral",
        "text": (
            "Theo bids 85. Then 95. Then 105 — past the value of the gold coin itself. "
            "He knows it's irrational but he can't stop. The **escalation of commitment** "
            "has him in its grip: each bid makes the next one feel necessary to justify "
            "the last. Walking away means admitting the previous bids were wasted.\n\n"
            "He finally stops at 200 copper pieces for a coin worth 100. The auctioneer "
            "smiles, pockets the money, and vanishes. The labyrinth grows darker around "
            "Theo, the walls contracting like a held breath.\n\n"
            "He wakes up with a lesson burned into his memory: *the hardest decision in "
            "any losing game is to stop playing.* Walking away feels like losing. But "
            "staying in a rigged game guarantees a bigger loss.\n\n"
            "He circles a sentence in his textbook: 'In a dollar auction, the only "
            "winning move is not to play.'"
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "neutral",
        "era": "game_theory",
        "vocabulary": [
            {"term": "escalation of commitment", "definition": "The tendency to increase investment in a failing course of action because of what's already been invested. Each step deeper makes walking away feel more costly — but staying is always more costly still."}
        ],
        "figures": ["Martin Shubik"],
        "tags": ["neutral_ending", "escalation", "sunk_cost"]
    },

    "end_commons_collapse": {
        "title": "The Tragedy Plays Out",
        "text": (
            "Theo does nothing. The farmers keep adding animals. The pasture browns, "
            "cracks, dies. The animals starve. The farmers scatter. The valley that "
            "sustained a community becomes a dust bowl in a matter of days — time "
            "moves strangely in the labyrinth.\n\n"
            "This is how the **tragedy of the commons** plays out in the real world: "
            "overfishing, climate change, antibiotic resistance. Everyone knows the "
            "problem. No one acts because acting alone means sacrificing while others "
            "don't.\n\n"
            "Theo wakes up frustrated. He learned something important but wished he'd "
            "learned it differently: doing nothing is itself a choice. And sometimes "
            "it's the worst choice of all."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "bad",
        "era": "game_theory",
        "vocabulary": [
            {"term": "tragedy of the commons", "definition": "When individuals deplete a shared resource by acting in rational self-interest, destroying the resource for everyone. The tragedy is that everyone knows what's happening and no one stops it."}
        ],
        "figures": ["Garrett Hardin"],
        "tags": ["bad_ending", "commons", "inaction"]
    },

    "end_one_model": {
        "title": "The Danger of One Model",
        "text": (
            "Theo never left the Hall of Mirrors. The comfortable room closed around "
            "him like a cocoon, warm and affirming. He became fascinated with cognitive "
            "biases — seeing them everywhere, in everyone, in every argument anyone made. "
            "Every conversation became an exercise in bias-spotting. Every disagreement "
            "was explained away as someone else's confirmation bias or anchoring or "
            "loss aversion.\n\n"
            "He forgot the labyrinth's first warning: *every model illuminates and every "
            "model obscures.* Cognitive bias research is a powerful lens — but it's still "
            "just one lens. Using it to dismiss everyone who disagrees with you is itself "
            "a bias: the **bias blind spot**, the tendency to see cognitive biases in "
            "others but never in yourself.\n\n"
            "Theo wakes up and writes 'BIAS!' in the margin of every argument in his "
            "textbook. He's learned the words but missed the music. The labyrinth had "
            "four wings. He only ever entered one."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "bad",
        "era": "biases",
        "vocabulary": [
            {"term": "bias blind spot", "definition": "The tendency to see cognitive biases in others but not in yourself. Ironically, learning about biases can make this worse: you become a bias-detector for everyone else while remaining blind to your own."}
        ],
        "figures": [],
        "tags": ["bad_ending", "one_model_danger", "overconfidence"]
    },
}
