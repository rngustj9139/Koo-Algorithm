import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1

while (True):
    if (B == A):
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        cnt = -1
        break
    else:
        if (B % 10 == 1):
            B = B // 10
            cnt += 1
        elif (B % 2 == 0):
            B = B // 2
            cnt += 1

print(cnt)

