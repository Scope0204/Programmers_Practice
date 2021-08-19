def solution(number, k):

    a = list(number)
    b = len(number) - k  # 출력해야할 숫자 길이 = 원래 숫자 길이 - 빼야할 길이
    answer = ""  # 맞는 숫자를 담는 칸
    count = 0  # 삭제하지 않은 숫자

    for i in range(len(number)):
        now = 0
        for j in range(count, len(number)):
            if number[i] < number[j]:
                if len(number) - k - len(answer) > len(number) - j:
                    break

    return answer


print(solution("1231234", 3))
print(solution("4177252841", 4))


# 빼야할 숫자의 조건.
# 1. 나보다 큰 수가 뒤에 있으면 안됨.
# 2. 만일 뒤에 있는 경우 해당숫자로부터 출력해야할 숫자길이가 된다면 뺌.
# 3.
