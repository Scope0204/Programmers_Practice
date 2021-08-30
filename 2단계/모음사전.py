def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    now = []
    count = 0  # 마지막 5번째 자리에서 바뀌는 값

    while 1:

        if "".join(now) == word:
            break

        answer += 1

        if len(now) != 5:
            count = 0
            now.append('A')

        elif len(now) == 5 and now[-1] == 'U':

            while now[-1] == 'U':
                now.pop()

            if alpha.index(now[-1])+1 <= 4:
                # U를 모두삭제하고 마지막 값을 다음 값으로 변경한다
                now[-1] = alpha[alpha.index(now[-1])+1]
            else:
                now[-1] = alpha[0]

        elif len(now) == 5:
            count += 1
            now[4] = alpha[count]

    return answer


# print(solution("AAAAE"))
# print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))


# 다른풀이 : product, lambda / 길이가 5인점을 이용하여 전부 생성
"""
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
"""
