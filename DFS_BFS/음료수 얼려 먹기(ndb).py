N, M = map(int, input().split())
graph = []
result = 0
for _ in range(N):
    graph.append(list(map(int, input()))) # input = sys.stdin.readline 쓸경우 에러 발생

def dfs(x, y):
    if (-1 >= x or x >= N or -1 >= y or y >= N):
        return False
    if (graph[x][y] == 0):
        graph[x][y] = 1
        dfs(x - 1, 0)
        dfs(x + 1, 0)
        dfs(0, y - 1)
        dfs(0, y + 1)

        return True

    return False

for i in range(N):
    for j in range(M):
        if (dfs(i, j) == True):
            result += 1

print(result)