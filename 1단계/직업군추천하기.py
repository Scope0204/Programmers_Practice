def solution(table, languages, preference):

    table.sort()  # 중복시 사전상 먼저나오는 값 return

    skill = [0] * len(table)
    score = [0] * len(table)

    for i in range(len(table)):
        skill[i] = table[i].split(" ")
        skill[i].reverse()

    for j in range(len(skill)):
        for a, b in enumerate(languages):
            if b in skill[j]:
                score[j] += (skill[j].index(b) + 1) * preference[a]

    return skill[score.index(max(score))][-1]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
      "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))

# 0 1 2 3 4 5
# 주제 5 4 3 2 1 점
# 0 1 2 3 4 주제
