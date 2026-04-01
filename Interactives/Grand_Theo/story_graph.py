#!/usr/bin/env python3
"""
Theo the Divine — CYOA Story Graph Engine
==========================================
Builds a ~107-node Choose Your Own Adventure as a NetworkX directed graph.

Architecture:
  - Entry node: Theo at the Forest Gate (Arcana 0 — The Threshold)
  - 42 nexus nodes: positive/negative pairs for Arcana I–XXI
  - ~50 connecting/horizontal nodes: exploration, transitions, crossovers
  - 13 endings: 1 best, 3 good, 2 neutral, 7 bad

Workflow:
  1. Define nodes in story_nodes.py (imported here)
  2. Run this script to validate, export, and visualize
  3. Open index.html to play

Exports:
  - story_data.js   (client-side, no server needed)
  - story.json      (machine-readable archive)
  - graph.png       (Matplotlib visualization)
  - validation.txt  (graph metrics and issues)

Usage:
    py -3 story_graph.py [--validate] [--export] [--viz] [--all]
"""

import json
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

SCRIPT_DIR = Path(__file__).resolve().parent

# Import nodes from the story data module
from story_nodes import NODES, START_NODE

# ─────────────────────────────────────────────────────────────────────────────
# Build Graph
# ─────────────────────────────────────────────────────────────────────────────

def build_graph(nodes: dict) -> nx.DiGraph:
    """Build a NetworkX directed graph from the node dictionary."""
    G = nx.DiGraph()

    for nid, data in nodes.items():
        G.add_node(
            nid,
            title=data["title"],
            is_ending=data.get("is_ending", False),
            ending_type=data.get("ending_type"),
            era=data.get("era", ""),
            vocab_count=len(data.get("vocabulary", [])),
            figure_count=len(data.get("figures", [])),
        )

    for nid, data in nodes.items():
        for choice in data.get("choices", []):
            G.add_edge(nid, choice["target"], label=choice["text"])

    return G


# ─────────────────────────────────────────────────────────────────────────────
# Validation
# ─────────────────────────────────────────────────────────────────────────────

def validate(G: nx.DiGraph, nodes: dict, start: str) -> dict:
    """Run comprehensive graph validation. Returns a report dict."""
    report = {
        "node_count": G.number_of_nodes(),
        "edge_count": G.number_of_edges(),
        "start_node": start,
        "endings": {},
        "issues": [],
        "warnings": [],
        "metrics": {},
        "vocabulary": {},
        "path_analysis": {},
    }

    # ── Basic checks ─────────────────────────────────────────────────────
    endings = {n: G.nodes[n]["ending_type"] for n in G.nodes() if G.nodes[n].get("is_ending")}
    report["endings"] = endings

    ending_counts = defaultdict(int)
    for etype in endings.values():
        ending_counts[etype] += 1
    report["ending_type_counts"] = dict(ending_counts)

    if start not in G:
        report["issues"].append(f"START node '{start}' not in graph")

    for nid, data in nodes.items():
        for choice in data.get("choices", []):
            if choice["target"] not in nodes:
                report["issues"].append(
                    f"BROKEN LINK: {nid} -> {choice['target']} (target does not exist)"
                )

    for n in G.nodes():
        if n == start:
            continue
        if G.in_degree(n) == 0:
            report["issues"].append(f"ORPHAN: {n} has no incoming edges")

    for n in G.nodes():
        if G.out_degree(n) == 0 and not G.nodes[n].get("is_ending"):
            report["issues"].append(f"DEAD END: {n} has no choices and is not an ending")

    for n in G.nodes():
        if G.nodes[n].get("is_ending") and G.out_degree(n) > 0:
            report["warnings"].append(f"ENDING WITH CHOICES: {n} is marked as ending but has outgoing edges")

    # ── Reachability ─────────────────────────────────────────────────────
    if start in G:
        reachable = nx.descendants(G, start) | {start}
        unreachable = set(G.nodes()) - reachable
        if unreachable:
            report["issues"].append(
                f"UNREACHABLE from start ({len(unreachable)}): {sorted(unreachable)[:10]}"
            )
        report["metrics"]["reachable_nodes"] = len(reachable)
        report["metrics"]["unreachable_nodes"] = len(unreachable)

        for end_id in endings:
            if end_id not in reachable:
                report["issues"].append(f"UNREACHABLE ENDING: {end_id}")

    # ── Path analysis ────────────────────────────────────────────────────
    if start in G:
        for end_id in endings:
            if not nx.has_path(G, start, end_id):
                report["path_analysis"][end_id] = {"reachable": False, "path_count": 0}
                continue

            try:
                shortest = nx.shortest_path_length(G, start, end_id)
                path_count = 0
                min_len = shortest
                max_len = shortest
                total_len = 0
                PATH_LIMIT = 5000
                for path in nx.all_simple_paths(G, start, end_id, cutoff=40):
                    path_count += 1
                    pl = len(path)
                    if pl < min_len: min_len = pl
                    if pl > max_len: max_len = pl
                    total_len += pl
                    if path_count >= PATH_LIMIT:
                        break
                capped = path_count >= PATH_LIMIT
                report["path_analysis"][end_id] = {
                    "reachable": True,
                    "path_count": f"{path_count}+" if capped else path_count,
                    "shortest": min_len,
                    "longest": max_len,
                    "avg_length": round(total_len / max(path_count, 1), 1),
                }
            except Exception:
                report["path_analysis"][end_id] = {"reachable": True, "path_count": "error"}

    # ── Vocabulary coverage ──────────────────────────────────────────────
    all_vocab = set()
    vocab_by_node = {}
    for nid, data in nodes.items():
        terms = {v["term"].lower() for v in data.get("vocabulary", [])}
        vocab_by_node[nid] = terms
        all_vocab |= terms

    report["vocabulary"]["total_unique_terms"] = len(all_vocab)
    report["vocabulary"]["terms"] = sorted(all_vocab)

    VOCAB_SAMPLE = 200
    if start in G:
        for end_id in endings:
            if not nx.has_path(G, start, end_id):
                continue
            try:
                path_vocabs = []
                for path in nx.all_simple_paths(G, start, end_id, cutoff=40):
                    pv = set()
                    for n in path:
                        pv |= vocab_by_node.get(n, set())
                    path_vocabs.append(len(pv))
                    if len(path_vocabs) >= VOCAB_SAMPLE:
                        break
                if not path_vocabs:
                    continue
                report["vocabulary"][f"coverage_{end_id}"] = {
                    "min_terms": min(path_vocabs),
                    "max_terms": max(path_vocabs),
                    "avg_terms": round(sum(path_vocabs) / len(path_vocabs), 1),
                }
            except Exception:
                pass

    # ── Era distribution ─────────────────────────────────────────────────
    era_counts = defaultdict(int)
    for nid, data in nodes.items():
        era_counts[data.get("era", "unknown")] += 1
    report["metrics"]["era_distribution"] = dict(era_counts)

    # ── Graph metrics ────────────────────────────────────────────────────
    report["metrics"]["avg_out_degree"] = round(
        sum(G.out_degree(n) for n in G.nodes()) / max(G.number_of_nodes(), 1), 2
    )
    report["metrics"]["max_out_degree"] = max((G.out_degree(n) for n in G.nodes()), default=0)
    report["metrics"]["avg_in_degree"] = round(
        sum(G.in_degree(n) for n in G.nodes()) / max(G.number_of_nodes(), 1), 2
    )

    convergence = sorted(G.nodes(), key=lambda n: G.in_degree(n), reverse=True)[:8]
    report["metrics"]["convergence_points"] = [
        {"node": n, "in_degree": G.in_degree(n), "title": nodes[n]["title"]}
        for n in convergence
    ]

    return report


def print_report(report: dict):
    """Pretty-print the validation report."""
    print("=" * 70)
    print("  THEO THE DIVINE — GRAPH VALIDATION")
    print("=" * 70)
    print()
    print(f"  Nodes: {report['node_count']}    Edges: {report['edge_count']}")
    print(f"  Start: {report['start_node']}")
    print()

    print(f"  Endings ({len(report['endings'])}):")
    for etype, count in sorted(report.get("ending_type_counts", {}).items()):
        icon = {"best": "*", "good": "+", "neutral": "o", "bad": "x"}.get(etype, "?")
        print(f"    {icon} {etype}: {count}")
    print()

    m = report["metrics"]
    print(f"  Reachable: {m.get('reachable_nodes', '?')}/{report['node_count']}")
    print(f"  Avg out-degree: {m.get('avg_out_degree', '?')}")
    print(f"  Max out-degree: {m.get('max_out_degree', '?')}")
    print()

    print("  Era distribution:")
    for era, count in sorted(m.get("era_distribution", {}).items()):
        print(f"    {era}: {count} nodes")
    print()

    print("  Path analysis (start -> ending):")
    for end_id, pa in report.get("path_analysis", {}).items():
        etype = report["endings"].get(end_id, "?")
        if pa.get("reachable"):
            print(f"    -> {end_id} ({etype}): {pa['path_count']} paths, "
                  f"len {pa.get('shortest','?')}-{pa.get('longest','?')} "
                  f"(avg {pa.get('avg_length','?')})")
        else:
            print(f"    -> {end_id} ({etype}): UNREACHABLE")
    print()

    v = report["vocabulary"]
    print(f"  Vocabulary: {v.get('total_unique_terms', 0)} unique terms")
    for key, cov in v.items():
        if key.startswith("coverage_"):
            end_id = key.replace("coverage_", "")
            print(f"    -> {end_id}: {cov['min_terms']}-{cov['max_terms']} terms per path "
                  f"(avg {cov['avg_terms']})")
    print()

    print("  Convergence points (highest in-degree):")
    for cp in m.get("convergence_points", []):
        print(f"    {cp['node']}: {cp['in_degree']} incoming -> \"{cp['title']}\"")
    print()

    if report["issues"]:
        print(f"  ISSUES ({len(report['issues'])}):")
        for iss in report["issues"]:
            print(f"    x {iss}")
    else:
        print("  No issues found.")

    if report["warnings"]:
        print(f"\n  WARNINGS ({len(report['warnings'])}):")
        for w in report["warnings"]:
            print(f"    ! {w}")

    print()
    print("=" * 70)


# ─────────────────────────────────────────────────────────────────────────────
# Export
# ─────────────────────────────────────────────────────────────────────────────

def export(G: nx.DiGraph, nodes: dict, start: str):
    """Export story_data.js, story.json."""

    # Add meta and era_labels to payload
    meta = {
        "title": "Theo the Divine",
        "icon": "THEO",
    }

    era_labels = {
        "threshold": "The Threshold",
        "forest":    "The Chartreuse Forest",
        "temple":    "The Forest Temple",
        "ravines":   "The Ravines of Nebo",
        "maiden":    "The Maiden's Domain",
        "depths":    "The Temple of Memories",
        "heights":   "The Heights of Nebo",
        "frame":     "Theo's Journey",
    }

    payload = {
        "meta": meta,
        "era_labels": era_labels,
        "nodes": nodes,
        "start_node": start,
        "edges": [[u, v] for u, v in G.edges()],
    }

    js_path = SCRIPT_DIR / "story_data.js"
    js_content = (
        "// Auto-generated by story_graph.py -- do not edit by hand\n"
        f"const STORY_DATA = {json.dumps(payload, indent=2, ensure_ascii=False)};\n"
    )
    js_path.write_text(js_content, encoding="utf-8")

    json_path = SCRIPT_DIR / "story.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"Exported: {js_path.name}, {json_path.name}")


# ─────────────────────────────────────────────────────────────────────────────
# Visualization
# ─────────────────────────────────────────────────────────────────────────────

ERA_COLORS = {
    "threshold": "#e879f9",  # fuchsia
    "forest":    "#4ade80",  # green
    "temple":    "#60a5fa",  # blue
    "ravines":   "#f97316",  # orange
    "maiden":    "#ec4899",  # pink
    "depths":    "#a78bfa",  # purple
    "heights":   "#fbbf24",  # gold
    "frame":     "#94a3b8",  # slate
}

ENDING_COLORS = {
    "best":    "#fbbf24",
    "good":    "#34d399",
    "neutral": "#94a3b8",
    "bad":     "#f87171",
}


def node_color(nid, data):
    if nid == START_NODE:
        return "#e879f9"
    if data.get("is_ending"):
        return ENDING_COLORS.get(data.get("ending_type"), "#94a3b8")
    return ERA_COLORS.get(data.get("era", ""), "#60a5fa")


def visualize(G: nx.DiGraph, nodes: dict):
    """Generate graph.png with hierarchical layout."""
    fig, ax = plt.subplots(figsize=(30, 20))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")

    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot", args="-Grankdir=TB")
    except Exception:
        try:
            for layer, ns in enumerate(nx.topological_generations(G)):
                for n in ns:
                    G.nodes[n]["layer"] = layer
            pos = nx.multipartite_layout(G, subset_key="layer", align="horizontal")
            pos = {n: (x * 25, -y * 12) for n, (x, y) in pos.items()}
        except Exception:
            pos = nx.spring_layout(G, k=3, iterations=100, seed=42)

    colors = [node_color(n, nodes.get(n, {})) for n in G.nodes()]
    sizes = [1400 if nodes.get(n, {}).get("is_ending") else 900 for n in G.nodes()]

    nx.draw_networkx_edges(
        G, pos, ax=ax,
        edge_color="#475569", arrows=True, arrowsize=14,
        arrowstyle="->", width=1.0, alpha=0.6,
        connectionstyle="arc3,rad=0.05",
    )

    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_color=colors, node_size=sizes, alpha=0.92,
    )

    labels = {}
    for n in G.nodes():
        title = nodes.get(n, {}).get("title", n)
        words = title.split()
        labels[n] = " ".join(words[:3]) + ("..." if len(words) > 3 else "")

    nx.draw_networkx_labels(
        G, pos, ax=ax, labels=labels,
        font_size=4.5, font_color="#0d1117", font_weight="bold",
    )

    legend_handles = [
        mpatches.Patch(color="#e879f9", label="Start / Threshold"),
        mpatches.Patch(color="#fbbf24", label="Best ending"),
        mpatches.Patch(color="#34d399", label="Good ending"),
        mpatches.Patch(color="#94a3b8", label="Neutral ending"),
        mpatches.Patch(color="#f87171", label="Bad ending"),
    ]
    for era, color in ERA_COLORS.items():
        if era not in ("threshold", "frame"):
            legend_handles.append(mpatches.Patch(color=color, label=era.replace("_", " ").title()))

    legend = ax.legend(
        handles=legend_handles, loc="upper right",
        facecolor="#1e293b", edgecolor="#334155", labelcolor="white",
        fontsize=7, framealpha=0.92, title="Legend", title_fontsize=8,
    )
    legend.get_title().set_color("white")

    endings = [n for n in G.nodes() if nodes.get(n, {}).get("is_ending")]
    ax.set_title(
        "Theo the Divine  --  Story Graph",
        color="#e2e8f0", fontsize=18, fontweight="bold", pad=16, loc="left",
    )
    ax.text(
        0.0, 1.02,
        f"{G.number_of_nodes()} nodes  --  {G.number_of_edges()} edges  --  "
        f"{len(endings)} endings",
        transform=ax.transAxes, color="#64748b", fontsize=9,
    )

    ax.axis("off")
    plt.tight_layout(pad=1.5)

    out_path = SCRIPT_DIR / "graph.png"
    plt.savefig(str(out_path), dpi=150, bbox_inches="tight", facecolor="#0d1117")
    plt.close()
    print(f"Exported: {out_path.name}")


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    args = set(sys.argv[1:])
    do_all = "--all" in args or not args

    G = build_graph(NODES)
    print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    if "--validate" in args or do_all:
        report = validate(G, NODES, START_NODE)
        print_report(report)
        report_path = SCRIPT_DIR / "validation.txt"
        import io
        buf = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        print_report(report)
        sys.stdout = old_stdout
        report_path.write_text(buf.getvalue(), encoding="utf-8")
        json_report_path = SCRIPT_DIR / "validation.json"
        with open(json_report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)

    if "--export" in args or do_all:
        export(G, NODES, START_NODE)

    if "--viz" in args or do_all:
        visualize(G, NODES)

    if do_all:
        print(f"\nAll done! Open index.html in a browser to play.")


if __name__ == "__main__":
    main()
