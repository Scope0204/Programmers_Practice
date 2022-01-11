def prime(num):
    if num == 1:
        return 0
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return 0
        return 1


m, n = list(map(int, input().split()))

for i in range(m, n+1):
    if prime(i) == 1:
        print(i)

# 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 참고 https://myjamong.tistory.com/139
