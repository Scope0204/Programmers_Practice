# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

# 필요조건 : 2진수 변환, 1의 갯수 세기
# 파이썬은 기본적으로 10진수 형태
# bin(): 2진수 , oct():8진수 , hex(): 16진수
# 숫자 앞에 접두어가 붙음
"""
2진수: 0b
8진수: 0o
16진수: 0x
"""


def solution(n):

    count = 1
    while True:
        if bin(n+count).count("1") == bin(n).count("1"):  # 2진수도 count 됨
            break
        count += 1
    return n+count


print(solution(15))
