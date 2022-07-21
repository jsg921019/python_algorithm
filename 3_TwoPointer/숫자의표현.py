# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(num):
    
    lo, hi = 1, 1
    tot = 1
    ans = 0
    
    while lo <= hi:
        
        if tot < num:
            hi += 1
            tot += hi
        
        elif tot > num:
            tot -= lo
            lo += 1
            
        else:
            ans += 1
            tot -= lo
            lo += 1
            
    return ans
    