# https://www.acmicpc.net/problem/2293

import sys
from functools import cache

def solutionRec(n, k, coins):

    @cache
    def f(n, k):

        if n == 0:
            return 1 if k == 0 else 0

        ret = f(n-1, k)
        if k >= coins[n-1]:
            ret += f(n, k-coins[n-1])
        
        return ret

    return f(n, k)
    
n, k = map(int, sys.stdin.readline().split())
coins = [*map(int, sys.stdin.readlines())]
print(solutionRec(n, k, coins))


# https://www.acmicpc.net/problem/2293

import sys
from functools import cache

def solutionDP(n, k, coins):

    dp = [1]+[0]*k
    for coin in coins:
        for price in range(coin, k+1):
            dp[price] += dp[price-coin]
    
    return dp[-1]
    
n, k = map(int, sys.stdin.readline().split())
coins = [*map(int, sys.stdin.readlines())]
print(solutionDP(n, k, coins))