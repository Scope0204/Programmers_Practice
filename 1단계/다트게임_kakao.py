def solution(dartResult):

    count = -1
    turn_num = ""
    sum_num = ["0"]*3

    for i in dartResult:

        if i in ["S", "D", "T"]:
            if i == "S":
                sum_num[count] = int(turn_num) ** 1
            elif i == "D":
                sum_num[count] = int(turn_num) ** 2
            elif i == "T":
                sum_num[count] = int(turn_num) ** 3

            turn_num = ""  # 초기화

        elif i in ["*", "#"]:
            if i == "*":
                if count - 1 < 0:  # -1시 -인 경우(첫번째의 경우)
                    sum_num[0] = sum_num[0] * 2
                else:
                    sum_num[count-1] = sum_num[count-1]*2
                    sum_num[count] = sum_num[count] * 2

            elif i == "#":
                sum_num[count] = sum_num[count] * -1

        else:  # 숫자일 때
            if turn_num == "":  # 현재 공백일때,
                count += 1

            turn_num += i

    return sum(sum_num)


# 총 3번의 기회
# 각 기회마다 0 - 10점
# S , D , T -> 1제곱, 2제곱, 3제곱
# * 스타상 시 해당 점수와 바로 전 점수 2배
# # 아차상 시 해당 점수 * -1
# * 은 첫번째도 나올 수있고 이 경우 첫번째 점수만 2배
# * 는 중첩가능
# *은 #과도 중첩가능 이때는 -2배가 됨
# S, D, T는 점수마다 하나씩 존재
# *, # 는 점수마다 둘 중 하나만 존재. 존재하지 않을 수도 있음

print(solution("1S2D*3T"))
# (1*1) * 2 + (2*2) * 2 + (3*3)
