# import sys
# input = sys.stdin.readline
#
# userInput = str(input()) # a1
# col = userInput[0]
# row = int(userInput[1])
# cnt = 0
#
# dx = [-2, -2, -1, 1, 2, 2, -1, 1]
# dy = [-1, 1, 2, 2, -1, 1, -2, -2]
#
# for i in range(8):
#     nx = row + dx[i]
#     ny = ord(col) + dy[i]
#
#     if (nx < 1 or nx > 8 or chr(ny) < 'a' or chr(ny) > 'h'):
#         continue
#     else:
#         cnt += 1
#
# print(cnt)

import sys
input = sys.stdin.readline

steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
result = 0

userInput = input()
col = ord(userInput[0]) - ord('a') + 1
row = int(userInput[1])

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]

    if (1 <= nrow and nrow <= 8 and 1 <= ncol and ncol <= 8):
        result += 1
    else:
        continue

print(result)



