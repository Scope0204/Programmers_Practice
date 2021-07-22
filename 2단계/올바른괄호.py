# 조건1 : (와 )의 개수가 같을 것
# 조건2 : (가 먼저 올 것

def solution(s):

    count = 0  # ( 와 )가 같다면 0

    if s[0] == ")":
        return False

    for i in s:
        if i == "(":
            count += 1

        elif i == ")":
            if count <= 0:  # 놓친부분: ( 가 없음에도 불구하고 )가 올 때
                return False
            else:
                count -= 1

    return True if count == 0 else False


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("(((())))"))

# 다른 풀이
# stack과 pop() 활용
"""
def is_pair(s):
    st = list() # 리스트. stack 선언 
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try: #예외처리 방식
                st.pop() #)가 오면 pop. 즉 리스트에서 제거
            except IndexError: 
                return False #제거할 (가 없을 시 false 

    return len(st) == 0 
"""
