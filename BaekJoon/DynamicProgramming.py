
# 2748
#N = int(input())
a, b= 0, 1
def fib1(N):
    for _ in range(N):
        a, b = b, a + b
# print(a)

# 1003
L = [(1, 0), (0, 1)]
def fib2():
    for k in range(int(input())):
        n = int(input())
        if n < 2:
            print(L[n][0], L[n][-1])
        elif len(L) > n:
            temp = (L[n-2][0] + L[n-2][1], L[n-1][0] + L[n-1][1])
            print(temp[0], temp[1])
        else:
            while len(L) <= n:
                L.append((L[-2][0] + L[-2][1], L[-1][0] + L[-1][1]))
            print(L[-1][0], L[-1][1])

