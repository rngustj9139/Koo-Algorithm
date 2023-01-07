# import sys
# input = sys.stdin.readline
#
# N = int(input())
# equipmentNumberList = list(map(int, input().split()))
# M = int(input())
# requireNumberList = list(map(int, input().split()))
# result = []
# equipmentNumberList.sort()
#
# for i in range(M):
#     s = 0
#     e = N - 1
#
#     while (True):
#         m = (s + e) // 2
#
#         if (equipmentNumberList[m] > requireNumberList[i]):
#             e = m - 1
#         elif (equipmentNumberList[m] < requireNumberList[i]):
#             s = m + 1
#         else:
#             result.append("yes")
#             break
#
#         if (s > e):
#             result.append("no")
#             break
#
# for i in range(M):
#     print(result[i], end = ' ')

import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while (True):
        mid = (start + end) // 2
        if (array[mid] == target):
            return mid
        elif (array[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
        return None

N = int(input())
equipmentNumberList = list(map(int, input().split()))
M = int(input())
requireNumberList = list(map(int, input().split()))

equipmentNumberList.sort()

for requireNumber in requireNumberList:
    result = binary_search(equipmentNumberList, requireNumber, 0, N - 1)

    if (result == None):
        print("no", end=" ")
    else:
        print("yes", end=" ")



