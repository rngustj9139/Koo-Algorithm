n, m = map(int, input().split())  # n*m 크기의 맵
x, y, d = map(int, input().split())  # 캐릭터 위치 (x,y), 바라보는 방향:d

# 전체 map 정보 입력받기(육지:0, 바다:1)
map_info = []
for i in range(n):
    map_info.append(list(map(int, input().split())))

# 방향 d: [0,1,2,3]에 따라 이동 방향 설정 (북,동,남,서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# map_info: 방문한 위치를 저장하기 위한 맵, 0으로 초기화 
check = [[0] * m for _ in range(n)]
check[x][y] = 1


# 왼쪽으로 회전시 방향 바뀌는 함수
def turn_left():
    global d
    d -= 1
    if d == -1:  # 0->-1 : 북 -> 서
        d = 3


count = 1  # 방문한 칸의 수
turn_num = 0
while True:
    # 왼쪽으로 회전
    turn_left()

    # 회전한 이후 정면이 가보지 않은 칸이고, 육지이면 이동
    nx = x + dx[d]
    ny = y + dy[d]

    if check[nx][ny] == 0 and map_info[nx][ny] == 0:
        check[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_num = 0
        continue
    # 회전한 이후 정면에 가본 칸이거나 바다인 경우 회전
    else:
        turn_num += 1

        # 4방향 모두 가본 칸이거나 바다로 되어 있는 칸 (네방향 모두 갈 수 없는 칸)
    # -> 앞에 else문이 연달아 4번 나올 경우
    if turn_num == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면(뒤에 있는 칸이 육지) 이동
        if map_info[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있다면 움직임을 멈춘다 -> 종료
        else:
            break
        turn_num = 0  # 방향 다시 순회

print(count)