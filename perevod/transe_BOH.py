"""
Функция перевода числа из десятичной системы
BOH = Binary, Octal, Hex
"""

def transe_boh(num):
    print(bin(num)[2:])
    print(oct(num)[2:])
    print(hex(num)[2:].upper())

number = int(input())

transe_boh(number)