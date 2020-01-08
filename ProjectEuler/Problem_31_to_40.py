from fractions import Fraction
from functools import reduce


def Problem31():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coinTable = [[1 for _ in range(201)] for _ in range(8)]

    for k in range(1, 8):
        for j in range(201):
            coin = coins[k]
            #print(k, coin)
            if coin > j:
                coinTable[k][j] = coinTable[k-1][j]
            else:
                coinTable[k][j] = coinTable[k-1][j] + coinTable[k][j-coin]
    print(coinTable[-1][-1])


def Problem32():
    res = []
    for k in range(1, 10):
        for j in range(1, 10):
            if j == k: continue
            for i in range(1, 10) :
                if i == j or i == k: continue
                for u in range(1, 10) :
                    if u == i or u == j or u == k: continue
                    for z in range(1, 10) :
                        if z == u or z == i or z == j or z == k: continue
                        n1, n2 = 0, 0 #n1 is 1 * 4 and n2 is 2 * 3:

                        n1 = k * (1000 * j + 100 * i + 10 * u + z)

                        n2 = (10 * k + j) * (100 * i + 10 * u + z)

                        s1 = set([str(k), str(j), str(i), str(u), str(z)])

                        if len(str(n1)) <= 4 and n1 != 0 and len(set(str(n1)) - s1) == 4 and str(n1).count('0') == 0:
                            #print(set(str(n1))- s1)
                            print("n1 : ", n1, k, j, i, u, z)
                            res.append(n1)
                        if len(str(n2)) <= 4 and n2 != 0 and len(set(str(n2)) - s1) == 4 and str(n2).count('0') == 0:
                            print("n2 : ", n2, k, j, i, u, z)
                            res.append(n2)
    print(sum(set(res)))

def Problem33():
    res = []
    for a in range(1, 10):
        for b in range(1, 10):
            if a == b: continue
            for c in range(1, 10):
                if c == a or c == b: continue
                f1 = Fraction(10*a + b, 10*c + a)
                f2 = Fraction(10*a + b, 10*c + b)

                if f1 == Fraction(b, c):
                    res.append(f1)

                if f2 == Fraction(a, c):
                    res.append(f2)

            for d in range(1, 10):
                if d == a or d == b : continue
                f3 = Fraction(10*a + b, 10*d + b) 
                if f3 == Fraction(a, d):
                    res.append(f3)
    print(res)
    print(1/reduce(lambda x, y : x*y, res))

def Problem34():
    sol = []
    factorialList = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    for k in range(1, 2540160):
        res = 0
        temp = str(k)
        for j in temp:
            res += factorialList[int(j)]
        if k == res:
            sol.append(k)
            print(k)

def SeiveOfEratos():
    boolList = [True for _ in range(1000001)]
    boolList[0] = False
    boolList[1] = False
    index = 2
    growth = 2
    
    while(index**2 < len(boolList)):
        if boolList[index + growth] != False:
            boolList[index + growth] = False
        growth += index
        if index + growth >= len(boolList) : 
            index += 1
            growth = index
    
    return boolList

def rotate(num):
    stringNum = str(num)
    returnList = []
    for k in range(len(stringNum)):
        returnList.append(stringNum)
        temp = stringNum[1:]
        stringNum = temp + stringNum[0]
    return returnList

def Problem35():
    primeList = SeiveOfEratos()
    flag = False
    num = 0
    for k in range(3, len(primeList), 2):
        if primeList[k] == True:
            temp = rotate(k)
            for j in temp:
                if primeList[int(j)] != True:
                    flag = False
                    break
                flag = True
            if flag:
                num += 1

    return num+1

def IsPalindromic(temp):
    stack = []
    middle = len(temp)//2

    for j in range(middle):
        stack.append(temp[j])

    if len(temp) % 2 != 0:
        middle += 1

    for j in range(middle, len(temp)):
        if stack[-1] == temp[j]:
            stack.pop()

    return True if len(stack) == 0 else False

def Problem36():
    sum = 0
    for k in range(1, 1000000):
        temp = str(k)
        binTemp = format(k, "b")
        if IsPalindromic(temp) and IsPalindromic(binTemp):
            sum += k

    return sum

def Problem37():
    primes = [2, 3, 5, 7]

    boolList = SeiveOfEratos()
    leftList = []
    rightList = []
    flag = 0
    for k in range(10, 900000):
        if boolList[k]:
            temp = str(k)
            flag += 1
            while True:
                temp = leftShift(str(temp))
                if temp is False or boolList[int(temp)] is False:
                    break

                if len(temp) == 1:
                    leftList.append(k)

            temp = str(k)
            while True:
                temp = rightShift(str(temp))
                if temp is False or boolList[int(temp)] is False:
                    break
                if len(temp) == 1:
                    rightList.append(k)

    leftList = set(leftList)
    rightList = set(rightList)

    return sum(leftList & rightList)


def leftShift(num):
    if len(num) > 1:
        return num[0:-1]
    else:
        return False

def rightShift(num):
    if len(num) > 1:
        return num[1:]
    else:
        return False

def Problem38():
    result = 0
    for k in range(2, 9999):
        if k % 5 == 0: continue
        temp = ""
        for j in range(1, k + 1):
            if j >= 10: break
            temp += str(k*j)
            if len(temp) > 9: break
            if set(list(temp)) == set(list("123456789")):
                if result <= int(temp):
                    result = int(temp)
    return result

if __name__ == "__main__":
    print(Problem38())