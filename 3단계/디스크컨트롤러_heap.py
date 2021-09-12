import heapq


def solution(jobs):
    answer = 0
    heap = []
    work_time = 0

    jobs.sort()

    for i in jobs:
        # a = [i[1], i[0]]
        # heapq.heappush(heap, a)
        heap.append(i)

    heap.sort()

    while heap:
        # b = heapq.heappop(heap)
        b = heap[0]

        if work_time < b[0]:
            work_time = b[0]
            answer += work_time + b[1] - b[0]
        else:
            work_time += b[1]
            answer += work_time - b[0]

        heap.pop(0)

    return jobs


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 1], [1, 2], [500, 6]]))

# [작업이 요청되는 시점, 작업의 소요시간] =>  b[1] , b[0]
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리한 것을 리턴
# 소수점 이하의 수는 버림
