import random

# Ініціалізація розміру матриць
rows1 = 2
cols1 = 3
rows2 = 3
cols2 = 3

# Ініціалізація порожніх матриць
matrix1 = [[0] * cols1 for _ in range(rows1)]
matrix2 = [[0] * cols2 for _ in range(rows2)]

# Заповнення матриць випадковими цілими числами від 1 до 12
for i in range(rows1):
    for j in range(cols1):
        matrix1[i][j] = random.randint(1, 12)

for i in range(rows2):
    for j in range(cols2):
        matrix2[i][j] = random.randint(1, 12)

# Виведення матриць
print("Матриця 1:")
for row in matrix1:
    print(row)

print("Матриця 2:")
for row in matrix2:
    print(row)

# Перемноження матриць
result = [[0] * cols2 for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Виведення результату перемноження
print("Результат перемноження матриць:")
for row in result:
    print(row)
