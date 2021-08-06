def solution(array, commands):

    answer = []
    for i in range(len(commands)):
        answer.append(
            sorted(array[commands[i][0]-1: commands[i][1]])[commands[i][2]-1])

    return answer


# n-1 번쨰 ~ n번째


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# 다른 풀이
# lambda 함수 활용
"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""
