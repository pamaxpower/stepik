"""
Зашифровка сообщения, когда сдвиг шифра - это кол-во букв в слове
"""

eng_alp = 'abcdefghijklmnopqrstuvwxyz'


def ru_code_ceasar(item, code):
    # rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
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


def word_len(string):
    count = 0
    for letter in string:
        if letter.isalpha():
            count += 1
    return count


text = input('Введите ваше сообщение: ')

res = ''

s = text.split()
for word in s:
    cod = word_len(word)
    for el in word:
        if el.lower() in eng_alp:
            if el.islower():
                res += en_code_ceasar(el, cod)
            elif el.isupper():
                a = en_code_ceasar(el.lower(), cod)
                res += a.upper()
            else:
                res += el
        else:
            if el.islower():
                res += ru_code_ceasar(el, cod)
            elif el.isupper():
                a = ru_code_ceasar(el.lower(), cod)
                res += a.upper()
            else:
                res += el
    res += ' ' 

print(f'Сообщение зашифровано: {res}')
