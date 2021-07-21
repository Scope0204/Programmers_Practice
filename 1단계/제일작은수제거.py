# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수
def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
    else:
        arr.remove(min(arr))
    return arr


print(solution([4, 3, 2, 1]))

# 최소값 : min() / 최대값 : max()
