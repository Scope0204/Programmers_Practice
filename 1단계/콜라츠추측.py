def solution(num):
    result = 0  # 반복횟수

    while num != 1:
        result = result + 1  # 반복마다 횟수 증가
        if num % 2 == 0:  # 짝수의 경우
            num = num / 2
        else:  # 홀수의 경우
            num = num * 3 + 1
        if result > 500:
            result = -1
            break

    return result


print(solution(1))

# 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측

# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.


# 다른 풀이
# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         # 영어 어휘처럼 ㅇㅇ다 ㅁㅁ면의 형식으로 조건문을 만들 수 있다.
#         if num == 1:
#             return i + 1
#     return -1
