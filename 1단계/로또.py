def solution(lottos, win_nums):
    answer = [0, 0]
    lank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}  # 6은 그 외

    for i in lottos:
        if i in win_nums:  # 맞춘 번호가 있는 경우
            answer[0] += 1
            answer[1] += 1
        elif i == 0:  # 0인경우
            answer[1] += 1  # 최고 경우의 수에 맞춘 확률 증가

    min_case = lank[answer[0]] if answer[0] in lank else 6
    max_case = lank[answer[1]] if answer[1] in lank else 6

    return [max_case, min_case]


print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))


# 다른 풀이
"""
def solution(lottos, win_nums):
    
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
"""
