'''
반례
1 1
1

*

5 5
2 4 1 5 4

      *
  *   * *
  *   * *
* *   * *
* * * * *


5 5
1 0 3 2 4

       *
   *   *
   * * *
*  * * *
'''

# import sys
# input = sys.stdin.readline
#
# H, W = map(int, input().split())
# blockHeightList = list(map(int, input().split()))
#
# maxBlockIndex = blockHeightList.index(max(blockHeightList)) # 최대높이를 갖는 곳의 인덱스 구하기
# result = 0 # ans
#
# if(maxBlockIndex != 0): # 최대 높이를 갖는 위치가 맨 왼쪽이면 그보다 왼쪽을 계산할 필요 없음
#     secondHighHeight = max(blockHeightList[0:maxBlockIndex]) # 최대 높이를 갖는 곳 왼쪽 편에서 두번째로 높은 블록의 높이 구하기
#     secondHighLocation = blockHeightList.index(secondHighHeight) # 최대 높이를 갖는 곳 왼쪽 편에서 두번째로 높은 블록의 좌표 구하기
#
#     if (secondHighHeight != 0):
#         for i in range(1, maxBlockIndex): # 최대 높이를 갖는 곳 왼쪽 편에서 빗물 구하기(맨 왼쪽에서는 빗물이 저장될 수 없음)
#             if (secondHighLocation <= i):
#                 result += (secondHighHeight - blockHeightList[i])
#             else:
#                 if (blockHeightList[i] < blockHeightList[i - 1]):
#                     result += (blockHeightList[i - 1] - blockHeightList[i])
#                 else:
#                     continue
#
# if(maxBlockIndex != len(blockHeightList) - 1): # 최대 높이를 갖는 위치가 맨 오른쪽이면 그보다 오른쪽을 계산할 필요 없음
#     secondHighHeight = max(blockHeightList[maxBlockIndex + 1:len(blockHeightList)]) # 최대 높이를 갖는 곳 오른쪽 편에서 두번째로 높은 블록의 높이 구하기
#     secondHighLocation = blockHeightList.index(secondHighHeight)  # 최대 높이를 갖는 곳 오른쪽 편에서 두번째로 높은 블록의 좌표 구하기
#
#     for i in range(maxBlockIndex + 1, len(blockHeightList) - 1): # 최대 높이를 갖는 곳 오른쪽 편에서 빗물 구하기(맨 오른쪽에는 빗물이 저장될 수 없음)
#         if (secondHighLocation >= i):
#             result += (secondHighHeight - blockHeightList[i])
#         else:
#             if (blockHeightList[i] > blockHeightList[i - 1]):
#                 result += (blockHeightList[i] - blockHeightList[i - 1])
#             else:
#                 continue
#
# print(result)

# def solution(blockHeightList):
#     result = 0
#
#     for i in range(1, len(blockHeightList) - 1): # 1, 2
#         leftMax = 0
#         rightMax = 0
#         for j in range(0, i):
#             leftMax = max(leftMax, blockHeightList[j])
#         for k in range(i + 1, len(blockHeightList)):
#             rightMax = max(rightMax, blockHeightList[k])
#         current = blockHeightList[i]
#         standard = min(leftMax, rightMax)
#         if (standard > current):
#             result += (standard - current)
#
#     return result
#
# H, W = map(int, input().split())
# blockHeightList = list(map(int, input().split()))
#
# print(solution(blockHeightList))

'''
특정 위치를 기준으로 양 옆에 현 위치보다 작은 높이의 블록이 있다면 해당 위치에는 물고이기 불가능
특정 위치에 물이 고이기 위해선 현 위치보다 더 높은 블록으로 왼쪽과 오른쪽이 둘러싸여 있어야한다.
and 이러한 조건을 만족할 때 물이 고이는 양은 왼쪽과 오른쪽 블록 중 더 낮은 블록과 현 위치의 높이를 뺀 값이다.
만약 높이가 2인 구역을 왼쪽 오른쪽으로 각각 5, 6 높이의 블록이 감싸고 있다면 해당 구역은 더 낮은 블록인 5에서 현 위치의 높이인 2을 뺀 3 만큼의 물이 고인다.
첫번째 칸과 마지막 칸은 물이 고일 수 없으므로 range에서 제외한다.
'''
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
blockHeightList = list(map(int, input().split()))
result = 0

for i, h in enumerate(blockHeightList):
    result += min(max(blockHeightList[i:]), max(blockHeightList[:i+1])) - h

print(result)
