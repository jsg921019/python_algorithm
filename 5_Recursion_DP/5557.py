# https://www.acmicpc.net/problem/5557

import sys
from functools import cache

def solutionRec(N, nums):

    @cache
    def f(i, n):

        if i == 0:
            return 1 if nums[0] == n else 0
        
        ret = 0
        if n + nums[i] <= 20:
            ret += f(i-1, n + nums[i])
        if n - nums[i] >= 0:
            ret += f(i-1, n - nums[i])
        
        return ret

    return f(N-2, nums[-1])
    
N = int(sys.stdin.readline())
nums = [*map(int, sys.stdin.readline().split())]
print(solutionRec(N, nums))


# https://www.acmicpc.net/problem/5557

import sys
from collections import Counter

def solutionDP(N, nums):

    dp = Counter({nums[0]: 1})

    for n1 in nums[1:-1]:
        dp_next = Counter()
        for n2, cnt in dp.items():
            if n2 - n1 >= 0:
                dp_next[n2 - n1] += cnt
            if n2 + n1 <= 20:
                dp_next[n2 + n1] += cnt
        dp = dp_next
    
    return dp[nums[-1]]
    

N = int(sys.stdin.readline())
nums = [*map(int, sys.stdin.readline().split())]
print(solutionDP(N, nums))