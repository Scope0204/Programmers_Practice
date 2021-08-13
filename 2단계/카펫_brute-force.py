def solution(brown, yellow):

    a = (brown - 4) // 2

    for i in range(1, a+1):
        if i * (a - i) == yellow:
            return [a-i+2, i+2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

# (brown - 4) / 2
# n + m = yellow -> result : [m+2,n+2]
