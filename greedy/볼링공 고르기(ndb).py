# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0
#
# arr.sort()
#
# for i in range(0, N - 1):
#     for j in range(i + 1, N):
#         if (arr[i] == arr[j]):
#             continue
#         else:
#             result += 1
#
# print(result)

'''
조합 : 순서를 생각하지 않고 n개중 r개 뽑기
1 2 2 3 3
A가 1을 뽑을 경우: 1 * 4 == 4
A가 2를 뽑을 경우: 2 * 2 == 4
A가 3을 뽑을 경우: 2 * 0 == 0
총 8가지 경우의 수 존재
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * (11) # M이 최대 10이라고 명시되어있음
result = 0

for i in data:
    array[i] += 1

for i in range(1, M + 1):
    N = N - data[i]
    

print(result)

