import numpy as np

# Ініціалізація розміру матриць
rows = 9
cols = 9

# Заповнення першої та другої матриць випадковими цілими числами від 1 до 5
matrix1 = np.random.randint(1, 6, size=(rows, cols))
matrix2 = np.random.randint(1, 6, size=(rows, cols))

# Виведення обох матриць
print("Перша матриця:")
print(matrix1)
print("Друга матриця:")
print(matrix2)

# Обчислення добутку матриць
result = np.dot(matrix1, matrix2)

# Виведення результату
print("Добуток матриць:")
print(result)
