"""
def solution(s):
    a = s.split(" ")
    b = ""

    for i in range(len(a)):
        for j in range(len(a[i])):
            if j % 2 == 0:
                b += a[i][j].upper()
            else:
                b += a[i][j].lower()

        if i+1 < len(a):
            b += " "

    return b
    
"""


# 다른 풀이
"""
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
"""


def toWeirdCase(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])


print("결과 : {}".format(toWeirdCase("try hello world")))
