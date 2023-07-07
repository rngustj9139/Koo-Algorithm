# import sys~ 하면 문자열 맨 뒤에 \n이 붙게 된다.
data = input()
dataSize = len(data)
summary = 0

for i in range(dataSize // 2):
    summary += int(data[i])
for i in range(dataSize // 2, dataSize):
    summary -= int(data[i])

if (summary == 0):
    print("LUCKY")
else:
    print("READY")