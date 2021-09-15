def solution(nums):

    answer = []
    for i in nums:
        if len(answer) == len(nums)/2:
            break

        if i not in answer:
            answer.append(i)

    return len(answer)


print(solution([3, 1, 2, 4]))

# 다른 풀이
"""
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""
