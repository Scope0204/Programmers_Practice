def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)  # 내림차순정의
    return int("".join(n_list))


print(solution(118372))
# n의 각 자릿수를 큰것부터 작은 순
