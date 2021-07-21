def solution(s):
    a = 1
    sum = 0
    while a <= s:
        if s % a == 0:
            sum += a
        a += 1
    return sum


print(solution(5))


# 다른 풀이
"""
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    # // 는 결과가 int로 나오고, /는 결과가 float으로 나옴
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

"""
