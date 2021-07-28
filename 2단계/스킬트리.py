def solution(skill, skill_trees):
    skill_list = list(skill)
    answer = 0

    for i in range(len(skill_trees)):

        point = -1  # 현재 배운 스킬.

        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill_list:  # 스킬에 포함되있을때
                # 현재 포인트에서 배울수 있는지 없는지 확인
                if point+1 < skill_list.index(skill_trees[i][j]):
                    # 만약 현재 스킬 포인트보다 두단계 높은 레벨의 스킬의 경우
                    answer += 1
                    break  # 반복문을 종료
                    # 1. 낮은 스킬의 경우
                    # 2. 한단계 높은 스킬의 경우 -> point 의 증가가 필요하다
                    # 3. 같은 단계의 스킬의 경우
                elif point+1 == skill_list.index(skill_trees[i][j]):
                    point += 1

    return len(skill_trees) - answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
# CBD => c-b-d 순으로 선마

# 다른 풀이
"""
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer
"""
