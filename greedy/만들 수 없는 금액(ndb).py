'''
입력값이 1, 2, 3, 8인 경우
target == 1일때 가능
target == 1 + 1 == 2일때 가능
target == 2 + 2 == 4일때 가능 (자연스럽게 3도 가능)
target == 4 + 3 == 7일때 불가능 (남은게 8이므로) (자연스럽게 5와 6도 가능)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = 1
for i in arr:
    if (i > target):
        break
    else:
        target += i # 1, 2, 3, 8

print(target)