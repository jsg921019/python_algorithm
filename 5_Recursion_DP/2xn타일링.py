import sys
sys.setrecursionlimit(60004)

# Recursion
def solution(n):
    
    cache = [0]*(n+1)
    cache[:2] = [1, 1]
    
    def f(n):
        
        if cache[n]:
            return cache[n]
        
        cache[n] = (f(n-1) + f(n-2)) % 1000000007
        return cache[n]
    
    return f(n)

# DP
def solution(n):
    
    dp1, dp2 = 1, 1
    
    for _ in range(n-1):
        dp1, dp2 = dp2, (dp1 + dp2)%1000000007
    
    return dp2