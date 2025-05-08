# Nama File     : IslandCounter.py
# Deskripsi     : Menghitung jumlah pulau dalam grid 2D menggunakan algoritma DFS
# Pembuat       : Gege Centiana Putra
# Tanggal       : 8 Mei 2025

m, n = map(int, input().split())
grid = []  
for _ in range(m):
    grid.append(list(map(int, input().split())))  

# Fungsi untuk menghitung jumlah pulau dalam grid
def count_islands(grid):
    m = len(grid)    
    n = len(grid[0]) 
    count = 0        # Variabel untuk menghitung jumlah pulau

    # Iterasi melalui setiap sel dalam grid
    for i in range(m):
        for j in range(n):
            # Jika menemukan daratan (1), lakukan DFS untuk menandai pulau
            if grid[i][j] == 1:
                count += 1  
                dfs(grid, i, j)  # Tandai seluruh pulau menggunakan DFS

    return count

# Fungsi DFS iteratif untuk menandai seluruh sel dalam satu pulau
def dfs(grid, start_x, start_y):
    m = len(grid)    
    n = len(grid[0]) 
    stack = [(start_x, start_y)]  # Stack untuk DFS
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arah: atas, bawah, kiri, kanan

    while stack:
        x, y = stack.pop()
        # Jika sel berada di luar batas atau bukan daratan, lanjutkan
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            continue
        # Tandai sel sebagai dikunjungi dengan mengubahnya menjadi 0
        grid[x][y] = 0
        # Tambahkan semua tetangga yang valid ke stack
        for dx, dy in directions:
            stack.append((x + dx, y + dy))


# Hitung jumlah pulau dan cetak hasilnya
print(count_islands(grid))