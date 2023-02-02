from collections import deque

N, M = map(int, input().split())
graph = []
visit = [[False] * (M + 1) for _ in range(N + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    graph.append(list(map(int, input()))) # input = sys.stdin.readline 쓸경우 에러 발생

def bfs(x, y):
    q = deque()
    visit[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (-1 >= nx or nx >= N or -1 >= ny or ny >= M):
                continue
            if (visit[nx][ny] == True):
                continue
            if (graph[nx][ny] == 0):
                continue
            if (graph[nx][ny] == 1):
                visit[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)

print(graph[N - 1][M - 1])