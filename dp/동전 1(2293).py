"""
[1 2 3 4 5 6 7 8 9 10] [만들어야하는 금액]
 1 1 1 1 1 1 1 1 1 1   [1원만 쓰는 경우의 수]
 1 2 2 3 3 4 4 5 5 6   [2원 혹은 1원, 혹은 둘다를 같이 쓰는 경우의수]
 ~~~~~~~~~~~~~~~~~~~   [5원 혹은 2원 혹은 1원, 혹은 셋다를 같이 쓰는 경우의수]
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
d = [0] * (k + 1)
for _ in range(n):
    coins.append(int(input()))

d[0] = 1
for i in coins:
    for j in range(i, k + 1):
        if (d[j - i]):
            d[j] = d[j] + d[j - i]

print(d[k])


