from collections import deque
# BFS


def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

# dfs
# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
#     dfs(0,0)
#     return answer


print(solution([1, 1, 1, 1, 1], 3))
