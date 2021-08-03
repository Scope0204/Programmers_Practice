def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        if i == len(prices)-1:  # 마지막의 경우 가격변동 x . 무조건 0
            answer.append(count)
            break
        else:
            for j in range(len(prices)):
                if j > i:
                    if prices[i] <= prices[j]:
                        count += 1
                    else:
                        count += 1
                        break

            answer.append(count)
    return answer


print(solution([1, 2, 3, 2, 3]))
