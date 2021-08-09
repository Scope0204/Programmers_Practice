def solution(d, budget):
    answer = [0]*len(d)
    d.sort()

    for i in range(len(d)):
        count = d[i]
        j = i+1
        while j < len(d):
            if count + d[j] <= budget:
                count += d[j]
                answer[i] += 1
            else:
                break

    return answer


print(solution([1, 3, 2, 5, 4], 9))


# result는 몇명을 지원할 수 있는지이다.
