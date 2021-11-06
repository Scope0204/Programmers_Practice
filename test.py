def solution(id_list, report, k):

    user = {}
    ben = [0]*len(id_list)
    answer = [0]*len(id_list)

    for i in report:
        user_name = i.split(" ")[0]
        ben_user = i.split(" ")[1]

        if user_name in user:  # 한번 한 유저가 또 고를 때
            if ben_user not in user[user_name]:  # 처음 고른 경우
                user[user_name] += [ben_user]
                ben[id_list.index(ben_user)] += 1

        else:
            user[user_name] = [ben_user]
            ben[id_list.index(ben_user)] += 1

    for i, name in enumerate(id_list):
        if name in user:
            for ben_user in user[name]:
                if ben[id_list.index(ben_user)] >= k:
                    answer[i] += 1

    return answer
