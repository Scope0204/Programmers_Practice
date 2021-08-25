def solution(bridge_length, weight, truck_weights):

    count = 0  # 들어오면 세는거
    start = []  # 출발한 자동차
    now_weight = 0
    answer = 0
    truck = 0

    while truck_weights:
        answer += 1

        if count == bridge_length:
            a = start.pop(0)
            now_weight -= a
            truck_weights.pop(truck_weights.index(a))
            # 제일 앞선 차량 제외하면서 리스트에도 제거

            if start:
                count -= 1
            else:
                count = 0

            truck -= 1

        if truck < len(truck_weights) and truck_weights[truck] <= weight-now_weight:
            start.append(truck_weights[truck])  # 하나씩 뺌
            now_weight += truck_weights[truck]
            truck += 1

        if start:  # 출발한 자동차가 있는경우 카운트 시작
            count += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 다리 길당 1초, 내릴때 1초 걸리는점 확인


# 힌트
"""
(Shift의 느낌으로 풀었습니다)

큐는 선입선출의 구조임을 이용해
시간에 따라 한칸씩 이동하는 것을 구현한다면

for(int i=0;i<bridge_length;i++)
    q.push(0);
이렇게 해서 큐를 다리라고 생각하고 공기(0)들을 미리 채운 다음에
매 시간마다 pop하고 현재 다리 위의 무게에 따라 트럭을 push하거나 공기(0)를 push해보는건 어떨까요!

"""
