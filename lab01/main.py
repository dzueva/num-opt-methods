import math
from dataclasses import dataclass
from decimal import getcontext, Decimal

import matplotlib.pyplot as plt
from numpy import logspace

from methods import dichotomy, bisection, golden_section

getcontext().prec = 50

@dataclass
class Method:
    method: callable
    name: str

def function(x: Decimal) -> Decimal:
    """
    Пример заданной функции.
    F = (x^4)/ln(x)

    :param x: значение x
    :return: решение функции от заданного числа
    """
    if x <= 0:
        raise ValueError(f"Значение X не может быть меньше или равно 0 на заданной функции. x={x}")
    log_val = x.ln() / Decimal(math.log(10))
    return (x**4) / log_val

def build_graph(
        methods: list[Method],
        func: callable,
        a: float,
        b: float
):
    epsilon_values = logspace(-4, -1, 20)
    plt.figure(figsize=(10, 6))

    for method in methods:
        iterations_list = []
        for epsilon in epsilon_values:
            _, iters = method.method(func, a, b, epsilon)
            iterations_list.append(iters)

        plt.plot(epsilon_values, iterations_list, marker="o", label=method.name)

    plt.xlabel("Погрешность")
    plt.ylabel("Число итераций")
    plt.title("Число итераций в зависимости от погрешности для разных методов")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    a, b = 1.1, 1.5
    print(f"Отрезок = [{a}, {b}]")
    methods = [
        Method(
            method=dichotomy,
            name="дихотомии"
        ),
        Method(
            method=bisection,
            name="бисекции"
        ),
        Method(
            method=golden_section,
            name="золотого сечения"
        ),
        Method(
            method=dichotomy,
            name="Фибоначчи"
        ),
    ]
    build_graph(methods, function, a, b)

if __name__ == "__main__":
    main()
