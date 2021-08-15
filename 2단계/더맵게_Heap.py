import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # scovile을 힙으로 변환

    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        else:
            a = heapq.heappop(scoville)  # 힙에서 가장작은 값 삭제 후 값 반환
            b = heapq.heappop(scoville)  # 2개 삭제해야함

            heapq.heappush(scoville, a + (b*2))
            answer += 1

    if scoville[0] >= K:
        return answer
    else:
        return -1


print(solution([1, 1, 1, 1, 1], 4))
# 단, 길이가 2 이하이거나 K이상으로 만들 수 없을 경우 -1 리턴


# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
# (자바의 PriorityQueue 클래스)


# 정확한 풀이 : heap에선 0이 가장 작은 값이 아닐수도 있기 때문
"""
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
"""
