def solution(n):

    for i in range(n):
        if i == 0:
            a, b = 0, 1
        else:
            a, b = b, a+b

    return b % 1234567


print(solution(3))
print(solution(5))


"""
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a


print(fibonacci(3))
"""
