# 15649

N, M = map(int, input().split())
L = [str(x) for x in range(1, N+1)]

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

f2(L, 0, M, "")