def solution(priorities, location):
    wait = {}
    answer = 0

    for i in range(len(priorities)):
        wait[i] = priorities[i]

    while 1:
        for i in wait.keys():
            if wait[i] != max(wait.values()):
                del wait[i]
                wait[i] = priorities[i]
                break
            elif wait[i] == max(wait.values()):
                answer += 1
                if i == location:
                    return answer
                else:
                    del wait[i]
                break


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 5, 3, 4, 5, 6], 2))


# 다른 풀이: use any()
""" 
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
"""