import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111) # 충분한 재귀 깊이를 주어 오류를 예방

def dfs(cur):
    visited[cur] = True
    nxt = S[cur]

    if (visited[nxt] == True):
        if (finished[nxt] == False):
            global cnt
            i = nxt
            while (i != cur):
                i = S[i]
                cnt += 1
            cnt += 1
    else:
        dfs(nxt)

    finished[cur] = True

T = int(input())

while (T > 0):
    T -= 1
    N = int(input())
    S = list(map(int, input().split()))
    for i in range(len(S)):
        S[i] -= 1
    visited = [False] * (N + 1)
    finished = [False] * (N + 1)
    cnt = 0

    for i in range(N):
        if (visited[i] == False):
            dfs(i)

    print(N - cnt)