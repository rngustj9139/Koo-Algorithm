import sys
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, i):
    if (parent[i] != i):
        return find_parent(parent, parent[i])
    return i

V, E = map(int, input().split())
parent_table = [0] * (V + 1)
for i in range(1, V + 1):
    parent_table[i] = i

for i in range(E):
    a, b = map(int, input().split())
    union_parent(parent_table, a, b)

for i in range(1, V + 1):
    print(find_parent(parent_table, i), end=" ")
