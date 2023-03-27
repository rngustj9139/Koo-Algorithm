'''
0 40
5 10
15 30
* 시작시간을 기준으로 오름차순으로 정렬한다.
* 최소힙(우선순위 큐)에 저장할 때 현재의 시작시간이 현재 힙에 들어있는 값보다 크거나 같으면 꺼내고, 아니면 count를 증가 시킨다. 그리고 현재의 끝나는 시간을 힙에 넣어준다.
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
result = 1
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x:x[0])
q = [0]

for startTime, finishTime in arr:
    if (startTime >= q[0]):
        heapq.heappop(q)
    else:
        result += 1
    heapq.heappush(q, finishTime)

print(result)