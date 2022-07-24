# https://www.acmicpc.net/problem/2293

import sys
from functools import cache

def solution(n, k, coins):

    dp = [1]+[0]*k
    for coin in coins:
        for price in range(coin, k+1):
            dp[price] += dp[price-coin]
    
    return dp[-1]
    
n, k = map(int, sys.stdin.readline().split())
coins = [*map(int, sys.stdin.readlines())]
print(solution(n, k, coins))