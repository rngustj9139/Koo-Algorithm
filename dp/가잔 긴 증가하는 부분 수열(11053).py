'''
수열: 15 10 20 5 50 60

(10 + 20 + 50 + 60 == 140) x
(15 + 20  + 50 + 60 == 145) o

수열: 15 10 40 30 35 5 50 60

(15 + 30 + 35 + 50 + 60 == 190) o
(15 + 40 + 50 + 60 == 175) x

-----------------

arr	10	20	10	30	20	50
dp	1	2	1	3	2	4

dp속 값은 순서(길이)를 의미한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [1] * 1001

for i in range(N):
    for j in range(i):
        if (numbers[i] > numbers[j]):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))





