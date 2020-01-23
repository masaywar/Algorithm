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

N = 8
result = 0
stack = []
def N_Queen(x, y, count):
    global result
    if count == N:
        result += 1
        stack.pop()
        return
    for k in range(N):
        flag = True
        for postX, postY in stack:
            if postY == k or abs(postX - x) == abs(postY - k):
                flag = False
                break

        if flag:
            stack.append((x, k))
            N_Queen(x + 1, 0, count + 1)
    if stack:
        stack.pop()

# 2580
L = [list(map(int, input().split())) for _ in range(9)]
zero = [(k, j) for k in range(len(L)) for j in range(len(L)) if L[k][j] == 0] 

def CheckRow(x, val):
    if val in L[x]:
        return False
    return True

def CheckCol(y, val):
    for k in range(0, 9):
        if L[k][y] == val:
            return False
    return True

def CheckSquare(x, y, val):
    a = x // 3 * 3
    b = y // 3 * 3
    for k in range(3):
        for j in range(3):
            if L[a + k][b + j] == val:
                return False
    return True

def Sudoku(count):
    if count == len(zero):
        for k in L:
            for j in k:
                print(j, end=" ")
            print()
        sys.exit(0)
    else:
        for k in range(1, 10):
            x, y = zero[count][0], zero[count][1]
            if CheckRow(x, k) and CheckCol(y, k) and CheckSquare(x, y, k):
                L[x][y] = k
                Sudoku(count + 1)
                L[x][y] = 0

Sudoku(0)