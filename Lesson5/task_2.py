"""

2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.

"""

count_lines = 0

my_file = open("task_2.txt", "r", encoding="utf-8")

for lines in my_file:
    count_lines += 1
    line = lines.split()
    print(f"Количество слов в {count_lines} строке равно {len(line)}")
    print(f"{count_lines} строка: {lines}")
print(f"Число строк в файле равно {count_lines}")

my_file.close()

