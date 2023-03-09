"""

4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

"""


def my_func(x, y):
    try:
        if y < 0:
            result = 1
            for i in range(y, 0, 1):
                result = result * x
            result = 1 / result
            return result
        else:
            print("Число y должно быть отрицательным!")
    except ZeroDivisionError:
        print("Делить на 0 запрещено!")


try:
    frs_numb = int(input("Введите x: "))
    sec_numb = int(input("Введите y: "))
    print(my_func(frs_numb, sec_numb))
except ValueError:
    print("Требуется вводить числа!")
