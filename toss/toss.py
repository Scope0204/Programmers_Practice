# def solution(name_list):
#     name = []
#     same_name = []
#     for i in range(len(name_list)):
#         if name_list[i] not in name:
#             name.append(name_list[i])
#             name_list[i] = name_list[i] + chr(65)
#         elif name_list[i] in name:
#             same_name.append(name_list[i])
#             name_list[i] = name_list[i] + chr(65+same_name.count(name_list[i]))

#     return name_list


# print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))


# def solution(seconds):

#     snack = [[300, 10], [130, 30], [120, 20], [20, 30]]
#     count = 0
#     snack_count = 0

#     while seconds != 0:
#         if seconds - snack[snack_count][0] >= 0 and snack[snack_count][1] != 0:
#             count += 1
#             seconds -= snack[snack_count][0]
#             snack[snack_count][1] -= 1
#         else:
#             snack_count += 1

#         if snack_count > 3:
#             break

#     return count


# print(solution(300))
# print(solution(450))


def solution(csv_string, keyword):
    answer = csv_string.split("\n")
    b = 0
    count = 0

    for i in range(1, len(answer)):
        a = answer[i].split(',')
        if keyword in a[1]:
            if a[2] == '':
                break
            else:
                count += int(a[3])

            if b < int(a[2]):
                b = int(a[2])

    for i in range(1, len(answer)):  # 하위 조직 수 계산
        a = answer[i].split(',')
        if b == 0:
            count += int(a[3])
        elif a[2] != '' and int(a[2]) == b and keyword not in a[1]:
            count += int(a[3])

    return -1 if count == 0 else count


print(solution("조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11", "비바"))
