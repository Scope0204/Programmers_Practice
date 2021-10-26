"""
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 
두 소수의 순서만 다른 것은 같은 파티션이다.
"""

# 에라토스테네스의 체
r = 1000001
prime_list = [True for _ in range(r)]
for i in range(2, int((r-1)**0.5)+1):
    if prime_list[i]:
        for j in range(i+i, r, i):
            prime_list[j] = False

t = int(input())

for _ in range(t):
    count = 0

    n = int(input())
    for a in range(2, n//2+1):
        if prime_list[a] and prime_list[n-a]:
            count += 1

    print(count)
