'''
0~1: [2, 1, 2]
1~2: [2, 0, 2]
2~3: [2, 0, 1]
3~4: [1, 0, 1]
4~5: [1, 0, 0]
5~6: 정지
'''
import sys
input = sys.stdin.readline

def solution(food_times, k):
    tmp_time = 0
    answer = 0

    while (answer == 0):
        for i in range(0, len(food_times)):
            if (tmp_time == k):

                break
            if (food_times[i] != 0):
                food_times[i] -= 1
            tmp_time += 1

    return answer

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))