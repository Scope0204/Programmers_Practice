# 문자열 s에는 공백으로 구분된 숫자들이 저장
# str에 나타나는 숫자 중 최소값과 최대값을 찾아
# 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수


def solution(s):

    a = []
    for i in s.split():
        a.append(int(i))

    a.sort()

    return "{0} {1}".format(a[0], a[len(a)-1])


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))


# 다른 풀이
# map함수를 잘 활용하자
"""
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

"""
