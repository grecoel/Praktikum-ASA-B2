# Nama File     : UkuranGambar.py
# Deskripsi     : Menemukan ukuran gambar terbesar di setiap tingkat pohon biner
#                menggunakan algoritma BFS
# Pembuat       : Gege Centiana Putra
# Tanggal       : 5 Mei 2025

from collections import deque
import sys
sys.setrecursionlimit(10**7)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_from_level_order(vals):
    """
    Membangun pohon biner dari daftar nilai level order, dengan 'null' sebagai penanda node kosong.
    """
    if not vals or vals[0] is None:
        return None

    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    n = len(vals)

    while q and i < n:
        node = q.popleft()
        # left child
        if i < n and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        # right child
        if i < n and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1

    return root

def largest_values_per_level(root):
    # Melakukan BFS per level untuk mencari nilai maksimum di setiap tingkat pohon.
    # Mengembalikan list maksimum per level.
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_max = -2**31  # batas bawah sesuai constraints
        for _ in range(level_size):
            node = q.popleft()
            level_max = max(level_max, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level_max)

    return result

# --- eksekusi input/output ---

# Baca jumlah node (tidak terlalu diperlukan untuk parsing Python list)
n = int(input().strip())

# Baca daftar nilai level order, 'null' untuk node kosong
raw = input().split()
vals = [None if x.lower() == 'null' else int(x) for x in raw]

# Bangun pohon dan hitung
root = build_tree_from_level_order(vals)
ans = largest_values_per_level(root)

# Cetak hasil
print(" ".join(map(str, ans)))
