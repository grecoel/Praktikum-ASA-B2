# Membaca ukuran grid (jumlah baris n dan kolom m)
n, m = map(int, input().strip().split())

# Membaca grid sebagai matriks karakter
grid = [input().strip().split() for _ in range(n)]

# Fungsi DFS iteratif untuk menjelajahi grid dan menghitung jumlah artefak yang bisa dijangkau
def dfs_iterative(grid, start, n, m, visited):
    # Arah gerakan (atas, bawah, kiri, kanan)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Stack untuk menyimpan posisi yang akan dijelajahi
    stack = [start]
    # Variabel untuk menghitung jumlah artefak yang ditemukan
    count = 0

    # Selama masih ada posisi dalam stack
    while stack:
        # Ambil posisi terakhir dari stack
        x, y = stack.pop()
        # Jika posisi ini belum dikunjungi
        if not visited[x][y]:
            # Tandai posisi ini sebagai dikunjungi
            visited[x][y] = True
            # Jika posisi ini adalah artefak, tambahkan ke hitungan
            if grid[x][y] == 'A':
                count += 1
            # Jelajahi semua arah
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Periksa apakah posisi valid dan belum dikunjungi
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                    stack.append((nx, ny))

    # Kembalikan jumlah artefak yang ditemukan
    return count

# Fungsi utama untuk menghitung jumlah artefak yang bisa dijangkau
def count_reachable_artifacts(n, m, grid):
    # Cari posisi awal (Y)
    start = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'Y':  # Jika menemukan posisi 'Y'
                start = (i, j)  # Simpan posisi awal
                break
        if start:
            break

    # Inisialisasi matriks visited untuk melacak posisi yang sudah dikunjungi
    visited = [[False for _ in range(m)] for _ in range(n)]

    # Mulai DFS dari posisi awal
    return dfs_iterative(grid, start, n, m, visited)

# Cetak hasil jumlah artefak yang bisa dijangkau
print(count_reachable_artifacts(n, m, grid))