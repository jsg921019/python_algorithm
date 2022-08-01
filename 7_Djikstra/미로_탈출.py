# https://school.programmers.co.kr/learn/courses/30/lessons/81304

from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    
    graph = [[] for _ in range(n+1)]
    
    for a, b, c in roads:
        graph[a].append((b, c, True))
        graph[b].append((a, c, False))
    
    visited = [set() for _ in range(n+1)]
    hq = [(0, start, tuple())]
    
    while hq:
        
        d, node, activated = heappop(hq)
        
        if activated in visited[node]:
            continue
        else:
            visited[node].add(activated)
            
        if node == end:
            return d
            
        for next_node, cost, flag in graph[node]:
            
            if next_node in traps:
                if next_node in activated:
                    if (node in activated) == flag:
                        heappush(hq, (d+cost, next_node, tuple(t for t in activated if t != next_node)))
                else:
                    if (node in activated) != flag:
                        heappush(hq, (d+cost, next_node, activated+(next_node,)))
            
            else:
                if (node in activated) != flag:
                    heappush(hq, (d+cost, next_node, activated))