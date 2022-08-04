# https://www.acmicpc.net/problem/10775

import sys

def find(a, parents):
    path = []
    p = parents[a]
    while a != p:
        path.append(a)
        a, p = p, parents[p]
    for x in path:
        parents[x] = a
    return a

def union(a, parents):
    p_a = find(a, parents)
    if p_a == 0:
        return False
    parents[p_a] = p_a - 1
    return True
    
def solution(G, planes):

    parents = list(range(G+1))
    for i, plane in enumerate(planes):
        if not union(plane, parents):
            return i  
    return i+1

G = int(sys.stdin.readline())
planes = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(solution(G, planes))