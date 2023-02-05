"""
Заполнение матрицы
"""


def print_matrix(matrix):
    [print(*row) for row in matrix]


def print_matrix2(matrix, demension):
    for i in range(demension[0]):
        for j in range(demension[1]):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def turn_r90(matr, dem):  # повоторот матрицы на 90градусов вправо
    res = [list(map(int, '0' * dem[1])) for _ in range(dem[0])]
    for i in range(dem[0]):
        for j in range(dem[1]):
            res[j][len - i - 1] = matr[i][j]



def fill_row(matrix, demension):
    for i in range(demension[0]):
        for j in range(demension[1]):
            matrix[i][j] = i * demension[1] + j + 1 
    print_matrix(matrix)


def fill_col(matrix, demension):
    for i in range(demension[0]):             
        for j in range(demension[1]):
            matrix[i][j] = i+1 + j*demension[0]
    print_matrix(matrix)


def fill_below_side_diag(matrix, demension):
    for i in range(demension[0]):             
        for j in range(demension[1]):
            if i >= demension[0] - j - 1:
                matrix[i][j] = 1
    print_matrix(matrix)


def fill_above_side_diag(matrix, demension):
    for i in range(demension[0]):             
        for j in range(demension[1]):
            if i <= demension[0] - j - 1:
                matrix[i][j] = 1
    print_matrix(matrix)


def fill_below_main_diag(matrix, demension):
    for i in range(demension[0]):             
        for j in range(demension[1]):
            if i >= j:
                matrix[i][j] = 1
    print_matrix(matrix)


def fill_above_main_diag(matrix, demension):
    for i in range(demension[0]):             
        for j in range(demension[1]):
            if i <= j:
                matrix[i][j] = 1
    print_matrix(matrix)


def fill_diag(matrix, demension):
    for i in range(demension[0]):
        for j in range(demension[1]):
            matrix[i][j] = (i + j) % demension[1] + 1
    print_matrix(matrix)


def fill_diag2(matrix, demension):
    count = 1
    for k in range(sum(demension)):
        for i in range(demension[0]):
            for j in range(demension[1]):
                if i + j == k:
                    matrix[i][j] = count
                    count += 1

    print_matrix(matrix)


def fill_snake(matrix, demension):
    for i in range(demension[0]):
        for j in range(demension[1]):
            matrix[i][j] = i*demension[1] + j + 1
        if i % 2 != 0:
            matrix[i] = matrix[i][::-1]
            # matrix[i].reverse()
    print_matrix2(matrix, demension)


def turn_l90(matrix, len):  # повоторот матрицы на 90градусов вправо
    res = [list(map(int, '0' * len[0])) for _ in range(len[1])]
    for i in range(len[1]):
        for j in range(len[0]):
            res[i][j] = matrix[j][len[1]-1-i]
    return res


def fill_spiral(matrix, dem):
    count = 1
    for i in range((dem[0]+1)//2):
        while i == 0:
            for j in range(dem[1]-1):
                matrix[i][j] = count
                count += 1
            
                # for j in range(dem[1]):
                #     matrix[i][j] = count
                #     count += 1
            
            [print(*row) for row in turn_l90(matrix, dem)]      
            dem[0], dem[1] = dem[1], dem[0] 
        break
    pass






# в строчку вводится размерность матрицы(строки/столбцы)
s = list(map(int, input().split()))
# создаем матрицу с нулями
matr = [[0 for _ in range(s[1])] for _ in range(s[0])]


fill_spiral(matr, s)



#print_matrix(matr)