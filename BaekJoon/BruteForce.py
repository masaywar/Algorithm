import sys

def BlackJack(): # 2798
    cards, maxNum = map(int, sys.stdin.readline().split())
    cardList = sorted(list(map(int, sys.stdin.readline().split())))

    closeToMax = 0
    for k in range(len(cardList) - 2):
        for j in range(k + 1, len(cardList) - 1):
            for q in range(j + 1, len(cardList)):
                sumsum = cardList[k] + cardList[j] + cardList[q]
                if closeToMax <= sumsum and sumsum <= maxNum:
                    closeToMax = sumsum

    print(closeToMax)

def DecompositionSum(): # 2231
    decomposedNum = int(input())
    for k in range(decomposedNum // 2, decomposedNum):
        if sum([int(x) for x in str(k)]) + k == decomposedNum: 
            print(k)
            return
    print(0)

def CheckBig(): # 7568
    students = int(input())
    studentList = [tuple(map(int, input().split())) for _ in range(students)]

    for k in range(students):
        ranking = 1
        for j in range(students):
            if k == j: continue
            if studentList[k][0] < studentList[j][0] and studentList[k][1] < studentList[j][1]:
                ranking += 1
        print(ranking, end=" ")

def ChessPaint(): # 1018
    col, row = map(int, input().split())

    whiteFirstPaintBoard = [[] for _ in range(col)]
    blackFirstPaintBoard = [[] for _ in range(col)]

    b = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"
    w = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
    count = 0
    for k in range(64):
        if k != 0 and k % 8 == 0:
            count += 1
        whiteFirstPaintBoard[count].append(w[k])
        blackFirstPaintBoard[count].append(b[k])

    userBoard = []
    for _ in range(col):
        userBoard.append(list(sys.stdin.readline()[:-1]))
   
    tempBoard = []
    result = col * row
    for k in range(col - 7):
        count = 0
        for j in range(row - 7):
            for q in range(8):
                tempBoard.append(userBoard[k + q][j:j + 8])
            A = CheckDiff(tempBoard, whiteFirstPaintBoard)
            B = CheckDiff(tempBoard, blackFirstPaintBoard)
            if result > min(A, B):
                result = min(A, B)
            tempBoard.clear()
        count += 1

    print(result)

def CheckDiff(boardA, boardB):
    res = 0
    for k in range(8):
        for j in range(8):
            if boardA[k][j] != boardB[k][j]:
                res += 1
    return res

def DirectorShom(): # 1436
    apocalypseNum = 666
    index = int(input())
    temp = 0
    count = 1
    while index != count:
        for k in range(apocalypseNum + 1, 1000000000):
            if index == count : 
                temp += 1
                break
            
            sixCount = 0
            for j in str(k):
                if j == "6":
                    sixCount += 1
                    if sixCount == 3:
                        apocalypseNum = k
                        count += 1
                        break
                else:
                    sixCount = 0

    print(apocalypseNum)

DirectorShom()