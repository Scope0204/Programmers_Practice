# # 조합문제
# # 조합이란 서로 다른 n개중에 r개를 선택하는 경우의 수를 의미합니다. (순서 상관 없음)
# # nCr = n!/(n-r)!r!

# n, m = map(int, input().split())

# answer = 1

# for i in range(n, n-m-1, -1):
#     answer *= i

# for j in range(n-m):
#     answer //= j+1

# count = 0

# for k in reversed(str(answer)):
#     if k == '0':
#         count += 1
#     else:
#         break

# print(count)

n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two


def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five


print(min(two_count(n) - two_count(n - m) - two_count(m),
      five_count(n) - five_count(n - m) - five_count(m)))

# 이해 필요.
