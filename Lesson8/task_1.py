"""

1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""


class Data:
    def __init__(self, full_date):
        self.full_date = str(full_date)

    @classmethod
    def int_numb(cls, full_date):
        my_date = []
        for i in full_date.split():
            if i != "-":
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def val_numb(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2023:
                    return "Дата введена правильно!"
                else:
                    return "Год указан не верно!"
            else:
                return "Месяц указан не верно!"
        else:
            return "День указан не верно!"

    def __str__(self):
        return f"Введена дата: {Data.int_numb(self.full_date)}"


obj = Data("12 - 12 - 1990")
print(obj)
print(obj.int_numb("12 - 12 - 1991"))
print(obj.val_numb(33, 12, 2015))
print(obj.val_numb(13, 13, 2015))
print(obj.val_numb(13, 6, 2024))
print(obj.val_numb(15, 12, 2015))

"""

4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
"""


class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {"Модель устройства": self.name, "Цена": self.price, "Количество": self.quantity}

    def income(self):
        try:
            name = input(f"Введите наименование: ")
            price = int(input(f"Введите цену: "))
            quantity = int(input(f"Введите количество: "))
            item = {"Модель устройства": name, "Цена": price, "Количество": quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print("Введено не верное значение!")


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


pr = Printer('Kyocera', 20000, 10)
scan = Scanner('Epson', 35000, 5)
xer = Xerox('Canon', 15000, 15)
pr.income()
scan.income()
xer.income()
