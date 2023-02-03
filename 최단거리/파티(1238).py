# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
# N, M, X = map(int, input().split())
# distance = [[INF] * (N + 1) for _ in range(N + 1)]
# result = -9999
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     distance[a][b] = c
#
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if (i == j):
#             distance[i][j] = 0
#
# for k in range(1, N + 1):
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
#
# for i in range(1, N + 1):
#     if (distance[i][X] + distance[X][i] > result):
#         result = distance[i][X] + distance[X][i]
#
# print(result)

# 플로이드 와샬로 풀 경우 시간초과 발생 => 다익스트라 사용하기
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
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
            if (distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

result = [[]] # 그냥 []로하면 result에는 인덱스 0부터 N - 1까지의 배열들만 들어가게 됨
time_list = []
for i in range(1, N + 1):
    distance = [INF] * (N + 1)
    dijkstra(i)
    result.append(distance)

for i in range(1, N + 1):
    time_list.append(result[i][X] + result[X][i])

print(max(time_list))


















