def solution(number, k):
    del_list = sorted(number, reverse=True)
    del del_list[k:]

    answer = ""
    for i in range(len(number)):

        if len(answer) + len(number)-i <= len(number)-k:
            answer += number[i]
        else:
            if del_list:  # 0이 아니면
                if number[i] in del_list:  # 최상위 수에 해당하는 값만 answer에 더한 후 리스트에서 삭제
                    del_list.pop(del_list.index(number[i]))
                    answer += number[i]
            else:
                answer += number[i]

    return answer


print(solution("1231234", 3))
print(solution("4177252841", 4))
