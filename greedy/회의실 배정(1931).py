"""
0         6
 1     4                                    *
  2                       13
   3    5
   3          8
        5   7                               *
        5      9
         6      10
              8       11                    *
              8         12
                        12  14              *
"""



import sys
input = sys.stdin.readline

N = int(input())
meetingTime = []
determinedMeetingTime = []

for _ in range(N):
    meetingTime.append(list(map(int, input().split())))

meetingTime.sort(key=lambda x:x[0]) # 첫번째 원소를 기준으로 오름차순 정렬

if (meetingTime[0][1] - meetingTime[0][0] > meetingTime[1][1] - meetingTime[1][0] and meetingTime[0][1] != meetingTime[1][0]):
    determinedMeetingTime.append(meetingTime[1])
elif (meetingTime[0][1] == meetingTime[1][0]):
    determinedMeetingTime.append(meetingTime[0])
    determinedMeetingTime.append(meetingTime[1])
else:
    determinedMeetingTime.append(meetingTime[0])

for i in range(2, N):
    if (meetingTime[i - 1][1] - meetingTime[i - 1][0] >= meetingTime[i][1] - meetingTime[i][0]):
        if (determinedMeetingTime[-1][1] <= meetingTime[i][0]):
            determinedMeetingTime.append(meetingTime[i])

print(len(determinedMeetingTime))
print(determinedMeetingTime)


'''
내가 회의실을 사용하고 있다고 가정했을 때, 내 회의가 끝난 후에 회의실에서 가장 많은 회의가 열리기 위해서는 어떤 상황이 되야할까? 
바로. 내 회의가 빨리 끝나야 하는 것이다. 즉, 종료 시간이 빨라야 한다.
1 2, 2 2라는 두개의 회의가 존재하면 우선 첫번째 원소를 기준으로 오름차순 정렬한 뒤, 두번째 원소를 기준으로 오름차순 정렬해야
두개의 회의를 완료할 수 있다.
'''
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# meetingTime = []
# cnt = 0
# lastTime = 0
#
# for _ in range(N):
#     startTime, finishTime = map(int, input().split())
#     meetingTime.append([startTime, finishTime])
#
# meetingTime.sort(key=lambda x:x[0])
# meetingTime.sort(key=lambda x:x[1])
#
# for startTime, finishTime in meetingTime:
#     if (startTime >= lastTime):
#         lastTime = finishTime
#         cnt += 1
#
# print(cnt)


