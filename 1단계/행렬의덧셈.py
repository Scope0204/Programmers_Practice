# 좀 어려운듯

# def solution(arr1, arr2):
#     # answer = []

#     # for i in range(len(arr1)):
#     #     arr_sum = []
#     #     for j in range(len(arr1[0])):  # len(arr1[0]) : 행렬의 첫번째 값의 길이
#     #         arr_sum.append(arr1[i][j] + arr2[i][j])
#     #     answer.append(arr_sum)

#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

#     return answer


def solution(arr1, arr2):

    for a, b in zip(arr1, arr2):
        for c, d in zip(a, b):
            print(c, d)
    # 이해가 어렵다
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2))

# zip() 함수를 활용하면 더욱 쉽게 풀이
# zip()란? 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
