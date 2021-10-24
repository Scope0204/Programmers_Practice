# 첫째줄 : 동생 수 와 현재 나의 위치
# 둘째줄 : 동생들의 위치
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    c = 1
    while c > 0:
        c = a % b
        a, b = b, c

    return a


n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

for i in range(n):

    if i == 0:
        answer = abs(s-a[i])
    else:
        answer = gcd(answer, abs(s-a[i]))

    # print(answer)

print(answer)
