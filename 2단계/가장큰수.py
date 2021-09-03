# def solution(numbers):

#     answer = ""

#     a = sorted(list(map(str, numbers)), reverse=True)

#     b = sorted(a, key=lambda x: x*3, reverse=True)

#     for i in a:
#         if answer == "" and int(i) == 0:  # 처음 시작시 아무것도없을때, 시작값이 0 이면 0 반환
#             return "0"

#         else:  # 시작이 아니고 0 아닌경우
#             if len(i) == 1:  # 한자리 수의 경우는 무조건 더함
#                 answer += i
#             else:
#                 # 두자리수 이상의 첫번재 자릿값이 a에 있는 경우 & 해당 숫자 안에서 첫번째 자릿수보다 작은 수가 있는 경우
#                 if i[0] in a and i[0] > sorted(i)[0]:
#                     answer += i[0]*a.count(i[0]) + i  # answer에는 그 한자리 숫자를 더함
#                 else:
#                     answer += i

#     return answer

def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))))


# print(solution([3, 30, 34, 5, 9]), "9534330")
# print(solution([6, 10, 2]), "6210")
# print(solution([0, 0, 0, 0]), "0")
# print(solution([15, 151]), "15151")
print(solution([70, 0, 0, 0]), "70000")
# print(solution([0, 0, 0, 1000]), "1000000")
print(solution([0, 0, 0, 0]), "0")
# print(solution([0, 0, 70]), "7000")
print(solution([887, 8, 8, 888, 886]))

# lambda 사용법 익힐것
