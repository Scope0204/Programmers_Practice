def solution(s):
    answer = []
    answer2 = {}
    answer3 = []  # 진짜 답
    int_str = ''

    for i, v in enumerate(s):
        if str.isdigit(v):
            int_str += v
        elif v == ',':
            answer.append(int_str)
            int_str = ''

        if i == len(s)-1 and int_str != '':  # 마지막인데 아직 int_str이 남아있는 경우(,가 안오기 때문)
            answer.append(int_str)

    for v2 in sorted(answer):
        if v2 not in answer2:
            answer2[v2] = 1
        else:
            answer2[v2] += 1

    for v3 in sorted(answer2.items(), key=lambda x: x[1], reverse=True):
        answer3.append(int(v3[0]))

    return answer3


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]


# 다른 풀이 : 정규표현식
""" 
def solution(s):
    
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
"""
