from math import pow

n = input('Введите систему счисления(2,4,8,16): ')
# if int(n) not in [2, 4, 8, 16]:
#     print('Вы ввели неправильное число')
num = input('Введите число для перевода: ')

def trans_num16(number):
    sum = 0
    exp = len(number) - 1
    for i in number:
        if i in 'ABCDEF':
            i = 'ABCDEF'.find(i) + 10
        sum += int(i) * pow(16, exp)
        exp -= 1
    return int(sum)


def trans_num(a, number):
    s = 0
    j = len(number)-1
    for i in range(len(number)):
        s += int(number[i]) * pow(int(a),j-i)
    return int(s)


if int(n) == 16:
    print(trans_num16(num))
else:
   print(trans_num(n, num))
