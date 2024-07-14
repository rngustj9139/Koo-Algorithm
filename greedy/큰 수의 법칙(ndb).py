'''
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True) # 내림차순
mCnt = 0
kCnt = 0
result = 0

while (mCnt < M):
    mCnt += 1
    kCnt += 1

    if (kCnt <= K):
        result += numbers[0]
    else:
        result += numbers[1]
        kCnt = 0

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