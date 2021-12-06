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
'''