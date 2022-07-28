from collections import deque
            
def solution(begin, target, words):
    
    words.append(begin)
    graph = {word:[] for word in words}
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if sum(c1 != c2 for c1, c2 in zip(words[i], words[j])) == 1:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
                
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        
        word, n = q.popleft()
        
        if word in visited:
            continue

        if word == target:
            return n
        
        visited.add(word)
        q += [(w, n+1) for w in graph[word]]

    return 0