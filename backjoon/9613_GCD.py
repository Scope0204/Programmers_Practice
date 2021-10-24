# GCD : 유클리드 알고리즘. 최대공약수 문제

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    c = 1
    while c > 0:
        c = a % b
        a, b = b, c

    return a


n = int(input())

for _ in range(n):
    answer = 0
    t = list(map(int, input().split()))

    for i in range(1, len(t)):
        a = t[i]
        while i < len(t):
            i += 1

            if i == len(t):
                break
            else:
                answer += gcd(a, t[i])

    print(answer)
