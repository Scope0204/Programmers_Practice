def solution(triangle):
    answer = 0
    map = [v for v in triangle]
    plus = []

    for i, v in enumerate(triangle):
        for i2, v2 in enumerate(v):
            if i == 0:
                map[1][0] += v[0]
                map[1][1] += v[0]
            elif i == len(triangle)-1:
                break
            else:
                map[i+1][i2] += v2
                map[i+1][i2+1] += v2

    return map


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
