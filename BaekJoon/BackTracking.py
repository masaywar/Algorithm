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

#9663
N = 8
stack = []
result = 0

def N_Queen(x, y):
    global result
    if len(stack) == N:
        result += 1
        stack.pop()
        return
    for k in range(N):
        flag = True
        for px, py in stack:
            if k == py or abs(x - px) == abs(k - py):
                flag = False
                break
        if flag:
            stack.append((x, k))
            N_Queen(x + 1, 0)
    if stack:
        stack.pop()

#2580
L = [list(map(int, input().split())) for _ in range(9)]
zero =  [(k, j) for k in range(9) for j in range(9) if L[k][j] == 0]

def CheckRow(x, val):
    if val in L[x]:
        return False
    return True    

def CheckCol(y, val):
    for k in range(9):
        if L[k][y] == val:
            return False
    return True

def CheckSquare(x, y, val):
    sx = x // 3 * 3
    sy = y // 3 * 3
    for k in range(3):
        for j in range(3):
            if L[k + sx][j + sy] == val:
                return False
    return True

def Sudoku(count):
    if count == len(zero):
        for k in L:
            for j in k:
                print(j, end=" ")
            print()
        sys.exit(0)
    for k in range(1, 10):
        x, y = zero[count][0], zero[count][1]
        if CheckRow(x, k) and CheckCol(y, k) and CheckSquare(x, y, k):
            L[x][y] = k
            Sudoku(count + 1)
            L[x][y] = 0

# Sudoku(0)

import math

#14888
N = int(input())
L = list(map(int, input().split()))
plus, minus, mult, divide = map(int, input().split())
maxVal, minVal = -math.inf, math.inf
def Op(cur, plus, minus, mult, divide, count):
    global maxVal, minVal
    if count == N:
        maxVal = max(maxVal, cur)
        minVal = min(minVal, cur)
        return
    if plus > 0 :
        Op(cur + L[count], plus-1, minus, mult, divide, count+1) 
    if minus > 0 : 
        Op(cur - L[count], plus, minus-1, mult, divide, count+1) 
    if mult > 0 :
        Op(cur * L[count], plus, minus, mult-1, divide, count+1) 
    if divide > 0 : 
        Op(cur // L[count] if cur > 0 else - (abs(cur) // L[count]), plus, minus, mult, divide-1, count+1) 

# Op(L[0], plus, minus, mult, divide, 1)
# print(maxVal)
# print(minVal)

#14889
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
stack = []
minVal = math.inf
def StartLink(x):
    global minVal
    if len(stack) == N // 2:
        start, link = 0, 0
        rest = [x for x in range(N) if x not in stack]
        for k in stack:
            for j in stack:
                if k == j: continue
                start += L[k][j]
        for k in rest:
            for j in rest:
                if k == j: continue
                link += L[k][j]
        minVal = min(minVal, abs(start - link))
        return
    for k in range(x, N):
        stack.append(k)
        StartLink(k + 1)
        stack.pop()

StartLink(0)
print(minVal)