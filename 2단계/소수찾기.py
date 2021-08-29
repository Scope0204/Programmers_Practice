from itertools import permutations


def solution(numbers):

    answer = 0
    num_list = []

    for i in range(1, len(numbers)+1):
        a = list(permutations(numbers, i))
        for j in a:
            if int("".join(j)) not in num_list:
                num_list.append(int("".join(j)))

    # for a in num_list:
    #     count = 1
    #     if a != 0 and a != 1:
    #         while 1:
    #             if a-count == 1:
    #                 answer += 1
    #                 break

    #             if a % (a-count) == 0:
    #                 break

    #             count += 1

    for a in num_list:
        if a != 0 and a != 1:
            for b in range(2, a):
                if a % b == 0:
                    break
            else:
                answer += 1

    return answer


print(solution("17"))


# 다른 풀이 : 에라토스테네스의 체 활용, list,map,set
"""
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

"""
