import numpy as np

# Ініціалізація розміру матриці та вектора
matrix_rows = 2
matrix_cols = 3
vector_size = 3

# Заповнення матриці та вектора випадковими дійсними числами від 0 до 1
matrix = np.random.uniform(0, 1, size=(matrix_rows, matrix_cols))
vector = np.random.uniform(0, 1, size=vector_size)

# Виведення матриці та вектора
print("Матриця:")
print(matrix)
print("Вектор:")
print(vector)

# Знаходимо середнє значення вектора
mean_value = np.mean(vector)

# Знаходимо елементи вектора, які менше середнього значення
less_than_mean = vector[vector < mean_value]

# Знаходимо суму цих елементів
sum_less_than_mean = np.sum(less_than_mean)

# Виведення результату
print("Середнє значення вектора:", mean_value)
print("Елементи вектора, які менше середнього значення:", less_than_mean)
print("Сума елементів вектора, які менше середнього значення:", sum_less_than_mean)
