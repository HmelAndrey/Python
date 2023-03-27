"""

3. Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

"""


class MyError(Exception):
    def __init__(self):
        pass


def check_value():
    my_list = []
    while True:
        try:
            try:
                val = int(input("Введите числа: "))
                exc = input(f"Введено число. Для выхода нажмите n, "
                            f"для продолжения ввода нажмите enter: ").lower()
                my_list.append(val)
                if exc == "n":
                    print(my_list)
                    break
            except ValueError:
                raise MyError
        except MyError:
            exc = input(f"Введено не число. Для выхода нажмите n, "
                        f"для продолжения ввода нажмите enter: ").lower()
            if exc == "n":
                print(my_list)
            else:
                check_value()


check_value()
