/* ═══════════════════════════════════════════════════════════════════════════
   CYOA Story Engine — shared across all Thinker's Labyrinth adventures
   ═══════════════════════════════════════════════════════════════════════════ */

if (typeof STORY_DATA === "undefined") {
  document.body.innerHTML = `
    <div style="font-family:system-ui;max-width:520px;margin:80px auto;padding:32px;
                background:#231e18;border:1px solid #c4553a;border-radius:8px;color:#c4553a;">
      <strong>story_data.js not found.</strong><br><br>
      Run <code style="background:#1a1410;padding:2px 6px;border-radius:4px;">
      python story_graph.py</code> first, then reload.
    </div>`;
  throw new Error("STORY_DATA not defined");
}

// ── State ─────────────────────────────────────────────────────────────────

const state = {
  current:  null,
  history:  [],
  step:     0,
  vocabSeen: new Set(),
};

// ── Data-driven labels (read from STORY_DATA, with fallbacks) ────────────

const ENDING_META = {
  best:    { icon: "\u2605", label: "Best Ending"    },
  good:    { icon: "\u2726", label: "Good Ending"    },
  neutral: { icon: "\u25C6", label: "Neutral Ending" },
  bad:     { icon: "\u2715", label: "Bad Ending"     },
};

// ERA_LABELS: prefer story data, fall back to generic
const ERA_LABELS = STORY_DATA.era_labels || {
  frame: "Theo's Journey",
};

// ── Utilities ────────────────────────────────────────────────────────────

/** Compute edge count from nodes (if STORY_DATA.edges is absent). */
function getEdgeCount() {
  if (STORY_DATA.edges) return STORY_DATA.edges.length;
  let count = 0;
  Object.values(STORY_DATA.nodes).forEach(n => {
    count += (n.choices || []).length;
  });
  return count;
}

/** Get course ID from ?course= URL parameter (for back button). */
function getCourseParam() {
  const params = new URLSearchParams(window.location.search);
  return params.get("course");
}

// ── Text processing ──────────────────────────────────────────────────────

function processText(text) {
  return text
    .split("\n\n")
    .filter(p => p.trim())
    .map(p => {
      let html = p.trim()
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.+?)\*/g, '<em>$1</em>');
      return `<p>${html}</p>`;
    })
    .join("\n");
}

function buildFootnotes(vocabulary) {
  if (!vocabulary || vocabulary.length === 0) return "";
  const items = vocabulary.map(v => {
    state.vocabSeen.add(v.term);
    return `<div class="footnote-item">
      <span class="footnote-term">${v.term}:</span> ${v.definition}
    </div>`;
  }).join("\n");
  return `<h3>Vocabulary</h3>\n${items}`;
}

// ── Rendering ────────────────────────────────────────────────────────────

function renderNode(nodeId, animate) {
  const node = STORY_DATA.nodes[nodeId];
  if (!node) {
    console.error("Unknown node:", nodeId);
    return;
  }

  const card = document.getElementById("story-card");

  function applyContent() {
    // Meta row
    const metaEl = document.getElementById("card-meta");
    if (node.is_ending) {
      const m = ENDING_META[node.ending_type] || { icon: "\u2726", label: "Ending" };
      metaEl.innerHTML =
        `<span class="ending-badge ${node.ending_type}">${m.icon} &nbsp;${m.label}</span>`;
    } else {
      const stepText = state.step === 0 ? "Begin your journey" : `Step ${state.step}`;
      const eraText = ERA_LABELS[node.era] || "";
      metaEl.innerHTML = `<span class="chapter-label">${stepText}</span>` +
        (eraText ? `<span class="era-badge">${eraText}</span>` : "");
    }

    // Title
    document.getElementById("story-title").textContent = node.title;

    // Prose
    document.getElementById("story-text").innerHTML = processText(node.text);

    // Footnotes
    const footnotesEl = document.getElementById("footnotes");
    const footnotesHTML = buildFootnotes(node.vocabulary);
    if (footnotesHTML) {
      footnotesEl.innerHTML = footnotesHTML;
      footnotesEl.hidden = false;
    } else {
      footnotesEl.hidden = true;
    }

    // Choices
    const choicesEl = document.getElementById("choices");
    choicesEl.innerHTML = "";
    for (const choice of node.choices) {
      const btn = document.createElement("button");
      btn.className = "choice-btn";
      btn.textContent = choice.text;
      btn.addEventListener("click", () => makeChoice(choice.target));
      choicesEl.appendChild(btn);
    }

    // Ending row
    document.getElementById("ending-row").hidden = !node.is_ending;

    // Breadcrumb
    renderPath();

    // Scroll to top
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  if (animate) {
    card.classList.add("is-leaving");
    setTimeout(() => {
      applyContent();
      card.style.transition = "none";
      card.style.opacity = "0";
      card.style.transform = "translateY(-14px)";
      card.classList.remove("is-leaving");
      void card.offsetWidth;
      card.style.transition = "";
      card.style.opacity = "";
      card.style.transform = "";
    }, 350);
  } else {
    applyContent();
  }
}

// ── Breadcrumb ───────────────────────────────────────────────────────────

function renderPath() {
  const nav = document.getElementById("path-nav");
  if (state.history.length === 0) {
    nav.innerHTML = "";
    return;
  }

  const allIds = [...state.history, state.current];
  const parts = [];

  allIds.forEach((id, i) => {
    const node = STORY_DATA.nodes[id];
    const title = node ? node.title : id;
    const short = title.split(" ").slice(0, 2).join(" ");
    const isCurrent = i === allIds.length - 1;

    if (i > 0) {
      parts.push('<span class="path-arrow">\u203A</span>');
    }
    parts.push(
      `<span class="path-node${isCurrent ? " current" : ""}">${short}</span>`
    );
  });

  nav.innerHTML = parts.join("");
}

// ── Navigation ───────────────────────────────────────────────────────────

function makeChoice(targetId) {
  state.history.push(state.current);
  state.current = targetId;
  state.step += 1;
  renderNode(targetId, true);
}

function restart() {
  state.current = STORY_DATA.start_node;
  state.history = [];
  state.step = 0;
  state.vocabSeen = new Set();
  renderNode(state.current, false);
}

// ── Graph Stats Modal ────────────────────────────────────────────────────

function showGraphStats() {
  const nodes = STORY_DATA.nodes;
  const nodeCount = Object.keys(nodes).length;
  const edgeCount = getEdgeCount();
  const endings = Object.entries(nodes).filter(([,n]) => n.is_ending);
  const endingsByType = {};
  endings.forEach(([id, n]) => {
    endingsByType[n.ending_type] = (endingsByType[n.ending_type] || 0) + 1;
  });

  let totalVocab = new Set();
  Object.values(nodes).forEach(n => {
    (n.vocabulary || []).forEach(v => totalVocab.add(v.term));
  });

  const eras = {};
  Object.values(nodes).forEach(n => {
    const era = n.era || "unknown";
    eras[era] = (eras[era] || 0) + 1;
  });

  const icons = { best: "\u2605", good: "\u2726", neutral: "\u25C6", bad: "\u2715" };
  const endingLines = Object.entries(endingsByType)
    .map(([t,c]) => `${icons[t] || ""} ${t}: ${c}`)
    .join("  \u00B7  ");

  const eraLines = Object.entries(eras)
    .filter(([e]) => e !== "frame")
    .sort(([,a],[,b]) => b - a)
    .map(([e,c]) => `<div style="display:flex;justify-content:space-between"><span>${ERA_LABELS[e] || e}</span><span>${c} nodes</span></div>`)
    .join("");

  const visited = state.history.length + (state.current ? 1 : 0);

  const modal = document.createElement("div");
  modal.style.cssText = "position:fixed;inset:0;z-index:999;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.4)";
  modal.innerHTML = `
    <div style="background:#FFFEF7;border:2px solid #D2B48C;border-radius:12px;padding:2rem;max-width:440px;width:90%;box-shadow:0 16px 40px rgba(139,69,19,0.3);font-family:'Crimson Text',serif">
      <h2 style="font-family:'Cinzel',serif;color:#8B4513;font-size:1.3rem;margin-bottom:1rem;border-bottom:2px solid #D2B48C;padding-bottom:0.5rem">Story Map</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem 1.5rem;margin-bottom:1rem;font-size:0.95rem;color:#2F4F4F">
        <div><strong>${nodeCount}</strong> scenes</div>
        <div><strong>${edgeCount}</strong> connections</div>
        <div><strong>${endings.length}</strong> endings</div>
        <div><strong>${totalVocab.size}</strong> terms</div>
      </div>
      <div style="font-size:0.85rem;color:#696969;margin-bottom:1rem">${endingLines}</div>
      <div style="font-size:0.85rem;color:#2F4F4F;margin-bottom:1rem">${eraLines}</div>
      <div style="border-top:1px solid #D2B48C;padding-top:0.8rem;font-size:0.85rem;color:#696969">
        Your journey: <strong>${visited}</strong> scenes visited
      </div>
      <button onclick="this.closest('div[style]').parentElement.remove()" style="margin-top:1rem;background:transparent;border:2px solid #D2B48C;border-radius:8px;padding:0.4rem 1.5rem;font-family:'Cinzel',serif;font-size:0.8rem;color:#8B4513;cursor:pointer;text-transform:uppercase;letter-spacing:0.05em">Close</button>
    </div>`;
  modal.addEventListener("click", e => { if (e.target === modal) modal.remove(); });
  document.body.appendChild(modal);
}

// ── Boot ─────────────────────────────────────────────────────────────────

document.addEventListener("DOMContentLoaded", () => {
  // Populate header from STORY_DATA.meta if available
  const meta = STORY_DATA.meta || {};
  if (meta.title) {
    document.title = meta.title;
    const titleEl = document.querySelector(".header-title");
    if (titleEl) titleEl.textContent = meta.title;
  }
  if (meta.icon) {
    const iconEl = document.querySelector(".header-icon");
    if (iconEl) iconEl.textContent = meta.icon;
  }

  // Back button: if ?course= is present, show a back link
  const courseId = getCourseParam();
  if (courseId) {
    const backBtn = document.getElementById("back-btn");
    if (backBtn) {
      backBtn.href = `../../courses/${courseId}.html`;
      backBtn.hidden = false;
    }
  }

  document.getElementById("restart-btn").addEventListener("click", restart);
  document.getElementById("graph-btn").addEventListener("click", showGraphStats);
  state.current = STORY_DATA.start_node;
  renderNode(state.current, false);
});
