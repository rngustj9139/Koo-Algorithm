def turn(C):
    global direction
    if (C == 'D'): # 오른쪽으로 90도 회전
        direction = (direction + 1) % 4
    if (C == 'L'): # 왼쪽으로 90도 회전
        direction = (direction - 1) % 4

N = int(input()) # 가장자리 벽을 제외한 맵의 크기
K = int(input()) # 사과의 갯수
data = [[0] * (N + 1) for _ in range(N + 1)] # 사과가 위치한 맵 데이터 0이면 사과 없음, 1이면 사과 있음
for _ in range(K):
    a, b = map(int, input().split())
    data[a][b] = 1
L = int(input()) # 방향 전환 정보 갯수
info = [] # 방향 전환 정보 (시간, 방향)
for _ in range(L):
    X, C = input().split()
    info.append((int(X), C)) # 시간 순서 오름차순대로 입력 시간은 양의 정수(1초 부터 시작)

dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0] # 동 남 서 북
direction = 0 # 처음에는 동쪽을 바라봄
x, y = 1, 1
data[1][1] = 2 # 몸통이 존재하는 위치는 2로 표시
time = 0 # 시간 정보
q = [(x, y)]
idx = 0

while (True):
    nx = x + dx[direction]
    ny = y + dy[direction]

    if (1 <= nx and nx <= N and 1 <= ny and ny <= N and data[nx][ny] != 2):
        if (data[nx][ny] == 0): # 이동할 위치에 사과가 없으면 (머리가 그 위치로 이동하고 꼬리는 사라짐)
            data[nx][ny] = 2
            q.append((nx, ny))
            preX, preY = q.pop(0)
            data[preX][preY] = 0
        if (data[nx][ny] == 1): # 이동할 위치에 사과가 있으면 (머리가 그 위치로 이동하고 꼬리는 그대로 남는다)
            data[nx][ny] = 2
            q.append((nx, ny))
    else:
        time += 1
        break

    x, y = nx, ny
    time += 1

    if (idx < L and info[idx][0] == time): # 방향 전환할 시간이 된다면
        turn(info[idx][1]) # 방향 전환
        idx += 1

print(time)