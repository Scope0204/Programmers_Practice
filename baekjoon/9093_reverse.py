n = int(input())

for _ in range(n):
    word = str(input())
    save = ""
    answer = ""

    for i, v in enumerate(word):
        if i == len(word)-1:
            save += v
            answer += save[::-1]
        elif v != ' ':
            save += v
        else:  # 공백의 경우
            answer += save[::-1]+' '
            save = ''
    print(answer)

    # 구현, 문자열
