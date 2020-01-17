def Hanoi(source, destination, middle, plates): # 11729번
    if plates == 1:
        print(source + " " + destination)
    else:
        Hanoi(source, middle, destination, plates - 1)
        Hanoi(source, destination, middle, 1)
        Hanoi(middle, destination, source, plates - 1)

# firstTower = "1"
# middleTower = "2"
# lastTower = "3"
# num = int(input())
# print(num*2 + 1)
# Hanoi(firstTower, lastTower, middleTower, num)



num = int(input())
mat = [[" " for _ in range(num)] for _ in range(num)]

def solve(n, i, j):
    if n == 1:
        mat[i][j] = "*"
    else:
        div = n // 3
        for k in range(3):
            for q in range(3):
                if k == 1 and q == 1:
                    continue
                solve(div, i + div*k, j + div*q)
    return 

# solve(num, 0, 0)
# for k in mat:
#     string = ""
#     for j in k:
#         string += j
#     print(string)

