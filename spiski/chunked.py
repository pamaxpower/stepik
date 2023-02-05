"""
Разбиение на чанки (куски)
"""


def chunked(lst, n):
    res = []
    for i in range(0, len(lst), n):
        list1 = []
        for j in range(n):
            if (i+j) < len(lst):
                list1.append(lst[j+i])
            else:
                continue
        res.append(list1)
    return res


def chunked2(lst, n):
    return [lst[i:i + n] for i in range(0,len(lst),n)]

#s = input().split()
s = 'a b c d e f g h i j k l m n'.split()
num = 3 #int(input())
print(chunked(s, num))
#print(chunked2(s, num))


""".
Сделать подсписки списка:
Input:      a b v
Output:     [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]
"""

# res_lst = []
# for i in range(len(s)):
#     for j in range(len(s) - i):
#         (print(i, j))
#         print(s[j:j+i+1])
#         res_lst.append(s[j:j+i+1])
# res_lst.insert(0, [])
# print(res_lst)
