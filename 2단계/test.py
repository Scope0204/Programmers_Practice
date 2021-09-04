def solution(number):
    a = list(map(str, number))

    for i in range(len(a)):
        a[i] = a[i]*2

    return sorted(a, reverse=True)


print(solution([3, 30, 34, 5, 9]), "9534330")
