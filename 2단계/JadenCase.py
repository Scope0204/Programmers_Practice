# JadenCase?
# 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열

def solution(s):

    s = list(s)
    answer = ""

    for i in range(len(s)):

        if i == 0 and s[i].isalpha or i-1 > 0 and s[i-1] == " ":  # isalpha 안해도될듯?
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer


print(solution("3people unFollowed me"))
print(solution("for the last week"))


# isalpha() : 문자열이 문자인지 아닌지
# isdigit() : 문자열이 숫자인지 아닌지

# 다른 풀이 : 공백때문에 오답이 나오지만 , title 내장함수를 참고
"""
return s.title() 

"""
# title() : 문자열을 단어 앞만 대문자로 바꿀 수 있음
