def solution(arr1, arr2):
    # 2중 for문으로 2중 리스트 선언
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]
    # # column : 열  /  row : 행

    for i, value1 in enumerate(arr1):
        for k, value2 in enumerate(value1):
            for j in range(len(arr2[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
# print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
#       [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

# 곱셈 시, 앞에 행렬의 열의 수와 뒤에 행렬의 행의 수가 같아야하고 최종적으로 나오는 행렬은 앞에 행렬의 행의 수 x 뒤에 행렬의 열의 수 가된다.
# 예를들면 5x3 과 3x7을 곱하면 결과 행렬은 5x7이 나온다
