# def solution(n, m):
#     n2, m2 = n, m
#     while n != m:
#         if n > m:
#             n -= m
#         else:
#             m -= n
#     n3 = (n2 * m2) / n

#     return [n, n3]

# print(solution(3, 12))

# 유클리드 호제법이란?
# 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘의 하나이다.
# 호제법이란 말은 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
# 큰 수에서 작은 수를 나누고 마지막 0으로 나올때 나누는 수가 최대 공약수이다.

# 다른 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)  # 큰수 c 작은수 d
    t = 1
    while t > 0:
        t = c % d  # 큰수에서 작은 수를 나눔
        c, d = d, t  # 작은 수는 큰수가 되고, 나눈 나머지는 작은수가 됨
    answer = [c, int(a*b/c)]  # 최대공약수, 최소공배수(= 두수의 곱 / 최대공약수)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))
