import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort()

for i in range(0, N - 1):
    for j in range(i + 1, N):
        if (arr[i] == arr[j]):
            continue
        else:
            result += 1

print(result)

