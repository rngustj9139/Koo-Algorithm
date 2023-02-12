'''
이동하는 대상인 지훈이(J)와 불(F)의 위치를 큐에 넣고 BFS를 진행한다. 그리고 지훈이의 탈출 시간을 출력해야 하므로 큐에는 위치와 함께 시간 정보도 넣어준다. (불의 시간은 고려 대상 X → -1로 넣어줌)
또, 주어진 예제만 봐도 한 타임에 지훈이가 불보다 먼저 이동해야 하는 건 쉽게 캐치할 수 있다.
그럼 같은 큐에 들어가는 지훈이와 불의 이동 순서를 어떻게 정해줄 수 있을까? 처음엔 우선순위 큐를 써야 하나 싶었다.
근데 조금만 생각해보니 가장 처음에 지훈이를 큐에 넣어주기만 하면 이후 타임에 계속 지훈이가 먼저 이동하게 되는 것을 알 수 있었다.
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
ans = "IMPOSSIBLE"
dx = [-1, 1, 0, 1]
dy = [0, 0, -1, 1]
q = deque()

for i in range(n):
    graph.append(list(input().rstrip())) # 그냥 list(input())을 넣게 되면 맨 오른쪽에 개행이 딸려 붙는다.
    if ('J' in graph[i]):
        q.append((0, i, graph[i].index('J')))

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 'F'):
            q.append((-1, i, j))

while (q):
    time, x, y = q.popleft()

    # 지훈이의 미로 탈출
    if (time > -1 and (x == 0 or x == n - 1 or y == 0 or y == m - 1) and graph[x][y] != 'F'):
        ans = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ((0 <= nx < n and 0 <= ny < m) and graph[nx][ny] != '#'):
            # 미로 속 지훈이 이동
            if (time > -1 and graph[nx][ny] == '.'):
                graph[nx][ny] = '_'
                q.append((time + 1, nx, ny))

            # 미로 속 불길 이동
            elif (time == -1 and graph[nx][ny] != 'F'):
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)
