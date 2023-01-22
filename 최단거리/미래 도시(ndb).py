import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
distance = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1
x, k = map(int, input().split())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if (a == b):
            distance[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

if (distance[k][x] == INF or distance[1][k] == INF):
    print(-1)
else:
    print(distance[1][k] + distance[k][x])