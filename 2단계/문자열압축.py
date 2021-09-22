def solution(s):
    answer = ['']*len(s)
    n = 0

    while n < len(s):
        result = []
        same = {}
        count = 0
        n += 1

        for i in range(0, len(s), n):
            if result and result[-1] == s[i:i+n]:  # result 의 마지막 값과 중복되는 경우
                if result[-1] not in same:
                    count += 2
                else:
                    count += 1
                same[result[-1]] = str(count)  # same 리스트에 count를 저장한다

            else:  # 중복되지않는 경우
                count = 0  # 중복 카운터를 초기화
                if same:  # 중복 리스트가 있는경우
                    for v2 in same:
                        result.append(same[v2])  # result에 중복됫 횟수를 저장

                    result.append(s[i:i+n])  # result에 중복되지않은 현재 값을 저장

                    same = {}  # 중복 리스트초기화
                else:
                    result.append(s[i:i+n])  # 아닌경우도 동일

        if same:
            for v2 in same:
                result.append(same[v2])  # 마지막이라 남은 same도 result에 중복됫 횟수를 저장

        answer[n-1] = len(''.join(result))
        # n번째가 끝난 후 result의 값을 전부 합쳐서 저장

    return min(answer)


# print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"))
# print(solution("abrabcabcadqabcabc"))  # abr2abcabq2abc

print(solution("aabbaccc"))
