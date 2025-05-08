# Nama File     : dfs.py
# Deskripsi     : penelusuran enode dalam graf yang dilakukan menuju ke child kiri dari parent
# Pembuat       : Gege Centiana Putra
# Tanggal       : 3 Mei 2025


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited