# 소문자, 대문자, 숫자, 공백의 갯수
# EOF (python 입력이 끝날때 까지 출력)를 사용하여 문제를 받음
# End of File

def solution(s):

    if s == '':
        return -1
    else:
        answer = [0] * 4

        for i in s:
            if i.islower():  # 소문자인 경우
                answer[0] += 1
            elif i.isupper():  # 대문자인 경우
                answer[1] += 1
            elif i.isdigit():  # 숫자인 경우
                answer[2] += 1
            elif i == ' ':  # r공백의 경우
                answer[3] += 1

        return ' '.join(map(str, answer))


while 1:
    try:
        s = input()
        if solution(s) == -1:
            break
        else:
            print(solution(s))
    except EOFError:
        break

# 구현,문자열
