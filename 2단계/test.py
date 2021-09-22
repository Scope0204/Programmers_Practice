def solution(s):
    result = []
    same = {}
    count = 0
    for i in range(0, len(s), 3):
        if result and result[-1] == s[i:i+3]:
            if result[-1] not in same:
                count += 2
            else:
                count += 1

            same[result[-1]] = str(count)

        else:
            count = 0
            result.append(s[i:i+3])

    return same


print(solution("abrabcabcadqabcabc"))  # abr2abcabq2abc
