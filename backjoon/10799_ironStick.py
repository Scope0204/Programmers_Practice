s = input()
stick = 0
answer = 0

for i, v in enumerate(s):
    if v == '(':
        stick += 1
    elif v == ')':
        if s[i-1] == '(':  # 그 전이 ( 일경우 레이저임 = ()
            stick -= 1  # 그 전 stick으로 처리한것이 레이저이므로 지워줌
            answer += stick
        else:  # 하나의 stick이 끝남.
            stick -= 1
            answer += 1

print(answer)

# 자료구조, 스택
