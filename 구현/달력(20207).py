'''
| 2일 | 3일 | 4일 | 5일 | 6일 | 7일 | 8일 | 9일 | 10일 | 11일 | 12일 |
  1개   1개   2개   3개   2개   2개   1개   1개   0개    1개    2개
 10일을 기준으로 왼쪽은 max가 3개 오른쪽은 max가 2개이다 따라서
 8 * 3 + 2 * 2 = 28
'''
import sys
input = sys.stdin.readline

N = int(input())
scheduleList = []
result = 0
width = 0
maxValue = 0

for _ in range(N):
    startDay, endDay = map(int, input().split())
    scheduleList.append([startDay, endDay])

scheduleList.sort(key = lambda x:x[0]) # 오름차순(시작일이 빠른 기준으로)
scheduleList.sort(key = lambda x:x[1]-x[0], reverse=True) # (시작일이 같은 경우 더 긴 일정 먼저)
minDay = min(map(min, scheduleList)) # 이차원 배열에서 최솟값 구하기
maxDay = max(map(max, scheduleList)) # 이차원 배열에서 최댓값 구하기
countSchedule = [0] * (maxDay + 1)

for i in scheduleList:
    for j in range(i[0], i[1] + 1):
        countSchedule[j] += 1

for i in range(minDay, maxDay + 1):
    if (countSchedule[i] > 0):
        width += 1
        if (countSchedule[i] > maxValue):
            maxValue = countSchedule[i]
    elif (countSchedule[i] == 0):
        result += maxValue * width
        width = 0
        maxValue = 0

if (width > 0 or maxValue > 0): # 마지막으로 남은 일정 채우기
    result += maxValue * width

print(result)




