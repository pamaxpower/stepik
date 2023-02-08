'''
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся 
слово строки s. Если таких слов несколько, должно быть выведено то, 
что меньше в лексикографическом порядке.
'''
s = 'orange strawberry barley gooseberry apple apricot barley currant orange ' \
    'melon pomegranate banana banana orange barley apricot plum grapefruit ' \
    'banana quince strawberry barley grapefruit banana grapes melon ' \
    'strawberry apricot currant currant gooseberry raspberry apricot currant ' \
    'orange lime quince grapefruit barley banana melon pomegranate barley ' \
    'banana orange barley apricot plum banana quince lime grapefruit ' \
    'strawberry gooseberry apple barley apricot currant orange melon ' \
    'pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana ' \
    'quince barley lime grapefruit pomegranate barley '

text = s.split()
dict = {}
for word in text:
    dict[word] = dict.get(word, 0) + 1
res = {}
for key in dict:
    if dict[key] == max(dict.values()):
        res[key] = res.get(key, 0 ) + dict[key]
print(min(res))


# 2 вариант
# dict1 = {s.count(i): i for i in sorted(s.split(), reverse=True)}
# print(dict1[max(dict1)])

# 3 вариант
# result = {word: s.count(word) for word in set(s.split())}
# print(min([key for key, value in result.items() if value == max(result.values())]))

# 4 вариант
# result = {i: s.count(i) for i in sorted(set(s.split()))}
# for key, values in result.items():
#     if values == max(result.values()):
#         print(key)
#         break