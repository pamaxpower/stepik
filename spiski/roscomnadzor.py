"""
Роскомнадзор запретил)))
"""

name = input('Введите имя: ')
letter = [chr(i) for i in range(1072, 1104)]    # русский алфавит
#letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
s = f'{name} запретил букву'       # строка, из которой будем удалять буквы
for el in letter:                   # перебор элементов в списке букв
    if el in s:                     # проверка, есть ли буква в строчке
        print(f'{s} {el}')
        s = s.replace(el, '').replace('  ',' ').strip()
                # s.replace(el, '') - удаляем букву
                # replace('  ',' ') - меняем двойной пробел на одинарный
                # strip() - удаляем лишние пробелы
