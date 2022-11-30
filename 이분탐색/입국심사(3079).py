import sys
input = sys.stdin.readline

N, M = map(int, input().split())
judgingTableTimeList = []
for _ in range(N):
    judgingTableTimeList.append(int(input()))

leftTime = 0
rightTime = max(judgingTableTimeList) * M
result = rightTime
judgingTableTimeList.sort()

while (leftTime <= rightTime):
    midTime = (leftTime + rightTime) // 2
    people = 0

    for judgingTableTime in judgingTableTimeList:
        people += (midTime // judgingTableTime)

    if (people < M):
        leftTime = midTime + 1
    else:
        rightTime = midTime - 1
        result = min(result, midTime)

print(result)

