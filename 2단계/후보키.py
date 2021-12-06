from itertools import combinations

def solution(relation):
    # key의 개수 
    N = len(relation[0])
    key_idx = list(range(N)) 
    candidate_keys = [] # 후보키 

    
    for i in range(1,N+1): # 1가지 경우의 수 ~ N가지 경우의 수 
        for comb in combinations(key_idx, i): # idx의 조합들
            hist = [] 
            for rel in relation:
                current_key = [rel[c] for c in comb]
                # print(i, rel, comb , current_key)
                # 하나라도 중복되는 경우: 식별 불가능 
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
            else:
                for ck in candidate_keys:
                    # 최소성 확인 
                    if set(ck).issubset(set(comb)): # ck 가 comb의 부분집합인가? 
                        break
                else:
                    candidate_keys.append(comb)

    
    return len(candidate_keys)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

'''
https://withcoding.com/77 : 파이썬 set집합 사용법 정리
https://programmers.co.kr/questions/10412 : 참고 풀이

# 라이브러리 안 쓴 풀이 : https://programmers.co.kr/learn/courses/30/lessons/42890/solution_groups?language=python3
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
'''