poets = [
    ('Тургенев', 14),
    ('Есенин', 13),
    ('Маяковский', 28),
    ('Фет', 15),
    ('Лермонтов', 20)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i] > poets[j]:     # лексикографическое сравнение
            poets[i], poets[j] = poets[j], poets[i]

# происходит сравнение элементов списка

# строки сравниваются сначала по индексам первых букв:
# print(ord('Е'))   = 1045
# print(ord('Т'))   = 1058
# print(ord('М'))   = 1052
# print(ord('Л'))   = 1051
# print(ord('Ф'))   = 1060 