import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    answer[a][b] = b
    answer[b][a] = a

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i == j):
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == j):
                continue
            if (graph[i][j] > graph[i][k] + graph[k][j]):
                graph[i][j] = graph[i][k] + graph[k][j]
                answer[i][j] = answer[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (answer[i][j] == 0):
            print('-', end=" ")
        else:
            print(answer[i][j], end=" ")
    print()