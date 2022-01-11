# 골드바흐의 추측
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.

# 에라토스테네스의 체
r = 1000001
prime_list = [True for _ in range(r)]
for i in range(2, int((r-1)**0.5)+1):
    if prime_list[i]:
        for j in range(i+i, r, i):
            prime_list[j] = False

while 1:
    n = int(input())
    count = 0
    if n == 0:
        break
    else:
        for a in range(3, len(prime_list)):
            if prime_list[a] and prime_list[n-a]:
                print("%d = %d + %d" % (n, a, n-a))
                count = 1
                break
        if count == 0:
            print("Goldbach's conjecture is wrong.")
