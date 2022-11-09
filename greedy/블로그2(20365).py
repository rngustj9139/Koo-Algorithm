# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# blueCount = 0
# redCount = 0
# totalCount = 0
#
# data = input()
#
# for i in range(n):
#     if (data[i] == "B"):
#         blueCount += 1
#     if (data[i] == "R"):
#         redCount += 1
#
# if (blueCount >= redCount):
#     totalCount += 1
#     totalCount += redCount
#
# if (blueCount < redCount):
#     totalCount += 1
#     totalCount += blueCount
#
# print(totalCount)

# 반례
#6
#BRBBRR
#output: 4
#answer: 3

import sys
input = sys.stdin.readline

n = int(input())
data = input()

blueCount = 0
redCount = 0

if data[0] == "B":
    blueCount += 1
if data[0] == "R":
    redCount += 1

for i in range(1, n):
    if data[i] != data[i - 1]:
        if data[i] == "R":
            redCount += 1
        if data[i] == "B":
            blueCount += 1

result = min(blueCount, redCount) + 1

print(result)