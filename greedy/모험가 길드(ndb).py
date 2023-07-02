'''
1 2 2 2 3
3 4 5
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = []
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort() # 오름차순 정렬

for i in arr:
    cnt += 1
    if (cnt >= i):
        result += 1
        cnt = 0

print(result)

