from itertools import combinations
import sys
input = sys.stdin.readline

def get_sum_chicken_distance(candidate):
    result = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        result += tmp

    return result

house = []
chicken = []
N, M = map(int, input().split())
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if (data[j] == 1): # 집이면
            house.append((i, j))
        if (data[j] == 2): # 치킨집이면
            chicken.append((i, j))

candidates = list(combinations(chicken, M))
# print(candidates)

result = 1e9
for candidate in candidates:
    result = min(result, get_sum_chicken_distance(candidate))

print(result)