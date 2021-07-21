# def solution(s, n):
#     a = list(s)
#     b = ""

#     for i in range(len(a)):
#         if a[i] != " ":  # 공백의 경우가 아닌경우
#             if 64 < ord(a[i]) < 91:  # 대문자
#                 if ord(a[i]) + n > 90:
#                     b += chr(ord(a[i]) + n - 91+65)
#                 else:
#                     b += chr(ord(a[i]) + n)
#             elif 96 < ord(a[i]) < 123:  # 소문자
#                 if ord(a[i]) + n > 122:
#                     b += chr(ord(a[i]) + n - 123+97)

#                 else:
#                     b += chr(ord(a[i]) + n)

#         else:
#             b += " "

#     return b


# print(solution("a B z", 4))

"""
<아스키코드>
A: 65 ~ Z: 90
a : 97 ~ z: 122  
0: 48 ~ 9: 57 



"""

# 다른 예시
# 알파벳 총 길이 : 26
# 대문자 소문자를 isupper()와 islower()로 구분 -> 나는 아스키코드 범위로 구분하엿음
# upper()은 대문자로 바꿔주는 것. isupper()은 대문자인지 확인하는 것(결과는 True/False)


def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():  # 대문자의 경우
            # (65~90사이의 수) - 65 + n % 26 + 65
            s[i] = chr((ord(s[i])-ord('A') + n) % 26+ord('A'))
        elif s[i].islower():  # 소문자의 경우
            s[i] = chr((ord(s[i])-ord('a') + n) % 26+ord('a'))

    return "".join(s)


print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
