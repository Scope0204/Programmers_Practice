def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(n, k):
    answer = 0
    now = ''
    if k == 10:
        number = str(n)
    else:
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += str(mod)
        number = rev_base[::-1]

    for i, j in enumerate(number):
        if j != "0":
            now += j
        elif j == "0" and now:
            if now == "1":
                now = ''
            else:
                if is_prime_number(int(now)):
                    answer += 1
                    now = ''

        if i+1 == len(number) and now:
            if not now == "1":
                if is_prime_number(int(now)):
                    answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))

# print(is_prime_number(11))

# 안되는거 0, 10, 20 , /...
