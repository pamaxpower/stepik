# from math import sqrt

# def solve(a, b, c):
#     dis = b**2 - 4*a*c
#     x1 = (-b - sqrt(dis)) / (2 * a)
#     x2 = (-b + sqrt(dis)) / (2 * a)
#     if x1 < x2:
#         return x1, x2
#     else:
#         return x2, x1
    
# a, b, c = int(input('a=')), int(input('b=')), int(input('c='))

# x1, x2 = solve(a, b, c)
# print(x1, x2)

# ===============================================================================


# def draw_triangle(x, y):
#     j = 1
#     for i in range(y):
#         print(' ' * (y-i) + '*' * j)
#         j+=2


# a = 15
# b = 8
# draw_triangle(a, b)  # вызов функции

# ===============================================================================


# from math import factorial

# def compute_binom(n, k):
#     binom = factorial(n) / (factorial(k) * factorial(n-k))
#     return binom

# n = int(input('n= '))
# k = int(input('k= '))

# print(compute_binom(n, k))

# ==============================================================================

# def number_to_words(num):
#     list1 = ['один', 'два','три','четыре','пять','шесть','семь','восемь','девять']
#     list2 = ['десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
#     list3 = ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
#     if 0 < num <= 9:
#         res = [list1[i-1] for i in range(1, len(list1)+1) if i == num]
#     elif 10 <= num < 20:
#         res = [list2[i-1] for i in range(1, len(list2)+1) if i == (num-9)]
#     elif 20 <= num < 100:
#         res = [list3[i-2] for i in range(1, len(list3)+2) if i == (num//10)] + [list1[i-1] for i in range(1, len(list1)+1) if i == num%10]
#     else:
#         return print('Вы ввели неправильное число')
#     return print(*res)
    
# n = int(input('Введите число: '))

# if n == 0:
#     print('ноль')
# # elif n < 0:
# #     print('минус' + number_to_words(n))
# else:
#     number_to_words(n)

# ==============================================================================

# сделать эту задачу через словарь

# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 
#               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 
#               'july', 'august', 'september', 'october', 'november', 'december']
#     for i in range(1, len(lng_ru)+1):
#         if i == number:
#             if language == 'ru':
#                 return lng_ru[i-1]
#             elif language == 'en':
#                 return lng_en[i-1]
#             else:
#                 return 'ошибка языка'
          
# lan = input()
# num = int(input())

# print(get_month(lan, num))

# ==============================================================================

# def is_magic(data):
#     lst = [int(i) for i in data.split('.')]
#     return lst[0] * lst[1] == lst[2]%100

# date = input()

# print(is_magic(date))

# ==============================================================================

# дописать для текста на русском

# def is_pangram(txt):
#     en_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     # ru_word = []
#     flag = True
#     for el in en_word:
#         if el not in txt.lower():
#             flag = False
#     return flag
    
# text = 'Jackdaws love my big sphinx of quartz'

# print(is_pangram(text))