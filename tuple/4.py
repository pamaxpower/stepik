"""
Алгоритм поиска чисел Фибоначчи с помощью кортежа
"""

n = int(input())
f1, f2 = 1, 1
fib = []
for i in range(n):
    fib.append(f1)
    f1, f2 = f2, f1 + f2

print(f'Последовательность Фибоначчи для {n} чисел: {fib}')

# Алгоритм поиска чисел Трибоначчи с помощью кортежа
# Трибоначчи - последовательность, при которой какждый последующий член равен сумме трех предыдущих 

f1, f2, f3 = 1, 1, 1
trib = []
for i in range(n):
    trib.append(f1)
    f1, f2, f3 = f2, f3, f1+f2+f3

print(f'Последовательность Трибоначчи для {n} чисел: {trib}')
