import re

def solution(skill, skill_trees):
    return sum(skill.startswith(re.sub('[^' + skill + ']', '', st)) for st in skill_trees)