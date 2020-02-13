
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
    for _ in range(int(input())):
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

#1904
def dp1():
    N = int(input())
    L = [0] * N
    L[0], L[1] = 1, 2
    if N <= 2:
        print(L[N-1])
        return
    for k in range(2, N):
        L[k] = (L[k-1] + L[k-2]) % 15746

    print(L[-1])

#9461
def dp2():
    for _ in range(int(input())):
        N = int(input())
        if N <= 3:
            print(1)
            continue
        L = [0] * N
        L[0], L[1], L[2] = 1, 1, 1
        for k in range(3, N):
            L[k] = L[k-2] + L[k-3]
        print(L[-1])

import math
import sys

input = sys.stdin.readline

#1149
def dp3():
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(N + 1) ] 
    L = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1, N + 1):
        dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + L[k-1][0]
        dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + L[k-1][1]
        dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + L[k-1][2]
    
    print(min(dp[N][0], dp[N][1], dp[N][2]))

#1932
def dp4():
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    if N <= 1:
        print(L[-1])
        return 

    dp = L.copy()

    for k in range(1, N):
        dp[k][0] = dp[k-1][0] + L[k][0]
        dp[k][-1] = dp[k-1][-1] + L[k][-1]

        if k == 1:
            continue

        for j in range(1, len(L[k])-1):
            dp[k][j] = max(dp[k-1][j], dp[k-1][j-1]) + L[k][j]

    print(max(dp))

#2579
def dp5():
    N = int(input())
    L = [int(input()) for _ in range(N)]
    dp = [0 for _ in range(N+1)]
    dp[1], dp[2] = L[0], L[0] + L[1] 
    for k in range(3, N+1):
        dp[k] = max(dp[k-2] + L[k-1], dp[k-3] + L[k-2] + L[k-1])
    print(dp)
    print(dp[-1])

#1463
def dp6():
    N = int(input())
    L = [0 for _ in range(N + 1)]
    if N == 1: 
        print(0)
        return
    if N == 2 or N == 3:
        print(1)
        return
    L[0], L[1], L[2], L[3] = 0, 0, 1, 1
    for k in range(4, N+1):
        if k % 3 == 0:
            L[k] = min(L[k-1] + 1, L[k//3] + 1)
        elif k % 2 == 0:
            L[k] = min(L[k-1] + 1, L[k//2] + 1)
        else:
            L[k] = L[k-1] + 1
    print(L[-1])

#10844
def dp7():
    N = int(input())
    dp = [[0 for _ in range(10)] for _ in range(N + 1)]
    for k in range(1, 10):
        dp[1][k] = 1

    if N == 1:
        print(9)
        return 

    for k in range(2, N+1):
        dp[k][0], dp[k][9] = dp[k-1][1], dp[k-1][8]
        for j in range(1, 9): 
            dp[k][j] = (dp[k-1][j-1] + dp[k-1][j+1])
    
    print(sum(dp[-1]) % 1000000000)

#2156
def dp8():
    N = int(input())
    L = [int(input()) for _ in range(N)]

    if N <= 2:
        print(L[0]) if N == 1 else print(L[0] + L[1]) 
        return

    dp = [0 for _ in range(N + 1)]
    dp[1], dp[2] = L[0], L[0] + L[1]
    for k in range(3, N + 1):
        dp[k] = max(dp[k-2] + L[k-1], dp[k-3] + L[k-2] + L[k-1])
        dp[k] = max(dp[k], dp[k-1])
    print(max(dp))
    print(dp)

#11053
def dp9():
    N = int(input())
    L = list(map(int, input().split()))
    
dp9()