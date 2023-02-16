import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

A.sort()
B.sort(reverse=True)

for i in range(K):
    if (A[i] < B[i]):
        A[i], B[i] = B[i], A[i]

for i in A:
    result += i

print(result)