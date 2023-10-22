import random

# Ініціалізація розміру масивів
n = 4

# Ініціалізація порожніх масивів
array1 = [0.0] * n
array2 = [0.0] * n

# Заповнення масивів випадковими дійсними числами від -10 до 10
for i in range(n):
    array1[i] = random.uniform(-10, 10)
    array2[i] = random.uniform(-10, 10)

# Виведення масивів
print("Масив 1:", array1)
print("Масив 2:", array2)

# Виконання поелементних операцій додавання, віднімання та множення
sum_result = [x + y for x, y in zip(array1, array2)]
subtract_result = [x - y for x, y in zip(array1, array2)]
multiply_result = [x * y for x, y in zip(array1, array2)]

# Виведення результатів операцій
print("Сума масивів:", sum_result)
print("Різниця масивів:", subtract_result)
print("Добуток масивів:", multiply_result)
