import sys
input = sys.stdin.readline

N = int(input())
muscle_decrease = []
results = []

muscle_decrease = list(map(int, input().split()))

muscle_decrease.sort()

if (len(muscle_decrease) % 2 == 1):
    results.append(muscle_decrease[N - 1])
    del muscle_decrease[N - 1]
    N = len(muscle_decrease)

for i in range(int(N / 2)):
    results.append(muscle_decrease[i] + muscle_decrease[N - 1 - i])

print(max(results))





