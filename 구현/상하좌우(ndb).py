import sys
input = sys.stdin.readline

N = int(input())
moveToList = list(map(str, input().split()))

x, y = 1, 1
# 상하좌우 순서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveToString = ['U', 'D', 'L', 'R']

for i in moveToList:
    for j in range(len(moveToString)):
        if (i == moveToString[j]):
            nx = x + dx[j]
            ny = y + dy[j]
    if (nx < 1 or nx > N or ny < 1 or ny > N):
        continue
    else:
        x, y = nx, ny

print(y, x)

