import sys
input = sys.stdin.readline

totalCraneCount = int(input())
cranes = list(map(int, input().split()))
totalBoxCount = int(input())
boxes = list(map(int, input().split()))
result = 0

# 내림차순 정렬 (가장 큰 무게를 들 수 있는 크레인이 가장 큰 무게의 박스를 옮기게 하는 것이 효율적)
cranes.sort(reverse=True)
boxes.sort(reverse=True)

# 모든 박스를 배로 옮길 수 없는 경우에는 -1 출력
if (cranes[0] < boxes[0]):
    print(-1)
    sys.exit()

# 모든 박스를 배로 옮길 수 있는 경우
while (len(boxes) > 0):
    for i in cranes:
        for j in boxes:
            if (i >= j):
                boxes.remove(j)
                break
    result += 1

print(result)





