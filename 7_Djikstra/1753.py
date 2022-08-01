# https://www.acmicpc.net/problem/1753

import sys
from heapq import heappop, heappush

def solution(V, E, K, graph):
    
    visited = [0]*(V+1)
    dist = ['INF']*(V+1)
    h = [(0, K)]

    while h:
        
        d, node = heappop(h)
        
        if visited[node]:
            continue
        visited[node] = 1
        
        dist[node] = d
        
        for next_node in graph[node]:
            heappush(h, (d + graph[node][next_node], next_node))

    return dist[1:]

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [{} for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

print(*solution(V, E, K, graph))