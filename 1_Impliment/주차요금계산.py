# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict

def price(log, fees):
    basic_t, base_price, unit_t, unit_price = fees
    if len(log) % 2:
        log.append(23*60+59)
    t = sum(log[i+1] - log[i] for i in range(0, len(log), 2))
    return unit_price * -(-max(0, t-basic_t) // unit_t) + base_price

def solution(fees, records):
    
    log = defaultdict(list)
    
    for record in records:
        t, n, _ = record.split()
        h, m = map(int, t.split(':'))
        log[n].append(60*h+ m)
    
    return [price(log[n], fees) for n in sorted(log)]