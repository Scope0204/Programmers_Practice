# 중복순열 풀이 -> 런타임에러
"""
def solution(n):
    answer = 0
    num = n

    while num >= n//2 + n % 2:
        for combi in product([1, 2], num):
            print(combi)
            if sum(combi) == n:
                answer += 1
        num -= 1

    return answer % 1000000007


def product(arr, r):
    for i in range(len(arr)):  # 함수에서 지금할 일
        if r == 1:  # 종료조건
            yield [arr[i]]
        else:
            for next in product(arr, r-1):  # 다음에 할 일
                yield [arr[i]] + next


print(solution(4))

# 1111 112 121 211 22  /  4//2
# 11111 1211 1121 1112 2111 122 221 / 5//2 + 1

"""


def solution(n):
    if n < 3:
        return n
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a % 1000000007


print(solution(4))
