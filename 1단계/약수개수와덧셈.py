def divisor(s):
    num = 1
    answer = 0
    while num <= s:
        if s % num == 0:
            answer += 1
        num += 1

    return answer


def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        if divisor(i) % 2 == 0:  # 짝수의 경우
            answer += i
        else:  # 홀수의 경우
            answer -= i

        print(answer, i)
    return answer


print(solution(13, 17))


# 다른풀이 : 제곱수는 약수의 갯수가 홀수임
"""
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
"""
