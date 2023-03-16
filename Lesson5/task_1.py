"""

1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.

"""

my_file = open("task_1.txt", "w", encoding="utf-8")

while True:
    line = input("Введите данные построчно: \n")
    if line == '':
        break
    my_file.write(line + "\n")
my_file.close()

my_file = open("task_1.txt", "r", encoding="utf-8")
content = my_file.read()
print(content)
my_file.close()
