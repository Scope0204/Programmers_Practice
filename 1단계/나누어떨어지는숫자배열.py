def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    # if answer == []:
    #     answer.append(-1)
    return sorted(answer) or [-1]

# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))


# 다른 풀이
# or [-1] : python은 or 앞이 참일 경우 해당 값 까지만. 거짓일경우 뒤에 것까지 호출
"""
return sorted([n for n in arr if n%divisor == 0]) or [-1]

"""
