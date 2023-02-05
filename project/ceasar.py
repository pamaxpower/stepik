"""
ЗАшифровка сообщения, где сдвиг указывается вручную:
'+' - сдвиг вправо
'-' - сдвиг влево
"""

eng_alp = 'abcdefghijklmnopqrstuvwxyz'      # нужен для проверки языка в основной программе

text = input('Введите ваше сообщение: ')
cod = int(input('Введите сдвиг: '))


def ru_code_ceasar(item, code):
    #rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for i in range(len(rus_alphabet)):
        if rus_alphabet[i] == item:
            if (i + code) <= (len(rus_alphabet)-1):
                return rus_alphabet[i + code]
            else:
                return rus_alphabet[code - (len(rus_alphabet) - i)]


def en_code_ceasar(item, code):
    eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(eng_alphabet)):
        if eng_alphabet[i] == item:
            if (i + code) <= (len(eng_alphabet)-1):
                return eng_alphabet[i + code]
            else:
                return eng_alphabet[code - (len(eng_alphabet) - i)]


res = ''

for el in text:
    if el.lower() in eng_alp:       # определяем язык
        if el.islower():            # если буква прописная
            res += en_code_ceasar(el, cod)
        elif el.isupper():          # если буква заглавная
            a = en_code_ceasar(el.lower(), cod)
            res += a.upper()
        else:                       # если символ или цифра
            res += el
    else:
        if el.islower():
            res += ru_code_ceasar(el, cod)
        elif el.isupper():
            a = ru_code_ceasar(el.lower(), cod)
            res += a.upper()
        else:
            res += el

print(res)