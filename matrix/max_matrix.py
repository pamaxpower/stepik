"""
Поиск максимума ниже главной диагонали включительно
"""
n = int(input())  # ранг матрицы
matrix = [list(map(int, input().split())) for _ in range(n)]  # заполнение матрицы

# 1 способ:
maximum = matrix[0][0]
res = []
for i in range(n):
    for j in range(n):
        if (j <= i <= n - j - 1) or (j >= i >= n - j - 1):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)

# # 2 способ
# res=[]
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             res.append(matrix[i][j])
# print(max(res))


# # 3 способ
# print(max([matrix[i][j] for i in range(n) for j in range(n) if i >= j]))

# ================================================================================

# максимум из левой и правой четверти матрицы
print(max([matrix[i][j] for i in range(n) for j in range(n) if
           (j <= i <= n - j - 1) or (j >= i >= n - j - 1)]))

# ================================================================================

# # Поиск индекса первого вхождения максимального элемента
# n = int(input())
# m = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(max(max(matrix, key=max)))        # максимум всей матрицы

# for i in range(n):
#     if max(max(matrix, key=max)) in matrix[i]:                  # проверка на наличие максимума в строке
#         print(i, matrix[i].index(max(max(matrix, key=max))))    # индекс первого максимума
#         break

# ================================================================================
