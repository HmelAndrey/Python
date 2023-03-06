"""

5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

"""

my_list = [7, 5, 5, 3, 3, 2]
number = int(input("Введите натуральное число: "))
flag = my_list.count(number)
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break
    elif number == my_list[i]:
        my_list.insert(i + flag, number)
        break
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
print(f"Результат: {my_list}")
