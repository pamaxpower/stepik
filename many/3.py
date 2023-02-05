'''Методы множеств

numbers = {1,2,3,4,5,6,7,8,9,10}
numbers.add(21)             # добавит 21
print(f'После add: {numbers}')
numbers.remove(3)           # удалит 3
# numbers.remove(12)        # ошибка KeyError
numbers.discard(5)          # удалит 5
numbers.discard(11)         # ничего не поменяется
print(f'После discard: {numbers}')
num = numbers.pop()         # удалит случайный элемент и запишет его в переменную
print(f'Удаленный элемент: {num}')
print(f'После pop: {numbers}')
numbers.clear()             # удалит все элементы
print(f'После clear: {numbers}')


myset1 = {'python'}
myset2 = set('python')

item1 = myset1.pop()
item2 = myset2.pop()

print(item1, len(myset1))
print(item2, len(myset2))
'''

# s = []
# [s.append(input()) for i in range(int(input()))]

# # Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
# for i in s:
#     print(len(set(i)))


# # Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
# total = ''
# for i in s:
#     total += i
# print(len(set(total.lower())))




# Напишите программу для определения общего количества различных слов в строке текста.
#s = input().lower().split()
# for i in range(len(s)):
#     for j in s[i]:
#         if j in ".,;:-?!":
#             s[i]=s[i].replace(j,"")
# print(len(set(s)))


# На вход программе подается строка текста, содержащая числа. 
# Для каждого числа выведите слово YES (в отдельной строке), 
# если это число ранее встречалось в последовательности или NO, 
# если не встречалось.

s = list(map(int, input().split()))
res = set()
for i in range(len(s)):
    print('YES' if s[i] in res else 'NO')
    res.add(s[i])