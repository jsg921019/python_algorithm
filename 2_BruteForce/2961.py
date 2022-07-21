# https://www.acmicpc.net/problem/2961

from itertools import combinations
import sys

def solution(N, ingredients):
   
    def diff(foods):
        sourness, bitterness = 1, 0
        for _sourness, _bitterness in foods:
            sourness *= _sourness
            bitterness += _bitterness
        return abs(sourness - bitterness)

    answer = float('inf')
    for n in range(1, N+1):
        for x in combinations(ingredients, n):
            answer = min(answer, diff(x))
            
    return answer
       
N = int(sys.stdin.readline())
ingredients = [tuple(map(int, x.split())) for x in sys.stdin.readlines()]
print(solution(N, ingredients))
