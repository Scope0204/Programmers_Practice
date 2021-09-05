def solution(new_id):

    answer = []

    for i in new_id.lower():  # 1
        if i.isalpha() or i.isdigit() or i == "-" or i == "_" or i == ".":  # 2
            if answer != [] and i == "." and answer[-1] == ".":  # 3
                answer.pop()
            answer.append(i)

    if answer[0] == ".":
        answer.pop(0)

    if answer != [] and answer[-1] == ".":  # 4
        answer.pop()

    if answer == []:  # 5
        answer.append("a")

    if len(answer) >= 16:  # 6
        answer = answer[0:15]
        if answer[-1] == ".":
            answer = answer[0:14]
    elif len(answer) <= 2:  # 7
        while len(answer) < 3:
            answer.append(answer[-1])

    return "".join(answer)


print(solution("./././././abcd/././././."))
print(solution("=.="))
print(solution("b......@"))


"""
<카카오 아이디 조건>
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

* 규칙에 맞지 않은 경우 7가지 처리과정을 통해 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
1.  new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2.  new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3.  new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4.  new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.

5.  new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6.  new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7.  new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""
