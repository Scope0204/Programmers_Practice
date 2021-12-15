# 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 
# 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
# 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
from collections import Counter

def solution(str1, str2):
    
    a = [] 
    for i in range(0,len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append((str1[i]+str1[i+1]).upper())    

    b = []
    for i in range(0,len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append((str2[i]+str2[i+1]).upper())    

    Counter1 = Counter(a)
    Counter2 = Counter(b)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())


    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))

print(solution('abcccc','cccdefff'))
print(solution('abccc','ccdefgg'))
print(solution("A+C","DEF"))
