# Nama File     : min_ops_to_zero.py
# Deskripsi     : Menghitung jumlah operasi minimum untuk mengubah N menjadi 0
#                menggunakan operasi: +1/-1, *2, /3ⁿ (n ≥ 1 dan 3ⁿ | x)
# Pembuat       : Gege Centiana Putra
# Tanggal       : 5 Mei 2025

from collections import deque  # Import deque untuk implementasi BFS

def min_ops_to_zero(N):
    """
    Mengembalikan jumlah operasi minimum
    untuk mengubah nilai N menjadi 0.
    """
    # Batas atas untuk BFS agar tidak tak terhingga
    MAX = 10000

    # Precompute semua pangkat 3 sampai melebihi MAX
    p3 = []  # List untuk menyimpan pangkat tiga
    x = 3
    while x <= MAX:
        p3.append(x)  # Tambahkan pangkat tiga ke dalam list
        x = x * 3  # Hitung pangkat tiga berikutnya

    # Dictionary untuk menyimpan jarak (jumlah operasi) dari N ke setiap bilangan
    dist = {N: 0}
    # Queue untuk BFS, dimulai dari N
    q = deque([N])

    # BFS untuk mencari jumlah operasi minimum
    while q:
        u = q.popleft()  # Ambil elemen pertama dari queue
        d = dist[u]  # Ambil jarak (jumlah operasi) dari elemen tersebut

        # Jika sudah mencapai 0, kembalikan jumlah operasi
        if u == 0:
            return d

        # Operasi -1
        v = u - 1
        if v >= 0 and v not in dist:  # Pastikan hasil valid dan belum dikunjungi
            dist[v] = d + 1  # Perbarui jarak
            q.append(v)  # Tambahkan ke queue

        # Operasi +1
        v = u + 1
        if v <= MAX and v not in dist:  # Pastikan hasil valid dan belum dikunjungi
            dist[v] = d + 1  # Perbarui jarak
            q.append(v)  # Tambahkan ke queue

        # Operasi *2
        v = u * 2
        if v <= MAX and v not in dist:  # Pastikan hasil valid dan belum dikunjungi
            dist[v] = d + 1  # Perbarui jarak
            q.append(v)  # Tambahkan ke queue

        # Operasi bagi dengan 3^n
        for power in p3:  # Iterasi melalui semua pangkat tiga
            if power > u:  # Jika pangkat tiga lebih besar dari u, hentikan
                break
            if u % power == 0:  # Jika u habis dibagi pangkat tiga
                v = u // power
                if v not in dist:  # Pastikan hasil belum dikunjungi
                    dist[v] = d + 1  # Perbarui jarak
                    q.append(v)  # Tambahkan ke queue

    # Jika tidak ada cara untuk mencapai 0, kembalikan -1
    return -1

# --- eksekusi ---
N = int(input().strip())  # Baca input dari pengguna
print(min_ops_to_zero(N))  # Cetak hasil jumlah operasi minimum
