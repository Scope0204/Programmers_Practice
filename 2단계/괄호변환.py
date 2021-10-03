"""
<조건>

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

* (' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
* 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
* p는 '(' 와 ')' 로만 이루어진 문자열이며 길이는 2 이상 1,000 이하인 짝수입니다. => 균형잡힌 문자열
* 문자열 p를 이루는 '(' 와 ')' 의 개수는 항상 같습니다.
"""


def uvsolution(w):

    if w == '':  # 1. 빈 문자열의 경우 빈 문자열을 반환
        return ''

    else:  # 2. 문자열 w 를 u와 v로 분리
        left, right = 0, 0  # ( , )
        u, v = '', ''

        for index, val in enumerate(w):
            if index == 0 or left != right:  # 처음이거나, (와 ) 갯수가 다를 때
                u += val
                if val == "(":
                    left += 1
                else:
                    right += 1
            else:  # 그 후 나머지 문자열
                v += val

        return u, v


def solution(p):
    answer = ''
    u, v = uvsolution(p)

    # 처음은 무조건 (가 와야함('올바른 괄호 문자열')
    if u[0] == "(":  # 3. u가 '올바른 괄호 문자열' 의 경우
        answer += u

        u, v = uvsolution(v)  # v가 1,2단계를 수행함
        answer += solution2(u, v)

    else:  # 아닌 경우
        answer = solution2(u, v)

    return answer


def solution2(u, v):
    answer = ''

    if u[0] == "(":  # 문자열 p의 (와 ) 갯수는 항상 동일하다 햇으므로
        answer += u

    elif u[0] == ")":   # 4. u가 '올바른 괄호 문자열' 이 아닌 경우
        answer += "("  # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.

        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        if v != '':
            u2, v2 = uvsolution(v)
            if v2 == '':
                answer += u2
            else:
                while v2 == '':
                    u2, v2 = uvsolution(v2)
                answer += u2

        answer += ")"  # 4-3. ')'를 다시 붙입니다.

        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.

        answer += reverse(u[1:-1])
        """
        for val2 in u[1:-1]:
            if val2 == ")":
                answer += "("
            else:
                answer += ")"
        """
        # 4-5. 생성된 문자열을 반환합니다.

    return answer


def reverse(strings):
    answer = ''
    r = {"(": ")", ")": "("}
    for s in strings:
        answer += r[s]
    return answer


# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))

# 풀이 참고
"""
def split(s):
    queue = []
    positive = 0
    negative = 0
    while s:
        c = s.pop(0)
        queue.append(c)
        if c == "(":
            positive += 1
        else:
            negative += 1
        if positive == negative:
            break
    return queue, s


def is_correct(s):
    if len(s) == 0:
        return True

    stack = []
    while s:
        c = s.pop(0)
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


def reverse(strings):
    r = {"(":")", ")": "("}
    return [r[s] for s in strings]


def solution(p):
    p = list(p)

    def recursive(s):
        if not s:
            return []
        u, v = split(s)
        if is_correct(list(u)):
            return u + recursive(v)
        else:
            u = u[1:-1]
            return ["("] + recursive(v) + [")"] + reverse(u)

    answer = recursive(p)
    return "".join(answer)
"""

# 다른 풀이 :
"""
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
"""
# (참고)
# map 또한 iterable이니 list()로 변환하는 과정은 필요 없음
# ''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) )) 대신 ''.join(['(' if x==')' else ')' for x in p[1:i]]) 도 가능
