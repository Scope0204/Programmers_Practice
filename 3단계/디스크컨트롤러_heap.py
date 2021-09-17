import heapq


def solution(jobs):
    answer = 0
    work_time = 0
    count = 0

    jobs.sort()  # 시작시간 순으로 정렬

    while jobs:

        heap = []
        count += 1

        for start, time in jobs:
            if heap == []:
                if work_time < start:  # 다음에 실행되는 순서의 요청시간이 현재 시간보다 뒤에 있을경우
                    work_time = start  # 그 다음 작업이 시작되는 시간 => 현재 작업의 요청시간이 됨
                heapq.heappush(heap, [time, start])

            elif start <= work_time:  # 현재 작업시간 보다 빨리 요청되는 작업들을 힙에 넣는다
                heapq.heappush(heap, [time, start])

        # if len(heap) > 1:  # 만약 현재 작업시간보다빨리 작업이 요청되는 것이 2개 이상일 경우
        work = heapq.heappop(heap)  # time, 작업의 소요시간이 가장 적은것을 꺼낸다.
        jobs.remove([work[1], work[0]])  # jobs에도 해당 값을 빼준다

        # 현재 작업시간 + 작업의 소요시간 - 작업이 요청되는 시점
        answer += work_time + work[0] - work[1]

        # 현재 작업시간에 요청처리 시간을 더함 -> 그다음 작업이 시작되는 시간
        work_time = work_time + work[0]

    return answer//count


print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[0, 1], [1, 2], [500, 6]]))

# [작업이 요청되는 시점, 작업의 소요시간]
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리한 것을 리턴
# 소수점 이하의 수는 버림

# 1. 현재 시간에 들어온 요청이 있다 ( 힘에 요청들 넣는 과정)
# 1-2. (없는경우) 들어올 요청 중 가장 빠른 시간을 현재 시간으로 지정
# 2. 들어온 요청(힙) 중 가장 작은 요청을 꺼낸다
# 3. 현재 시간에 요청처리 시간을 더한다
