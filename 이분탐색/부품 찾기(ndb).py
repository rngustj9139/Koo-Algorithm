import sys
input = sys.stdin.readline

N = int(input())
equipmentNumberList = list(map(int, input().split()))
M = int(input())
requireNumberList = list(map(int, input().split()))
result = []

for i in range(M):
    s = 0
    e = N - 1

    while (True):
        m = (s + e) // 2

        if (equipmentNumberList[m] > requireNumberList[i]):
            e = m - 1
        elif (equipmentNumberList[m] < requireNumberList[i]):
            s = m + 1
        else:
            result.append("yes")
            break

        if (s > e):
            result.append("no")
            break

for i in range(M):
    print(result[i], end = ' ')