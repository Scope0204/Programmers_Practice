def solution(weights, head2head):

    recode = []
    win_rate = 0

    for index, a in enumerate(weights):
        win, fight, bonus = 0, 0, 0
        for index2, b in enumerate(head2head[index]):
            if b == "W":
                win += 1
                fight += 1
                if weights[index2] > a:
                    bonus += 1
            elif b == "L":
                fight += 1

        if fight == 0:
            win_rate = 0
        else:
            win_rate = win/fight

        recode.append(
            {"index": index+1, "weight": weights[index], "win_rate": win_rate, "bonus": bonus})

    recode.sort(key=lambda x: x["index"])
    recode.sort(key=lambda x: x["weight"], reverse=True)
    recode.sort(key=lambda x: x["bonus"], reverse=True)
    recode.sort(key=lambda x: x["win_rate"], reverse=True)

    return [x["index"] for x in recode]


# 중요도
# 1. 승률 2. 자기보다 무거운 복서와의 승률 3. 자기몸무게가 무거운 복서 4. 번호가 작은순서
print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]), 3412)
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))

# 다른 풀이 : 한방에 정렬 -> 파이썬의 sort()는 동률이면 그 다음 요소를 보고 정렬
"""
def solution(weights, head2head):
    result = []
    l = len(weights)
    # 한 번에 정렬해서 풀어봅시다!
    ans = [[0 for _ in range(4)] for _ in range(l)] # 승률, 무거운복서 이긴횟수, 자기 몸무게, 번호(음수로)
    for i in range(l):
        ans[i][2] = weights[i]
        ans[i][3] = -(i+1)
        cnt = 0 # 판수
        for j in range(l):
            if head2head[i][j] == 'W':
                ans[i][0] += 1 # 일단 이김
                cnt += 1
                if weights[i] < weights[j]:
                    ans[i][1] += 1 # 무거운 복서 이김
            elif head2head[i][j] == 'L':
                cnt += 1 # 판수만 늘려준다
        if cnt == 0:
            ans[i][0] = 0
        else:
            ans[i][0] /= cnt
    ans.sort(reverse=True) # 역순으로 정렬하면 모든 조건이 한 번에 정렬된다

    for i in range(l):
        result.append(-ans[i][3])
    return result

"""
