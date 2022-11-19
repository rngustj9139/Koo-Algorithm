import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(0, N + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            if ('3' in str(i) or '3' in str(j) or '3' in str(k)):
                cnt += 1

print(cnt)