import math

# Ініціалізуємо розмір матриці
rows = 3
cols = 3

# Ініціалізуємо порожню матрицю
matrix = [[0] * cols for _ in range(rows)]

# Функція для обчислення факторіалу числа
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Заповнюємо матрицю факторіалами
current_number = 1
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = factorial(current_number)
        current_number += 1

# Виводимо значення матриці
for row in matrix:
    print(row)
