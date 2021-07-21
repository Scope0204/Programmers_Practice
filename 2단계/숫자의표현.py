def solution(n):
    count = 0

    for i in range(n):  # 0~14
        a = 1
        s = i+1  # 현재 숫자
        while s < n:  # 0 < 15
            s += a
            a += 1  # a++

            if s == n:
                count += 1

    return count


print(solution(10))
