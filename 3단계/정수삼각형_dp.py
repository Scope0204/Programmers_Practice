def solution(triangle):

    map = [ v for v in triangle]

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                map[i][j] += map[i-1][j]
            elif j == i:
                map[i][j] += map[i-1][j-1]
            else:
                map[i][j] = max(map[i-1][j-1],map[i-1][j]) + triangle[i][j]

    return max(map[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
