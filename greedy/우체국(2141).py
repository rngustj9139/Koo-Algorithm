# 시간 초과
'''
import sys
input = sys.stdin.readline

N = int(input())
A = []
X = []
result = 0

for i in range(N):
    a, b = map(int, input().split())
    X.append(a)
    A.append(b)

for i in range(N):
    distance = 0
    for j in range(N):
        if (i == j):
            continue
        else:
            distance += (abs(X[i] - X[j]) * A[j])
    if (distance > result):
        result = i

print(result)
'''

'''
*   *   *   *   *   *   *   *   *   * 
15     8                            4

16 + 36 == 52
30 + 28 == 58
28 + 135 == 163
총인구:27
절반인구:13.5

*   *   *   *   *   *   *   *   *   * 
4      8                            15

16 + 135 == 151
8 + 105 == 113
36 + 56 == 92
총인구:27
절반인구:13.5

*   *   *   *   *   *   *   *   *   * 
    15                          8  13

56 + 104 == 160
105 + 13 == 118
8 + 120 == 128
총인구:36
절반인구:18

=> 총인구의 절반이 넘어서는 지점의 마을에 우체국을 세우면 된다.
=> 우체국이 위치한 마을의 좌측 방향 인구 수와 우측 방향에 있는 인구 수의 차이가 최소가 되어야 하고
전체 인구 수의 절반에 가까운 값이 우체국의 좌, 우에 퍼져 있으면 두 값의 차이가 최소가 되기 때문에
"인구 수 절반 이상"이 탐색 break의 조건
'''
import sys
input = sys.stdin.readline

N = int(input())
village = []
totalPopulation = 0
tmpPopulation = 0
result = 0

for _ in range(N):
    villageLocation, villagePopulation = map(int, input().split())
    village.append([villageLocation, villagePopulation])
    totalPopulation += villagePopulation

village.sort(key=lambda x:x[0])

for i in range(N):
    tmpPopulation += village[i][1]

    if (tmpPopulation >= (totalPopulation / 2)):
        result = village[i][0]
        break

print(result)


