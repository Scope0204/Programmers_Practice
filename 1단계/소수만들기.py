def solution(nums):

    nums_list = []
    answer = 0

    for a, b in enumerate(nums):
        for c, d in enumerate(nums):
            for e, f in enumerate(nums):
                if a < c and c < e:
                    nums_list.append(b+d+f)

    # new_list = set(nums_list)

    for i in nums_list:
        count = 1

        while 1:
            if i-count == 1:
                answer += 1
                break

            if i % (i-count) == 0:
                break

            count += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))


# 다른풀이 : combinations 함수
"""
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

"""

# 다른풀이2
"""
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])
"""
