def solution(x):
    a = list(map(int, str(x)))  # 각 숫자의 리스트 , [1, 0]
    b = 0  # 자릿수의 합
    for i in range(len(a)):  # range(2)
        b = b + a[i]  # 1, 0

    # if x % b == 0:
    #     return True
    # else:
    #     return False

    return x % b == 0  # true 인지 false인지는 return을 통해 바로나옴


print(solution(10))


# 다른 풀이
# return x % sum([int(c) for c in str(x)]) == 0

# 하샤드 수 : 양의 정수 자릿수의 합으로 정수가 나누어 떨어지는 것
