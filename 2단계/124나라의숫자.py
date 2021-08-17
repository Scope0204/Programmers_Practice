def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        # 각 자리수 별로 표현할 수 있는 숫자가 1부터 시작하는 것을 0부터 시작하는 것으로 바꿔야함
        n //= 3
    return answer
