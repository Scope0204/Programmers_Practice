def solution(s):
    a = list(s)
    p = 0
    y = 0
    for i in range(len(a)):
        if ord(a[i]) == 112 or ord(a[i]) == 80:
            p += 1
        elif ord(a[i]) == 121 or ord(a[i]) == 89:
            y += 1

    return True if p == y else False
    # return p, y


print(solution("Pyyp"))

# p: 112 , P: 80 , o : 111 , y:121 , Y:89

# 다른 풀이
"""
def numPY(s):
    # return s.lower().count('p') == s.lower().count('y')
    return s.upper().count('p') == s.upper().count('y')

print(numPY("Pyy"))
"""
