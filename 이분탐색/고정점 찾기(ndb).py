import sys
input = sys.stdin.readline

N = int(input())
numberList = list(map(int, input().split()))

numberList.sort()
startIndex = 0
endIndex = N - 1
findCheck = True

while (startIndex <= endIndex):
    mid = (startIndex + endIndex) // 2

    if (numberList[mid] == mid):
        print(mid)
        findCheck = False
        break
    elif (numberList[mid] < mid):
        startIndex = mid + 1
    elif (numberList[mid] > mid):
        endIndex = mid - 1

if (findCheck == True):
    print(-1)
