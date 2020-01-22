import sys

input = sys.stdin.readline
# 15649
def f(L,count, M, res):
    if count == M:
        for k in res:
            print(k, end=" ")
        print()
        return 

    for k in range(len(L)):
        res += L[k]
        f(L[:k] + L[k+1:], count + 1, M, res)
        res = res[:-1]

# 15650
def f2(L, count, M, res):
    if count == M:
        for k in res:
            print(k, end=" ")
        print()
        return
    for k in range(len(L)):
        res += L[k]
        f2(L[k+1:], count + 1, M, res)
        res = res[:-1]

# 15651
def f3(L, count, M, res):
    if count == M:
        for k in res:
            print(k, end=" ")
        print()
        return
    for k in range(len(L)):
        res += L[k]
        f3(L, count + 1, M, res)
        res = res[:-1]

# 15652
def f4(L, count, M, res):
    if count == M:
        for k in res:
            print(k, end=" ")
        print()
        return
    for k in range(len(L)):
        if len(res) == 0 or int(L[k]) >= int(res[-1]):
            res += L[k]
            f4(L, count + 1, M, res)
            res = res[:-1]

# 9663
def N_Queen():
    pass

# 2580
L = [list(map(int, input().split())) for _ in range(9)]
rowSet = [set() for _ in range(9)]
colSet = [set() for _ in range(9)]
squareSet = [set() for _ in range(9)]

for k in range(9):
    for j in range(9):
        if L[k][j] != 0:
            rowSet[k].add(L[k][j])
            colSet[k].add(L[k][j])
            squareSet[k // 3 * 3 + j // 3].add(L[k][j])

for k in squareSet:
    print(k)

