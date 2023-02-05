"""
Сумма элементов матрицы (диагонали и четверти)
"""
n = int(input())        # ранг матрицы
matrix = [list(map(int, input().split())) for _ in range(n)] # заполнение матрицы

res = []
for i in range(n):
    for j in range(n):
        if i == j:
            res.append(matrix[i][j])
            
print(f'Сумма главной диагонали: {sum([matrix[i][i] for i in range(n) for j in range(n) if i == j])}')
print(f'Сумма побочной диагонали: {sum([matrix[i][n-i-1] for i in range(n) for j in range(n) if i+j+1 == n])}')
print(f'Сумма верхней четверти: {sum([matrix[i][j] for i in range(n) for j in range(n) if i < j and i < n-j-1])}')
print(f'Сумма правой четверти: {sum([matrix[i][j] for i in range(n) for j in range(n) if i < j and i > n-j-1])}')
print(f'Сумма нижней четверти: {sum([matrix[i][j] for i in range(n) for j in range(n) if i > j and i > n-j-1])}')
print(f'Сумма левой четверти: {sum([matrix[i][j] for i in range(n) for j in range(n) if i > j and i < n-j-1])}')


