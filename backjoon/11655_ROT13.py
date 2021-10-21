# ROT13은 카이사르 암호의 일종으로
# 영어 알파벳을 13글자씩 밀어서 만든다.
# 예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다.

# ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다.
# 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
# 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.

# a ~ z : 97 ~ 122  // A ~ Z : 65 ~ 90
s = input()
answer = ''

for i in s:
    if i.isdigit() or i == ' ':
        answer += i
    else:
        if ord(i) < 91:  # 대문자
            answer += chr(ord(i)+13-91+65 if ord(i)+13 > 90 else ord(i)+13)
        else:  # 소문자
            answer += chr(ord(i)+13-123+97 if ord(i)+13 > 122 else ord(i)+13)

print(answer)
