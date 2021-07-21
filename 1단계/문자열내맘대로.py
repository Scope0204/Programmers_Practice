def solution(strings, n):

    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 1))

# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.


# 다른 풀이

# return sorted(strings, key=lambda x: x[n])
