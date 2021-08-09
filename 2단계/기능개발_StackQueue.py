def solution(progresses, speeds):

    clear_speed, answer = [], []

    for i in progresses:
        clear_speed.append((100 - i) / speeds[progresses.index(i)])

    return answer

# progresses : 먼저 배포 되어야하는 순서대로의 작업의 진도 / speeds: 각 작업의 속도
# 뒤의 작업은 전의 작업이 완료되지 않으면 배포가 안됨
# 배포시 뒤의 작업은 같이 나감


print(solution([93, 30, 55], [1, 30, 5]))
# 7 , 3 , 9 -> 완료 순서 2-1-3
# 첫 배포-> 2,1 -> 2개
# 두번째 배포-> 3 -> 1개


# print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]))
# 5,10,1,1,20,1 -> 완료순서 3,4,6-1-2-5
# 첫 배포 -> 1
# 두 번째 배포 -> 2,3,4
# 세 번쨰 배포 -> 5,6

# 100이거나 그 이상일 경우 작업 종료
# len(progresses) 와 len(speeds) 는 같음
# 배포할 index보다 전의 index에서 value 값보다 -1이 있을 경우 +1
