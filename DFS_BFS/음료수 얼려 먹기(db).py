import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
result = 0
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if (-1 >= x and x >= N and -1 >= y and y >= N):
        return False
    if (graph[x][y] == 0):
        graph[x][y] == 1
        dfs(x - 1, 0)
        dfs(x + 1, 0)
        dfs(y - 1, 0)
        dfs(y + 1, 0)

        return True

    return False

for i in range(N):
    for j in range(M):
        if (dfs(i, j) == True):
            result += 1

print(result)