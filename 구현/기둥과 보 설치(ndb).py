import sys
input = sys.stdin.readline

def possible(answer): # 현재 구조물이 올바른 구조물인지 확인하는 함수
    for x, y, stuff in answer:
        if (stuff == 0): # 기둥인 경우
            if (y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer): # 땅위에있는경우, 기둥위에 있는경우, 보의 양쪽 끝 위에 있는 경우는 가능
                continue
            else:
                return False
        if (stuff == 1): # 보인 경우
            if ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)): # 한쪽 끝 부분이 기둥의 위에 있는경우, 양쪽이 보의 끝인 경우는 가능
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operation = frame[0], frame[1], frame[2], frame[3]

        if (operation == 0): # 삭제 연산인 경우
            answer.remove([x, y, stuff])
            if (not possible(answer)): # 현재 구조물이 불가능한 구조물일 경우 다시 되돌림
                answer.append([x, y, stuff])
        if (operation == 1): # 설치 연산인 경우
            answer.append([x, y, stuff])
            if (not possible(answer)): # 현재 구조물이 불가능한 구조물일 경우 다시 되돌림
                answer.remove([x, y, stuff])

    return sorted(answer)

N = int(input())
build_frame = []
build_frame_N = int(input())
for _ in range(build_frame_N):
    build_frame.append(list(map(int, input().split())))

print(solution(N, build_frame))
