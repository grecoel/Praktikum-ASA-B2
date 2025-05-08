from collections import deque  # Import deque untuk implementasi BFS

# Membaca jumlah node dalam graf
n = int(input().strip())  # Jumlah node (0 hingga n-1)

# Membaca jumlah sisi dalam graf
E = int(input().strip())  # Jumlah sisi

# Membaca daftar sisi (edges) sebagai pasangan node (u, v)
edges = [tuple(map(int, input().split())) for _ in range(E)]

# Membaca node awal (start) dan node tujuan (target)
start, target = map(int, input().split())


def has_path_bfs(n, edges, start, target):
    """
    Fungsi untuk menentukan apakah ada jalur dari node `start` ke node `target`
    menggunakan algoritma Breadth-First Search (BFS).
    
    Parameter:
    - n      : jumlah node (0 hingga n-1)
    - edges  : list of tuples (u, v) merepresentasikan sisi tak berarah
    - start  : node awal
    - target : node tujuan
    
    Return:
    - True jika ada jalur dari `start` ke `target`, False jika tidak ada.
    """
    # Membangun adjacency list untuk merepresentasikan graf
    graph = {i: [] for i in range(n)}  # Inisialisasi adjacency list kosong
    for u, v in edges:
        graph[u].append(v)  # Tambahkan node v ke daftar tetangga node u
        graph[v].append(u)  # Tambahkan node u ke daftar tetangga node v (graf tak berarah)

    # Array untuk menandai node yang sudah dikunjungi
    visited = [False] * n

    # Queue untuk BFS, dimulai dari node `start`
    queue = deque([start])
    visited[start] = True  # Tandai node `start` sebagai dikunjungi

    # Proses BFS
    while queue:
        u = queue.popleft()  # Ambil node pertama dari queue
        if u == target:  # Jika node saat ini adalah target, kembalikan True
            return True
        # Iterasi semua tetangga dari node `u`
        for v in graph[u]:
            if not visited[v]:  # Jika tetangga belum dikunjungi
                visited[v] = True  # Tandai tetangga sebagai dikunjungi
                queue.append(v)  # Tambahkan tetangga ke queue untuk diproses

    # Jika semua node telah dijelajahi dan target tidak ditemukan, kembalikan False
    return False


# Cetak hasil apakah ada jalur dari `start` ke `target`
print(has_path_bfs(n, edges, start, target))