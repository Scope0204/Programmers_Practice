def solution(s):

    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else:
        return False


print(solution("1234"))

# 다른풀이 : isdigit()내장 함수 이용하기
# 문자열의 구성이 알파벳인지에 대해서 확인하는 방법

"""

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

"""
