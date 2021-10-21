def prime(num):
    if num == 1:
        return 0
    else:
        for i in range(2, num):
            if num % i == 0:
                return 0
        return 1


n = int(input())
s = list(map(int, input().split()))
answer = 0

for i in range(n):
    answer += prime(s[i])

print(answer)

# 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 참고 https://myjamong.tistory.com/139
