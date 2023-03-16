"""

3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.

"""

count = 0
salary = 0

with open("task_3.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    for line in content:
        my_list = line.split()
        if int(my_list[1]) < 20000:
            print(f"Фамилия: {my_list[0]}, Оклад: {my_list[1]}")
            salary += int(my_list[1])
            count += 1
    res_sum = salary / count
    print(f"Средняя величина дохода сотрудников: {res_sum:.2f}")
