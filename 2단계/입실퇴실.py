"""
def solution(enter, leave):
    answer = [0] * len(enter)

    for v in leave:
        now = []
        index = 0
        for v2 in enter:
            if leave[index] not in now:  # 아직 나보다 우선순위가 앞인 숫자가 나타나지않은경우
                now.append(v2)

            while 1:
                if leave[index] in now:
                    if leave[index] == v:
                        break

                    if v not in now:  # 앞의 우선숫자가 먼저 나간경우 -> 그 숫자는 못본 것
                        now.remove(leave[index])

                    index += 1
                else:
                    break

        answer[v-1] += len(now) - 1

    return answer
"""

# 내 앞의 인덱스가 내가 나올때까지안나옴
# 그럼 계속 진행. 걔가 나올떄까지
# 2 -> 앞에아무도없음 - 2가나올떄까지 하면됨
# 1 -> 앞에 2가잇음 - 2가 나올떄까지함 - 1,4,2 - 자기뒤에 2가나왓으므로 2는 만난거
# 3 -> 앞에 2,1이 있음 - 우선 2부터함 - 1,4,2 - 자기가 아직안나왓으므로 2는 제외(1,4) - 그 다음 1함 - 이미 리스트에잇음 제외(4) - 3이 나올떄 까지함 - 4,3 - 자기는 뺌
# 4 -> 앞에 2,1,3이 있음 - 우선 2부터 - 1,4,2 - 자기뒤에 2가 나왓으므로 2는 만남(1,4,2) - 다음 1 - 자기 앞에 나왓으므로 1은 제외(4,2) - 다음 3 - 4,2,3 - 자기 뒤에있으므로 냄겨둠 - 4 끝

# 효율성 똥


def solution(enter, leave):
    # 사람의 번호가 1번부터 시작하는데 컴퓨터에서 인덱스는 0부터 시작하기 때문에 0번 인덱스를 비워두고 1번부터 시작하기 위해 1 크게 설정
    answer = [[] for _ in range(len(enter)+1)]
    # room은 특정 시간에 회의실에 존재하는 사람들을 저장하는 리스트
    room = []
    ei, li = 0, 0
    while ei < len(enter) or li < len(leave):
        if leave[li] not in room:  # 해당 번호가 들어올 때 까지 사람을 room에 저장 -> 마주친 사람들
            answer[enter[ei]] = room[:]  # 사람이 입장할 때 answer에 현재 room에 있던 인원을 저장
            room.append(enter[ei])
            ei += 1
        else:
            room.remove(leave[li])
            li += 1

    # 이 과정이 끝나면 answer에는 각자 마주친 사람의 번호가 저장된 리스트가 저장되어 있음
    for p, person in enumerate(answer):
        for met in person:
            answer[met].append(p)  # 다른 번호에 마주친 기억이 있다면 그것또한 저장해둬야함

    return [len(set(i)) for i in answer][1:]
    # set()으로 중복을 없앤 후 마주친 사람의 수를 반환
    # 이때, answer의 0번 인덱스를 비워놨으므로 [1:]로 슬라이싱하여 반환


print(solution([1, 10, 9, 2, 3, 8, 7, 4, 5, 6],
      [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

print(solution([1, 4, 2, 3], [2, 1, 3, 4]))


# 다른 풀이

"""
def solution(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer
"""
