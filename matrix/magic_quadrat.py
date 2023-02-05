"""
Магическим квадратом порядка nn называется квадратная таблица размера n x n,
составленная из всех чисел 1, 2, 3,…,n**2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равны между собой.

Напишите программу, которая проверяет, является ли заданная квадратная
матрица магическим квадратом.
"""
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
flag = True

# print(sum([matrix[i][i] for i in range(n) for j in range(n) if i == j]))
# главная диагональ

for s in matrix:
    if sum(s) != sum(
            [matrix[i][i] for i in range(n) for j in range(n) if i == j]):
        flag = False
for i in range(n):
    col = []
    for k in range(n):
        col.append(matrix[k][i])
    if sum(col) != sum(
            [matrix[i][i] for i in range(n) for j in range(n) if i == j]):
        flag = False
if sum([matrix[i][i] for i in range(n) for j in range(n) if i == j]) \
        != sum([matrix[i][i] for i in range(n) for j in range(n) if i == n - j - 1]):
    flag = False

res = [el for i in matrix for el in i]  # список всех элементов матрицы
res.sort()
lst_ran = list(range(1, n ** 2 + 1))  # список элементов от [1, n**2]

if lst_ran != res:
    flag = False

if flag:
    print('YES')
else:
    print('NO')
