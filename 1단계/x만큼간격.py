def solution(x, n):
    answer = []
    x2 = x  # 초기의 x값
    for i in range(n):
        answer.append(x)
        x = x+x2
    return answer


print(solution(3, 5))


# 문제 : 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴


# 핵심은 등차수열(좋은 예시)
# def solution(x, n):
#     answer=list(range(x, x*(n+1) ,x))
#     return answer

# range(start, stop, step)
