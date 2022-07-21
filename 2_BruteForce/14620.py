# https://www.acmicpc.net/problem/14620

from itertools import combinations
import sys

def solution(N, grid):

    def get_price(i, j):
        return sum(grid[_i][_j] for _i, _j in [(i+1, j), (i, j+1), (i, j), (i-1, j), (i, j-1)])
    
    def collide(coor1, coor2):
        return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1]) <= 2
    
    prices = {(i, j): get_price(i, j) for i in range(1, N-1) for j in range(1, N-1)}
    ans = float('inf')

    for choices in combinations(prices, 3):
        for pair in combinations(choices, 2):
            if collide(*pair):
                break
        else:
            ans = min(ans, sum(prices[coor] for coor in choices))
            
    return(ans)

N = int(sys.stdin.readline())
grid = [list(map(int, row.split())) for row in sys.stdin.readlines()]
print(solution(N, grid))