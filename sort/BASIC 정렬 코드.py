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

######## 삽입 정렬 ########
# 데이터를 적절한 위치에 삽입
# 데이터가 거의 정렬이 되어있을때 효율적이다.
# 판단하는 데이터의 앞쪽 데이터들은 정렬이 되어있다고 판단한다.
# 시작시 첫번째 원소는 정렬이 되어있다고 판단하고 두번째 원소부터 판단을 시작한다.


