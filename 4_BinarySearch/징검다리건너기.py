# https://school.programmers.co.kr/learn/courses/30/lessons/64062?language=python3

def solution(stones, k):

    def possible(n):
        cnt = 0
        for s in stones:
            if s >= n:
                cnt = 0
            else:
                cnt += 1
                if cnt == k:
                    return 0
        return 1
        
    lo, hi = 0, max(stones)        
    
    while lo <= hi:
        
        mid = (lo + hi) // 2
        flag = possible(mid)
        
        if flag:
            lo = mid + 1 
        else:
            hi = mid - 1
            
    return hi
            