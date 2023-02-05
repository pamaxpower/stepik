# def trans_to_num10(n, num):
#     res = ''
#     while num > 0:
#         rest = num % n
#         if rest in range(10, 16):
#             rest = 'ABCDEF'[rest-10]
#         res = str(rest) + res
#         num = num // n
#     return res


# number = int(input('Введите число: '))
# x = int(input('Введите сичтему счисления: '))


# print(trans_to_num10(x, number))


"""
для перевода числа из десятичной системы в другие,
используются встроенные функции:
bin(), oct(), hex()
Они возвращают строковое представление целого 
десятичного числа в соответствующей системе счисления
"""

num = 127

bin_num = bin(num)      # 0b1111111
oct_num = oct(num)      # 0o177
hex_num = hex(num)      # 0x7f

"""
Приставки 0b, 0o, 0x сигнализируют о том, что число представлено 
в двоичной, восьмеричной, шестнадцатиричной системе счисления
"""

# Чтобы избавиться от приставки, можно воспользоваться срезом
print(bin_num[2:])
print(oct_num[2:])
print(hex_num[2:].upper())      # вернет строку с большой буквой

print(type(bin_num))        # класс 'str'
