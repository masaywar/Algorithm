def Hanoi(source, destination, middle, plates): # 11729번
    if plates == 1:
        print(source + " " + destination)
    else:
        Hanoi(source, middle, destination, plates - 1)
        Hanoi(source, destination, middle, 1)
        Hanoi(middle, destination, source, plates - 1)

firstTower = "1"
middleTower = "2"
lastTower = "3"
num = int(input())
print(num*2 + 1)
Hanoi(firstTower, lastTower, middleTower, num)