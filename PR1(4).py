import random

# Ініціалізуємо розмір матриці
rows = 6
cols = 6

# Ініціалізуємо порожню матрицю
matrix = [[0.0] * cols for _ in range(rows)]

# Заповнюємо матрицю випадковими дійсними числами від 0 до 1
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = random.uniform(0, 1)

# Виводимо значення матриці
for row in matrix:
    print(row)

# Обчислюємо суму діагональних елементів
diagonal_sum = 0.0
for i in range(rows):
    diagonal_sum += matrix[i][i]

print("Сума діагональних елементів:", diagonal_sum)
