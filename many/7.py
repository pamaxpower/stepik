m = int(input('Уроки: '))
myset = set()
for i in range(m):
    for el in range(int(input('Кол-во: '))):
        el = input()
        if el not in myset:
            myset.add(el)
        else:
            myset.discard(el)
print(*sorted(myset))