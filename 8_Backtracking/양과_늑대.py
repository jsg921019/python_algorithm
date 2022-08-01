def solution(info, edges):

    graph = [[] for _ in range(len(info))]
    for p, c in edges:
        graph[p].append(c)
        
    ans = 0
    cnts = [0, 0]
    available = [0]*len(info)
    
    def bt(node):
        
        nonlocal ans
        
        if info[node] and cnts[0] <= cnts[1] + 1:
            return
        
        cnts[info[node]] += 1
        ans = max(cnts[0], ans)
        
        for next_node in graph[node]:
            available[next_node] = 1
            
        for i, f in enumerate(available):
            if f:
                available[i] = 0
                bt(i)
                available[i] = 1
        
        for next_node in graph[node]:
            available[next_node] = 0
            
        cnts[info[node]] -= 1
        
    bt(0)        
                
    return ans