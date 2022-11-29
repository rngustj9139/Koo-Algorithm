import sys
input = sys.stdin.readline

userInput = input()
userInput = int(userInput, 16)

for i in range(1, 16):
    print('%X'%userInput + '*%X'%i + '=%X'%(userInput * i), end='\n')