import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(f, a, b, num_samples):
    x_samples = np.random.uniform(a, b, num_samples)
    y_samples = f(x_samples)
    integral_estimate = (b - a) * np.mean(y_samples)
    return integral_estimate

# Кількість випадкових вибірок
num_samples_list = [1000, 10000, 100000]

for num_samples in num_samples_list:
    # Обчислення методом Монте-Карло
    integral_estimate = monte_carlo_integration(f, a, b, num_samples)
    print(f"Оцінка інтегралу методом Монте-Карло з {num_samples} випадковими вибірками: {integral_estimate}")

    # Аналітичне обчислення інтегралу за допомогою SciPy
    result, error = spi.quad(f, a, b)
    print(f"Інтеграл (аналітичний результат): {result}")
    print(f"Оцінка абсолютної похибки: {error}")

    # Різниця між оцінкою методом Монте-Карло та аналітичним результатом
    print(f"Різниця між оцінкою методом Монте-Карло та аналітичним результатом: {abs(integral_estimate - result)}\n")

    # Графічне представлення
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    x_samples = np.random.uniform(a, b, 100)
    y_samples = f(x_samples)
    ax.scatter(x_samples, y_samples, color='blue', s=10)  # Змінено розмір точок на графіку
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}\nОцінка інтегралу методом Монте-Карло з {num_samples} випадковими вибірками: {integral_estimate:.4f}')
    plt.grid()
    plt.show()
