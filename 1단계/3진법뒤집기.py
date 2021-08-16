def solution(n):

    a = ""

    while n:
        a += str(n % 3)
        n = n // 3

    return int(a, 3)


print(solution(125))
