def solution(n):
    answer = list(map(int, str(n)))
    # answer.reverse()
    # reverse메소드 자체의 반환 값이 없어 루프를 돌릴 수 없음. 따라서 reverse 작업 후 루프를 돌려야함.

    return reversed(answer)  # reversed()또한 값을 반환함

    # return list(map(int, reversed(str(n))))


print(solution(12345))
