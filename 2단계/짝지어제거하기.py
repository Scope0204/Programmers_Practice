def solution(s):
    answer = []

    for v in s:
        answer.append(v)
        if len(answer) > 1 and answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()

    return 1 if answer == [] else 0


print(solution("cdcd"))


# 다른 풀이 : 더 좋은거 같다
"""
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i) # 없는 경우 추가
        else: # 잇는 경우
            if(answer[-1] == i): # 마지막 값과 같은 경우 
                answer.pop() # 마지막 부분 삭제
            else:
                answer.append(i) # 아니면 더하기
    return not(answer) 
"""
