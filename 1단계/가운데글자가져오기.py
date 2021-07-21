# 단어의 길이가 짝수라면 가운데 두글자를 반환
# /2 + 1

def solution(s):

    return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2-1:len(s)//2+1]
    # return s[(len(s)-1)//2:len(s)//2+1]
    # // 하면 소숫점도 사라지므로 짝,홀 둘다 한번에 정리가능


print(solution("abcde"))
print(solution("qwer"))
