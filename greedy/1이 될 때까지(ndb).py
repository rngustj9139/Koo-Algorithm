import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0

while (N >= K):
    while (N % K != 0):
        N -= 1
        cnt += 1
    N = N / K
    cnt += 1

while (N > 1):
    N -= 1
    cnt += 1

print(cnt)