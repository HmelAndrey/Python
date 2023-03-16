"""

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task_4_input.txt", "r", encoding="utf-8") as my_input:
    for line in my_input:
        for i in rus_dict:
            line = line.replace(i, rus_dict[i])
        with open("task_4_output.txt", "a", encoding="utf-8") as my_output:
            my_output.write(line + "\n")
