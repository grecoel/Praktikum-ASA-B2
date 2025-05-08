# Nama File     : bfs.py
# Deskripsi     : penelusuran enode dalam graf yang dilakukan level demi level
# Pembuat       : Gege Centiana Putra
# Tanggal       : 2 Mei 2025

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited