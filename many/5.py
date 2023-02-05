'''
set1 = {2, 3}
set2 = {1, 2, 3, 4, 5}

# подмножества
print(set1.issubset(set2))          # True
print(set1 <= set2)                 # True

# надмножества
print(set2.issuperset(set1))        # True
print(set2 >= set1)                 # True

# отсутствие общих элементов
set3 = {7, 8, 9}

print(set1.isdisjoint(set2))        # False
print(set1.isdisjoint(set3))        # True
print(set2.isdisjoint(set3))        # True
'''

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

# если ли в числах одинаковые цифры
if set(map(int, s1)).isdisjoint(set(map(int, s2))):
    print('NO')
else:
    print('YES')
#print('NO' if set(map(int, set(input()))).isdisjoint(set(map(int, set(input())))) else 'YES')


# проверить входят ли в запись первого числа все цифры второго
if set(map(int, s2)).issubset(set(map(int, s1))): # через подмножество
    print('YES')
else:
    print('NO')
# через множество
#print('YES' if set(map(int, set(input()))).issuperset(set(map(int, set(input())))) else 'NO')


# множество оценок, которые есть и у первого и у второго учеников, но которых нет у третьего ученика
s3 = set(map(int, input().split()))

# s1&s2 - пересечение s1 и s2
# s1&s2&s3 - пересечение всех трех множеств
s4 = (s1 & s2) - (s1 & s2 & s3)       # разность множеств
print(*sorted(s4, reverse=True))


#множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников
# не более, чем у двух - значт, это все, кроме тех, которые встречаются у всех трех
s5 = (s1 | s2 | s3) - (s1 & s2 & s3)
print(*sorted(s5))


#множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
s6 = (s1 | s2 | s3) - (s1 | s2)
print(*sorted(s6, reverse=True))

#множество оценок, не встречающихся ни у одного из трех учеников.

# множество оценок, не встречающихся ни у одного из трех учеников.
s0 = set(range(11))
s7 = s0 - (s1 | s2 | s3)
print(*sorted(s7))



