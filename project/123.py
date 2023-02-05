matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

for i in matrix:
    for el in i:
        print(el, end=' ')

print([el for i in matrix for el in i])

n = 3
s = '123456789'.split()
a = list(range(1, n**2+1))
# print(a)

