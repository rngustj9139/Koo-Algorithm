import sys
input = sys.stdin.readline

def cutRiceCake(riceCakeLengthList, cutHeight):
    totalLength = 0

    for riceCakeLength in riceCakeLengthList:
        if (riceCakeLength > cutHeight):
            totalLength += (riceCakeLength - cutHeight)
        else:
            totalLength += 0

    return totalLength

N, M = map(int, input().split())
riceCakeLengthList = list(map(int, input().split()))

riceCakeLengthList.sort()
s = 0
e = max(riceCakeLengthList)

while (s <= e):
    m = (s + e) // 2

    totalLength = cutRiceCake(riceCakeLengthList, m)
    if (totalLength > M):
        s = m + 1
    elif (totalLength < M):
        e = m - 1
    else:
        print(m)
        sys.exit()