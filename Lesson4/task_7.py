"""

7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

"""

from itertools import count
from math import factorial


def fact(n):
    factor = 1
    for el in count(1):
        if el > n:
            break
        else:
            factor *= el
        yield factor


numb = int(input("Введите целое положительное число: "))
flag = 1
for i in fact(numb):
    print(f"Значение факториала {flag}! = {i}")
    flag += 1
