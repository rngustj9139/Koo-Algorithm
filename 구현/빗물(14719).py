'''
반례
1 1
1

5 5
2 4 1 5 4

5 5
1 0 3 2 4
'''

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blockHeightList = list(map(int, input().split()))

maxBlockIndex = blockHeightList.index(max(blockHeightList)) # 최대높이를 갖는 곳의 인덱스 구하기
secondHighHeight = 0 # 두번째로 높은 블록의 높이
result = 0 # ans

##########################
if(maxBlockIndex != 0): # 최대 높이를 갖는 위치가 맨 왼쪽이면 그보다 왼쪽을 계산할 필요 없음
    secondHighHeight = max(blockHeightList[0:maxBlockIndex]) # 최대 높이를 갖는 곳 왼쪽 편에서 두번째로 높은 블록의 높이 구하기

    if (secondHighHeight != 0):
        for i in range(1, maxBlockIndex): # 최대 높이를 갖는 곳 왼쪽 편에서 빗물 구하기(맨 왼쪽에서는 빗물이 저장될 수 없음)
            result += (secondHighHeight - blockHeightList[i])
##########################

secondHighHeight = 0

##########################
if(maxBlockIndex != len(blockHeightList) - 1): # 최대 높이를 갖는 위치가 맨 오른쪽이면 그보다 오른쪽을 계산할 필요 없음
    secondHighHeight = max(blockHeightList[maxBlockIndex + 1:len(blockHeightList)])

    for i in range(maxBlockIndex + 1, len(blockHeightList) - 1): # 최대 높이를 갖는 곳 오른쪽 편에서 빗물 구하기(맨 오른쪽에는 빗물이 저장될 수 없음)
        result += (secondHighHeight - blockHeightList[i])
##########################

print(result)

