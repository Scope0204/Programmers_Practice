def solution(priorities, location):
    wait = {}
    answer = 0
    for i in range(len(priorities)):
        wait[i] = priorities[i]

    for i in range(len(priorities)):
        for j in range(len(priorities)):
            if i != j and i < j and priorities[i] < priorities[j]:
                del wait[i]
                wait[i] = priorities[i]
                break

    # for i in wait.keys():
    #     answer += 1
    #     if i == location:
    #         return answer

    return wait


# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 1, 1, 1, 1], 2))
print(solution([1, 5, 3, 4, 5, 6], 2))
