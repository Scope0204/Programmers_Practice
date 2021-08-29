def solution(progresses, speeds):

    answer = []

    while progresses:
        count = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        for j in progresses:
            if j >= 100:
                count += 1
            else:
                break

        if count > 0:
            for _ in range(count):
                progresses.pop(0)
                speeds.pop(0)

            answer.append(count)

    return answer

# progresses : 먼저 배포 되어야하는 순서대로의 작업의 진도 / speeds: 각 작업의 속도
# 뒤의 작업은 전의 작업이 완료되지 않으면 배포가 안됨
# 배포시 뒤의 작업은 같이 나감


print(solution([93, 30, 55], [1, 30, 5]))
# 7 , 3 , 9 -> 완료 순서 2-1-3
# 첫 배포-> 2,1 -> 2개
# 두번째 배포-> 3 -> 1개


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# 5,10,1,1,20,1 -> 완료순서 3,4,6-1-2-5
# 첫 배포 -> 1
# 두 번째 배포 -> 2,3,4
# 세 번쨰 배포 -> 5,6

# 100이거나 그 이상일 경우 작업 종료
# len(progresses) 와 len(speeds) 는 같음


# 다른 풀이 : zip 함수, -100
"""
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""
