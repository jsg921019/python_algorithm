from functools import lru_cache

# Recursion
def solution(triangle):
    
    @lru_cache(maxsize=None)
    def f(i, j):
        
        if i == len(triangle) - 1:
            return triangle[i][j]
        
        return triangle[i][j] + max(f(i+1, j), f(i+1, j+1))
    
    return f(0, 0)

# DP
def solution(triangle):

    for row in range(len(triangle)-1)[::-1]:
        for i in range(row+1):
            triangle[row][i] += max(triangle[row+1][i], triangle[row+1][i+1])
    
    return triangle[0][0]