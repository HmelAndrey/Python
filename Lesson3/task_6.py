"""

6. Реализовать функцию int_func(),
принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием.
В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


def int_func(my_str):
    return my_str.title()


my_string = input("Введите строку: ")
print(int_func(my_string))


def sec_func(sec_string):
    for i in range(len(sec_string)):
        print(int_func(sec_string[i]), end=' ')


sec_str = input("Введите строку: ").split()
sec_func(sec_str)
