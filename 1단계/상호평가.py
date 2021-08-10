# 평균. 단 자신이 평가한 점수가 유일한 최고 최저점은 제외

def solution(scores):

    average, my_score = [[0]*len(scores)
                         for i in range(len(scores))],  [0]*len(scores)

    answer = [0]*len(scores)

    answer2 = ''

    for i in range(len(scores)):

        for j in range(len(scores[i])):
            average[j][i] = scores[i][j]
            if i == j:
                my_score[i] += scores[i][j]

    for i in range(len(scores)):

        if my_score[i] == max(average[i]) or my_score[i] == min(average[i]):
            if average[i].count(my_score[i]) == 1:
                average[i].pop(average[i].index(my_score[i]))

        answer[i] = (sum(average[i])) / len(average[i])

        if answer[i] >= 90:
            answer2 += "A"
        elif 90 > answer[i] >= 80:
            answer2 += "B"
        elif 80 > answer[i] >= 70:
            answer2 += "C"
        elif 70 > answer[i] >= 50:
            answer2 += "D"
        elif 50 > answer[i]:
            answer2 += "F"

    return answer2


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))


# 다른 풀이
"""
def solution(scores) :
    
    avgs=[]

    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])

"""

# 다른 풀이2
# collection
# enumerate, map , zip
"""
from collections import Counter
def solution(scores):   
    answer = ''

    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

"""

# 다른 풀이3
"""
solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))
"""
