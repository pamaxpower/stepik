"""
Поиск зараженных холодильников
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных 
холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв 
и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие 
буквы, главное наличие последовательности букв), то холодильник заражен и нужно 
вывести номер холодильника, нумерация начинается с единицы
"""
import re
for i in range(1, int(input()) + 1):
    if re.search(r'a.*n.*t.*o.*n', input()):
        print(i, end=' ')


def search_anton(s):                    # функция поиска слова
    search = 'anton'                    # цель поиска
    for el in search:                   # поочередно берем буквы из ключевого слова
        if el in s:                     # проверяем наличие этой буквы в строке данных
            s = s[(s.index(el)+1):]     # если есть, то делаем срез от этой буквы и до конца списка
            
        else:
            return False                # если буквы нет, то проверка не пройдена, функция вернет False
    return True                         # проверка пройдена, функция возвращает True


s = []
# список состоящий из строк данных для каждого холодильника
[s.append(input()) for i in range(int(input()) )]

count = 0
[print(j+1, end=' ') for j in range(len(s)) if search_anton(s[j])]

# for j in range(len(s)):                 # перебираем список данных холодильников
#     if search_anton(s[j]):              # данных каждого холодильника прогоняем через функцию поиска
#         print(j+1, end=' ')             # печатаем номер холодильника, если прошел проверку
#                                         # (j+1) - для j не смог написать условие