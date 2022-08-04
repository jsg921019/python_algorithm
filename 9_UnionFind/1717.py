# https://www.acmicpc.net/problem/1717

import sys

def find(a, parents):
        p = parents[a]
        path = []
        while a != p:
            path.append(a)
            a, p = p, parents[p]
        for x in path:
            parents[x] = a
        return a

def union(a, b, parents):
    p_a = find(a, parents)
    p_b = find(b, parents)
    parents[p_b] = p_a
    
def solution(n, m, queries):

    parents = list(range(n+1))

    for o, a, b in queries:
        if o:
            print('YES' if find(a, parents) == find(b, parents) else 'NO')
        else:
            union(a, b, parents)

n, m = map(int, sys.stdin.readline().split())
queries = [[*map(int, sys.stdin.readline().split())] for _ in range(m)]
solution(n, m, queries)