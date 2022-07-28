# https://www.acmicpc.net/problem/2606

import sys

def solution(N, graph):

    stack = [1]
    visited = [0]*(N+1)
    visited[1] = 1
    cnt = -1

    while stack:

        node = stack.pop()
        cnt += 1

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            stack.append(next_node)
    
    return cnt

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(solution(N, graph))