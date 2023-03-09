"""

5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

"""


def enter_sum(arg_sum=0):
    my_list = input("Введите числа через пробел: ").split(' ')
    for i in range(len(my_list)):
        if my_list[i] != "a":
            arg_sum = arg_sum + int(my_list[i])
        else:
            break
    print(arg_sum)
    if 'a' in my_list:
        print("Конец программы")
    else:
        enter_sum(arg_sum)


enter_sum()
