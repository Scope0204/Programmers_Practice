"""
1. 구명보트 최대 인원은 2명. 무게제한 잇음
2. 구명보트를 최대한 적게 사용하여 구출
"""


def solution(people, limit):

    people.sort()
    a, b = 0, len(people)-1
    answer = 0  # 구명보트 수

    while a <= b:
        answer += 1
        if people[a]+people[b] <= limit:
            a += 1
        b -= 1

    return answer


print(solution([20, 50, 50, 80], 100))


""" 
# 오답 
def solution(people, limit):

    answer = 0  # 구명보트 수
    people.sort(reverse=True)
    count = 0

    while count < len(people):
        for i in range(len(people)):
            if count != i and people[count] + people[i] <= limit:
                people.pop(i)
                break

        answer += 1
        count += 1

    return answer


print(solution([70, 50, 80, 50], 100))
"""
