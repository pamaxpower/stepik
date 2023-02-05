'''
# сумма квадратов элементов множества
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
total = 0
for el in numbers:
    total += el**2
print(total)

# вывести элементы множества fruits, каждый на отдельной строке, 
# отсортированные по убыванию (в обратном лексикографическом порядке).
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sort_fruits = sorted(fruits, reverse=True)
print(*sort_fruits, sep='\n')

# определить верно ли, что в строке ни одна из цифр не повторяется
numbers = input()
if sorted(set(numbers)) == sorted(numbers):
    print('YES')
else:
    print('NO')
# print(('NO','YES')[len(numbers) == len(set(numbers))]) 

# используются ли строках все 10 цифр
a = input()
b = input()
print('YES' if len(set(a+b))==10 else 'NO')
# определить используются ли в строках одинаковые наборы цифр
print('YES' if set(a)==set(b) else 'NO')
'''

# проверить, что для всех введенных слов используется один набор букв
s = input().split()
print('YES' if set(s[0]) == set(s[1]) == set(s[2]) else 'NO')