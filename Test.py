import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
distance = [[INF] * (1 + n) for _ in range(1 + n)]

for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if (i == j):
            distance[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, 1 + n):
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if (distance[i][j] == INF):
            print("INFINITY", end=" ")
        else:
            print(distance[i][j], end=" ")
    print()