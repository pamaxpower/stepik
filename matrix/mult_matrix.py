"""
Действия над матрицами
"""
import copy

# Сложение
s = list(map(int, input().split()))
matrix1 = [list(map(int, input().split())) for _ in range(s[0])]
print(input())
matrix2 = [list(map(int, input().split())) for _ in range(s[0])]
res = [[0 for _ in range(s[1])] for _ in range(s[0])]
for i in range(s[0]):
    for j in range(s[1]):
        res[i][j] = matrix1[i][j] + matrix2[i][j]
[print(*row) for row in res]

# Умножение
s1 = list(map(int, input().split()))
matrix1 = [list(map(int, input().split())) for _ in range(s1[0])]
print(input())
s2 = list(map(int, input().split()))
matrix2 = [list(map(int, input().split())) for _ in range(s2[0])]
if s1[1] == s2[0]:
    res = [[0 for _ in range(s2[1])] for _ in range(s1[0])]
    for i in range(s1[0]):
        for j in range(s2[1]):
            for k in range(s1[1]):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    [print(*row) for row in res]
else:
    print('Матрицы нельзя перемножить')


# Возведение в степень
n = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
s = int(input())
matrix2 = copy.deepcopy(matrix1)

while s > 1:
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix2[i][k] * matrix1[k][j]

    matrix2 = copy.deepcopy(res)     
    s -= 1

[print(*row) for row in res]