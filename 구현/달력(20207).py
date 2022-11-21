import sys
input = sys.stdin.readline

scheduleList = []
area = 0
checkHeightLevel = 1

N = int(input())

for _ in range(7):
    startTime, endTime = map(int, input().split())
    scheduleList.append([startTime, endTime])

scheduleList.sort(key = lambda x: x[0])
scheduleList.sort(key = lambda x: x[1] - x[0], reverse=True)

for _ in range(scheduleList[0][0], scheduleList[0][1]):
    area += 1

for i in range(1, len(scheduleList)):
    checkHeightLevelBool = True
    for timeRange in range(scheduleList[i][0], scheduleList[i][1] + 1):
        area += 1
        if (timeRange <= scheduleList[i - 1][1] and checkHeightLevelBool):
            checkHeightLevel += 1
            checkHeightLevelBool = False

print(area)