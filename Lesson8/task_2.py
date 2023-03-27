"""

2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numerator = int(input("Введите числитель: "))
    denominator = int(input("Введите знаменатель: "))
    if denominator == 0:
        raise OwnError("Делить на ноль нельзя!")
    else:
        res = numerator / denominator
        print(f"Результат деления: {res}")
except ValueError:
    print("Ошибка!Нужно вводить число!")
except OwnError as err:
    print(err)
