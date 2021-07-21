# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다.
# 이러한 과정을 배열의 길이만큼 반복하며 두 수를 곱한 값을 누적하여 더합
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표
# 단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.

def solution(A, B):

    A.sort()
    B.sort(reverse=True)

    answer = 0

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer


print(solution([1, 4, 2], [5, 4, 4]))

# 다른풀이 : 한줄코드
#  return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
