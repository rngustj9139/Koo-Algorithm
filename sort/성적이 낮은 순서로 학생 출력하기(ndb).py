import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    studentName, grade = input().split()
    arr.append([studentName, grade])

arr.sort(key=lambda x:x[1])

for i in range(len(arr)):
    print(arr[i][0], end=' ')