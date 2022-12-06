# 예시
# 12 2
# 3 5
# 1 1
# dp[비용]=최대얻을수있는인원 (인덱스는 비용 (최대 1000명 모집가능하고 최대홍보비용이 100이므로) 100001으로 설정)
#
#                                                       dp[0]:0
#                              dp[1]:1                                    dp[3]:5
#                dp[2]:2             dp[4]:6                    dp[4]:6              dp[6]:10
#         dp[3]:3   dp[5]:7     dp[5]:7  dp[7]:11          dp[5]:7   dp[7]:11     dp[7]:11   dp[9]:15
#                                                                            (dp[8]:12)
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
hotelCostAndPopulationList = []
for _ in range(N):
    hotelCostAndPopulationList.append(list(map(int, input().split())))
dp = [0] * (100001)

for hotelCostAndPopulation in hotelCostAndPopulationList:
    for cost in range(1, 100001):
        if (cost - hotelCostAndPopulation[0] >= 0):
            dp[cost] = max(dp[cost], dp[cost - hotelCostAndPopulation[0]] + hotelCostAndPopulation[1])

for cost in range(1, 100001):
    if (dp[cost] >= C):
        print(cost)
        break