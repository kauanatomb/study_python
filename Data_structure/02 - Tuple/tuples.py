# Declare a tuple (immutable list)
t = (1, 2, 3, 4, 5,)

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

# Access an element in the tuple
print(f"First element in the tuple {matriz[0]}")  # (1, 2, 3)

# Cut the tuple
print(f"Cut the tuple {matriz[0][1:]}")  # (2, 3)
print(f"Cut the tuple {matriz[1][1:]}")  # (5, 6)
print(f"Cut the tuple {matriz[2][2:]}")  # (9,)

# Count the number of elements in the tuple
print(f"Number of elements in the tuple {len(t)}")  # 5
print(f"Number of elements in the tuple {len(matriz)}")  # 3

# index of the first element with the specified value
print(f"Index of the first element with the specified value {t.index(3)}")  # 2

for i, sublist in enumerate(matriz):
    if 2 in sublist:
        print(f"Index of the first element with the specified value in sublist {i}: {sublist.index(2)}") # 1
        break

# Length of the tuple
print(f"Length of the tuple {len(t)}")  # 5
print(f"Length of the tuple {len(matriz)}")  # 3