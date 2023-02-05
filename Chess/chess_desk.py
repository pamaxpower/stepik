"""
Зарисовка шахматной доски:
'*' - черная клетка
'.' - белая клетка
"""

#s = list(map(int, input().split()))
s = [8, 8]
matrix = [[0 for _ in range(s[1])] for _ in range(s[0])]
for i in range(s[0]):
    for j in range(s[1]):
        if i%2==0 and j%2!=0:
            matrix[i][j] = '*'
        elif i%2!=0 and j%2==0:
            matrix[i][j] = '*'
        else:
            matrix[i][j] = '.'
[print(*row) for row in matrix]
