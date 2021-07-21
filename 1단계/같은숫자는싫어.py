def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i < len(arr):
            if i == 0:
                answer.append(arr[i])

            elif arr[i] != arr[i-1]:
                answer.append(arr[i])

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))

# 다른 풀이
# slice 활용
# a[-1: ] : -1번쨰(가장 뒤)에서 끝까지 반환
# continue : 코드 실행 건너뛰기
"""
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a[-1]


print(no_continuous([1, 1, 3, 3, 0, 1, 1]))

"""
