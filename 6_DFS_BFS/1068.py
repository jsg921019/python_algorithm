# https://www.acmicpc.net/problem/1068

import sys

def solution(N, parents, to_remove):

    graph = [[] for _ in range(N)]
    root = None
    for i, p in enumerate(parents):
        if i == to_remove:
            continue
        if p == -1:
            root = i
        else:
            graph[p].append(i)
    
    if root is None:
        return 0

    leafs = 0

    def dfs(node):
        nonlocal leafs
        if graph[node]:
            for next_node in graph[node]:
                dfs(next_node)
        else:
            leafs += 1
    
    dfs(root)
    return leafs

N = int(sys.stdin.readline())
parents = map(int, sys.stdin.readline().split())
to_remove =int(sys.stdin.readline())
print(solution(N, parents, to_remove))