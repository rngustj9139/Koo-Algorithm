'''
*은 센서, -는 집중국, 숫자는 좌표

1  2  3  4  5  6  7  8  9
*     *        *  *     *
               *
   -                -
(왼쪽부터 2 + 1.5 + 1.5 == 5)

각 센서들간의 거리차이를 구하면
2, 3, 0, 1, 2 이다 이때 이를 내림차순으로 정렬하면
3, 2, 2, 1, 0 이 되고 한 덩어리를 두 덩어리로 나누려면(두개의 집중국이 존재하기 때문에) K - 1번 즉 1번의 횟수만큼 이 거리차이에서 가장 큰 값을 제거하면 된다.
그 후 2 + 2 + 1 + 0을 하면 답인 5가 도출된다.

3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
*        *  *  *      *       *      *    *          *       *
-           -             -             -                -
(오른쪽부터 2 + 1 + 2 + 2 + 0 == 7)

각 센서들간의 거리차이를 구하면
3, 1, 1, 2, 2, 2, 1, 3, 2이고 내림차순으로 정렬하면
3, 3, 2, 2, 2, 2, 1, 1, 1이 나온다. 이때 한 덩어리를 다섯 덩어리로 나누려면(다섯개의 집중국이 존재하기 때문에) K - 1 즉 4번의 횟수만큼 이 거리차이에서 가장 큰 값을 제거하면 된다.
'''
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
censorLocation = list(map(int, input().split()))
censorLocationDifferenceList = []
result = 0

if (N <= K): # 센서의 개수보다 집중국의 수가 더 많거나 같은경우 최소 거리의 합은 0
    print(0)
    sys.exit()

censorLocation.sort() # 센서의 좌표를 오름차순으로 정렬

for i in range(0, len(censorLocation) - 1):
    censorLocationDifference = censorLocation[i + 1] - censorLocation[i]
    censorLocationDifferenceList.append(censorLocationDifference)

censorLocationDifferenceList.sort(reverse=True) # 센서간 거리차이를 내림차순으로 정렬

for _ in range(K - 1):
    del censorLocationDifferenceList[0]

for i in censorLocationDifferenceList:
    result += i

print(result)
