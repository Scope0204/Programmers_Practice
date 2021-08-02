def solution(n, lost, reserve):
    no_clear = len(lost)
    clear = 0
    lost1 = set(lost)
    reserve1 = set(reserve)

    lost1.remove(lost1 & reserve1)

    # for i in lost:  # 같은 값 제거
    #     if i in reserve:
    #         reserve.pop(reserve.index(i))
    #         lost.pop(lost.index(i))
    #         clear += 1

    # for j in lost:
    #     for z in reserve:
    #         if j + 1 == z or j - 1 == z in reserve:
    #             reserve.pop(reserve.index(z))
    #             clear += 1
    #             break

    # return n - no_clear + clear
    return lost1


# level 1
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 수업을 들을 수 있는 학생의 최댓값을 return
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다

print(solution(2, [2, 1], [1, 2]))
