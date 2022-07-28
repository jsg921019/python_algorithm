# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(N, M, V, graph):

    path = []
    s = [V]
    visited = [0]*(N+1)

    while s:
        v = s.pop()
        if not visited[v]:
            visited[v] =1
            path.append(v)
            s += graph[v]

    return path

def bfs(N, M, V, graph):

    path = []
    q = deque([V])
    visited = [0]*(N+1)

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] =1
            path.append(v)
            q += graph[v][::-1]

    return path


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for neighbors in graph:
    neighbors.sort(reverse=True)

print(*dfs(N, M, V, graph))
print(*bfs(N, M, V, graph))