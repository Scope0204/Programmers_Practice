def solution(enter, leave):
    answer = [0] * len(enter)

    for v in leave:
        now = []
        index = 0
        for v2 in enter:

            if leave[index] not in now:  # 아직 나보다 우선순위가 앞인 숫자가 나타나지않은경우
                now.append(v2)

            if leave[index] in now:
                if leave[index] == v:
                    break
                else:
                    while 1:
                        if leave[index] == v:
                            break

                        if leave[index] in now:
                            if v not in now:  # 앞의 우선숫자가 먼저 나간경우 -> 그 숫자는 못본 것
                                now.remove(leave[index])
                            index += 1
                        else:
                            break

        answer[v-1] += len(now) - 1

    return answer


print(solution([1, 10, 9, 2, 3, 8, 7, 4, 5, 6],
      [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# 1. 먼저 들가고 먼저 나감 =, 1-2. 먼저 들갔지만 뒤에 나감 / 2. 뒤에 들어왔지만 먼저 나감 ,  2-2.뒤에 들어오고 뒤에 나감 (말안됨)


# 내 앞의 인덱스가 내가 나올때까지안나옴
# 그럼 계속 진행. 걔가 나올떄까지
# 2 -> 앞에아무도없음 - 2가나올떄까지 하면됨
# 1 -> 앞에 2가잇음 - 2가 나올떄까지함 - 1,4,2 - 자기뒤에 2가나왓으므로 2는 만난거
# 3 -> 앞에 2,1이 있음 - 우선 2부터함 - 1,4,2 - 자기가 아직안나왓으므로 2는 제외(1,4) - 그 다음 1함 - 이미 리스트에잇음 제외(4) - 3이 나올떄 까지함 - 4,3 - 자기는 뺌
# 4 -> 앞에 2,1,3이 있음 - 우선 2부터 - 1,4,2 - 자기뒤에 2가 나왓으므로 2는 만남(1,4,2) - 다음 1 - 자기 앞에 나왓으므로 1은 제외(4,2) - 다음 3 - 4,2,3 - 자기 뒤에있으므로 냄겨둠 - 4 끝
