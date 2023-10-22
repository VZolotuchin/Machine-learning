import numpy as np

# Ініціалізація розміру матриці
rows = 5
cols = 5

# Заповнення матриці випадковими дійсними числами в діапазоні від -5 до 5
matrix = np.random.uniform(-5, 5, size=(rows, cols))

# Виведення початкової матриці
print("Початкова матриця:")
print(matrix)

# Транспонування матриці
transposed_matrix = np.transpose(matrix)

# Виведення транспонованої матриці
print("Транспонована матриця:")
print(transposed_matrix)
