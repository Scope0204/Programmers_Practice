def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] not in answer:
                    answer.append(numbers[i] + numbers[j])

    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))

# 다른 풀이
# 파이썬 set에서는 같은 요소가 존재할 수 없음
"""
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

"""

# 다른 풀이 2
# from itertools import combinations 하여 조합을 구하는 내장 함수가 있음
