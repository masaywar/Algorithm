import sys

def Sorting_1(): # 2750
    size = int(input())
    unsortedList = [int(input()) for _ in range(size)]
    for k in range(1, size):
        for j in range(k, 0, -1):
            if unsortedList[j] <= unsortedList[j-1]:
                unsortedList[j], unsortedList[j-1] = unsortedList[j-1], unsortedList[j]
            else: break
    for k in unsortedList:
        print(k)

def Sorting_2(): #2751
    size = int(input())
    unsortedList = [int(input()) for _ in range(size)]
    result = Sort(unsortedList)
    for k in result:
        print(k)

def Sort(L):
    if len(L) == 1:
        return L
    else:
        return Merge(Sort(L[0:len(L)//2]), Sort(L[len(L)//2:]))

def Merge(L1, L2):
    L1Count = 0
    L2Count = 0
    returnList = []
    while True:
        if L1Count == len(L1) or L2Count == len(L2):
            break
        
        if L1[L1Count] >= L2[L2Count]:
            returnList.append(L2[L2Count])
            L2Count += 1
        else:
            returnList.append(L1[L1Count])
            L1Count += 1
    
    for k in range(L1Count, len(L1)):
        returnList.append(L1[k])

    for k in range(L2Count, len(L2)):
        returnList.append(L2[k])

    return returnList

# 10989
def Sorting_3():
    size = int(sys.stdin.readline())
    table = [0 for _ in range(10001)]
    
    for _ in range(0, size):
        table[int(sys.stdin.readline())] += 1
    
    count = 0
    index = 0
    while count < size:
        if table[index] != 0:
            count += table[index]
            for k in range(table[index]):
                print(index)
        index += 1

from functools import reduce

# 2108
def Statistics():
    size = int(sys.stdin.readline())
    L = [int(sys.stdin.readline()) for _ in range(size)]
    temp = dict()
    for k in L:
        if k not in temp:
            temp[k] = 1
        else:
            temp[k] += 1
    print(round(reduce(lambda x, y : x + y, L) / size))
    L.sort()
    print(L[len(L)//2])

    maxVal = max(temp.values())
    _key = []

    for key in temp.keys():
        if maxVal == temp[key]:
            _key.append(key)
    
    _key.sort()
    if len(_key) > 1:
        print(_key[1])
    else:
        print(_key[0])

    print(L[-1] - L[0])

# 1427
def SortInside():
    num = input()
    num = sorted(num)
    num.reverse()
    stringBuilder = ""
    for k in num:
        stringBuilder += k
    print(stringBuilder)

#11650
def CoordinateSorting():
    size = int(sys.stdin.readline())
    L = [tuple(map(int, sys.stdin.readline().split())) for _ in range(size)]
    temp = dict()
    def _Bucket(index):
        for k in L:
            if k[index] not in temp:
                temp[k[index]] = [k]
            else:
                temp[k[index]].append(k)

    def _Listing():
        count = 0
        for k in sorted(temp.keys()):
            if len(temp[k]) > 1:
                for j in temp[k]:    
                    L[count] = j
                    count += 1
            else:
                L[count] = temp[k][0]
                count += 1
    _Bucket(1)
    _Listing()
    temp.clear()
    _Bucket(0)
    _Listing()
    
    for k in L:
        strBuilder = ""
        for j in k:
            strBuilder += str(j) + " "
        print(strBuilder)

#11651
def CoordinateSorting_2():
    size = int(sys.stdin.readline())
    L = [tuple(map(int, sys.stdin.readline().split())) for _ in range(size)]
    temp = dict()
    def _Bucket(index):
        for k in L:
            if k[index] not in temp:
                temp[k[index]] = [k]
            else:
                temp[k[index]].append(k)

    def _Listing():
        count = 0
        for k in sorted(temp.keys()):
            if len(temp[k]) > 1:
                for j in temp[k]:    
                    L[count] = j
                    count += 1
            else:
                L[count] = temp[k][0]
                count += 1
    _Bucket(0)
    _Listing()
    temp.clear()
    _Bucket(1)
    _Listing()
    
    for k in L:
        strBuilder = ""
        for j in k:
            strBuilder += str(j) + " "
        print(strBuilder)

CoordinateSorting_2()
