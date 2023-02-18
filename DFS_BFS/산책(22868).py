'''
S에서 E로, E에서 S로 BFS를 두번 진행한다.
S에서 E로 진행할 때는 경로를 리턴한다.
E에서 S로 진행할 때는 전체 경로의 길이를 리턴한다.
BFS 함수에서 파라미터는 시작점, 끝점, 방문 체크 배열, 첫번째 BFS인지 두번째 BFS인지 확인할 변수이다.
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 인접 리스트
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
S, E = map(int, input().split())

for i in range(1, N + 1):
    graph[i].sort()

def solve():
    visited = [-1] * (N + 1)  # 방문 체크
    visited[S] = 0 # 1로 할당할 경우 시간초과 발생
    route = bfs(S, E, visited, 0)

    visited = [-1] * (N + 1)
    for idx in route:
        visited[idx] = 1
    cnt = bfs(E, S, visited, len(route))
    print(cnt)

def bfs(start, end, visited, secondRound):
    q = deque()
    q.append((start, secondRound)) # 노드와 몇번째로 거쳐왔는지 cnt 입력

    while (q):
        now, cnt = q.popleft()
        if (now == end):
            if (secondRound == 0):
                break
            else:
                return cnt
        for nxt in graph[now]:
            if (visited[nxt] == -1):
                visited[nxt] = now
                q.append((nxt, cnt + 1))
    route = [end]
    nxt = visited[end]
    while (nxt != 0):
        route.append(nxt)
        nxt = visited[nxt]

    return route[:-1]

solve()
