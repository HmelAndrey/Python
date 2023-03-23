"""

1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

"""

import copy


class Matrix:
    def __init__(self, *matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = ""
        for i in range(len(self.matrix)):
            my_str = my_str + "\t".join(map(str, self.matrix[i])) + "\n"
        return my_str

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return "Матрицы разной размерности!"
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)


mat_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
mat_2 = Matrix([11, 12, 13], [14, 15, 16], [17, 18, 19])
print(mat_1)
print(mat_2)
sum_matrix = mat_1 + mat_2
print(sum_matrix.__str__())
