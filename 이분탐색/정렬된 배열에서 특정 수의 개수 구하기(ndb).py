import sys
input = sys.stdin.readline

N, x = map(int, input().split())
numberList = list(map(int, input().split()))
cnt = 0

numberList.sort()
start = 0
end = N - 1
mid = (start + end) // 2

while (start <= end):
    mid = (start + end) // 2

    if (numberList[mid] == x):
        cnt += 1
        del numberList[mid]
    elif (numberList[mid] < x):
        start = mid + 1
    elif (numberList[mid] > x):
        end = mid - 1

if (cnt == 0):
    print(-1)
else:
    print(cnt)



