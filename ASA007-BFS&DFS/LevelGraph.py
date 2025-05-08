# Nama File     : LevelGraph.py
# Deskripsi     : penelusuran node dalam graf tak berarah dan tak berbobot secara level demi level (BFS),
#                mencetak urutan kunjungan dan jarak (level) dari simpul awal ke semua simpul
# Pembuat       : Gege Centiana Putra
# Tanggal       : 3 Mei 2025

from collections import deque
import ast

n = int(input().strip())
edges = ast.literal_eval(input().strip())
start = int(input().strip())

def bfs_with_levels(graph, start):
    visited = set([start])
    level = {start: 0}
    order = []
    queue = deque([start])

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(graph[u]):
            if v not in visited:
                visited.add(v)
                queue.append(v)
                level[v] = level[u] + 1

    return order, level


# bangun adjacency list
graph = {i: [] for i in range(1, n+1)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

order, level = bfs_with_levels(graph, start)

print("Urutan BFS: " + ", ".join(map(str, order)))
print("Level:")
for u in order:
    print(f"simpul {u}: {level[u]}")
