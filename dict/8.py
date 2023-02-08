'''
На вход программе подается строка текста. 
Напишите программу, которая выводит слово, которое встречается реже всего, 
без учета регистра. Если таких слов несколько, выведите то, 
которое меньше в лексикографическом порядке.

На вход программе подается строка текста.

Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, 
слова apple и Apple должна воспринимать как одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте 
могут присутствовать пробелы и знаки препинания .,!?:;-, 
которые нужно игнорировать. Других символов в тексте нет.
'''
#s = 'London is the capital of Great Britain. More than six million people live in London. London lies on both banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university city, and the seat of the government of Great Britain!'
s = input()
text = s.lower().split()
dict = {}
for let in text:

    word = ''               # ищем знаки препинания и перезаписываем слово без них
    for i in let:
        if i.isalpha():
            word+=''.join(i)
    # или [word.strip('.,!?:;-') for word in input().lower().split()]

    dict[word] = dict.get(word, 0) + 1
res = {}
for key in dict:
    if dict[key] == min(dict.values()):
        res[key] = res.get(key, 0 ) + dict[key]
print(min(res))
