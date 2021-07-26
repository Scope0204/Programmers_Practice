def solution(arr):
    for i in range(len(arr)):  # 0 1 2 3
        if i+1 < len(arr):  # 4
            a, b = max(arr[i], arr[i+1]), min(arr[i], arr[i+1])
            t = 1
            while t > 0:
                t = a % b
                a, b = b, t
            arr[i+1] = arr[i]*arr[i+1]//a

    return arr[-1]


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))


# 다른 사람풀이
# 함수 gcd를 사용
"""

from fractions import gcd


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));

"""
