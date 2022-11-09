# 반례: MMM, KKK
import sys
input = sys.stdin.readline

userInput = input()
maxResult = ""
minResult = ""
M_count = 0
K_count = 0

# 최대의 값을 구할때는 K가 나올 때까지 M의 횟수를 누적해서 센 뒤 K가 나오면 계산을 수행한다.
if (userInput[0]) == 'M':
    M_count += 1
if (userInput[0]) == 'K':
    maxResult = str(5)
    K_count += 1

for i in range(1, len(userInput)):
    if (userInput[i] == 'M'):
        M_count += 1
    if (userInput[i] == 'K' and userInput[i - 1] == 'M'):
        maxResult += str((10 ** M_count) * 5)
        M_count = 0
    if (userInput[i] == 'K' and userInput[i - 1] == 'K'):
        maxResult += "5"

if (M_count > 0):
    while (M_count):
        maxResult += "1"
        M_count -= 1

if (K_count == 0):
    while (M_count):
        maxResult += "1"
        M_count -= 1

print(maxResult)

# 최소의 값을 구할때는 최대한 M과 K를 분리해서 계산한다.
M_count = 0
K_count = 0

if (userInput[0]) == 'M':
    M_count += 1
if (userInput[0]) == 'K':
    minResult = str(5)
    K_count += 1

for i in range(1, len(userInput)):
    if (userInput[i] == 'M'):
        M_count += 1
    if (userInput[i] == 'K'):
        if (M_count > 0):
            minResult += str(10 ** (M_count - 1))
        minResult += "5"
        M_count = 0
        K_count += 1

if (M_count > 0):
    minResult += str(10 ** (M_count - 1))

if (K_count == 0):
    minResult = str(10 ** (M_count - 1))

print(minResult)

'''
import sys
input = sys.stdin.readline

mCount = 0
kCount = 0
maxValue = ''
minValue = ''

userInput = input()

#=== 최댓값 구하기 시작 ===#
for i in range(len(userInput)):
    if(userInput[i] == 'M'):
        mCount += 1
    elif(userInput[i] == 'K' and mCount > 0):
        maxValue += str((10 ** mCount) * 5)
        mCount = 0
    elif(userInput[i] == 'K' and mCount == 0):
        maxValue += str(5)

if(mCount > 0):
    while (mCount):
        maxValue += str(1)
        mCount -= 1

print(maxValue)
#=== 최댓값 구하기 끝 ===#

#=== 최솟값 구하기 시작 ===#
for i in range(len(userInput)):
    if(userInput[i] == 'M' and userInput[i + 1] != 'K'):
        mCount += 1
    elif (userInput[i] == 'M' and userInput[i + 1] == 'K'):
        mCount += 1
        minValue += str(10 ** (mCount - 1))
        mCount = 0
    elif(userInput[i] == 'K'):
        minValue += str(5)

if(mCount > 0):
    minValue += str(10 ** (mCount - 1))

print(minValue)
#=== 최솟값 구하기 끝 ===#
'''



