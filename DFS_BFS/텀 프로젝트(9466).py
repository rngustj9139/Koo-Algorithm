import sys
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True
    nxt = S[cur]

    if (visited[nxt] == True):
        if (finished[nxt] == False):
            global cnt
            i = nxt
            while (i != cur):
                i += 1
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