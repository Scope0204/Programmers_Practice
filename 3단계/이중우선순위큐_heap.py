def solution(operations):
    answer = []

    for v in operations:
        order = v.split(" ")[0]
        number = v.split(" ")[1]

        if order == "I":
            answer.append(int(number))

        elif order == "D":
            if answer != []:
                if number == "1":
                    answer.pop(answer.index(max(answer)))
                elif number == "-1":
                    answer.pop(answer.index(min(answer)))

    return [0, 0] if answer == [] else [max(answer), min(answer)]

#  모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
