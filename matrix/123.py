def change_col(matr, n, m, ch):
    res = [list(map(int, '0' * m)) for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if col == ch[0]:
                res[row][ch[1]] = matr[row][col]
            elif col == ch[1]:
                res[row][ch[0]] = matr[row][col]
            else:
                res[row][col] = matr[row][col]
        print(*res[row])


def change_col2(matr, len, ch):
    for i in range(len):
        matr[i][ch[0]], matr[i][ch[1]] = matr[i][ch[1]], matr[i][ch[0]]
    for row in matr:
        print(*row)


def change_diag(matr, len):
    for i in range(len):
        matr[i][i], matr[len - i - 1][i] = matr[len - i - 1][i], matr[i][i]
    for row in matr:
        print(*row)


def turn_l90(matr, len):  # повоторот матрицы на 90градусов влево
    res = [list(map(int, '0' * len)) for _ in range(len)]
    for i in range(len):
        for j in range(len):
            res[i][j] = matr[j][len - i - 1]
            # res[i][j] = matr[len-j-1][i]
    for row in res:
        print(*row)


def turn_r90(matr, len):  # повоторот матрицы на 90градусов вправо
    res = [list(map(int, '0' * len[0])) for _ in range(len[1])]
    for i in range(len[0]):
        for j in range(len[1]):
            res[j][s[0]-1-i] = matr[i][j]
    for row in res:
        print(*row)

def fill_row(matrix, demension):
    for i in range(demension[0]):
        for j in range(demension[1]):
            matrix[i][j] = i * demension[1] + j + 1

#n = int(input())
# m = int(input())
s = list(map(int, input().split()))
#matrix = [list(map(int, input().split())) for _ in range(n)]
matrix = [[0 for _ in range(s[1])] for _ in range(s[0])]
fill_row(matrix,s)
[print(*row) for row in matrix]
print()

turn_r90(matrix, s)

#[print(*row) for row in matrix[::-1]]  # зеркальное отображение относительно горизонтальной оси


