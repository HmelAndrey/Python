"""

2. Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

"""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = []

for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        lst.append(my_list[el])

print(lst)

lst_2 = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]

print(lst_2)
