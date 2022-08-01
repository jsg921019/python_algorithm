# https://www.acmicpc.net/problem/1504

import sys
from heapq import heappop, heappush

def solution(N, v1, v2, graph):

    def dijkstra(start):
    
        visited = [0]*(N+1)
        dist = [float('inf')]*(N+1)
        dist[start] = 0
        h = [(0, start)]

        while h:

            d, node = heappop(h)

            if visited[node]:
                continue
            visited[node] = 1

            for next_node, cost in graph[node]:

                if visited[next_node]:
                    continue
                
                new_d = d + cost
                if dist[next_node] > new_d:
                    dist[next_node] = new_d
                    heappush(h, (new_d, next_node))

        return dist

    dist_v1 = dijkstra(v1)
    dist_v2 = dijkstra(v2)

    ans = min(dist_v1[1] + dist_v1[v2] + dist_v2[N], dist_v2[1] + dist_v2[v1] + dist_v1[N])
    return -1 if ans == float('inf') else ans

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, sys.stdin.readline().split())
print(solution(N, v1, v2, graph))