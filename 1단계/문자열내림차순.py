"""
def solution(s):
    a = list(s)
    b = list()
    for i in range(len(s)):
        b.append(chr(ord(a[i])))

    b.sort(reverse=True)
    return "".join(b)


print(solution("Zbcdefg"))

"""
# 팁 : 아스키코드로 변환안해도 자동으로 바뀜.


def solution(s):
    a = list(s)

    a.sort(reverse=True)
    return "".join(a)


print(solution("Zbcdefg"))
