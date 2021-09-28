def solution(n):
    ans = 0

    while n > 0:
        if n % 2 != 0:
            n -= 1
            ans += 1
        else:
            n = n/2

    return ans


# 다른 풀이 : 2진법 활용
"""
def solution(n):
    return bin(n).count('1')
"""

# 다른 풀이2 : //
"""
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2 
    return answer
"""
