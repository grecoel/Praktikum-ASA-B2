# Nama File     : Interstallar.py
# Deskripsi     : Menentukan sumber daya minimum untuk menjelajahi planet menggunakan DFS pada graf
# Pembuat       : Gege Centiana Putra
# Tanggal       : 8 Mei 2025

import sys
sys.setrecursionlimit(10**6)

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def is_connected(graph, u, v, n):
    visited = [False] * (n + 1)
    dfs(graph, u, visited)
    return visited[v]

def find_min_cost(graph, node, A, n):
    visited = [False] * (n + 1)
    dfs(graph, node, visited)
    min_cost = float('inf')
    for i in range(1, n + 1):
        if visited[i]:
            min_cost = min(min_cost, A[i])
    return min_cost

def process_interstellar_journey(n, m, q, A, graph, path):
    """
    Proses perjalanan antar planet berdasarkan input yang diberikan.
    """
    total_cost = 0
    for i in range(q - 1):
        u, v = path[i], path[i + 1]
        if not is_connected(graph, u, v, n):
            # Jika tidak terhubung, ambil biaya minimum dari masing-masing komponen
            cost_u = find_min_cost(graph, u, A, n)
            cost_v = find_min_cost(graph, v, A, n)
            total_cost += cost_u + cost_v
        # Jika terhubung → tidak perlu biaya tambahan
    return total_cost

# --- Proses Input ---
n, m, q = map(int, input().split())             # Jumlah planet, relasi, urutan perjalanan
A = [0] + list(map(int, input().split()))       # Biaya warp tiap planet (1-based indexing)

# Bangun graf tak berarah
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Baca urutan perjalanan
path = list(map(int, input().split()))

# --- Proses Perjalanan ---
total_cost = process_interstellar_journey(n, m, q, A, graph, path)

# Cetak hasil
print(total_cost)
