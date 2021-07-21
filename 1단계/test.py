def solution(n):

    a = 0
    for i in str(n):
        print(i)
        a += int(i)

    return a


print(solution(11))

# def solution(arr):
#     min = list(arr)
#     min.sort()
#     arr.remove(min[0])
#     return [-1] if arr == [] else arr


# print(solution([4, 3, 2, 1]))
