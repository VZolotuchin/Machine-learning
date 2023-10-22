import numpy as np

# Ініціалізація розміру матриці
rows = 3
cols = 3

# Ініціалізація порожньої матриці та заповнення її випадковими цілими числами від 1 до 7
matrix = np.random.randint(1, 7, size=(rows, cols))

# Виведення матриці
print("Матриця:")
print(matrix)

# Обчислення оберненої матриці, якщо це можливо
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Обернена матриця:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Матриця не має оберненої.")
