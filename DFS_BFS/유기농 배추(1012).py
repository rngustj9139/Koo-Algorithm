from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))

    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and graph[nx][ny] == 1):
                visited[nx][ny] = True
                q.append((nx, ny))

T = int(input())
while (T > 0):
    T -= 1
    M, N, K = map(int, input().split())
    graph = [[0] * (51) for _ in range(51)]
    visited = [[False] * (51) for _ in range(51)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):
        for j in range(M):
            if (visited[i][j] == False and graph[i][j] == 1):
                bfs(i, j)
                cnt += 1

    print(cnt)