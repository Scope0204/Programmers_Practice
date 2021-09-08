def solution(record):
    answer = []
    user = {}
    answer2 = []

    for a in record:
        b = list(a.split(" "))
        # b[0]:명령 /  b[1]:아이디 /  b[2]: 닉네임
        if b[0] == "Enter":
            user[b[1]] = b[2]
            answer.append([b[1], b[0]])

        elif b[0] == "Change":
            user[b[1]] = b[2]

        if b[0] == "Leave":
            answer.append([b[1], b[0]])

    for id, command in answer:
        if command == "Enter":
            answer2.append(user[id]+"님이 들어왔습니다.")
        elif command == "Leave":
            answer2.append(user[id]+"님이 나갔습니다.")

    return answer2


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
# 명령문 / 유저 아이디 / 바꾼 아이디

# 다른 풀이
"""
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
"""
