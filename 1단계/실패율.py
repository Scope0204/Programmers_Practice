# 실패율 정의
"""
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
"""

# 제한사항
"""
1. 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
2. stages의 길이는 1 이상 200,000 이하이다.
3. stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
  3-1. 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
  3-2. 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
4. 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
5. 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
"""


def solution(N, stages):
    users = len(stages)
    a = {}  # 실패율

    for i in range(1, N+1):
        # 갯수/ 플레이 사용자 수
        if stages.count(i):
            a[i] = stages.count(i) / users
            users = users - stages.count(i)
        else:
            a[i] = 0

    print(a)
    return sorted(a, key=lambda x: a[x], reverse=True)


# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

# N : 전체 스테이지 개수, stages : 현재 멈춰있는 스테이지 번호
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 리턴
