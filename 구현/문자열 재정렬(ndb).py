data = input()
integerSum = 0
characterArray = []
result = ""

for i in range(len(data)):
    if (data[i].isalpha()):
        characterArray.append(data[i])
    else:
        integerSum += int(data[i])

characterArray.sort()

for i in characterArray:
    result += i

if (integerSum != 0):
    result += str(integerSum)

print(result)