'''
Анаграммы
Анаграмма – слово (словосочетание), образованное путём перестановки букв, 
составляющих другое слово (или словосочетание). 
Например, английские слова evil и live – это анаграммы
'''

# Определите являются ли заданные слова анаграммами
# word1 = input()
# word2 = input()
# dict1 = {}
# dict2 = {}
# for i in word1:
#     dict1[i] = dict1.get(i, 0) + 1
# for i in word2:
#     dict2[i] = dict2.get(i, 0) + 1

# print('YES') if dict1 == dict2 else print('NO')


# Определить, являются ли предложения анаграммами
text1 = input().lower()                     # делает текст строчными буквами
text2 = input().lower()
dict1 = {}
dict2 = {}

for el in text1:            
    if el not in '.,!?;:- ':                # убирает знаки препинания и пробелы
        dict1[el] = dict1.get(el, 0) + 1

for el in text2:
    if el not in '.,!?;:- ':
        dict2[el] = dict2.get(el, 0) + 1
        
print('YES') if dict1 == dict2 else print('NO')