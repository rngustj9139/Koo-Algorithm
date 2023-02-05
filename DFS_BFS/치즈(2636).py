# BFS 이용
# 입력값이 0에서 1로 갔을 때만 체크를 해줘야 한다. 그래야 가장자리 부분만 녹아서 사라지기 때문이다.
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
time = 0
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs():
    cnt = 0
    q = deque()
    visited[0][0] = 1
    q.append((0, 0))

    while (q):
        nowX, nowY = q.popleft()
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if (0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0):
                if (graph[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif (graph[nx][ny] == 1):
                    cnt += 1
                    graph[nx][ny] = 0 # 치즈 녹아 없어지게 하기
                    visited[nx][ny] = 1
    ans.append(cnt)

    return cnt

while (True):
    time += 1
    visited = [[0] * M for _ in range(N)]
    cnt = bfs()
    if (cnt == 0):
        break

print(time - 1)
print(ans[time - 2])