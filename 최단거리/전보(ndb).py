import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, start = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if (cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

totalCity = 0
maxTime = -9999
for i in distance:
    if (i != INF):
        totalCity += 1
        maxTime = max(maxTime, i)
print(totalCity - 1, maxTime) # 시작 노드는 제외해야 하므로 -1
