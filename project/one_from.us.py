n = int(input())            # кол-во человек   
k = int(input())            # шаг выбывания

lst = list(range(1, n+1))
i = 0
while len(lst) > 1:
    i = (i + k - 1) % (len(lst))
    del lst[i]

print(lst[0])





exit()
def search_one(list1, step):
    res = []
    for i in range(len(list1)):
        if len(list1) == 1:
            return list1
        if i % step != 0:
            res.append(i)

    list1 = res
    print(list1)
    return search_one(list1, step)


print(search_one(lst, k))


