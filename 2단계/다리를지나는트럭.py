# 속도가 많이 느림. pop,sum 개선
def solution(bridge_length, weight, truck_weights):

    bridge = [0]*bridge_length
    answer = 0

    while bridge:
        answer += 1
        bridge.pop(0)  # 매 시간 가장 앞을 비워줌
        if truck_weights:
            # 다리위의 차 무게값의 합 <= 제한된 무게값
            if sum(bridge)+truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))  # 트럭 앞순서부터 출발
            # 이미 무게가 꽉찻을 경우
            else:
                bridge.append(0)  # 공기를 채워줌

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 참고할만한 힌트
"""
(Shift의 느낌으로 풀었습니다)

큐는 선입선출의 구조임을 이용해
시간에 따라 한칸씩 이동하는 것을 구현한다면

for(int i=0;i<bridge_length;i++)
    q.push(0);
이렇게 해서 큐를 다리라고 생각하고 공기(0)들을 미리 채운 다음에
매 시간마다 pop하고 현재 다리 위의 무게에 따라 트럭을 push하거나 공기(0)를 push해보는건 어떨까요!

"""
