import itertools


def solution(k, dungeons):
   
    answer = [] 

    for i in itertools.permutations(dungeons):
        gauge = k
        score = 0 
        # print(i)
        for j in i:
            # j[0] = 최소피로도 , j[1] = 소모피로도
            if j[0] > gauge or gauge - j[1] < 0 :
                break
            else:
                gauge -= j[1]
                score += 1

        answer.append(score)
    return max(answer)

print(solution(80,[[80,20],[50,40],[30,10]]))

# 내가 푼 풀이 : 모든 경우의 수 탐색 

# 다른 풀이 
'''
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
'''