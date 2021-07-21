# 소수 : Prime Number. 1과 자기자신 외에는 나누어떨어지지 않는 수
# 약수의 중간값을 기준으로 한 쪽만 검사를 하더라도 다른 쪽의 약수들을 알 수 있다.

# 소수 판별 알고리즘 -> 에라토스테네스의 체
"""
<에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법>
1. 1은 제거 
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다. 
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다. 
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다. 
5. (반복)
"""


# def solution(n):
#     num_lst = set(range(1, n+1))
#     num_lst -= set([1])

#     for i in range(2, n+1):
#         num_lst -= set(range(2*i, n+1, i))

#     return len(num_lst)


def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:  # 세트(num)에 특정값(i)이 있는지 확인 : in
            print(num)

            num -= set(range(2*i, n+1, i))
    return len(num)


print(solution(10))
