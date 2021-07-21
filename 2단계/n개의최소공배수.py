def solution(arr):
    arr2 = []
    for i in range(len(arr)):
        for j in range(1, arr[i]+1):
            # print(j, arr[i])
            if arr[i] % j == 0:
                arr2.append(j)
                print(j)
    arr2.sort()
    return arr2


print(solution([2, 6, 8, 14]))
