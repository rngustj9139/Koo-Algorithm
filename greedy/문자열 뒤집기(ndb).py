arr = input()
count0 = 0 # 0으로 바꿔야하는 경우
count1 = 0 # 1로 바꿔야하는 경우

if (arr[0] == '1'):
    count0 += 1
else:
    count1 += 1

for i in range(0, len(arr) - 1):
    if (arr[i] != arr[i + 1]):
        if (arr[i + 1] == '1'):
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))