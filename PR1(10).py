import numpy as np

# Ініціалізація розміру матриці та вектора
matrix_rows = 3
matrix_cols = 4
vector_size = 4

# Заповнення матриці випадковими цілими числами від 1 до 10
matrix = np.random.randint(1, 11, size=(matrix_rows, matrix_cols))

# Заповнення вектора випадковими дійсними числами від 0 до 1
vector = np.random.uniform(0, 1, size=vector_size)

# Виведення матриці та вектора
print("Матриця:")
print(matrix)
print("Вектор:")
print(vector)

# Обчислення добутку матриці на вектор
result = np.dot(matrix, vector)

# Виведення результату добутку
print("Результат добутку матриці на вектор:")
print(result)
