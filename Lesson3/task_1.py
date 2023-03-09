"""

1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def division(first_numb, second_numb):
    try:
        return first_numb / second_numb
    except ZeroDivisionError:
        return "Делить на ноль запрещено!"


try:
    numerator = int(input("Введине числитель: "))
    denominator = int(input("Введите Знаменатель: "))
    print(division(numerator, denominator))
except ValueError:
    print("Требуется вводить только числа!")
