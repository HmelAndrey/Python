"""

1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать
скрипт с параметрами.

"""

from sys import argv

my_script, prod_hour, rate_hour, f_prize = argv


def payroll(prod, rate, prize):
    try:
        return int(prod) * int(rate) + int(prize)
    except ValueError:
        print("Ошибка формата ввода!Требуется вводить только числа!")
        exit()


print(f"Заработаная плата сотрудника: {payroll(prod_hour, rate_hour, f_prize)}")
