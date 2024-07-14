'''
n = 12

원을 길게 늘려서 직선을 만들고 사이클이 도는 것은 다시 직선을 한번 반복함으로써 해결한다
weak => [1] 2 [3] [4] 5 6 7 8 [9] [10] 11 12 | [13] 14 [15] [16] 17 18 19 20 [21] [22] 23 24
=> 1 3 4 9 10 | 13 15 16 21 22

dist => 3 5 7

7을 좌표 9에 투입하여 시계방향(오른쪽)으로 가면 1명으로 해결된다.
'''
import sys
input = sys.stdin.readline
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak) # 5
    for i in range(length): # 0부터 4까지
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length): # 0부터 4까지
        for friends in list(permutations(dist, len(dist))): # 투입할 친구의 모든 경우의 수
            count = 1 # 투입할 친구의 수
            position = weak[start] + friends[count - 1] # 해당 친구가 점검할 수 있는 마지막 위치
            for index in range(start, start + length):
                if (position < weak[index]): # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1 # 새로운 친구를 투입
                    if (count > len(dist)): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if (answer > len(dist)):
        return -1

    return answer

n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))

print(solution(n, weak, dist))





