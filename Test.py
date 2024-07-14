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
