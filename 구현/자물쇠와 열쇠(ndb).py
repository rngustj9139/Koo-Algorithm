'''
행렬이 시계방향으로 90도 회전시 (data1 -> data2)
data1 = [[1, 2, 3, 4],
         [5, 6, 7 ,8]]

data2 = [[5, 1],
         [6, 2],
         [7, 3],
         [8, 4]]
'''
import sys
input = sys.stdin.readline

def rotate_a_matrix_by_90_degree(matrix): # 행렬을 시계방향으로 90도 회전시키는 함수
    n = len(matrix) # 행의 수 구하기
    m = len(matrix[0]) # 열의 수 구하기
    new_matrix = [[0] * (n) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - i - 1] = matrix[i][j]

    return new_matrix

def check(new_lock): # 키가 자물쇠에 맞는지(자물쇠의 값이 다 1이 되는지) 검사
    new_lock_real_length = len(new_lock) // 3
    for i in range(new_lock_real_length, new_lock_real_length * 2):
        for j in range(new_lock_real_length, new_lock_real_length * 2):
            if (new_lock[i][j] != 1):
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 3배로 변경(원래 자물쇠에 0이 둘러쌂)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 가운데에 원래 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    for rotation in range(4): # 4개의 방향 고려
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if (check(new_lock) == True):
                    return True

                # 자물쇠에 넣은 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

key = []
lock = []
N, M = map(int, input().split())
for i in range(N):
    lock.append(list(map(int, input().split())))
for i in range(M):
    key.append(list(map(int, input().split())))

print(solution(key, lock))