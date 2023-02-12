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
# 최악의 경우에는 O(N^2)
'''
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
'''

######## 계수 정렬(Counting sort) O(N + K) ########
# 특정 조건에 부합할 때만 사용할 수 있지만, 매우 빠른 정렬 알고리즘
# 데이터의 크기 범위가 제한되어 정수형태로 표현할 수 있을 때만 사용 가능
# N은 데이터의 개수, K는 최댓값
# 계수정렬은 직접 데이터의 값을 비교한 뒤에 위치를 변경하는 비교 기반의 정렬 알고리즘이 아니다.
# 계수정렬은 일반적으로 데이터의 개수만큼의 리스트를 선언하고 그안에 정렬에 대한 정보를 담는다는 특징이 있다.
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
'''