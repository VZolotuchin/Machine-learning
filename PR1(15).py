import numpy as np

# Ініціалізація розміру матриці
rows = 10
cols = 10

# Заповнення матриці випадковими дійсними числами від -2 до 2
matrix = np.random.uniform(-2, 2, size=(rows, cols))

# Виведення матриці
print("Матриця:")
print(matrix)

# Знаходимо індекси мінімальних за модулем значень в кожному рядку
min_indices = np.argmin(np.abs(matrix), axis=1)

# Створюємо вектор-стовпчик із мінімальними за модулем значеннями
result_vector = matrix[np.arange(rows), min_indices].reshape(-1, 1)

# Виведення результату
print("Вектор-стовпчик з найменшими за модулем значеннями в кожному рядку:")
print(result_vector)
