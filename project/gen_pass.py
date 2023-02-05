from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

ans_yes = ['д', 'да', 'lf', 'y', 'yes']

chars = ''

count_pass = int(input('Введите количество паролей: '))
length_pass = int(input('Введите длину пароля: '))
q1 = input('Использовать ли в пароле цифры? ')
if q1 in ans_yes:
    chars += digits
q2 = input('Использовать ли в пароле прописные буквы? ')
if q2 in ans_yes:
    chars += lowercase_letters
q3 = input('Использовать ли в пароле строчные буквы? ')
if q3 in ans_yes:
    chars += uppercase_letters
q4 = input('Использовать ли в пароле символы? ')
if q4 in ans_yes:
    chars += punctuation
# q5 = input('Использовать ли в пароле похожие символы?\t')
# if q5 in ans_yes:
#     for el in 'il1Lo0O':
#         chars = chars.replace(el, '')
    

def generate_password(lst, value):
    return ''.join(sample(lst,value))


for i in range(count_pass):
    print(generate_password(chars, length_pass))






























exit()
def valid_que():
    n = input()
    if n in ans_yes:
        return n
    elif n in ans_no:
        return n
    else:
        print('Нужен ответ "да" или "нет"')
        valid_que()
    



que = ['цифры', 'прописные буквы', 'строчные буквы', 'символы', 'похожие символы']
lst_ans = []
for i in range(len(que)):
    print(f'Использовать ли в пароле {que[i]}?\t')
    lst_ans.append(valid_que())

print(lst_ans)

    




