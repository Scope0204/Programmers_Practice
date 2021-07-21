import math


def solution(n):
    a = int(math.sqrt(n))
    return (a+1)**2 if a**2 == n else -1


print(solution(121))

# **(1/2) 는 제곱근이다
"""
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'

"""
