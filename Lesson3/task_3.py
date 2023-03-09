"""

3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.

"""


def my_func(*arg):
    arg = sorted(arg)
    my_sum = arg[-1] + arg[-2]
    print(f"Сумма двух наибольших аргументов: {my_sum}")


try:
    fist_arg = int(input("Введите первый аргумент: "))
    second_arg = int(input("Введите второй аргумент: "))
    third_arg = int(input("Введите третий аргумент: "))
    my_func(fist_arg, second_arg, third_arg)
except ValueError:
    print("Требуется ввести число!")
