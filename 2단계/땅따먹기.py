# 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙


def solution(land):
    for y in range(1, len(land)):
        for i in range(4):  # 열의 갯수는 고정 4개
            land[y][i] = max([land[y][i] + land[y-1][j]
                             for j in range(4) if not i == j])
    return max(land[-1])


# print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))


# 동적 계획법( dynamic programming ) . 통칭 dp를 활용한 문제임
# 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법
# 해결된 문제의 답을 저장해두고 그것을 재활용하여 해결된 문제를 다시 푸는 비효율을 제거한다
# 공간복잡도를 늘리고 시간복잡도를 줄이는 방식
# 대표적으로 피보나치 수열이 있음

# 다른풀이

"""
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

"""
