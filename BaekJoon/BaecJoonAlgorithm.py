#1000번과 1001번은 넘모 쉬우니 Pass
import sys

def Turret(): #1002
    test = int(input())
    while test > 0:
        test -= 1
        x1, y1, r1, x2, y2, r2, = map(int, input().split(" "))
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        if distance == 0 and r1 == r2:
            print(-1)
        elif distance == r1 + r2 or distance == abs(r1 - r2):
            print(1)
        elif distance >= r1 + r2 or r1 >= distance + r2 or r2 >= r1 + distance:
            print(0)
        else:
            print(2)

#Turret()
def Fibonaccci(): #1003
    test = int(input())
    while test > 0:
        dp = []
        test -= 1
        fibo = int(input())
        if fibo == 0: print(dp[0][0], dp[0][1])
        elif fibo == 1: print(dp[1][0], dp[1][1])
        else:
            for k in range(2, fibo + 1):
                dp.append((dp[k-1][0] + dp[k-2][0], dp[k-1][1] + dp[k-2][1]))
            print(dp[fibo][0], dp[fibo][1])

#Fibonaccci()

def LittlePrince(): #1004
    test = int(input())
    while(test > 0):
        test -= 1
        x1, y1, x2, y2 = map(int, input().split(" "))
        planets = [None for _ in range(int(input()))]

        for k in range(len(planets)):
            planets[k] = list(map(int, input().split(" ")))

        inside_1, inside_2 = 0, 0

        for k in planets:
            dist_1, dist_2 = (x1 - k[0])**2 + (y1 - k[1])**2, (x2 - k[0])**2 + (y2 - k[1])**2
            if dist_1 < k[2]**2:
                if dist_2 >= k[2]**2:
                    inside_1 += 1
            elif dist_2 < k[2] ** 2:
                if dist_1 >= k[2] ** 2:
                    inside_2 += 1

        print(inside_1 + inside_2)

#LittlePrince()

def ACMCraft(): #1005
    for _ in range(int(sys.stdin.readline())):
        numOfNodes, numOfEdges = map(int, sys.stdin.readline().split())
        graph = {key : [] for key in range(1, numOfNodes + 1)}
        data = [0]
        data.extend(list(map(int, sys.stdin.readline().split())))
        indegree = [0 for _ in range(numOfNodes + 1)]

        for k in range(1, numOfEdges + 1):
            node1, node2 = map(int, sys.stdin.readline().split())
            graph[node1].append(node2)
            indegree[node2] += 1
        destination = int(sys.stdin.readline())
        TopologySort(graph, indegree, data, destination)

def TopologySort(graph, indegree, data, destination):
    queue = []
    result = data.copy()
    for k in range(1, len(graph) + 1):
        if indegree[k] == 0:
            queue.append(k)
    while queue:
        cur = queue.pop(0)
        for k in graph[cur]:
            indegree[k] -= 1
            result[k] = max(result[k], result[cur] + data[k])
            if indegree[k] == 0:
                queue.append(k)
    print(result[destination])
# ACMCraft()

def BallEscape():
    col, row = map(int, sys.stdin.readline().split())
    R, B, O = [], [], []
    board = []
    for k in range(col):
        board.append(list(sys.stdin.readline()))
        board[k].pop()
        for j in range(row):
            if board[k][j] == 'R':
                R.append(k)
                R.append(j)
            elif board[k][j] == 'B':
                B.append(k)
                B.append(j)
            elif board[k][j] == 'O':
                O.append(k)
                O.append(j)
    for k in board:
        print(k)
    print(R, B, O)
    MoveRight(board, R, B, O)
    print(R, B, O)

def MoveLeft(board, r, b, o):
    while board[r[0]][r[1] - 1] != "#":
        r[1] -= 1
        if r[0] == b[0] and r[1] == b[1]:
            r[1] += 1
            break
        if r[0] == o[0] and r[1] == o[1] :
            print("Goal")
            break
    while board[b[0]][b[1] - 1] != "#":
        b[1] -= 1
        if r[0] == b[0] and r[1] == b[1]:
            b[1] += 1
            break

def MoveRight(board, r, b, o):
    while board[r[0]][r[1] + 1] != "#" :
        r[1] += 1
        if r[0] == b[0] and r[1] == b[1]:
            r[1] -= 1
            break
        if r[0] == o[0] and r[1] == o[1] :
            print("Goal")
            break
    while board[b[0]][b[1] + 1] != "#" :
        b[1] += 1
        if r[0] == b[0] and r[1] == b[1] :
            b[1] -= 1
            break

def MoveUp(board, r, b, o):
    while board[r[0] - 1][r[1]] != "#" :
        r[0] -= 1
        if r[0] == b[0] and r[1] == b[1]:
            r[0] += 1
            break
        if r[0] == o[0] and r[1] == o[1] :
            print("Goal")
            break
    while board[b[0] - 1][b[1]] != "#":
        b[0] -= 1
        if r[0] == b[0] and r[1] == b[1] :
            b[0] += 1
            break

def MoveDown(board, r, b, o):
    while board[r[0] + 1][r[1]] != "#" :
        r[0] += 1
        if r[0] == b[0] and r[1] == b[1] :
            r[0] -= 1
            break
        if r[0] == o[0] and r[1] == o[1]:
            print("Goal")
            break
    while board[b[0] + 1][b[1] - 1] != "#" :
        b[0] += 1
        if r[0] == b[0] and r[1] == b[1]:
            b[1] -= 1
            break
BallEscape()