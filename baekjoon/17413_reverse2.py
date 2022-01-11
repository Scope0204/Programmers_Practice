s = input()
word = []
answer = ''
temp = True
for i in s:
    if i == '<':
        if word:
            answer += ''.join(reversed(word))
            word = []
        answer += '<'
        temp = False

    elif i == '>':
        answer += '>'
        temp = True

    else:
        if temp:
            if i == ' ':
                answer += ''.join(reversed(word)) + ' '
                word = []
            else:
                word.append(i)
        else:
            answer += i

if word:
    answer += ''.join(reversed(word))

print(answer)

# 구현, 문자열
