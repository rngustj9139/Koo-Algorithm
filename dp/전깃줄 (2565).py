# https://yabmoons.tistory.com/572 참고

import sys
input = sys.stdin.readline

n = int(input())
wireList = []
dp = [1] * n

for _ in range(n):
    wireList.append(list(map(int, input().split())))

wireList.sort(key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if (wireList[j][1] < wireList[i][1]):
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
