"""
Матрицы
"""


def print_matrix(matrix, n, width=1):
    """
    Вывод матрицы
    :param matrix: матрица
    :param n: размер матрицы
    :param width: выравнивание по ширине
    :return: str(matrix[row][col]) - вывод элемента матрицы в типе string
            ljust(width) - выравнивание по width
    """
    for row in range(n):
        for col in range(n):
            print(str(matrix[row][col]).ljust(width), end=' ')
        print()


# # считываение матрицы из n-строк
# k = int(input())            # размер матрицы
# matr = []
# for i in range(k):
#     temp = [int(num) for num in input(f'Введите {i+1} строку: ').split()]
#     # вводим строку и добавляем ее в матрицу
#     matr.append(temp)
# print(matr)                 # вывод вложенного списка


# заполнение матрицы с клавиатуры
n = int(input())    # кол-во строк
m = int(input())    # кол-во столбцов
matrix = [[input() for _ in range(n)] for _ in range(m)]

for s in matrix:
    print(*s)
print()
[print(*[matrix[j][i] for j in range(m)]) for i in range(n)]
print()

lst = []
[lst.append(int(matrix[i][i])) for i in range(n)]
print(sum(lst))
    