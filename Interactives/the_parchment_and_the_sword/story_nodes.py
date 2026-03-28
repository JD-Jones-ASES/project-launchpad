"""
The Parchment and the Sword
A Thinker's Labyrinth Choose-Your-Own-Adventure

Course: History & Humanities II — Alfred the Great through the Protestant Reformation
Protagonist: Theodore "Theo" Ernest O'Hare (age 17)
Setting: Seven centuries of medieval and early modern Europe (793–1555)

GRAPH STRUCTURE: PARALLEL TRACKS
After a shared prologue (3 nodes), Theo makes a FACTION CHOICE that sends him
down one of three largely independent storylines covering the same 762 years
from different perspectives:

  Track A — THE SCHOLAR'S PATH (knowledge, faith, learning)
    Lindisfarne scriptorium → Alfred's court → Medieval university → Aquinas →
    Wycliffe → Gutenberg → Erasmus/Tyndale
    ~13 unique nodes

  Track B — THE WARRIOR'S PATH (power, politics, conquest)
    Viking raids → Norman conquest → Crusades → Hundred Years' War →
    Joan of Arc → Machiavelli
    ~13 unique nodes

  Track C — THE MERCHANT'S PATH (trade, cities, innovation)
    Viking trade → Domesday Book → Silk Road → Florence → Leonardo →
    Age of Exploration
    ~13 unique nodes

CROSSOVER POINTS (all tracks converge briefly):
  1. The Black Death (1348) — cross_plague
  2. The Fall of Constantinople (1453) — cross_fall

CONVERGENCE: The Reformation (1517–1555) — 5 shared nodes → 9 endings

Graph metrics:
  - 3 prologue nodes (shared)
  - ~13 Track A nodes (scholar)
  - ~13 Track B nodes (warrior)
  - ~13 Track C nodes (merchant)
  - 2 crossover nodes (shared)
  - 5 convergence nodes (shared)
  - 9 endings
  - Total: ~58 nodes
  - 80+ vocabulary terms from the H&H II glossary
  - 7 historical eras
"""

START_NODE = "start"

NODES = {

    # ══════════════════════════════════════════════════════════════════════
    #  PROLOGUE — SHARED OPENING (3 nodes)
    # ══════════════════════════════════════════════════════════════════════

    "start": {
        "title": "The Scriptorium Burns",
        "text": (
            "Theo's head drops onto the open textbook. The last thing he sees "
            "before sleep takes him is a map of Viking expansion routes and a "
            "sentence about the raid on Lindisfarne.\n\n"
            "He wakes to screaming.\n\n"
            "The room is wrong. Stone walls. A vaulted ceiling. Rows of wooden "
            "desks where monks hunch over manuscripts, their quills frozen mid-stroke. "
            "Through the narrow window, the grey sea churns — and cutting through the "
            "waves, long shallow-keeled ships with carved dragon prows.\n\n"
            "'*Vikings!*' A monk seizes Theo's arm. His face is young, terrified, "
            "ink-stained. '*The Northmen are here. God preserve us — they'll burn "
            "everything.*'\n\n"
            "Smoke curls under the door. On the desk before Theo lies a strange "
            "manuscript — layers of text visible beneath the surface writing, older "
            "words bleeding through newer ones. A **palimpsest**. As he touches it, "
            "the topmost text shimmers and rearranges itself.\n\n"
            "The monk stares. '*That manuscript — it was blank an hour ago. It's "
            "writing itself.*'\n\n"
            "The door splinters. Flames lick the hallway beyond."
        ),
        "choices": [
            {"text": "Grab the palimpsest and run deeper into the monastery", "target": "prologue_library"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "frame",
        "vocabulary": [
            {"term": "Viking", "definition": "A Norse seafarer from Scandinavia (modern Denmark, Norway, Sweden) who raided, traded, and settled across Europe from the 8th to 11th centuries. The word may come from Old Norse vik, meaning 'inlet' or 'bay.'"},
            {"term": "longship", "definition": "A shallow-draft Norse ship designed for both ocean voyages and river navigation. Its shallow keel allowed Vikings to sail up rivers and beach directly on shores, making their raids devastatingly fast and unpredictable."},
        ],
        "figures": [],
        "tags": ["entry", "frame_story"],
    },

    "prologue_library": {
        "title": "The Library of Lindisfarne",
        "text": (
            "Theo clutches the palimpsest and plunges through a side passage. The young "
            "monk — Brother Aldric — follows, carrying an armful of scrolls.\n\n"
            "'*The library,*' Aldric gasps. '*We cannot let them take the library. "
            "Centuries of learning — the Gospels, Bede's histories, letters from Rome. "
            "This is the light of the world, and they will use it for kindling.*'\n\n"
            "They reach a stone chamber lined with shelves. Through the walls, Theo hears "
            "the crash of axes. The Vikings are systematic — they know monasteries hold "
            "gold, silver, and reliquaries worth a fortune.\n\n"
            "Aldric looks at Theo, then at the burning corridor behind them. '*There are "
            "two ways. The tunnel beneath the chapel leads to the shore — we could escape "
            "with what we can carry. Or we could hide the most precious manuscripts in the "
            "crypt. They may survive the fire even if we do not.*'\n\n"
            "The palimpsest in Theo's hands pulses with warmth. New words form on its surface: "
            "*What is worth more — the vessel or the cargo?*"
        ),
        "choices": [
            {"text": "Save the manuscripts — hide them in the crypt and trust God", "target": "prologue_crypt"},
            {"text": "The smoke, the screaming, the axes — it's too much. Drop the parchment and hide", "target": "end_lost"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [
            {"term": "Anglo-Saxon Chronicle", "definition": "A year-by-year record of English history, begun at Alfred's command around 890 and continued by monks at various monasteries until the mid-twelfth century. One of the most important historical documents in English history."},
        ],
        "figures": ["Bede"],
        "tags": ["prologue", "viking", "choice_save_flee"],
    },

    "prologue_crypt": {
        "title": "Three Roads from the Ashes",
        "text": (
            "They work fast. Theo and Aldric wrap the most precious volumes — the Lindisfarne "
            "Gospels, Bede's *Ecclesiastical History*, a collection of saints' lives — in "
            "oiled cloth and lower them into a stone-lined vault beneath the altar.\n\n"
            "The smoke thickens. Aldric coughs blood. But the crypt is sealed.\n\n"
            "They stumble out through a garden passage just as the roof of the scriptorium "
            "collapses in a shower of sparks. On the beach below, Viking warriors load "
            "chalices and crosses into their longships. Their leader — tall, red-bearded, "
            "wearing a silver arm-ring — surveys the burning monastery with satisfaction.\n\n"
            "Aldric pulls Theo into the dunes. The palimpsest rewrites itself. Three "
            "images form on its surface, shimmering in the firelight:\n\n"
            "A scholar-king at a desk, translating philosophy by candlelight — *the life "
            "of the mind, where parchment preserves what swords destroy.*\n\n"
            "A Norman knight on horseback, castle walls rising behind him — *the life "
            "of power, where the sword shapes kingdoms and crowns.*\n\n"
            "A merchant ship laden with silk and spices, sailing past golden domes — *the "
            "life of exchange, where the coin connects worlds.*\n\n"
            "The palimpsest writes: *Choose your road. Each covers the same seven centuries. "
            "Each sees them differently. All roads converge at the end.*"
        ),
        "choices": [
            {"text": "Follow the parchment — seek the scholar-king in the marshes (The Scholar's Path)", "target": "scholar_alfred"},
            {"text": "Follow the sword — the Viking warband has spotted you (The Warrior's Path)", "target": "warrior_vikings"},
            {"text": "Follow the coin — a Norse trader on the beach offers passage (The Merchant's Path)", "target": "merchant_trade"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [
            {"term": "fyrd", "definition": "The Anglo-Saxon militia. Free men were required to serve in the fyrd when summoned by the king to defend the realm. Unlike professional warriors, the fyrd was made up of ordinary freemen who returned to their farms after the campaign."},
        ],
        "figures": [],
        "tags": ["prologue", "faction_choice"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  TRACK A — THE SCHOLAR'S PATH (~13 nodes)
    #  Knowledge, faith, learning: manuscripts → universities → printing press
    # ══════════════════════════════════════════════════════════════════════

    "scholar_alfred": {
        "title": "The Scholar-King",
        "text": (
            "The palimpsest pulls Theo south through a landscape divided. North and east "
            "of a rough line from London to Chester, Danish law holds sway — the **Danelaw**, "
            "established by the **Treaty of Wedmore** after Alfred's victory at Edington in 878.\n\n"
            "Alfred's court at Winchester is not what Theo expected. The king sits not on a "
            "throne but at a desk, surrounded by manuscripts. He is translating Boethius's "
            "*Consolation of Philosophy* from Latin into English — personally, word by word.\n\n"
            "'*He seems to me a very foolish man, and very wretched, who will not increase his "
            "understanding while he is in the world,*' Alfred reads aloud, testing the rhythm.\n\n"
            "He sees the palimpsest in Theo's hands and his eyes sharpen. '*A layered text. "
            "Old words beneath new. That is the nature of all wisdom — it is never entirely "
            "new, only recovered and built upon.*'\n\n"
            "Alfred is building something unprecedented: a network of schools, a legal code, "
            "a system of fortified towns — **burhs** — and a written record of his people's "
            "history — the Anglo-Saxon Chronicle.\n\n"
            "'*The Danes destroyed our books,*' he says. '*So we must write new ones. I need "
            "men who can read. Will you help?*'"
        ),
        "choices": [
            {"text": "Help Alfred — record what you've witnessed in the Chronicle", "target": "scholar_chronicle"},
            {"text": "The palimpsest pulls forward — to the first universities", "target": "scholar_university"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [
            {"term": "Danelaw", "definition": "The area of northern and eastern England under Danish law and custom after the Treaty of Wedmore (878). The boundary ran roughly from London northwest to Chester."},
            {"term": "Treaty of Wedmore", "definition": "The peace agreement between Alfred the Great and the Viking leader Guthrum in 878, which established the boundary of the Danelaw and required Guthrum's baptism as a Christian."},
            {"term": "burh", "definition": "A fortified town in Alfred's defensive network. Alfred built burhs throughout Wessex, spaced no more than a day's march apart, so that any part of the kingdom could be defended quickly."},
        ],
        "figures": ["Alfred the Great", "Boethius"],
        "tags": ["scholar", "viking", "alfred", "learning"],
    },

    "scholar_chronicle": {
        "title": "The Written Record",
        "text": (
            "Theo works in Alfred's **scriptorium** for what feels like weeks. He learns to cut "
            "quills, to mix ink from oak galls and iron salts, to write in the clear English "
            "script Alfred has standardized.\n\n"
            "The Chronicle grows. Year by year, the monks record invasions, battles, eclipses, "
            "the deaths of kings. Theo adds his own entry — carefully, in period style — about "
            "the raid on Lindisfarne.\n\n"
            "One evening, Alfred asks him: '*Why do we write history?*'\n\n"
            "Theo thinks of the palimpsest. '*Because the past speaks through the present. "
            "Because what's written can survive what's burned.*'\n\n"
            "Alfred nods. '*Exactly. The parchment outlasts the sword.*'\n\n"
            "That night, the palimpsest rewrites itself violently. The text shudders, words "
            "dissolving and reforming. Theo sees soaring arches, stained glass, and a professor "
            "debating in a great hall. A new age of learning is calling."
        ),
        "choices": [
            {"text": "Follow the vision — to the medieval universities", "target": "scholar_university"},
            {"text": "The parchment shows a murdered archbishop — church versus state", "target": "scholar_becket"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [
            {"term": "scriptorium", "definition": "The room in a medieval monastery dedicated to the copying and illumination of manuscripts. Monks worked in silence, producing the handwritten books that preserved classical and Christian learning through the Middle Ages."},
        ],
        "figures": ["Alfred the Great"],
        "tags": ["scholar", "viking", "chronicle", "writing"],
    },

    "scholar_becket": {
        "title": "Murder in the Cathedral",
        "text": (
            "December 29, 1170. Canterbury Cathedral.\n\n"
            "Thomas Becket stands before the altar. He was once Henry II's closest friend, "
            "his chancellor, his drinking companion. Henry made him Archbishop of Canterbury "
            "expecting a loyal ally. Instead, Becket transformed overnight into the Church's "
            "fiercest defender.\n\n"
            "The **Investiture Controversy** — the struggle over whether kings or popes "
            "appoint bishops — has been raging across Europe for decades. In England, "
            "it has turned murderous.\n\n"
            "Four knights stride into the cathedral, swords drawn. '*Where is Thomas Becket, "
            "traitor to the king?*'\n\n"
            "Becket faces them. '*I am here. No traitor, but a priest of God.*'\n\n"
            "Theo watches, unable to intervene, as the knights cut Becket down on the "
            "cathedral floor. The murder shocks all of Christendom. Within three years, "
            "Becket will be declared a saint.\n\n"
            "The palimpsest burns in Theo's hands. Words form: *When the king is above the "
            "law, the law means nothing. But who teaches the law? The scholars. Come.*"
        ),
        "choices": [
            {"text": "Follow the scholars — to the universities where reason and faith meet", "target": "scholar_university"},
            {"text": "Follow the law — to a meadow called Runnymede", "target": "scholar_magna_carta"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "Investiture Controversy", "definition": "The prolonged struggle between popes and European monarchs over who had the authority to appoint ('invest') bishops and abbots. It represented the fundamental tension between spiritual and secular power in medieval Europe."},
        ],
        "figures": ["Thomas Becket", "Henry II"],
        "tags": ["scholar", "norman", "becket", "church_state"],
    },

    "scholar_magna_carta": {
        "title": "The Great Charter",
        "text": (
            "June 15, 1215. A meadow along the Thames at Runnymede.\n\n"
            "King John — hated, distrusted, excommunicated — faces a wall of armed barons. "
            "They have rebelled. They have seized London. And they have brought a document.\n\n"
            "The **Magna Carta**.\n\n"
            "Theo reads over a clerk's shoulder: '*No free man shall be seized or imprisoned "
            "or stripped of his rights or possessions except by the lawful judgment of his "
            "equals or by the law of the land. To no one will we sell, to no one deny or "
            "delay right or justice.*'\n\n"
            "It is not a democratic document — it protects barons, not peasants. But the "
            "principle it establishes will echo through centuries: *the **rule of law** "
            "stands above even the king*.\n\n"
            "The palimpsest whispers: *The sword forced the king to sign. But the parchment "
            "is what endures. Words on vellum, outlasting every crown.*"
        ),
        "choices": [
            {"text": "Follow the words — to the universities where ideas take root", "target": "scholar_university"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "Magna Carta", "definition": "The 'Great Charter' signed by King John at Runnymede in 1215 under pressure from rebellious barons. It established the principle that even the king is subject to the law — a foundation stone of constitutional government."},
            {"term": "rule of law", "definition": "The principle that all people and institutions, including the king, are accountable to laws that are publicly promulgated, equally enforced, and independently adjudicated."},
        ],
        "figures": ["King John"],
        "tags": ["scholar", "norman", "magna_carta", "law"],
    },

    "scholar_university": {
        "title": "The Schools of Paris",
        "text": (
            "The **university** is a medieval invention. Theo sits in a crowded lecture hall "
            "at the University of Paris — founded around 1150, one of the first in Europe — "
            "where a master lectures on Aristotle's *Physics*.\n\n"
            "Students study the **liberal arts**: first the **trivium** (grammar, rhetoric, "
            "and logic — the arts of language and argument) and then the **quadrivium** "
            "(arithmetic, geometry, music, and astronomy — the arts of number). Only after "
            "mastering these does a student proceed to theology, law, or medicine.\n\n"
            "The method is the **scholastic method**: pose a question, cite authorities on "
            "both sides, reason through the arguments, and reach a conclusion. It is rigorous, "
            "systematic, and sometimes maddening in its attention to logical detail.\n\n"
            "'*It's like coding,*' Theo mutters, watching a disputatio where students argue "
            "whether angels can occupy the same space. '*If-then-else, but with Latin.*'\n\n"
            "The greatest of the scholastics is a large, quiet Dominican friar named Thomas."
        ),
        "choices": [
            {"text": "Study with Thomas Aquinas — the greatest medieval thinker", "target": "scholar_aquinas"},
            {"text": "Seek the barefoot friars who reject the university's wealth", "target": "scholar_mendicant"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "high_medieval",
        "vocabulary": [
            {"term": "university", "definition": "A self-governing community of scholars organized for teaching and learning. The medieval university was a new institution — a corporation with its own laws, degrees, and privileges, independent of both Church and king."},
            {"term": "trivium", "definition": "The lower division of the seven liberal arts: grammar, rhetoric, and logic. These 'three roads' taught students how to read, write, argue, and think clearly — the foundation of all further study."},
            {"term": "quadrivium", "definition": "The upper division of the seven liberal arts: arithmetic, geometry, music, and astronomy. These 'four roads' taught students the mathematical arts — the structure of the universe expressed in number."},
            {"term": "scholastic method", "definition": "The method of intellectual inquiry dominant in medieval universities: pose a question, cite authorities on both sides, use logical reasoning to resolve the disagreement, and reach a conclusion. Thomas Aquinas perfected it."},
        ],
        "figures": ["Thomas Aquinas"],
        "tags": ["scholar", "high_medieval", "university", "learning"],
    },

    "scholar_aquinas": {
        "title": "Faith Meets Reason",
        "text": (
            "Thomas Aquinas is enormous — his fellow students call him 'the Dumb Ox' for "
            "his size and silence. But when he speaks, everything becomes clear.\n\n"
            "'*There are two kinds of truth,*' Thomas explains to a group of students, Theo "
            "among them. '*Truths of faith, which come from revelation — that God exists as "
            "Trinity, that Christ rose from the dead. And truths of reason, which can be "
            "known by the natural light of the mind — that God exists, that the world has "
            "order, that good is to be done and evil avoided.*'\n\n"
            "His **Five Ways** — five arguments for God's existence from reason alone — "
            "draw on Aristotle, whom Thomas calls simply 'the Philosopher.' The works of "
            "**Averroes**, the great Spanish-Arab commentator on Aristotle, have profoundly "
            "shaped Thomas's thinking. Faith and reason cannot contradict each other, "
            "because both come from God.\n\n"
            "Theo raises his hand. '*But what if they seem to contradict?*'\n\n"
            "Thomas smiles. '*Then either the reasoning is flawed, or the interpretation "
            "of Scripture is wrong. The task of the theologian is to show the harmony.*'\n\n"
            "The palimpsest trembles. Dark words form: *But the harmony will break. A "
            "darkness approaches that no argument can answer.*"
        ),
        "choices": [
            {"text": "The darkness comes — the plague will shatter this world of faith", "target": "cross_plague"},
            {"text": "Follow the dawn star — Wycliffe translates the Bible into English", "target": "scholar_wycliffe"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "high_medieval",
        "vocabulary": [
            {"term": "Five Ways", "definition": "The five arguments for the existence of God presented by Thomas Aquinas in the Summa Theologica. Each begins from an observable feature of the world (motion, causation, contingency, degrees of perfection, purposeful design) and reasons to God as the ultimate explanation."},
            {"term": "Averroes", "definition": "The Spanish-Arab philosopher (1126-1198) whose commentaries on Aristotle profoundly influenced European scholastic thought. He argued that philosophy and religion are compatible paths to truth."},
        ],
        "figures": ["Thomas Aquinas", "Aristotle", "Averroes"],
        "tags": ["scholar", "high_medieval", "aquinas", "faith_reason"],
    },

    "scholar_mendicant": {
        "title": "The Barefoot Friar",
        "text": (
            "Francis of Assisi gave away everything — his father's wealth, his fine clothes, "
            "his future — and walked barefoot into a life of radical poverty. He called poverty "
            "his 'Lady' and preached to birds and wolves.\n\n"
            "Theo meets a **friar** — a member of a **mendicant** order, from the Latin "
            "*mendicare*, 'to beg.' Unlike monks who live in wealthy monasteries, friars "
            "live among the people, owning nothing, begging for their bread.\n\n"
            "'*The cathedrals are magnificent,*' the friar says, '*but Christ was born in a "
            "stable. Aquinas writes brilliantly, but the poor cannot read. We go where the "
            "need is.*'\n\n"
            "The mendicant orders — Francis's Franciscans and Dominic's Dominicans — are "
            "a reform movement within the Church, a reminder that Christianity began with "
            "a carpenter who had nowhere to lay his head.\n\n"
            "Dante, the exiled poet writing his **Divine Comedy** in Ravenna, has placed "
            "Francis in Paradise and corrupt popes in Hell — because the scholar and the "
            "saint both serve truth.\n\n"
            "The palimpsest shows Theo a world about to be tested beyond anything Francis "
            "could have imagined."
        ),
        "choices": [
            {"text": "The plague comes — witness the Black Death", "target": "cross_plague"},
            {"text": "Follow the morning star — Wycliffe and the English Bible", "target": "scholar_wycliffe"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "high_medieval",
        "vocabulary": [
            {"term": "friar", "definition": "A member of a mendicant religious order (such as the Franciscans or Dominicans) who lives not in a monastery but in the world, preaching, teaching, and begging for sustenance. From the Latin frater, meaning 'brother.'"},
            {"term": "mendicant", "definition": "From the Latin mendicare, 'to beg.' Mendicant religious orders embraced voluntary poverty, owning no property and depending on charity for survival. The Franciscans and Dominicans were the two great mendicant orders."},
            {"term": "Divine Comedy", "definition": "Dante Alighieri's epic poem (begun c. 1308, completed 1320), describing a journey through Hell, Purgatory, and Paradise. Written in Italian rather than Latin, it is considered the supreme literary achievement of the Middle Ages."},
        ],
        "figures": ["Francis of Assisi", "Dante Alighieri"],
        "tags": ["scholar", "high_medieval", "mendicant", "poverty"],
    },

    "scholar_wycliffe": {
        "title": "The Morning Star",
        "text": (
            "Oxford, 1380s. John Wycliffe sits in his study, surrounded by manuscripts. "
            "He is doing something revolutionary: translating the Bible into English.\n\n"
            "'*The Scriptures belong to the people,*' Wycliffe tells Theo. '*Not to priests "
            "who use Latin to keep the faithful ignorant. If God spoke to Moses in Hebrew and "
            "to Paul in Greek, why should He not speak to an English ploughman in English?*'\n\n"
            "Wycliffe goes further. He questions the Church's wealth, its political power, "
            "and the doctrine of **transubstantiation** — the belief that the bread and wine "
            "of communion literally become Christ's body and blood.\n\n"
            "His followers — the **Lollards** — carry handwritten English Bibles through the "
            "countryside. The Church condemns them. Wycliffe dies in 1384. Decades later, the "
            "Council of Constance orders his bones dug up and burned.\n\n"
            "In Prague, a professor named Jan Hus reads Wycliffe's writings and takes them "
            "further. Hus will be burned alive in 1415. But the sparks are spreading.\n\n"
            "The palimpsest shows an empire falling — and a machine that will change everything."
        ),
        "choices": [
            {"text": "The ancient world dies — witness the fall of Constantinople", "target": "cross_fall"},
            {"text": "Follow the sparks — to Gutenberg's printing press", "target": "scholar_press"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crisis",
        "vocabulary": [
            {"term": "transubstantiation", "definition": "The Catholic doctrine that the bread and wine of the Eucharist literally become the body and blood of Christ during the Mass, while retaining the outward appearance of bread and wine. Wycliffe and later Protestants challenged this teaching."},
            {"term": "Lollards", "definition": "Followers of John Wycliffe who advocated for Bible translation into English, questioned Church wealth, and challenged clerical authority. The name probably derives from a Dutch word meaning 'mumbler' — a term of mockery."},
        ],
        "figures": ["John Wycliffe", "Jan Hus"],
        "tags": ["scholar", "crisis", "pre_reformation", "bible"],
    },

    "scholar_press": {
        "title": "Knowledge Unbound",
        "text": (
            "Mainz, Germany, c. 1450. Johannes Gutenberg's workshop smells of ink and molten "
            "lead. Theo watches the most important invention since the wheel take shape.\n\n"
            "The **printing press** with **movable type** — individual metal letters that can "
            "be arranged, locked into a frame, inked, and pressed onto paper, then rearranged "
            "for the next page. Before Gutenberg, a single book took months to copy by hand in "
            "a scriptorium. Now, hundreds of identical copies can be produced in days.\n\n"
            "The first major work: the Gutenberg Bible. Forty-two lines per page, printed in "
            "two columns, with hand-painted illuminated initials.\n\n"
            "'*Do you understand what this means?*' Theo asks the palimpsest. '*Everything "
            "changes. Books become cheap. Ideas spread like fire. The Church can't control "
            "what people read anymore. This is — this is the internet.*'\n\n"
            "The palimpsest responds: *Yes. And fire can warm a house or burn it down. In "
            "sixty-seven years, a monk in Wittenberg will use this machine to shake the world.*\n\n"
            "But first, scholars are using the press for something gentler — the humanist "
            "dream of recovering and sharing ancient wisdom."
        ),
        "choices": [
            {"text": "Follow Erasmus — the prince of humanists, who wants to heal the Church through learning", "target": "scholar_erasmus"},
            {"text": "Follow the spark forward — to Luther's Reformation", "target": "reform_indulgences"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "printing press", "definition": "The machine developed by Johannes Gutenberg around 1440 that used movable metal type to mass-produce printed text. It democratized knowledge, lowered the cost of books dramatically, and made the Reformation possible."},
            {"term": "movable type", "definition": "Individual metal letters that can be arranged to form words, locked into a frame for printing, and then rearranged for the next page. Gutenberg's key innovation was casting these letters in a lead alloy that was durable and precise."},
        ],
        "figures": ["Johannes Gutenberg"],
        "tags": ["scholar", "renaissance", "printing", "technology"],
    },

    "scholar_erasmus": {
        "title": "The Prince of Humanists",
        "text": (
            "Desiderius Erasmus is the most famous scholar in Europe. His *Praise of Folly* — "
            "a witty satire of monks, theologians, and popes — has been printed in dozens of "
            "editions. He practices **Christian humanism**: applying the Renaissance's love of "
            "classical learning to reform the Church through education, not revolution.\n\n"
            "'*I wish the weakest woman might read the Gospels,*' Erasmus tells Theo. '*I wish "
            "they were translated into all languages. I wish the farmer sang them at his plow "
            "and the weaver hummed them at his shuttle.*'\n\n"
            "His friend Thomas More has written ***Utopia*** — from Greek *ou-topos*, 'no "
            "place' — imagining an ideal society where property is shared and reason governs "
            "all. The word **Utopia** will enter every language.\n\n"
            "But a volcanic force is rising in Wittenberg. Martin Luther does not want to "
            "heal the Church gently. He wants to tear down what is rotten and rebuild.\n\n"
            "Erasmus will write to Luther: '*I laid a hen's egg; Luther hatched a bird of "
            "quite a different species.*'"
        ),
        "choices": [
            {"text": "Follow Luther — conscience against the world", "target": "reform_indulgences"},
            {"text": "Enough — the scholar's path ends in the quiet room of the mind", "target": "end_scholar"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "Christian humanism", "definition": "A movement led by scholars like Erasmus and Thomas More who applied Renaissance humanist methods — close reading of original texts, classical education, rational inquiry — to Christian Scripture and theology, seeking to reform the Church through scholarship rather than revolution."},
            {"term": "Utopia", "definition": "An imaginary ideal society, from the book of the same name by Thomas More (1516). The word combines Greek ou ('no') and topos ('place') — literally 'no-place.' It has come to mean any vision of a perfect but unrealizable society."},
        ],
        "figures": ["Erasmus", "Thomas More"],
        "tags": ["scholar", "renaissance", "humanism", "erasmus"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  TRACK B — THE WARRIOR'S PATH (~13 nodes)
    #  Power, politics, conquest: battles → castles → crusades → war
    # ══════════════════════════════════════════════════════════════════════

    "warrior_vikings": {
        "title": "The Danelaw",
        "text": (
            "Theo stumbles onto the beach — and finds himself face to face with a Viking "
            "raiding party. The Norsemen stare at this strange boy in stranger clothes. "
            "Their leader speaks in accented English — many Vikings have traded with the "
            "English for decades.\n\n"
            "'*You are no monk. What are you?*'\n\n"
            "The Viking's eyes widen when he sees the palimpsest. He has seen rune-magic "
            "before. '*A seer's book. Come — you will be useful.*'\n\n"
            "Theo is swept into the **Great Heathen Army** — the massive Danish coalition "
            "that has invaded England and crushed every kingdom except Wessex. He sees the "
            "boundary of the **Danelaw** drawn across England: Danish law to the north and "
            "east, English law to the south and west.\n\n"
            "He is given to a **thegn** — an Anglo-Saxon nobleman — as a translator. The "
            "**ealdorman** of the local **shire** eyes him suspiciously but accepts the "
            "palimpsest's authority.\n\n"
            "The sword defines this world. But even the sword needs the law to hold what "
            "it conquers."
        ),
        "choices": [
            {"text": "Witness the conquest — Hastings, 1066, where an arrow changed everything", "target": "warrior_hastings"},
            {"text": "See how the conquerors build — Norman castles and the feudal order", "target": "warrior_castle"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [
            {"term": "Great Heathen Army", "definition": "The large Danish coalition that invaded England in 865 and spent the next fourteen years conquering the Anglo-Saxon kingdoms of Northumbria, East Anglia, and Mercia, leaving only Wessex under Alfred standing by 878."},
            {"term": "thegn", "definition": "An Anglo-Saxon nobleman who held land directly from the king in exchange for military service. Thegns formed the backbone of the English warrior class."},
            {"term": "ealdorman", "definition": "The royal official responsible for administering a shire in Anglo-Saxon England. The title later evolved into 'earl.'"},
            {"term": "shire", "definition": "An administrative division of Anglo-Saxon England, roughly equivalent to a county. Many English counties today still bear the names of their Anglo-Saxon shires."},
        ],
        "figures": [],
        "tags": ["warrior", "viking", "danelaw", "governance"],
    },

    "warrior_hastings": {
        "title": "The Arrow and the Crown",
        "text": (
            "October 14, 1066. Senlac Hill.\n\n"
            "Theo stands among the English **housecarls** — Harold Godwinson's elite "
            "warriors, locked in a shield wall at the top of the ridge. Below, the Norman "
            "cavalry charges again and again, horses screaming against the English axes.\n\n"
            "The battle has raged since morning. The Normans feign retreat — the English "
            "break ranks to pursue — and William's cavalry wheels to cut them down.\n\n"
            "Then the arrow. It arcs over the shield wall and strikes Harold in the eye. "
            "The king falls. The English line shatters.\n\n"
            "William of Normandy will be crowned on Christmas Day. He will bring a new "
            "system: **feudalism** — land held in exchange for military service, loyalty "
            "sworn upward through a chain from **villein** to knight to lord to king.\n\n"
            "The palimpsest shows a great stone tower rising over London — the power of "
            "the conqueror made permanent in stone."
        ),
        "choices": [
            {"text": "Follow the tower — see the new Norman order", "target": "warrior_castle"},
            {"text": "The parchment leaps — a pope calls for holy war", "target": "warrior_clermont"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "feudalism", "definition": "A political and economic system in which land (fiefs) is granted by lords to vassals in exchange for military service and loyalty. It created a pyramid of obligation from king down to the lowest serf."},
            {"term": "villein", "definition": "A medieval peasant bound to the land they worked. Villeins owed labor and a share of their produce to the lord of the manor. They were not slaves but could not leave without permission."},
        ],
        "figures": ["Harold Godwinson", "William the Conqueror"],
        "tags": ["warrior", "norman", "hastings", "conquest"],
    },

    "warrior_castle": {
        "title": "Stone and Power",
        "text": (
            "The White Tower rises over London — massive, square, built of pale Caen stone "
            "shipped from Normandy. It is a statement: *We are here. We are staying.*\n\n"
            "Theo walks through a Norman **motte-and-bailey** castle being constructed in "
            "the countryside. Workers — English peasants conscripted for the labor — raise "
            "an earthen mound (the motte) and surround it with a wooden palisade (the bailey). "
            "Later, the wood will be replaced with stone.\n\n"
            "A Norman lord explains the new order. '*I hold this **fief** from the baron. He "
            "holds his from the earl. The earl holds his from the king. Each of us has sworn "
            "**homage** and **fealty** — an oath of loyalty sealed by kneeling, placing our "
            "hands between our lord's, and pledging our sword.*'\n\n"
            "'*And the English who lived here before?*' Theo asks.\n\n"
            "The lord shrugs. '*They work the **demesne** — the lord's personal land. They "
            "pay their rents. They are **vassals** now, whether they like it or not.*'\n\n"
            "The palimpsest shows a new vision: a cross, a desert, and an army marching east."
        ),
        "choices": [
            {"text": "Follow the army — to a council where the Pope calls for Crusade", "target": "warrior_clermont"},
            {"text": "Follow the law — Henry II builds common law, and a friend becomes an enemy", "target": "warrior_law"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "motte-and-bailey", "definition": "A type of castle with an earthen mound (motte) topped by a keep, surrounded by an enclosed courtyard (bailey) protected by a ditch and palisade. The Normans built hundreds across England after the Conquest."},
            {"term": "fief", "definition": "A grant of land given by a lord to a vassal in exchange for homage, loyalty, and military service. From the Latin feudum, which gives us the word 'feudalism.'"},
            {"term": "homage", "definition": "The formal ceremony in which a vassal pledged loyalty to a lord, kneeling and placing his hands between the lord's hands. It created a sacred bond of mutual obligation."},
            {"term": "fealty", "definition": "The oath of faithfulness sworn by a vassal to a lord as part of the feudal contract. Breaking fealty was one of the gravest offenses in the medieval world."},
            {"term": "vassal", "definition": "A person who holds land (a fief) from a lord in exchange for military service and loyalty. A vassal could himself be a lord to lesser vassals below him."},
            {"term": "demesne", "definition": "The portion of a manor's land farmed directly for the lord, as opposed to the land worked by tenants for their own sustenance. Pronounced 'deh-MANE.'"},
        ],
        "figures": ["William the Conqueror"],
        "tags": ["warrior", "norman", "castle", "feudalism"],
    },

    "warrior_law": {
        "title": "The King's Justice",
        "text": (
            "Decades pass on the palimpsest's surface. Henry II sits on the English throne — "
            "energetic, impatient, brilliant. He is building something revolutionary: a system "
            "of **common law** that applies equally across the realm.\n\n"
            "Before Henry, justice was local — each baron's court made its own rules. Now, "
            "royal judges ride circuits through the shires, hearing cases and recording their "
            "decisions. Over time, these decisions build on each other, creating a body of law "
            "common to all of England.\n\n"
            "'*The genius,*' a clerk explains to Theo, '*is that the law now has a memory. "
            "What one judge decides, another judge in another shire will follow. Precedent, "
            "they call it.*'\n\n"
            "But Henry's great project has a problem. The Church claims its own courts, "
            "its own laws, its own jurisdiction. Henry's friendship with Thomas Becket — "
            "the Archbishop he himself appointed — shatters over this question. Four knights "
            "will murder Becket in Canterbury Cathedral.\n\n"
            "The palimpsest shows the cross and the sword, forever at war."
        ),
        "choices": [
            {"text": "The Pope calls for Crusade — the sword marches east", "target": "warrior_clermont"},
            {"text": "The parchment leaps ahead — battlefields of the Hundred Years' War", "target": "warrior_war"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "common law", "definition": "The system of law developed in England based on court decisions and precedent rather than written statutes. Henry II established royal circuit courts that created a unified body of law 'common' to the whole realm."},
        ],
        "figures": ["Henry II"],
        "tags": ["warrior", "norman", "law", "common_law"],
    },

    "warrior_clermont": {
        "title": "God Wills It",
        "text": (
            "November 27, 1095. Clermont, France.\n\n"
            "Pope Urban II stands before an enormous crowd in an open field — the cathedral "
            "was too small to hold them all. His voice carries across the assembly:\n\n"
            "'*A race from the kingdom of the Persians has invaded the lands of the Christians "
            "and has depopulated them by the sword, pillage, and fire. I exhort you — take "
            "the road to the Holy Sepulchre. Whoever goes on this journey and ends his life "
            "there shall have remission of sins.*'\n\n"
            "An **indulgence** — forgiveness of the punishment for sin — offered to every "
            "warrior who takes the cross. The crowd roars: '***Deus lo volt!*** God wills it!'\n\n"
            "The First **Crusade** is born. Within four years, Jerusalem will fall to Christian "
            "armies. New military orders — the **Knights Templar** and **Knights Hospitaller** — "
            "will guard the **Crusader states** established along a narrow coastal strip.\n\n"
            "Theo watches men sew crosses onto their tunics. The palimpsest glows hot — the "
            "sword is marching, and it demands a witness."
        ),
        "choices": [
            {"text": "March with the Crusaders toward Jerusalem", "target": "warrior_jerusalem"},
            {"text": "Follow the war to its darkest hour — the Fourth Crusade", "target": "warrior_fourth"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crusade",
        "vocabulary": [
            {"term": "indulgence", "definition": "In Catholic theology, a remission of the temporal punishment due for sins already forgiven. The Pope offered indulgences to Crusaders, and later their sale became a major source of Church revenue — and eventually, a trigger for the Reformation."},
            {"term": "Crusade", "definition": "A military expedition authorized by the Pope to recover the Holy Land from Muslim control. The major Crusades spanned from 1095 to 1291, reshaping relations between Christian Europe and the Islamic world."},
            {"term": "Knights Templar", "definition": "A military religious order founded around 1119 to protect Christian pilgrims traveling to the Holy Land. The Templars became enormously wealthy and powerful, operating an early form of international banking."},
            {"term": "Knights Hospitaller", "definition": "A military religious order originally founded to care for sick pilgrims in Jerusalem. Like the Templars, they became a formidable military force defending the Crusader states."},
            {"term": "Crusader states", "definition": "The four Latin Christian principalities established in the Holy Land after the First Crusade: the County of Edessa, the Principality of Antioch, the County of Tripoli, and the Kingdom of Jerusalem. They lasted from 1099 to 1291."},
            {"term": "Deus lo volt!", "definition": "Latin/Old French for 'God wills it!' — the battle cry of the First Crusade, shouted by the crowd at Clermont after Pope Urban II's call to arms."},
        ],
        "figures": ["Pope Urban II"],
        "tags": ["warrior", "crusade", "clermont", "call_to_arms"],
    },

    "warrior_jerusalem": {
        "title": "The Holy City",
        "text": (
            "Jerusalem has changed hands many times. Theo watches the Crusader kingdom "
            "at its height — the great **concentric castle** of **Krak des Chevaliers** "
            "dominating the Syrian landscape, its double walls and round towers representing "
            "the pinnacle of military architecture.\n\n"
            "But the kingdom is fragile. Surrounded by Muslim territory, dependent on "
            "reinforcements from Europe that arrive slowly or not at all.\n\n"
            "Then **Saladin** comes. The Kurdish sultan who united Egypt and Syria is not "
            "the savage that Crusader propaganda describes. He is cultured, devout, and "
            "merciful — when he retakes Jerusalem in 1187, he spares the Christian inhabitants, "
            "a sharp contrast to the bloodbath of the First Crusade's conquest.\n\n"
            "Theo watches Richard the Lionheart and Saladin negotiate the Treaty of Jaffa — "
            "a compromise. The code of **chivalry** demands honor between enemies, and both "
            "men embody it — in their fashion.\n\n"
            "The palimpsest flickers with darker visions: Christian soldiers sacking a "
            "Christian city. Constantinople, 1204."
        ),
        "choices": [
            {"text": "Witness the Fourth Crusade — when the mission went horribly wrong", "target": "warrior_fourth"},
            {"text": "The plague comes — the sword cannot fight what it cannot see", "target": "cross_plague"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crusade",
        "vocabulary": [
            {"term": "concentric castle", "definition": "A castle design with two or more concentric rings of defensive walls, one inside the other. If attackers breached the outer wall, they found themselves trapped in a killing ground before the inner wall."},
            {"term": "Krak des Chevaliers", "definition": "The greatest of the Crusader castles, located in modern Syria. Held by the Knights Hospitaller, its concentric design and massive walls made it nearly impregnable. T. E. Lawrence called it 'the finest castle in the world.'"},
            {"term": "Saladin", "definition": "The Kurdish Muslim sultan (1137-1193) who united Egypt and Syria and recaptured Jerusalem from the Crusaders in 1187. Renowned for his military skill and chivalric conduct."},
            {"term": "chivalry", "definition": "The code of conduct for medieval knights, combining martial skill with Christian virtues: courage, honor, loyalty, courtesy, and protection of the weak. In practice, chivalry was an ideal often honored more in literature than in life."},
        ],
        "figures": ["Saladin", "Richard I"],
        "tags": ["warrior", "crusade", "jerusalem", "chivalry"],
    },

    "warrior_fourth": {
        "title": "The Betrayal of Constantinople",
        "text": (
            "1204. The Fourth Crusade. The army that was supposed to liberate Jerusalem "
            "has been diverted — by debt, by politics, by Venetian greed — to Constantinople, "
            "the greatest Christian city in the world.\n\n"
            "Theo watches in horror as Crusader knights storm the walls of the city that "
            "has stood for nine centuries. They loot churches, smash icons, ride horses into "
            "the Hagia Sophia. A prostitute sits on the patriarch's throne and sings bawdy "
            "songs.\n\n"
            "Geoffrey of Villehardouin, a Crusader chronicler, will write an account that "
            "tries to justify the madness. But the truth is plain: the Crusading ideal has "
            "devoured itself.\n\n"
            "'*Men set out to do God's work,*' the palimpsest writes, '*and did the devil's "
            "instead. Is the fault in the idea or in the men?*'\n\n"
            "The Eastern Roman Empire — Byzantium — will never recover. But the warrior's "
            "road continues — to the longest war Europe has ever seen."
        ),
        "choices": [
            {"text": "The Hundred Years' War — when warfare itself was transformed", "target": "warrior_war"},
            {"text": "The plague comes first — death on a scale no army can match", "target": "cross_plague"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crusade",
        "vocabulary": [],
        "figures": ["Geoffrey of Villehardouin"],
        "tags": ["warrior", "crusade", "fourth_crusade", "betrayal"],
    },

    "warrior_war": {
        "title": "The Long War",
        "text": (
            "The **Hundred Years' War** (1337-1453) between England and France is not one "
            "war but a series of campaigns spanning five generations. It transforms warfare.\n\n"
            "At the Battle of Cr\u00e9cy (1346), Theo watches English **longbow**men — common "
            "soldiers, not knights — cut down the flower of French chivalry. Arrows rain on "
            "armored horsemen like a steel hailstorm. The age of the mounted knight is ending.\n\n"
            "**Gunpowder** — arriving from China via the Silk Road — appears on European "
            "battlefields for the first time. Crude cannons shake the earth. Within a century, "
            "they will make castle walls obsolete.\n\n"
            "The old world of chivalry — knights on horseback, personal combat, honor and "
            "courtesy — is dying in the mud of Cr\u00e9cy and Agincourt. Something harder, "
            "more ruthless, more modern is being born.\n\n"
            "But in the darkest hour of France's defeat, an impossible figure appears: "
            "a seventeen-year-old peasant girl who says God has sent her to save the kingdom."
        ),
        "choices": [
            {"text": "Follow Joan of Arc — the girl who turned the tide", "target": "warrior_joan"},
            {"text": "Follow the fall — Constantinople is about to fall forever", "target": "cross_fall"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crisis",
        "vocabulary": [
            {"term": "Hundred Years' War", "definition": "The series of conflicts between England and France from 1337 to 1453 over the English claim to the French throne. It transformed warfare, ended the age of chivalric combat, and forged the national identities of both countries."},
            {"term": "longbow", "definition": "The English weapon that revolutionized medieval warfare. A six-foot bow of yew wood, it could pierce armor at 200 yards. English longbowmen — common soldiers, not knights — won stunning victories at Cr\u00e9cy, Poitiers, and Agincourt."},
            {"term": "gunpowder", "definition": "An explosive mixture of saltpeter, sulfur, and charcoal, invented in China and transmitted to Europe via the Silk Road. Its use in cannons eventually made castle walls and armored knights obsolete."},
        ],
        "figures": [],
        "tags": ["warrior", "crisis", "war", "military_revolution"],
    },

    "warrior_joan": {
        "title": "The Maid of Orl\u00e9ans",
        "text": (
            "**Joan of Arc** is seventeen — Theo's age. She is illiterate, she is a peasant, "
            "and she is standing before the **Dauphin** — the uncrowned heir to the French "
            "throne — telling him that God has sent her to drive the English from France.\n\n"
            "Against all reason, the Dauphin gives her an army. Against all military logic, "
            "she lifts the siege of Orl\u00e9ans in nine days. She leads Charles to his "
            "coronation at Reims.\n\n"
            "Theo watches her ride at the head of the army — a small figure in white armor, "
            "carrying a banner embroidered with lilies. The soldiers worship her. The English "
            "fear her.\n\n"
            "Then Burgundian soldiers capture her. The English put her on trial for heresy and "
            "witchcraft. She is nineteen when they burn her alive at Rouen.\n\n"
            "Twenty-five years later, a second trial will declare her innocent. Five centuries "
            "after that, she will be canonized a saint.\n\n"
            "The palimpsest weeps — or seems to. Its surface glistens."
        ),
        "choices": [
            {"text": "Follow Machiavelli — the man who asked how power really works", "target": "warrior_machiavelli"},
            {"text": "The warrior has seen enough death — retreat into survival", "target": "end_survivor"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crisis",
        "vocabulary": [
            {"term": "Joan of Arc", "definition": "The French peasant girl (c. 1412-1431) who claimed divine visions told her to drive the English from France. She lifted the siege of Orl\u00e9ans, helped crown Charles VII, was captured, tried for heresy, and burned at the stake. She was canonized as a saint in 1920."},
        ],
        "figures": ["Joan of Arc"],
        "tags": ["warrior", "crisis", "joan", "faith"],
    },

    "warrior_machiavelli": {
        "title": "The Dangerous Question",
        "text": (
            "Florence, 1513. Niccol\u00f2 Machiavelli sits in exile, writing. He has been "
            "tortured on the rack by the Medici — the same family that once employed him "
            "as a diplomat. Now he writes *The Prince*, the most notorious book on power "
            "ever written.\n\n"
            "'*I am not interested in how men should live,*' Machiavelli tells Theo. '*I am "
            "interested in how they do live. A prince who tries to be good in every way will "
            "be ruined among so many who are not good.*'\n\n"
            "His advice is ruthlessly pragmatic: it is better to be feared than loved. A prince "
            "must be willing to act against mercy, against faith, against humanity — when "
            "necessity demands it. The word '**Machiavellian**' will enter every European "
            "language as a synonym for cunning.\n\n"
            "The palimpsest responds with a vision: a monk nailing a document to a church "
            "door. The warrior's world of swords and princes is about to be shaken by "
            "something no army can stop — an idea."
        ),
        "choices": [
            {"text": "Follow the idea — to the Reformation's beginning", "target": "reform_indulgences"},
            {"text": "The warrior's road has led only to power and more power — there must be something else", "target": "end_survivor"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "Machiavellian", "definition": "Cunning, scheming, and unscrupulous in political dealings. Named after Niccol\u00f2 Machiavelli, whose book The Prince advised rulers to prioritize effective governance over moral idealism."},
        ],
        "figures": ["Niccol\u00f2 Machiavelli"],
        "tags": ["warrior", "renaissance", "machiavelli", "power"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  TRACK C — THE MERCHANT'S PATH (~13 nodes)
    #  Trade, cities, innovation: commerce → guilds → Florence → exploration
    # ══════════════════════════════════════════════════════════════════════

    "merchant_trade": {
        "title": "The Dragon Ships' Cargo",
        "text": (
            "The Norse trader on the beach is not a raider — or not only a raider. '*The "
            "same ships that carry swords carry silver,*' he tells Theo. '*War is expensive. "
            "Trade pays for it.*'\n\n"
            "Theo discovers that the Vikings are not merely destroyers. They are the "
            "greatest traders of their age, linking the markets of Scandinavia to "
            "Constantinople and Baghdad through river routes across Russia. Norse coins "
            "have been found as far as Central Asia.\n\n"
            "The trader shows Theo his cargo: amber from the Baltic, furs from the north, "
            "walrus ivory, and — most precious — Frankish swords, the finest blades in "
            "Europe. '*Everything has a price,*' the trader says. '*Even a monastery. "
            "Especially a monastery.*'\n\n"
            "The palimpsest writes: *The coin connects what the sword divides. Follow "
            "the trade routes and you will find the real story of these centuries.*"
        ),
        "choices": [
            {"text": "Follow the coin south — to the great survey of England's wealth", "target": "merchant_domesday"},
            {"text": "Follow the trade routes east — toward the pilgrim roads", "target": "merchant_pilgrim_road"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "viking",
        "vocabulary": [],
        "figures": [],
        "tags": ["merchant", "viking", "trade"],
    },

    "merchant_domesday": {
        "title": "The Great Survey",
        "text": (
            "1086. William the Conqueror has ordered something no king has attempted before: "
            "a complete inventory of every piece of property in England. Every manor, every "
            "acre, every cow, every pig — recorded by royal commissioners who travel from "
            "shire to shire, asking questions under oath.\n\n"
            "Theo watches the process in a village hall. A Norman commissioner reads from "
            "a list: '*How much land? How many plows? How many villeins, how many freemen? "
            "What was it worth in King Edward's time? What is it worth now?*'\n\n"
            "The English call it the **Domesday Book** — the Book of Judgment — because "
            "its record is final, like God's judgment on the Last Day. There is no appeal.\n\n"
            "'*This is power,*' Theo realizes. '*Not just the sword — the record. Whoever "
            "controls the written account controls the land.*'\n\n"
            "The palimpsest agrees. New words form: *The pen and the sword serve the same "
            "master — but the coin outlasts them both. Follow the money east.*"
        ),
        "choices": [
            {"text": "Follow the pilgrim road east — where trade and faith intertwine", "target": "merchant_pilgrim_road"},
            {"text": "Follow the merchants who see opportunity in the Crusades", "target": "merchant_crusade_trade"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "norman",
        "vocabulary": [
            {"term": "Domesday Book", "definition": "The comprehensive survey of English landholding completed in 1086 on William the Conqueror's orders. It recorded the ownership, size, and value of nearly every piece of property in England — an administrative achievement unmatched in medieval Europe."},
        ],
        "figures": ["William the Conqueror"],
        "tags": ["merchant", "norman", "domesday", "administration"],
    },

    "merchant_pilgrim_road": {
        "title": "The Pilgrim Road",
        "text": (
            "The road east is long. Theo travels with merchants, pilgrims, and soldiers — "
            "all mixed together in the great tide flowing toward the Holy Land. A **pilgrimage** "
            "it is called: a sacred journey to a holy place, undertaken for penance, devotion, "
            "or (Theo suspects, watching the merchants) profit.\n\n"
            "The **spice trade** draws European merchants eastward as powerfully as faith draws "
            "the knights. Pepper, cinnamon, cloves, nutmeg — worth more than their weight in "
            "silver. And the route passes through lands where Islamic civilization far surpasses "
            "Christian Europe in medicine, mathematics, and astronomy.\n\n"
            "A Frankish trader shows Theo an **astrolabe** — a brass instrument acquired from "
            "Arab astronomers. '*They call the stars by names we cannot pronounce,*' he says. "
            "'*Their libraries hold books that Rome forgot a thousand years ago.*'\n\n"
            "The palimpsest shows a forking road: one path leads to the markets of the East, "
            "where the real exchange is happening. The other leads to the greatest road of all."
        ),
        "choices": [
            {"text": "Follow the merchants — the exchange of goods and ideas", "target": "merchant_crusade_trade"},
            {"text": "Follow the Silk Road — to Cathay and beyond", "target": "merchant_silk_road"},
            {"text": "The violence and greed are too much — turn back and wait for history to pass", "target": "end_bystander"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crusade",
        "vocabulary": [
            {"term": "pilgrimage", "definition": "A journey to a sacred place undertaken for religious devotion, penance, or spiritual growth. Major Christian pilgrimage destinations included Jerusalem, Rome, and Santiago de Compostela."},
            {"term": "spice trade", "definition": "The commerce in exotic spices (pepper, cinnamon, cloves, nutmeg) between Asia and Europe, worth enormous sums. Control of spice routes was a major driver of exploration and conflict."},
            {"term": "astrolabe", "definition": "A sophisticated astronomical instrument used for navigation, timekeeping, and surveying. Developed by Greek astronomers and refined by Islamic scholars, astrolabes were introduced to Europe through contact during the Crusades."},
        ],
        "figures": [],
        "tags": ["merchant", "crusade", "trade", "pilgrimage"],
    },

    "merchant_crusade_trade": {
        "title": "The Bridge Between Worlds",
        "text": (
            "The most lasting legacy of the Crusades is not conquest but contact. In the "
            "markets of Acre and Antioch, Theo watches European merchants discover goods "
            "and ideas that will transform their world.\n\n"
            "Arab mathematicians preserved and advanced Greek knowledge. The works of "
            "**Avicenna** in medicine will reshape European thought. Arabic numerals — far "
            "superior to Roman ones — will revolutionize commerce. Sugar, cotton, and paper "
            "flow westward.\n\n"
            "**Bernard of Clairvaux**, the great Cistercian monk who preached the Second "
            "Crusade, warned against the spiritual dangers of the East. But the East's "
            "knowledge is irresistible — and for the merchants, its goods are more "
            "irresistible still.\n\n"
            "'*This is what always happens,*' Theo tells the palimpsest. '*People go to "
            "conquer and come back changed.*'\n\n"
            "The parchment responds: *The coin cares nothing for borders. Follow it further "
            "east, to the greatest road the world has ever known.*"
        ),
        "choices": [
            {"text": "Follow the Silk Road — to Cathay and the Mongol Empire", "target": "merchant_silk_road"},
            {"text": "Stay in the Mediterranean — watch the cathedral cities rise", "target": "merchant_cathedral"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crusade",
        "vocabulary": [
            {"term": "Avicenna", "definition": "The Persian physician and philosopher (980-1037) whose Canon of Medicine was the standard medical textbook in both the Islamic world and European universities for centuries."},
            {"term": "Bernard of Clairvaux", "definition": "The French Cistercian monk and theologian (1090-1153) whose preaching launched the Second Crusade. He was the most influential churchman of his age, founding 68 monasteries and shaping the spirituality of medieval Europe."},
        ],
        "figures": ["Avicenna", "Bernard of Clairvaux"],
        "tags": ["merchant", "crusade", "trade", "knowledge_transfer"],
    },

    "merchant_silk_road": {
        "title": "The Road to Cathay",
        "text": (
            "The **Silk Road** stretches from Venice to China — a network of caravan routes "
            "crossing deserts, mountains, and empires. Under the **Pax Mongolica** — the peace "
            "imposed by the vast **Mongol Empire** — the road is safer than it has been in "
            "centuries.\n\n"
            "Theo travels with Venetian merchants following the route Marco Polo described in "
            "his *Travels*: through Persia, across the Pamir Mountains, to the court of Kublai "
            "Khan. Along the way, the merchants carry westward not just silk and spices but "
            "ideas: paper, gunpowder, the magnetic compass.\n\n"
            "'*Europe thinks it is the center of the world,*' a Mongol guide tells Theo. "
            "'*But from here, Europe is a small, cold, quarrelsome peninsula.*'\n\n"
            "Theo sees the palimpsest absorb this broader perspective. Its text grows denser, "
            "more layered — as if it is writing not just European history but the story of "
            "a world connected by trade and curiosity.\n\n"
            "But the Silk Road carries more than goods. Along these same routes, something "
            "terrible is moving westward."
        ),
        "choices": [
            {"text": "The horror arrives — rats, fleas, and death beyond counting", "target": "cross_plague"},
            {"text": "Follow the wealth to the cathedral cities of Europe", "target": "merchant_cathedral"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "high_medieval",
        "vocabulary": [
            {"term": "Silk Road", "definition": "The network of overland trade routes connecting China to the Mediterranean. Silk, spices, paper, and gunpowder moved westward; gold, silver, and glass moved eastward. The routes also carried ideas, religions, and — eventually — plague."},
            {"term": "Pax Mongolica", "definition": "The period of relative peace and stability across the vast Mongol Empire (c. 1206-1368) that made long-distance trade along the Silk Road safer and more profitable than at any time before or since."},
            {"term": "Mongol Empire", "definition": "The largest contiguous land empire in history, founded by Genghis Khan in 1206. At its peak, it stretched from Korea to Hungary, encompassing China, Persia, Central Asia, and Russia."},
        ],
        "figures": ["Marco Polo", "Kublai Khan"],
        "tags": ["merchant", "high_medieval", "silk_road", "global"],
    },

    "merchant_cathedral": {
        "title": "Theology in Stone",
        "text": (
            "Chartres, France. The cathedral is rising.\n\n"
            "Theo stands in the nave and looks up — and up — and up. The **Gothic architecture** "
            "is a revolution in stone: pointed arches that carry weight downward, **flying "
            "buttresses** that brace the walls from outside, allowing them to be pierced with "
            "enormous stained-glass windows.\n\n"
            "Light pours through the glass in rivers of color — blue, red, gold. Each window "
            "tells a story: the life of Christ, the saints, the Last Judgment. For a population "
            "that cannot read, these windows are the Bible made visible.\n\n"
            "But the merchant sees what the pilgrim does not: cathedrals are funded by trade. "
            "The guilds — associations of craftsmen and merchants — donate the great windows. "
            "Each window bears the guild's emblem: the bakers, the weavers, the furriers. "
            "Commerce and faith are intertwined.\n\n"
            "Construction will take generations. The grandfather who laid the foundation will "
            "never see the spire. It is an act of faith in the future — the belief that what "
            "you build matters even if you never see it finished."
        ),
        "choices": [
            {"text": "The plague comes — it will devastate the merchant class most of all", "target": "cross_plague"},
            {"text": "Follow the wealth to Renaissance Florence — where bankers become princes", "target": "merchant_florence"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "high_medieval",
        "vocabulary": [
            {"term": "Gothic architecture", "definition": "The medieval building style characterized by pointed arches, ribbed vaults, flying buttresses, and large stained-glass windows. Gothic cathedrals aspired to maximum height and light, creating spaces that lifted the spirit toward heaven."},
            {"term": "flying buttress", "definition": "An external arch that transfers the weight of a roof or vault away from the wall, allowing the wall to be thinner and filled with windows. This engineering innovation made the soaring, light-filled Gothic cathedrals possible."},
        ],
        "figures": [],
        "tags": ["merchant", "high_medieval", "cathedral", "architecture"],
    },

    "merchant_florence": {
        "title": "The City of Flowers",
        "text": (
            "Florence under Lorenzo de' Medici — 'the Magnificent' — is a city drunk on beauty "
            "and ambition. The **Renaissance** — the 'rebirth' of classical learning — is "
            "in full bloom.\n\n"
            "**Humanism** — the intellectual movement at the heart of the Renaissance — "
            "has rediscovered the **studia humanitatis**: grammar, rhetoric, poetry, history, "
            "and moral philosophy. Not to replace Christianity, but to enrich it.\n\n"
            "Lorenzo is a **patron** of the arts — a wealthy banker who commissions "
            "paintings, sculptures, and buildings. His Platonic Academy brings together "
            "scholars who translate Plato directly from Greek for the first time.\n\n"
            "Theo walks through a city where Botticelli paints the *Birth of Venus*, where "
            "Michelangelo carves his first sculptures, where the young Leonardo da Vinci "
            "sketches machines that will not be built for five hundred years.\n\n"
            "The palimpsest shimmers: *The merchant made this possible. Without the banker's "
            "gold, the artist starves. Follow the money — it leads to wonders.*"
        ),
        "choices": [
            {"text": "Enter Leonardo's workshop — where art meets science", "target": "merchant_workshop"},
            {"text": "Follow the explorers heading west into the unknown", "target": "merchant_exploration"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "Renaissance", "definition": "The 'rebirth' of classical Greek and Roman learning that began in Italy in the 14th century and spread across Europe. It transformed art, literature, philosophy, and science, bridging the medieval and modern worlds."},
            {"term": "humanism", "definition": "The intellectual movement at the heart of the Renaissance, centered on the study of classical Greek and Roman texts (the studia humanitatis). Humanists believed that education in literature, history, and philosophy could develop the full potential of the human person."},
            {"term": "studia humanitatis", "definition": "Latin for 'the studies of humanity' — the Renaissance educational curriculum of grammar, rhetoric, poetry, history, and moral philosophy, drawn from classical sources. The origin of our word 'humanities.'"},
            {"term": "patron", "definition": "A wealthy supporter of the arts who commissions and funds the work of artists, writers, and scholars. The Medici family of Florence were the most famous Renaissance patrons."},
        ],
        "figures": ["Lorenzo de' Medici", "Leonardo da Vinci", "Michelangelo"],
        "tags": ["merchant", "renaissance", "florence", "humanism"],
    },

    "merchant_workshop": {
        "title": "The Universal Man",
        "text": (
            "Leonardo's workshop is chaos made productive. Anatomical drawings pin next to "
            "flying machine sketches. A half-finished painting of the Virgin stands beside "
            "a design for a military fortification.\n\n"
            "Leonardo is the **Renaissance man** — the ***uomo universale*** — the ideal of "
            "a person accomplished in every field. Painter, sculptor, architect, engineer, "
            "anatomist, inventor, musician, writer.\n\n"
            "He shows Theo his notebooks — thousands of pages, written in mirror script. "
            "'*The eye is the window of the soul,*' Leonardo says. '*I paint what I see, "
            "and to see truly, I must understand. To paint a hand, I dissect hands. To paint "
            "water, I study currents.*'\n\n"
            "His technique of **linear perspective** — the mathematical illusion of three-"
            "dimensional depth on a flat surface — has revolutionized painting. Artists now "
            "use geometry to create **vanishing points** where parallel lines converge, "
            "making their paintings windows into another world.\n\n"
            "But Leonardo sees something the palimpsest also sees: beyond the workshop, "
            "beyond Florence, ships are sailing into the unknown."
        ),
        "choices": [
            {"text": "Follow the explorers — the Age of Exploration begins", "target": "merchant_exploration"},
            {"text": "The beauty of Florence is enough — the merchant's journey ends here", "target": "end_pilgrim"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "linear perspective", "definition": "A mathematical technique for creating the illusion of three-dimensional depth on a flat surface. Developed during the Renaissance by Brunelleschi and refined by Alberti, it uses converging lines and vanishing points to mimic how the human eye perceives space."},
            {"term": "vanishing point", "definition": "The point on the horizon at which parallel lines appear to converge in a perspective drawing or painting. A single vanishing point creates the illusion of depth and distance."},
        ],
        "figures": ["Leonardo da Vinci"],
        "tags": ["merchant", "renaissance", "leonardo", "art_science"],
    },

    "merchant_exploration": {
        "title": "Beyond the Horizon",
        "text": (
            "The **caravel** — a small, maneuverable ship with **lateen sails** that can "
            "sail into the wind — is carrying European explorers into waters no European has "
            "ever charted.\n\n"
            "Portuguese navigators creep down the African coast. Columbus, in 1492, sails west "
            "and stumbles onto a continent no European knew existed. Vasco da Gama rounds "
            "Africa and reaches India by sea in 1498.\n\n"
            "The world is suddenly larger — and smaller — than anyone imagined.\n\n"
            "Theo watches from the harbor of Lisbon as ships return with spices, gold, and "
            "stories of peoples and civilizations beyond European knowledge. The astrolabe "
            "and compass guide them; the printing press spreads their discoveries.\n\n"
            "'*They think they are discovering the world,*' the palimpsest writes. '*But the "
            "world was already there. What they are discovering is their own ignorance.*'\n\n"
            "A new age is being born — but it carries the old age's worst impulses alongside "
            "its best aspirations. And in Europe, a rupture is coming that will reshape "
            "everything the merchant has built."
        ),
        "choices": [
            {"text": "Return to Europe — the Reformation is about to begin", "target": "reform_indulgences"},
            {"text": "The journey itself is the destination — Theo has traveled far enough", "target": "end_pilgrim"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "renaissance",
        "vocabulary": [
            {"term": "caravel", "definition": "A small, highly maneuverable sailing ship developed by the Portuguese in the 15th century. Its combination of square and lateen sails allowed it to sail into the wind, making long-distance ocean voyages possible."},
        ],
        "figures": [],
        "tags": ["merchant", "renaissance", "exploration", "technology"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  CROSSOVER POINTS — ALL TRACKS CONVERGE BRIEFLY (2 nodes)
    # ══════════════════════════════════════════════════════════════════════

    "cross_plague": {
        "title": "The Black Death",
        "text": (
            "1348. The dying world.\n\n"
            "The **Black Death** — **bubonic plague** — has arrived. Carried by fleas on "
            "rats, the bacterium **Yersinia pestis** spreads with terrifying speed. Black "
            "swellings — **buboes** — appear in the groin and armpits. Most who show "
            "symptoms are dead within days.\n\n"
            "It does not matter if you are a scholar, a warrior, or a merchant. The plague "
            "takes all.\n\n"
            "Theo walks through streets where corpses are stacked like firewood. The stench "
            "is unbearable. Physicians in beaked masks — stuffed with herbs against the "
            "**miasma** they believe causes plague — move through the desolation, helpless.\n\n"
            "Boccaccio will write: '*Brother abandoned brother, uncle abandoned nephew, wife "
            "abandoned husband.*'\n\n"
            "**Flagellants** march through the streets, whipping themselves bloody, believing "
            "the plague is God's punishment. Others turn on Jewish communities, blaming them "
            "for poisoning wells.\n\n"
            "**Serfdom** collapses in western Europe. With a third of the population dead, "
            "survivors demand higher wages. The **Peasants' Revolt** of 1381 will erupt — "
            "crushed, but the old feudal bonds never fully recover.\n\n"
            "The **Great Western Schism** has produced two popes — one in Rome, one in "
            "Avignon — each claiming to be the true Vicar of Christ.\n\n"
            "One third of Europe will die. The world that existed before — its certainties, "
            "its hierarchies, its faith in order — will not survive."
        ),
        "choices": [
            {"text": "Follow the aftermath — the fall of Constantinople reshapes the world", "target": "cross_fall"},
            {"text": "The plague destroyed everything — retreat into detachment", "target": "end_bystander"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crisis",
        "vocabulary": [
            {"term": "Black Death", "definition": "The devastating pandemic of bubonic plague that struck Europe between 1347 and 1351, killing an estimated one-third to one-half of the population. It was the worst demographic catastrophe in European history."},
            {"term": "bubonic plague", "definition": "An infectious disease caused by the bacterium Yersinia pestis, transmitted through flea bites. Symptoms include fever, chills, and painful swollen lymph nodes (buboes). It was the primary form of the Black Death."},
            {"term": "Yersinia pestis", "definition": "The bacterium that causes bubonic plague. Carried by fleas that lived on rats, it traveled along trade routes from Central Asia to Europe, arriving in Sicily in October 1347."},
            {"term": "flagellants", "definition": "Groups of people who publicly whipped themselves as penance, believing the Black Death was God's punishment for sin. The movement spread across Europe during the plague years, sometimes turning violent against perceived sinners and minorities."},
            {"term": "serfdom", "definition": "The condition of being bound to the land and owing labor and produce to the lord of the manor. Serfs were not slaves — they had rights and could not be sold — but they could not leave the manor without the lord's permission."},
            {"term": "Peasants' Revolt", "definition": "The English uprising of 1381, triggered by the poll tax and led by Wat Tyler. Peasants marched on London demanding an end to serfdom and unjust taxation. Though crushed, it demonstrated that the old feudal order was crumbling."},
            {"term": "Great Western Schism", "definition": "The division in the Catholic Church from 1378 to 1417, during which two (and eventually three) rival popes each claimed supreme authority. The scandal weakened public faith in the Church as an institution."},
        ],
        "figures": ["Giovanni Boccaccio"],
        "tags": ["crossover", "crisis", "plague", "death"],
    },

    "cross_fall": {
        "title": "The Fall of the City",
        "text": (
            "May 29, 1453. Constantinople.\n\n"
            "The city that has stood for eleven centuries — the last remnant of the Roman "
            "Empire — falls to the **Ottoman Empire** under Sultan Mehmed II. Massive cannons "
            "breach the ancient walls. Janissary soldiers pour through the gaps.\n\n"
            "Theo watches from the harbor as Greek scholars flee westward, carrying manuscripts "
            "of Plato, Aristotle, Euclid — texts that Western Europe has not seen in a thousand "
            "years. They carry the seeds of a rebirth.\n\n"
            "The Hagia Sophia — the greatest church in Christendom — becomes a mosque. The "
            "trade routes to the East are disrupted. European merchants will need new routes — "
            "by sea, around Africa, across the Atlantic.\n\n"
            "The fall means something different depending on where you stand: the scholar mourns "
            "lost texts, the warrior mourns a fallen frontier, the merchant mourns disrupted "
            "trade routes. But all of them feel it — the ancient world is truly over.\n\n"
            "The palimpsest rewrites itself completely. The old text vanishes. New words appear "
            "in a Renaissance hand — elegant, humanistic, confident:\n\n"
            "*The ancient world dies. The modern world is born. Between them stands a question "
            "that will tear Europe apart: who speaks for God?*"
        ),
        "choices": [
            {"text": "Follow the Reformation — the question that reshapes Europe", "target": "reform_indulgences"},
            {"text": "The Bible in every hand — follow the technology that makes it possible", "target": "reform_theses"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "crisis",
        "vocabulary": [
            {"term": "Ottoman Empire", "definition": "The Turkish Muslim empire that conquered Constantinople in 1453 and controlled southeastern Europe, the Middle East, and North Africa for centuries. Its rise disrupted traditional trade routes and helped spur European exploration."},
            {"term": "vernacular", "definition": "The everyday language spoken by ordinary people in a particular region, as opposed to Latin, which was the language of the Church, the universities, and international diplomacy. Printing in the vernacular made books accessible to anyone who could read."},
        ],
        "figures": ["Mehmed II"],
        "tags": ["crossover", "crisis", "constantinople", "fall"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  CONVERGENCE — THE REFORMATION (5 shared nodes)
    #  All tracks converge for the final act (1517–1555)
    # ══════════════════════════════════════════════════════════════════════

    "reform_indulgences": {
        "title": "The Price of Salvation",
        "text": (
            "Wittenberg, 1517. The Dominican friar Johann Tetzel travels through Germany "
            "selling **indulgences** — certificates that promise to reduce time in "
            "**purgatory** for the buyer or their dead relatives.\n\n"
            "His sales pitch is unforgettable: '*As soon as the coin in the coffer rings, "
            "the soul from purgatory springs!*'\n\n"
            "The money goes to rebuild St. Peter's Basilica in Rome. The theology is dubious "
            "at best — can forgiveness really be bought? — but the revenue is enormous.\n\n"
            "Theo watches an old woman hand over her last coins, weeping, hoping to free her "
            "dead husband's soul. Beside him, a young Augustinian monk watches too, his face "
            "white with anger.\n\n"
            "His name is Martin Luther.\n\n"
            "'*This is **simony**,*' Luther whispers. '*The buying and selling of sacred "
            "things. It is not Christianity. It is a marketplace wearing a cross.*'\n\n"
            "He turns and walks toward the Castle Church. He is carrying a document."
        ),
        "choices": [
            {"text": "Follow Luther to the church door — witness the 95 Theses", "target": "reform_theses"},
            {"text": "Luther's rage is righteous — stand with the reformers now", "target": "end_reformer"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "reformation",
        "vocabulary": [
            {"term": "purgatory", "definition": "In Catholic theology, a state of purification after death where souls destined for heaven are cleansed of remaining sin. The doctrine of purgatory made indulgences possible — and their abuse triggered the Reformation."},
            {"term": "simony", "definition": "The buying or selling of sacred things, especially Church offices or sacraments. Named after Simon Magus in the Book of Acts, who tried to buy the power of the Holy Spirit from the apostles."},
        ],
        "figures": ["Martin Luther", "Johann Tetzel"],
        "tags": ["reformation", "indulgences", "corruption"],
    },

    "reform_theses": {
        "title": "The Hammer Falls",
        "text": (
            "October 31, 1517. Martin Luther nails his Ninety-Five Theses to the door of "
            "the Castle Church in Wittenberg. It is meant as an academic invitation to debate "
            "— the medieval equivalent of posting a paper online.\n\n"
            "But the printing press turns a local quarrel into a continental firestorm. "
            "Within weeks, Luther's theses are printed in thousands of copies and distributed "
            "across Germany. Within months, all of Europe is reading them.\n\n"
            "The **Reformation** has begun.\n\n"
            "Luther's core arguments are radical: salvation comes through faith alone — "
            "**sola fide**. Scripture is the only authority — **sola scriptura**. Grace "
            "is God's free gift, not something earned or purchased — **sola gratia**.\n\n"
            "'***The three solas***,*' Luther explains to Theo. '*Everything else — popes, "
            "councils, indulgences, the whole apparatus — is human invention. Strip it away "
            "and you find the Gospel.*'\n\n"
            "The Pope is not amused. Luther is summoned to answer for his writings."
        ),
        "choices": [
            {"text": "Follow Luther to the Diet of Worms — the trial of the century", "target": "reform_worms"},
            {"text": "Follow the Bible translators — the radical power of reading Scripture", "target": "reform_tyndale"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "reformation",
        "vocabulary": [
            {"term": "Reformation", "definition": "The 16th-century movement to reform the Catholic Church, which led to the creation of Protestant churches. Beginning with Luther's 95 Theses in 1517, it reshaped the religious, political, and cultural map of Europe."},
            {"term": "sola fide", "definition": "Latin for 'by faith alone.' The Protestant doctrine that salvation comes through faith in Christ, not through good works, rituals, or payments to the Church."},
            {"term": "sola scriptura", "definition": "Latin for 'by Scripture alone.' The Protestant doctrine that the Bible is the sole infallible source of authority for Christian faith and practice, rejecting the authority of Church tradition and papal decrees."},
            {"term": "sola gratia", "definition": "Latin for 'by grace alone.' The Protestant doctrine that salvation is entirely a free gift from God, not something that can be earned, merited, or purchased."},
            {"term": "the three solas", "definition": "The three foundational principles of Protestant theology: sola fide (faith alone), sola scriptura (Scripture alone), and sola gratia (grace alone). Together, they challenged the entire medieval Church's system of authority and salvation."},
        ],
        "figures": ["Martin Luther"],
        "tags": ["reformation", "theses", "sola"],
    },

    "reform_worms": {
        "title": "Here I Stand",
        "text": (
            "April 1521. The **Diet of Worms** — an assembly of the princes and rulers of "
            "the **Holy Roman Empire** — convenes. Luther stands before Emperor Charles V, "
            "the most powerful man in Europe.\n\n"
            "A table is piled with Luther's books. The imperial spokesman asks: '*Do you "
            "recant these writings?*'\n\n"
            "Luther asks for a day to think. The next evening, he returns.\n\n"
            "'*Unless I am convinced by Scripture and plain reason — I do not accept the "
            "authority of popes and councils, for they have contradicted each other — my "
            "conscience is captive to the Word of God. I cannot and I will not recant "
            "anything, for to go against conscience is neither right nor safe.*'\n\n"
            "And then, perhaps: '*Here I stand. I can do no other. God help me.*'\n\n"
            "Luther is declared an outlaw. But Frederick of Saxony hides him in Wartburg "
            "Castle, where Luther translates the New Testament into German — putting the "
            "Bible into the hands of ordinary people.\n\n"
            "The **excommunication** from Rome means nothing to Luther. His conscience "
            "answers to a higher court.\n\n"
            "The palimpsest shows Theo the final chapter: how this rupture resolves."
        ),
        "choices": [
            {"text": "Follow the English Bible — Tyndale's dangerous mission", "target": "reform_tyndale"},
            {"text": "Follow the resolution — the Peace of Augsburg", "target": "reform_augsburg"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "reformation",
        "vocabulary": [
            {"term": "Diet of Worms", "definition": "The imperial assembly at the city of Worms in 1521 where Martin Luther was called to recant his writings before Emperor Charles V. Luther refused, declaring his conscience bound to Scripture. He was declared an outlaw."},
            {"term": "Holy Roman Empire", "definition": "The loose confederation of Central European territories that lasted from 962 to 1806. Voltaire famously quipped that it was 'neither holy, nor Roman, nor an empire' — but it was the political framework within which the Reformation played out."},
            {"term": "excommunication", "definition": "The formal exclusion of a person from the sacraments and fellowship of the Church. Pope Leo X excommunicated Luther in January 1521 after Luther publicly burned the papal bull threatening him."},
        ],
        "figures": ["Martin Luther", "Charles V"],
        "tags": ["reformation", "worms", "conscience"],
    },

    "reform_tyndale": {
        "title": "The Smuggled Word",
        "text": (
            "William Tyndale is England's Luther — but without a powerful prince to protect "
            "him. He has translated the New Testament into English from the original Greek, "
            "and the authorities want him dead for it.\n\n"
            "Theo helps smuggle copies of Tyndale's Bible across the Channel in bales of "
            "cloth. Each copy is printed on Gutenberg's technology, small enough to hide in "
            "a pocket. In England, they are contraband — possession is a death sentence.\n\n"
            "'*If God spare my life,*' Tyndale wrote, '*ere many years I will cause a boy "
            "that driveth the plough to know more of the Scripture than the Pope does.*'\n\n"
            "In 1535, Tyndale is betrayed, arrested in Belgium, and strangled at the stake. "
            "His last words: '*Lord, open the King of England's eyes.*'\n\n"
            "Within a year, Henry VIII — who had Tyndale hunted — authorizes an English "
            "Bible based largely on Tyndale's translation. The **Act of Supremacy** (1534) "
            "has already made Henry, not the Pope, head of the English Church.\n\n"
            "The palimpsest shows Theo one final scene."
        ),
        "choices": [
            {"text": "See how it ends — the Peace of Augsburg and a divided Europe", "target": "reform_augsburg"},
            {"text": "The Bible in every language, in every hand — this is the legacy worth carrying home", "target": "end_builder"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "reformation",
        "vocabulary": [
            {"term": "Act of Supremacy", "definition": "The 1534 act of Parliament that declared King Henry VIII the 'Supreme Head of the Church of England,' severing England's ties to the Pope and the Catholic Church. It was motivated less by theology than by Henry's desire to annul his marriage."},
        ],
        "figures": ["William Tyndale", "Henry VIII"],
        "tags": ["reformation", "tyndale", "bible_translation"],
    },

    "reform_augsburg": {
        "title": "The Peace That Divided",
        "text": (
            "1555. The **Peace of Augsburg**.\n\n"
            "After decades of religious war and theological argument, the princes of the Holy "
            "Roman Empire reach a compromise: ***cuius regio, eius religio*** — 'whose realm, "
            "his religion.' Each prince chooses Catholic or Lutheran for his territory. His "
            "subjects must follow or leave.\n\n"
            "It is not religious freedom — it is religious partition. But it ends the immediate "
            "bloodshed. The **Counter-Reformation** — the Catholic Church's own reform movement, "
            "led by the **Council of Trent** (1545-1563) and the **Jesuits** founded by Ignatius "
            "of Loyola — is already underway.\n\n"
            "Theo stands at the crossroads of the modern world. The medieval unity of Christendom "
            "is broken forever. In its place: nation-states, vernacular Bibles, individual "
            "conscience, the printing press, the beginnings of religious pluralism.\n\n"
            "The palimpsest writes its final message. The layers of text — Viking runes beneath "
            "Norman Latin beneath Gothic script beneath Renaissance humanistic hand — all "
            "shimmer together:\n\n"
            "*The parchment outlasts the sword. What will you carry home?*"
        ),
        "choices": [
            {"text": "Carry the truth: be a faithful witness to what you have seen", "target": "end_chronicler"},
            {"text": "Carry the question: the examined life spans every age", "target": "end_examined"},
            {"text": "Carry the fire: reform and conscience are worth any cost", "target": "end_reformer"},
        ],
        "is_ending": False,
        "ending_type": None,
        "era": "reformation",
        "vocabulary": [
            {"term": "Peace of Augsburg", "definition": "The 1555 treaty that allowed each prince of the Holy Roman Empire to choose Catholicism or Lutheranism for his territory. It established the principle of cuius regio, eius religio and temporarily ended religious warfare in the Empire."},
            {"term": "cuius regio, eius religio", "definition": "Latin for 'whose realm, his religion.' The principle established by the Peace of Augsburg (1555) that the ruler of each territory determined its official religion. Subjects who disagreed could emigrate."},
            {"term": "Counter-Reformation", "definition": "The Catholic Church's response to the Protestant Reformation, including internal reforms (the Council of Trent), new religious orders (the Jesuits), and efforts to win back Protestant territories. Also called the Catholic Reformation."},
            {"term": "Council of Trent", "definition": "The Catholic council (1545-1563) that defined Catholic doctrine in response to Protestant challenges, reformed Church practices, and launched the Counter-Reformation. It clarified Catholic teaching on Scripture, tradition, sacraments, and salvation."},
            {"term": "Jesuits", "definition": "The Society of Jesus, a Catholic religious order founded by Ignatius of Loyola in 1540. Known for their rigorous education, intellectual excellence, and missionary zeal, the Jesuits became the leading force of the Counter-Reformation."},
        ],
        "figures": ["Ignatius of Loyola"],
        "tags": ["reformation", "augsburg", "peace"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  ENDINGS (9 nodes)
    # ══════════════════════════════════════════════════════════════════════

    "end_chronicler": {
        "title": "The Faithful Witness",
        "text": (
            "Theo wakes at his desk. The textbook is open to a blank page — no, not blank. "
            "His own handwriting fills it, in a script he does not remember learning.\n\n"
            "He has written a chronicle. Like the monks at Lindisfarne, like the scribes of "
            "the Anglo-Saxon Chronicle, like Villehardouin and Froissart and Boccaccio, he "
            "has recorded what he witnessed — faithfully, without flinching.\n\n"
            "The palimpsest taught him this: truth is not a sword. It is a parchment. It "
            "can be burned, buried, rewritten — but the old words bleed through, persistent "
            "as memory, patient as stone.\n\n"
            "Alfred translated Boethius. Monks hid manuscripts in crypts while their monastery "
            "burned. Tyndale translated the Bible knowing it would cost his life. They did it "
            "because the written word is the thread that connects the living to the dead and "
            "the dead to those not yet born.\n\n"
            "Theo closes the book. He knows now what he is meant to do: bear witness. Write "
            "it down. Pass it on. The parchment outlasts the sword."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "best",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "chronicler", "witness"],
    },

    "end_examined": {
        "title": "The Examined Life",
        "text": (
            "Theo wakes slowly. The textbook has fallen open to the glossary, and every term "
            "seems to glow — not with magic, but with meaning.\n\n"
            "He has traveled seven centuries. He has stood with monks who saved manuscripts "
            "and with knights who burned cities. He has watched faith build cathedrals and "
            "fear burn heretics. He has seen reason flourish in universities and cruelty "
            "flourish on battlefields.\n\n"
            "And the question that echoes through every century is the one Socrates asked "
            "first: *How should we live?*\n\n"
            "Alfred answered: with learning and justice. Aquinas answered: with faith and "
            "reason in harmony. Joan answered: with courage, even unto death. Luther answered: "
            "with conscience captive to truth.\n\n"
            "None of them had the final answer. That is the point. The examined life is not "
            "a destination but a practice — a daily act of asking the hard questions, "
            "reading carefully, thinking honestly, and refusing the easy comfort of certainty.\n\n"
            "Theo picks up his pen. He has an exam tomorrow. But he understands now: the "
            "exam that matters is the one you give yourself."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "best",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "examined_life", "synthesis"],
    },

    "end_reformer": {
        "title": "The Courage of Conscience",
        "text": (
            "Theo wakes with Luther's words ringing in his ears: *Here I stand. I can do "
            "no other.*\n\n"
            "He has learned that the world does not change because people are comfortable. "
            "It changes because someone — Wycliffe, Hus, Luther, Tyndale — sees injustice "
            "and refuses to be silent, even when silence is safer.\n\n"
            "The palimpsest taught him that every age has its Tetzels — people who sell what "
            "should be free, who use power to silence truth, who tell the crowd what it wants "
            "to hear. And every age needs its reformers — not revolutionaries who tear "
            "everything down, but people who love the institution enough to demand it live "
            "up to its own ideals.\n\n"
            "Theo does not know what he will reform. His school's honor code, maybe. The "
            "way his community treats the people it overlooks. The way he himself has been "
            "content with comfortable answers.\n\n"
            "He picks up the textbook. It feels heavier now — weighted with seven centuries "
            "of people who stood up when sitting down was easier."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "reformer", "conscience"],
    },

    "end_builder": {
        "title": "The Cathedral You Never See",
        "text": (
            "Theo wakes thinking about cathedrals.\n\n"
            "The men who laid the foundation stones of Chartres never saw the spires. They "
            "worked knowing the cathedral would take generations to complete — and they built "
            "anyway, because some things are worth building even if you never see them finished.\n\n"
            "Tyndale translated a Bible he knew would cost his life. Alfred built schools in a "
            "kingdom that had been nearly destroyed. Francis gave away everything and found that "
            "having nothing was a kind of freedom.\n\n"
            "The palimpsest taught Theo this: the things that last — laws, books, institutions, "
            "ideas — are always built by people who care more about the future than the present. "
            "They are the builders, and their cathedrals are still standing long after the "
            "swords have rusted away.\n\n"
            "Theo does not know what he will build. But he knows now that building matters "
            "more than conquering, that the parchment outlasts the sword, and that the best "
            "work is done for people you will never meet."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "builder", "legacy"],
    },

    "end_pilgrim": {
        "title": "The Road Itself",
        "text": (
            "Theo wakes with dust on his shoes — or he imagines he does.\n\n"
            "He has walked the pilgrim roads: from Lindisfarne to Winchester, from Clermont "
            "to Jerusalem, from Florence to Wittenberg. He has traveled with monks and "
            "merchants, knights and friars, scholars and peasant girls who heard the voice "
            "of God.\n\n"
            "And he has learned what every pilgrim learns: the destination is not the point. "
            "The road itself transforms you. Every step is a small act of faith — faith that "
            "the road leads somewhere, that the walking matters, that the stranger beside you "
            "has something to teach.\n\n"
            "Chaucer knew this. His *Canterbury Tales* are not about Canterbury — they are "
            "about the pilgrims. The stories they tell on the road. The way laughter and "
            "grief and wisdom get shared between strangers who would never have met if they "
            "had stayed home.\n\n"
            "Theo picks up his backpack. He has a history class in the morning. But the road "
            "does not end when you arrive."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "pilgrim", "journey"],
    },

    "end_scholar": {
        "title": "The Quiet Room",
        "text": (
            "Theo wakes in a library. Not a medieval scriptorium — his own school library. "
            "But the light falls the same way.\n\n"
            "He has spent seven centuries among scholars: monks who copied Bede by candlelight, "
            "professors who debated Aristotle in the schools of Paris, humanists who translated "
            "Plato in Medici Florence. He has learned that the life of the mind is its own "
            "reward — not because it leads to power or wealth, but because understanding is "
            "a form of love.\n\n"
            "Aquinas said: '*To one who has faith, no explanation is necessary. To one without "
            "faith, no explanation is possible.*' But then he spent his whole life explaining "
            "anyway — because the act of reasoning, of reaching for truth, honors the God "
            "who gave us minds.\n\n"
            "Theo will not save the world with a sword. He will not nail theses to a church "
            "door. But he will read, and think, and understand — and in the quiet room of his "
            "own mind, the conversation that began in Lindisfarne's scriptorium will continue."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "good",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "scholar", "learning"],
    },

    "end_survivor": {
        "title": "The Long Road Home",
        "text": (
            "Theo wakes exhausted.\n\n"
            "He has survived — Vikings, plagues, wars, the sack of Constantinople, the fires "
            "of the Reformation. He has seen everything and changed nothing. He watched history "
            "happen from a safe distance, clutching the palimpsest like a tourist clutching "
            "a guidebook.\n\n"
            "The palimpsest is blank now. Its layers of text have faded, as if the parchment "
            "is tired of carrying messages for someone who never replied.\n\n"
            "Theo passed through seven centuries of human struggle and came home with "
            "souvenirs instead of scars. He saw the Black Death and thought about death. He "
            "saw Luther's courage and thought about courage. But he never risked anything, "
            "never committed to anything, never let any of it change him.\n\n"
            "The textbook lies open. The words are just words. The exam is tomorrow.\n\n"
            "There is still time to go back and read more carefully."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "neutral",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "survivor", "detachment"],
    },

    "end_bystander": {
        "title": "The Empty Page",
        "text": (
            "Theo wakes on the pilgrim road, or thinks he does. The road stretches in both "
            "directions — back toward the violence he fled, forward toward destinations he "
            "never reached.\n\n"
            "He turned back when the road grew dark. He chose safety over engagement, "
            "comfort over risk. The palimpsest offered him seven centuries of human drama — "
            "its greatest achievements and its worst atrocities — and he declined the invitation.\n\n"
            "The parchment is still in his hands, but its text has stopped writing itself. "
            "It waits for someone willing to engage — to argue with Thomas Aquinas, to stand "
            "beside Joan of Arc, to watch the fall of empires without looking away.\n\n"
            "History does not reward bystanders. It forgets them.\n\n"
            "Theo closes the textbook. He has learned nothing — except, perhaps, that choosing "
            "not to choose is itself a choice, and usually the worst one."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "neutral",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "bystander", "disengagement"],
    },

    "end_lost": {
        "title": "The Dropped Parchment",
        "text": (
            "Theo drops the palimpsest and runs.\n\n"
            "The screaming, the smoke, the axes — it was too much. He was seventeen and "
            "terrified and the world was ending in fire and he just ran, leaving the "
            "miraculous manuscript in the sand.\n\n"
            "Without the parchment, there is no guide. No thread through the labyrinth of "
            "centuries. Theo stumbles through fragments of history — glimpses of battles, "
            "plagues, cathedrals — but they blur together, meaningless without context, "
            "without connection.\n\n"
            "He wakes at his desk with nothing. The textbook is open to the chapter on the "
            "Viking Age. The words might as well be in Old English.\n\n"
            "The palimpsest offered him a gift: the chance to see history from the inside, "
            "to understand that the past is not dead weight but living wisdom. He threw it "
            "away because he was afraid.\n\n"
            "Fear is understandable. But history belongs to those who hold on."
        ),
        "choices": [],
        "is_ending": True,
        "ending_type": "bad",
        "era": "frame",
        "vocabulary": [],
        "figures": [],
        "tags": ["ending", "lost", "fear"],
    },
}
