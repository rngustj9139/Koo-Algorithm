# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         if (arr[j] > arr[j - 1]):
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#         else:
#             break
#
# print(arr)
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

print(arr)