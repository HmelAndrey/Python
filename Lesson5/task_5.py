"""

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

"""

with open("task_5.txt", "w", encoding="utf-8") as my_file:
    try:
        conten = input("Введите числа через пробел: ")
        my_file.write(conten)
        my_list = conten.split()
        print(sum(map(int, my_list)))
    except ValueError:
        print("Ошибка ввода!Требуется вводить только цифры!")
