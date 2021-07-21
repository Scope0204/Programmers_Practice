def solution(phone_number):
    a = list(phone_number)  # 문자열을 배열로 list()
    for i in range(len(a)):
        if len(a) - i > 4:
            a[i] = "*"
    b = "".join(a)  # 배열을 문자열로 joun()
    return b


phone_number = "01033334444"
print(solution(phone_number))

# 문자열을 곱셈이 가능한 점을 생각하면 더 쉽다
# 총 핸드폰 번호의 길이만 알면 간단. 어차피 뒤에 4개만 바꾸면 되니깐
# return "*"*(len(phone_number)-4) + s[-4:]
