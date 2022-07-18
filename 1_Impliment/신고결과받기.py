# https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict, Counter

def solution(id_list, report, k):

    report_dict = defaultdict(set) 
    report_cntr = Counter()

    for r in report:
        user1, user2 = r.split()
        report_dict[user1].add(user2)

    for v in report_dict.values():
        report_cntr.update(v)

    blacklist = {x for x in report_cntr if report_cntr[x] >= k}

    return [len(report_dict[user] & blacklist) for user in id_list]

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}
#     set_report = set(report)

#     for r in set_report:
#         reports[r.split()[1]] += 1

#     for r in set_report:
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer