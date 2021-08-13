def solution(d, budget):
    d.sort()
    count = d[0]
    i = 1
    
    if count > budget:
        return 0
    else:
        while i < len(d):
            if count + d[i] <= budget:
                count += d[i]
                i += 1
            else:
                break

        return i


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))


# result는 몇명을 지원할 수 있는지이다.
