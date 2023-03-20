# '''
# food_times = [3,1,2], k = 5
# [2,1,2] 0~1초 1번
# [2,0,2] 1~2초 2번
# [2,0,1] 2~3초 3번
# [1,0,1] 3~4초 1번
# [1,0,0] 4~5초 3번
# 5초 장애발생
# 이후 1번부터 먹어야함 (result)
# '''
# import sys
# input = sys.stdin.readline
#
# def solution(food_times, k):
#     time = 0
#     answer = 0
#     while (True):
#         if (k == time):
#             break
#         for i in range(0, len(food_times)):
#             if (k != time):
#                 if (food_times[i] != 0):
#                     food_times[i] -= 1
#                     time += 1
#                 elif (food_times[i] == 0):
#                     continue
#             if (k == time):
#                 answer = i
#                 break
#
#     return answer
#
# food_times = list(map(int, input().split()))
# k = int(input())
#
# print(((solution(food_times, k) + 1) % len(food_times) + 1))

'''
효율성을 고려한 풀이법(탐욕적 기법)
k = 15, food_time=[8, 6, 4]일 때 가장 적은 3번째 음식을 다 먹으려면
1 2 3 1 2 3 1 2 3 1 2 3 => 12초 걸림 (남은 음식의 종류 * 3번째 음식을 다 먹으려면 걸리는 시간)

이후 k까지는 3초남았고, food_times=[4, 2]
1를 다먹으려면 => 4초 남음
2를 다먹으려면 => 2초 남음

가장 적은 2번째 음식을 다 먹으려면
1 2 1 2 => 4초 걸림 (남은 음식의 종류 * 2번째 음식을 다 먹으려면 걸리는 시간)
but 3초를 초과하기 때문에 일단 먹지 않음

1 2 1 2에서 3초 다음이 2번째 음식이기 때문에 2번째 음식을 출력

우선순위 큐(heapq)는 디폴트가 최소힙(min heap) => heapq.heappop(q)[0] == q[0][0]
'''
import heapq
import sys
input = sys.stdin.readline

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_time = 0
    previous_time = 0
    length = len(food_times)

    while (sum_time + (q[0][0] - previous_time) * length <= k):
        now = heapq.heappop(q)[0]
        sum_time += (now - previous_time) * length
        previous_time = now
        length -= 1

    result = sorted(q, key=lambda x:x[1])

    return result[(k - sum_time) % length][1]

k = int(input())
food_times = list(map(int, input().split()))

print(solution(food_times, k))