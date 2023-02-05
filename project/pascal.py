"""
Треугольник Паскаля
"""
from math import factorial


def pascal(n):                      # Вывод первых n-строк (включая 0-строку)
    for i in range(n):
        lst = []
        for j in range(n):
            if i < j:               # Проверяем условие. Если не проверим, выдаст ошибку 
                                    # вычисления factorial(i-j), где i-j отрицаиельное число
                break
            else:
                res = factorial(i) // (factorial(j)*(factorial(i-j)))
                # формула вычисления биноминального коэффициента
                lst.append(res)     # результат добавляем в список
        print(*lst)                 # печать элементов через пробел
    

def pascal2(n):                     # Получение n-строчки 
    # отличие двух функций в том, что в первом варианте каждая новая строчка выводится на экран, 
    # а во втором - создается список(треугольник) списков(строки) и по запросу берется только 1 строка
    res = []
    for i in range(n+1):
        lst = []
        for j in range(n+1):
            if i < j:
                break
            else:
                lst.append(factorial(i) // (factorial(j)*(factorial(i-j))))
        res.append(lst)
    return res


def print_pascal(lst, n):           # вывод треугольника Паскаля в виде дерева
    for i in range(n):
        for j in range(n-i-1):
            print(format(' ', '<2'), end='')
        for j in range(i+1):
            print(format(lst[i][j], '<4'), end='')
        print()    


num = int(input())
pascal(num)

print(pascal2(num)[num])

print_pascal(pascal2(num), num)

