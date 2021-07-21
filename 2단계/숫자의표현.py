def solution(n):
    # a, 2a+1, 3a+3 ,4a+6 , 5a+10
    # 0 , 1, 2 ,3, 4 ...
    # n으로 나눠서 나머지가 0인 경우만 성립한다
    # a: 순서 , b: 추가된 수
    a, b = 1, 0 
    answer = 0
    while (n-b)/a > 0:
        if (n-b) % a == 0:
            answer += 1
        b += a
        a += 1
    return answer


print(solution(15))


# 다른 풀이 :  등차수열 합 공식
# return len([i  for i in range(1,num+1,2) if num % i is 0])
