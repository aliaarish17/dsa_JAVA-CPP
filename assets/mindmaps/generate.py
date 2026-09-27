"""Generate Minecraft-themed SVG mindmaps for the README.

Nodes/edges stay visible if GitHub rasterizes the file and skips CSS.
"""

from pathlib import Path

OUT = Path(__file__).parent

THEMES = {
    "overworld": {
        "bg": "#071208",
        "grid": "#143016",
        "hub": "#1d4a18",
        "hub_stroke": "#7CFF4A",
        "cat": "#2d5a1e",
        "cat_stroke": "#8BC34A",
        "leaf": "#102410",
        "leaf_stroke": "#4A7C1F",
        "ink": "#E8F5D8",
        "muted": "#9CCC7A",
        "edge": "#55C500",
        "glow": "#55C500",
    },
    "nether": {
        "bg": "#140a08",
        "grid": "#2a1810",
        "hub": "#4a2a12",
        "hub_stroke": "#FFB020",
        "cat": "#6b4423",
        "cat_stroke": "#D4A017",
        "leaf": "#241408",
        "leaf_stroke": "#8A6420",
        "ink": "#FFE7B0",
        "muted": "#C9A227",
        "edge": "#E09B1A",
        "glow": "#FFB020",
    },
    "stone": {
        "bg": "#101214",
        "grid": "#22262a",
        "hub": "#2b2f33",
        "hub_stroke": "#C5C9CE",
        "cat": "#3d444b",
        "cat_stroke": "#A8B0B8",
        "leaf": "#1a1d20",
        "leaf_stroke": "#6A727A",
        "ink": "#F2F4F6",
        "muted": "#B0B8C0",
        "edge": "#8A9199",
        "glow": "#D0D5DA",
    },
    "end": {
        "bg": "#061318",
        "grid": "#0d2a33",
        "hub": "#12343f",
        "hub_stroke": "#4AC6E8",
        "cat": "#1b5566",
        "cat_stroke": "#5ED4F0",
        "leaf": "#071c24",
        "leaf_stroke": "#2D6B80",
        "ink": "#D7F6FF",
        "muted": "#7FD4EA",
        "edge": "#3EB7D6",
        "glow": "#4AC6E8",
    },
    "dragon": {
        "bg": "#160606",
        "grid": "#2a0c0c",
        "hub": "#5a1010",
        "hub_stroke": "#FF5555",
        "cat": "#8b2020",
        "cat_stroke": "#FF7A7A",
        "leaf": "#240808",
        "leaf_stroke": "#B33939",
        "ink": "#FFE4E4",
        "muted": "#FF9A9A",
        "edge": "#E24A4A",
        "glow": "#FF5555",
    },
}


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_wrap(slug: str, view_w: int, view_h: int, theme: str, kicker: str, title: str, inner: str) -> str:
    t = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_w} {view_h}" width="{view_w}" height="{view_h}" role="img" aria-label="{esc(title)}">
  <title>{esc(title)}</title>
  <defs>
    <pattern id="grid-{slug}" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="16" height="16" fill="{t['bg']}"/>
      <rect width="16" height="1" fill="{t['grid']}" opacity="0.55"/>
      <rect width="1" height="16" fill="{t['grid']}" opacity="0.55"/>
    </pattern>
    <filter id="glow-{slug}" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.6" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="scan-{slug}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.22"/>
    </linearGradient>
    <style>
      .edge-{slug} {{
        fill: none;
        stroke: {t['edge']};
        stroke-width: 2.5;
        stroke-linecap: square;
        stroke-dasharray: 10 6;
        animation: march-{slug} 1.1s linear infinite;
      }}
      .pulse-{slug} {{
        animation: pulse-{slug} 2.6s ease-in-out infinite;
      }}
      .twinkle-{slug} {{
        animation: twinkle-{slug} 2.2s ease-in-out infinite;
      }}
      @keyframes march-{slug} {{
        to {{ stroke-dashoffset: -16; }}
      }}
      @keyframes pulse-{slug} {{
        0%, 100% {{ filter: url(#glow-{slug}); }}
        50% {{ filter: none; }}
      }}
      @keyframes twinkle-{slug} {{
        0%, 100% {{ opacity: 0.25; }}
        50% {{ opacity: 0.95; }}
      }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid-{slug})"/>
  <rect x="8" y="8" width="{view_w - 16}" height="{view_h - 16}" fill="none" stroke="{t['hub_stroke']}" stroke-width="3"/>
  <rect x="14" y="14" width="{view_w - 28}" height="{view_h - 28}" fill="none" stroke="{t['leaf_stroke']}" stroke-width="1" opacity="0.7"/>
  <rect width="100%" height="100%" fill="url(#scan-{slug})"/>
  <circle class="twinkle-{slug}" cx="36" cy="36" r="3" fill="{t['glow']}"/>
  <circle class="twinkle-{slug}" cx="{view_w - 36}" cy="42" r="2.5" fill="{t['glow']}" style="animation-delay:0.6s"/>
  <circle class="twinkle-{slug}" cx="{view_w - 48}" cy="{view_h - 34}" r="3" fill="{t['glow']}" style="animation-delay:1.1s"/>
  <text x="28" y="42" fill="{t['muted']}" font-family="ui-monospace, Cascadia Code, Consolas, monospace" font-size="11" letter-spacing="2">{esc(kicker.upper())}</text>
  <text x="28" y="66" fill="{t['ink']}" font-family="Segoe UI, Tahoma, sans-serif" font-size="20" font-weight="700">{esc(title)}</text>
{inner}
</svg>
'''


def rect_node(x, y, w, h, fill, stroke, text, slug, delay, font=13, pulse=False):
    cls = f"pulse-{slug}" if pulse else f"node-{slug}"
    lines = text.split("\n")
    ts = []
    start_y = y + h / 2 - (len(lines) - 1) * 8
    for i, line in enumerate(lines):
        ts.append(
            f'<text x="{x + w/2}" y="{start_y + i * 16}" text-anchor="middle" dominant-baseline="middle" fill="white" font-family="Segoe UI, Tahoma, sans-serif" font-size="{font}" font-weight="700">{esc(line)}</text>'
        )
    filt = f' filter="url(#glow-{slug})"' if pulse else ""
    return (
        f'  <g class="{cls}" style="animation-delay:{delay}s"{filt}>\n'
        f'    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>\n'
        f'    <rect x="{x + 3}" y="{y + 3}" width="{w - 6}" height="2" fill="{stroke}" opacity="0.35"/>\n'
        f'    {"".join(ts)}\n'
        f'  </g>'
    )


def cubic(x1, y1, x2, y2, slug):
    mx = (x1 + x2) / 2
    return f'  <path class="edge-{slug}" d="M{x1:.1f},{y1:.1f} C{mx:.1f},{y1:.1f} {mx:.1f},{y2:.1f} {x2:.1f},{y2:.1f}"/>'


def mindmap(filename, theme, title, kicker, hub, left, right):
    slug = filename.replace(".svg", "")
    t = THEMES[theme]
    W, H = 1000, 640
    hub_w, hub_h = 196, 76
    hx, hy = (W - hub_w) / 2, 292
    hcx, hcy = hx + hub_w / 2, hy + hub_h / 2

    cat_w, cat_h = 168, 42
    leaf_w, leaf_h = 164, 28
    left_cat_x = 198
    right_cat_x = 634
    left_leaf_x = 22
    right_leaf_x = 814

    edges, nodes = [], []

    def place(items, cat_x, leaves_left: bool):
        if not items:
            return
        usable_top, usable_bot = 96, 612
        span = usable_bot - usable_top
        step = span / len(items)
        for i, (cat, leaves) in enumerate(items):
            cy = usable_top + step * i + step / 2 - cat_h / 2
            delay = 0.12 + i * 0.09
            cat_cy = cy + cat_h / 2
            nodes.append(rect_node(cat_x, cy, cat_w, cat_h, t["cat"], t["cat_stroke"], cat, slug, delay, font=13))
            if leaves_left:
                edges.append(cubic(hx, hcy, cat_x + cat_w, cat_cy, slug))
                leaf_x = left_leaf_x
                attach_x, leaf_attach = cat_x, leaf_x + leaf_w
            else:
                edges.append(cubic(hx + hub_w, hcy, cat_x, cat_cy, slug))
                leaf_x = right_leaf_x
                attach_x, leaf_attach = cat_x + cat_w, leaf_x
            leaf_span = max(len(leaves) * 32, 32)
            ly0 = cat_cy - leaf_span / 2
            # keep leaves inside frame
            if ly0 < 90:
                ly0 = 90
            if ly0 + leaf_span > 618:
                ly0 = 618 - leaf_span
            for j, leaf in enumerate(leaves):
                ly = ly0 + j * 32
                ld = delay + 0.1 + j * 0.04
                nodes.append(rect_node(leaf_x, ly, leaf_w, leaf_h, t["leaf"], t["leaf_stroke"], leaf, slug, ld, font=11))
                edges.append(cubic(attach_x, cat_cy, leaf_attach, ly + leaf_h / 2, slug))

    place(left, left_cat_x, True)
    place(right, right_cat_x, False)
    nodes.append(
        rect_node(hx, hy, hub_w, hub_h, t["hub"], t["hub_stroke"], hub, slug, 0.02, font=16, pulse=True)
    )
    inner = "\n".join(edges + nodes)
    (OUT / filename).write_text(svg_wrap(slug, W, H, theme, kicker, title, inner), encoding="utf-8")


def world_map():
    slug = "world"
    W, H = 1000, 600
    biomes = [
        (52, "OVERWORLD", "wood pickaxe era", ["Arrays", "Strings", "Recursion"], "overworld"),
        (360, "THE NETHER", "gold rush at 2am", ["Hashing", "Sort / Search", "Linked List"], "nether"),
        (668, "THE END", "not emotionally ready", ["Trees / Graphs", "DP", "Greedy"], "end"),
    ]
    edges, nodes = [], []
    for i, (x, name, tag, topics, theme_key) in enumerate(biomes):
        tt = THEMES[theme_key]
        delay = 0.12 + i * 0.1
        topic_svg = []
        for k, topic in enumerate(topics):
            topic_svg.append(
                f'<rect x="{x + 28}" y="{228 + k * 42}" width="224" height="32" fill="{tt["leaf"]}" stroke="{tt["leaf_stroke"]}" stroke-width="2"/>'
                f'<text x="{x + 140}" y="{248 + k * 42}" text-anchor="middle" fill="{tt["ink"]}" font-size="13" font-weight="700" font-family="Segoe UI, Tahoma, sans-serif">{esc(topic)}</text>'
            )
        nodes.append(
            f'''  <g class="node-{slug}" style="animation-delay:{delay}s">
    <rect x="{x}" y="140" width="280" height="228" fill="{tt['hub']}" stroke="{tt['hub_stroke']}" stroke-width="3"/>
    <rect x="{x + 8}" y="148" width="264" height="8" fill="{tt['hub_stroke']}" opacity="0.35"/>
    <text x="{x + 140}" y="184" text-anchor="middle" fill="{tt['ink']}" font-size="18" font-weight="700" font-family="Segoe UI, Tahoma, sans-serif">{name}</text>
    <text x="{x + 140}" y="206" text-anchor="middle" fill="{tt['muted']}" font-size="11" font-family="ui-monospace, Consolas, monospace">{esc(tag)}</text>
    {''.join(topic_svg)}
  </g>'''
        )
        edges.append(f'  <path class="edge-{slug}" d="M500,118 C500,128 {x + 140},132 {x + 140},140"/>')
        edges.append(f'  <path class="edge-{slug}" d="M{x + 140},368 C{x + 140},400 500,412 500,430"/>')

    nodes.append(rect_node(392, 78, 216, 40, THEMES["overworld"]["hub"], THEMES["overworld"]["hub_stroke"], "DSA WORLD SAVE", slug, 0.02, font=14, pulse=True))
    nodes.append(rect_node(280, 430, 440, 72, THEMES["dragon"]["hub"], THEMES["dragon"]["hub_stroke"], "ENDER DRAGON  ·  the interview", slug, 0.5, font=16, pulse=True))
    inner = "\n".join(edges + nodes)
    (OUT / "world.svg").write_text(svg_wrap(slug, W, H, "overworld", "world save // biomes", "The Mining Map", inner), encoding="utf-8")


def speedrun():
    slug = "speedrun"
    t = THEMES["overworld"]
    W, H = 1000, 250
    steps = ["Read", "Goal", "Brute", "Bottleneck", "Pattern", "Optimize", "Code", "Edges", "TC/SC", "Next"]
    box_w, box_h = 78, 50
    gap = 16
    total = len(steps) * box_w + (len(steps) - 1) * gap
    x0 = (W - total) / 2
    y = 120
    edges, nodes = [], []
    for i, s in enumerate(steps):
        x = x0 + i * (box_w + gap)
        fill = t["hub"] if i in (0, len(steps) - 1) else t["cat"]
        stroke = t["hub_stroke"] if i in (0, len(steps) - 1) else t["cat_stroke"]
        nodes.append(rect_node(x, y, box_w, box_h, fill, stroke, s, slug, 0.06 * i, font=11, pulse=(i in (0, len(steps) - 1))))
        if i:
            edges.append(
                f'  <path class="edge-{slug}" d="M{x - gap},{y + box_h/2} L{x},{y + box_h/2}"/>'
            )
    inner = "\n".join(edges + nodes)
    (OUT / "speedrun.svg").write_text(svg_wrap(slug, W, H, "overworld", "quest pipeline", "How I Speedrun a Problem", inner), encoding="utf-8")


if __name__ == "__main__":
    world_map()
    speedrun()
    mindmap(
        "arrays.svg",
        "overworld",
        "Arrays & Strings",
        "overworld biome",
        "ARRAYS &\nSTRINGS",
        left=[
            ("Two Pointers", ["Pair sum", "Reverse in place", "Palindrome"]),
            ("Prefix Sum", ["Range queries", "Subarray sum = k"]),
        ],
        right=[
            ("Sliding Window", ["Fixed window", "Variable window", "Longest substring"]),
            ("Kadane", ["Max subarray"]),
            ("Sorting-based", ["Merge intervals", "Dutch flag"]),
        ],
    )
    mindmap(
        "hashing.svg",
        "nether",
        "Hashing",
        "nether biome",
        "HASHING",
        left=[
            ("Frequency Count", ["Anagrams", "Majority element"]),
            ("Set for Dedup", ["Longest consecutive"]),
        ],
        right=[
            ("Two Sum Pattern", ["Complement lookup"]),
            ("Map as Cache", ["Grouping", "Index tracking"]),
        ],
    )
    mindmap(
        "linked-list.svg",
        "stone",
        "Linked List",
        "mineshaft biome",
        "LINKED\nLIST",
        left=[
            ("Fast & Slow", ["Cycle detection", "Middle of list"]),
            ("Dummy Node", ["Merge lists", "Remove nth node"]),
        ],
        right=[
            ("Reversal", ["Full reverse", "Reverse in groups"]),
            ("Recursion", ["Recursive reverse"]),
        ],
    )
    mindmap(
        "trees.svg",
        "overworld",
        "Trees",
        "dark forest biome",
        "TREES",
        left=[
            ("DFS", ["Pre / In / Post", "Path sum", "Diameter"]),
            ("BST Properties", ["Validate BST", "Kth smallest"]),
        ],
        right=[
            ("BFS", ["Level order", "Zigzag traversal"]),
            ("Backtracking", ["Root to leaf paths"]),
        ],
    )
    mindmap(
        "graphs.svg",
        "end",
        "Graphs",
        "the end biome",
        "GRAPHS",
        left=[
            ("Traversal", ["BFS", "DFS"]),
            ("Union-Find", ["Cycle detection", "Components"]),
        ],
        right=[
            ("Shortest Path", ["Dijkstra", "BFS unweighted"]),
            ("Topo Sort", ["Course schedule", "Task ordering"]),
        ],
    )
    mindmap(
        "dp.svg",
        "dragon",
        "Dynamic Programming",
        "ender dragon loot",
        "DYNAMIC\nPROGRAMMING",
        left=[
            ("1D DP", ["Fibonacci style", "House robber"]),
            ("Knapsack", ["0/1 knapsack", "Unbounded"]),
        ],
        right=[
            ("2D DP", ["Grid paths", "Edit distance"]),
            ("Subsequence", ["LCS", "LIS"]),
            ("State Machine", ["Buy / sell stock"]),
        ],
    )
    print("ok", sorted(p.name for p in OUT.glob("*.svg")))
