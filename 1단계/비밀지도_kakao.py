def binary(num, n):
    answer = []
    while len(answer) < n:
        if num:
            answer.insert(0, num % 2)
            num = num // 2
        else:
            answer.insert(0, 0)

    return answer


def solution(n, arr1, arr2):
    answer = ['']*n

    for i in range(n):
        a, b = binary(arr1[i], n), binary(arr2[i], n)
        for j in range(n):
            if a[j] == 1 or b[j] == 1:
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))


# 다른풀이: 정규식을 쓰는 코드
"""
import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer
"""

# 다른풀이2 : 비트연산자. rjust
"""
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

"""
