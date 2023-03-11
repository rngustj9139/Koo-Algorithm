import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
maxValue = int(-1e9)
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    if (maxValue <= min(arr[i])):
        maxValue = min(arr[i])

print(maxValue)