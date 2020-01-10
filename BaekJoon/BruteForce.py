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
