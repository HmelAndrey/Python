"""

3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.

"""

numb_month = int(input("Введите номер месяца: "))

my_list = [
    "Зима", "Зима",
    "Весна", "Весна", "Весна",
    "Лето", "Лето", "Лето",
    "Осень", "Осень", "Осень",
    "Зима"]
print(f'Время года через список: {my_list[numb_month - 1]}')

my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
           6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень",
           11: "Осень", 12: "Зима"}
print(f"Время года через словарь: {my_dict.get(numb_month)}")
