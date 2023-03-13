# 0이나 1일 경우 곱하기보다는 더하기
s = input()
result = 0

for i in s:
    if (int(i) == 0 or int(i) == 1 or result == 0):
        result += int(i)
    else:
        result *= int(i)

print(result)