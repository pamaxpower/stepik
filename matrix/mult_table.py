"""
Таблица умножения
"""


def print_matrix(matrix, n, m, width=1):
    """
    Вывод матрицы
    :param matrix: матрица
    :param n: размер матрицы
    :param width: выравнивание по ширине
    :return: str(matrix[row][col]) - вывод элемента матрицы в типе string
            ljust(width) - выравнивание по width
    """
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).rjust(width), end=' ')
        print()


n = 9
m = 9

matrix = [list(map(int, '0' * m)) for _ in range(n)]

for row in range(n):
    for col in range(m):
        matrix[row][col] = (row+1) * (col+1)

print('\nТАБЛИЦА УМНОЖЕНИЯ:\n')
print_matrix(matrix, n, m, 3)


    