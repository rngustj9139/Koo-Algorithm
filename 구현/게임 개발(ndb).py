import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
worldVisitCheck = [[0] * n for _ in range(m)]
worldVisitCheck[x][y] = 1
world = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
timeToTurn = 0
cnt = 1
for _ in range(n):
    world.append(list(map(int, input().split())))

def turnLeft():
    global d
    d -= 1
    if (d == -1):
        d = 3

while (True):
    turnLeft()
    timeToTurn += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if (world[nx][ny] == 0 and worldVisitCheck[nx][ny] == 0):
        x = nx
        y = ny
        worldVisitCheck[x][y] = 1
        cnt += 1
        timeToTurn = 0
        continue
    else:
        timeToTurn += 1
    if (timeToTurn == 4):
        nx = x - dx[d]
        ny = y - dy[d]
        if (world[nx][ny] == 0):
            x = nx
            y = ny
            continue
        else:
            break
        timeToTurn = 0

print(cnt)






