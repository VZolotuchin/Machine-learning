import random

# Ініціалізуємо розмір матриці
rows = 5
cols = 5

# Ініціалізуємо порожню матрицю
matrix = [[0] * cols for _ in range(rows)]

# Заповнюємо матрицю випадковими цілими числами від 1 до 10000
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = random.randint(1, 10000)

# Виводимо значення матриці
for row in matrix:
    print(row)
