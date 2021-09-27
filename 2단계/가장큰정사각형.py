# 동적 계획법(Dynamic Programming) : 복잡한 문제를 여러 개의 작은 부분 문제(Sub-Problem)로 나누어 해결하는 방법
def solution(board):
    length = 0
    flag = False
    map = [rv for rv in board]

    for ri, rv in enumerate(board):
        for ci, cv in enumerate(rv):
            if ri == 0 or ci == 0:  # 가장 첫번째 줄 or 가장 첫번째 (n,0)
                if board[ri][ci] == 1:
                    length = max(length, 1)
                continue
            minimum = min(map[ri-1][ci], map[ri][ci-1])  # 왼쪽, 위
            minimum = min(minimum, map[ri-1][ci-1])  # 왼쪽대각선 위

            if board[ri][ci] == 1:
                map[ri][ci] = minimum+1
                length = max(length, map[ri][ci])

    answer = length*length

    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1], [0, 0, 1, 1, 1]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
# 1, 1, 1 , 1, 1
