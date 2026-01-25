import sys
from pathlib import Path

# Ensure repo root is importable even when running from tools/
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from frontend_dash.app import app
import json
from collections import defaultdict

def parse_outputs(key: str):
    # Multi-output keys look like: "..id1.prop1...id2.prop2.."
    if isinstance(key, str) and key.startswith("..") and key.endswith(".."):
        return key[2:-2].split("...")
    return [key]

def fmt_id(x):
    if isinstance(x, dict):
        return json.dumps(x, sort_keys=True)
    return str(x)

# Build directed edges: input_node -> output_node
edges = defaultdict(set)
nodes = set()

for out_key, meta in app.callback_map.items():
    outs = [str(x) for x in parse_outputs(out_key)]
    ins = [f'{fmt_id(i.get("id"))}.{i.get("property")}' for i in meta.get("inputs", [])]

    for o in outs:
        nodes.add(o)
    for i in ins:
        nodes.add(i)
        for o in outs:
            edges[i].add(o)

# Detect 2-node ping-pong cycles quickly
twos = set()
for u, vs in edges.items():
    for v in vs:
        if u in edges.get(v, set()):
            twos.add(tuple(sorted((u, v))))

print("Total callbacks:", len(app.callback_map))
print("Nodes:", len(nodes), "Edges:", sum(len(v) for v in edges.values()))

if twos:
    print("\nTwo-node cycles (ping-pong):")
    for u, v in sorted(twos):
        print("  ", u, "<->", v)
else:
    print("\nNo two-node cycles found.")

# DFS for longer cycles
state = {}
stack = []
cycles = []

def dfs(u):
    state[u] = 1
    stack.append(u)
    for v in edges.get(u, ()):
        if state.get(v, 0) == 0:
            dfs(v)
        elif state.get(v, 0) == 1:
            if v in stack:
                idx = stack.index(v)
                cycles.append(stack[idx:] + [v])
    stack.pop()
    state[u] = 2

for n in list(nodes):
    if state.get(n, 0) == 0:
        dfs(n)

print("\nCycles found:", len(cycles))
for c in cycles[:10]:
    print("  CYCLE:", " -> ".join(c))

print("\nSelf-referential outputs (output also an input to same callback):")
for out_key, meta in app.callback_map.items():
    outs = set(str(x) for x in parse_outputs(out_key))
    ins = set(f'{fmt_id(i.get("id"))}.{i.get("property")}' for i in meta.get("inputs", []))
    overlap = outs & ins
    if overlap:
        print("  OUT_KEY:", out_key)
        print("    overlap:", sorted(overlap))

print("\nCallbacks involving legs/store/strategy/spot (filtered):")
for out_key, meta in app.callback_map.items():
    txt = str(out_key) + " " + " ".join(str(i.get("id")) for i in meta.get("inputs", []))
    if any(k in txt.lower() for k in ["leg", "store", "analysis", "spot", "strategy"]):
        outs = parse_outputs(out_key)
        ins = [(fmt_id(i.get("id")), i.get("property")) for i in meta.get("inputs", [])]
        print("  OUT:", outs)
        print("   IN:", ins)
