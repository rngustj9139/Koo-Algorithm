import sys
input = sys.stdin.readline

T = int(input())

def calculateFactorial(number):
    calculateResult = 1
    for i in range(1, number + 1):
        calculateResult *= i

    return calculateResult

for _ in range(T):
    N, M = map(int, input().split())
    print(calculateFactorial(M) // (calculateFactorial(N) * calculateFactorial(M - N))) # 조합(n개중 순서를 고려하지 않고 k개를 뽑기) -> n! / (k! * (n - k)!)

