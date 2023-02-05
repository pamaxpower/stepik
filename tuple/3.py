# === произведение элементов кортежа ===

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# mult = 1
# for el in numbers:
#     mult *= el
# print(mult)

# === исправление значения элемента кортежа ===

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# lst_poet = list(poet_data)
# lst_poet[2] = 'Москва'
# poet_data = tuple(lst_poet)

# print(poet_data)

# === среднее арифметическое каждого элемента кортежа ===

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# res = []
# for el in numbers:
#     res.append(sum(el)/len(el))
# print(res)

# === вершина параболы по уравнению функции ===

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# def pik_parabola(a,b,c):
#     x = -(b/(2*a))
#     y = (4*a*c - b**2) / (4*a)
#     return x, y
# print(pik_parabola(n1,n2,n3))

# === 

n = int(input())
res = []
[res.append(tuple(input().split())) for i in range(n)]
for el in res:
    print(*el)
print()
for i in range(len(res)):
    if int(res[i][1]) >= 4:
        print(*res[i])
