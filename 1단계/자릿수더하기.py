def solution(n):
    a = list(map(int, str(n)))
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum


print(solution(987))
