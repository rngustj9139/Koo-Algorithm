# import sys
# input = sys.stdin.readline
#
# N = int(input())
# numberList = list(map(int, input().split()))
#
# numberList.sort()
# startIndex = 0
# endIndex = N - 1
# findCheck = True
#
# while (startIndex <= endIndex):
#     mid = (startIndex + endIndex) // 2
#
#     if (numberList[mid] == mid):
#         print(mid)
#         findCheck = False
#         break
#     elif (numberList[mid] < mid):
#         startIndex = mid + 1
#     elif (numberList[mid] > mid):
#         endIndex = mid - 1
#
# if (findCheck == True):
#     print(-1)

import sys
input = sys.stdin.readline

def binary_search(array, start, end):
    if (start > end):
        return None

    mid = (start + end) // 2

    if (array[mid] == mid):
        return mid
    elif (array[mid] < mid):
        return binary_search(array, start, mid - 1)
    elif (array[mid] > mid):
        return binary_search(array, mid + 1, end)

N = int(input())
numberList = list(map(int, input().split()))

result = binary_search(numberList, 0, N - 1)

if (result == None):
    print(-1)
else:
    print(result)