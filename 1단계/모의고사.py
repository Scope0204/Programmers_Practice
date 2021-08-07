def solution(answers):
    answer = [0, 0, 0]

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    top_score = []

    for i in range(len(answers)):

        print(first[i % len(first)],  second[i %
              len(second)],  third[i % len(third)], answers[i])

        if first[i % len(first)] == answers[i]:
            answer[0] += 1
        if second[i % len(second)] == answers[i]:
            answer[1] += 1
        if third[i % len(third)] == answers[i]:
            answer[2] += 1

    for j in range(len(answer)):
        if max(answer) == answer[j]:
            top_score.append(j+1)

    return top_score


print(solution([1, 3, 2, 4, 2]))

# 1번 : 12345 | 12345
# 2번 : 21 23 24 25 |  21 23 24 25
# 3번 : 33 11 22 44 55 | 33 11 22 44 55
