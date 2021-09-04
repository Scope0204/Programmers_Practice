def solution(citations):
    answer = []*len(citations)
    a = sorted(citations)
    for i in a:
        # 0 1 3 5 6
        if i > len(citations)-(a.index(i)):  # 현재수 > 인용한 수
            answer.append(len(citations)-(a.index(i)))
        else:
            answer.append(i)

    return max(answer)


print(solution([3, 0, 6, 1, 5]))
print(solution([1, 1, 1, 1, 1]))  # 1, 1, 1, 1 -> 1
print(solution([5, 5, 5, 5]), "4")  # 4, 4, 4, 4, -> 4


# 다른풀이 : enumerate 의 내장함수 start 활용
"""
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
"""
# 6 5 3 1 0
# 1,6 min -> 1 / 2,5 min -> 2 / 3,3 min -> 3 / 4,1 min -> 1 / 5,0  min -> 0
# answer 의 max 값 : 3
