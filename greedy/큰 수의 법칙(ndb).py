'''
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort(reverse=True)

for _ in range(M):
    if (cnt < K):
        result += arr[0]
        cnt += 1
    else:
        cnt = 0
        result += arr[1]

print(result)
'''

#시간 복잡도를 고려한 풀이
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort(reverse=True)
first = arr[0]
second = arr[1]

cnt = int(M / (K + 1)) * K
cnt += int(M % (K + 1))

result += (cnt * first)
result += ((M - cnt) * second)

print(result)