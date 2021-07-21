def solution(a, b):
    sum = 0
    if a > b:
        for i in range(a, b-1, -1):
            sum += i
    else:
        for i in range(a, b+1):
            sum += i

    return sum


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))


# 다른 풀이

# 1. sum함수 사용
"""
  if a > b: a, b = b, a

    return sum(range(a,b+1))

"""

# 2. 절대값 사용, 함수 abs()
# 수열공식  n(n+1)/2 => 정수 사이의 값이 출력
"""
return (abs(a-b)+1)*(a+b)//2

"""
