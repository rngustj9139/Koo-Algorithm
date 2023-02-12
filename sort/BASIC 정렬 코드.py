######## 선택 정렬 O(N^2) ########
# 전체 데이터중 제일 작은 것을 찾아 맨 앞으로 보낸다.
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if (array[j] < array[min_index]):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
'''

######## 삽입 정렬 O(N^2) ########
# 데이터를 적절한 위치에 삽입
# 데이터가 거의 정렬이 되어있을때 효율적이다.
# 판단하는 데이터의 앞쪽 데이터들은 정렬이 되어있다고 판단한다.
# 시작시 첫번째 원소는 정렬이 되어있다고 판단하고 두번째 원소부터 판단을 시작한다.
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if (array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
'''

######## 퀵 정렬 O(NlogN) ########
# 데이터가 이미 정렬되어 있을 경우 느리게 동작한다.
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if (start >= end): # 원소가 1개이면 종료
        return
    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)