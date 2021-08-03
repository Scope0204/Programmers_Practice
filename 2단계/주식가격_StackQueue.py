# use Stack
def solution(prices):
    answer = [0]*len(prices)  # 답이 담길 prices 길이의 배열.
    stack = []

    for i, price in enumerate(prices):  # i -> index , price -> value
        # stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stac
    # k에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer


print(solution([1, 2, 2, 2, 3]))


# 이중 for문
"""
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer
"""
