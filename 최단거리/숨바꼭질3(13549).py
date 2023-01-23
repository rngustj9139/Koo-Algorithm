# 간선의 가중치가 일정한 경우는 BFS/DFS를 사용하고 아니면 최단거리 알고리즘 사용
# https://www.daleseo.com/python-yield/
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N, K = map(int, input().split())
distance = [INF] * (100001)

def toList(i):
    yield (i - 1, 1)
    yield (i + 1, 1)
    yield (i * 2, 0)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for i in toList(now):
            if (0 <= i[0] and i[0] <= 100000):
                cost = dist + i[1]
                if (cost < distance[i[0]]):
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(N)

print(distance[K])