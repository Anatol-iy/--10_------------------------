import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
L = pulp.LpVariable('L', lowBound=0, cat='Integer')  # Кількість одиниць лимонаду
F = pulp.LpVariable('F', lowBound=0, cat='Integer')  # Кількість одиниць фруктового соку

# Функція цілі (Максимізація виробництва)
model += L + F, "Total Production"

# Додавання обмежень
# Обмеження за кількістю ресурсів
model += 2 * L + F <= 100  # Вода
model += L <= 50  # Цукор
model += L <= 30  # Лимонний сік
model += 2 * F <= 40  # Фруктове пюре
model += F <= 30  # Вода для фруктового соку

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Кількість виробленого лимонаду:", L.varValue)
print("Кількість виробленого фруктового соку:", F.varValue)
