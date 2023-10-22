# Ініціалізуємо початкове значення
start_value = 30

# Ініціалізуємо порожній список для збереження чисел
vector = []

# Заповнюємо список числами
while start_value >= 0:
    vector.append(start_value)
    start_value -= 2

# Виводимо значення вектора
for number in vector:
    print(number)
