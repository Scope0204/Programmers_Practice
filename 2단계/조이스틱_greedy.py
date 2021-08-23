def solution(name):

    answer = 0
    min_move = len(name) - 1
    next = 0

    for i in name:
        if ord(i) <= 78:  # 중간인 78도 포함
            answer += ord(i)-ord("A")
        elif ord(i) > 78:  # - 가 더 가까움
            answer += ord("Z") - ord(i) + 1

    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)

    answer += min_move

    return answer


print(solution("ZAAAZZZZZZZ"))
# print(solution("ABABAAAAAAABA"))


# 알파벳은 26개
# 중간인 13번쨰는 N(78) 그 이상은 - 커서, 그 이하는 + 커서
# 기본은 A(65)
