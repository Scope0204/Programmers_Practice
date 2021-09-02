def solution(numbers):

    answer = ""

    b = list(map(str, numbers))

    for i in range(len(b)):
        b[i] = b[i]+b[i]

    a = sorted(b, reverse=True)

    for i in a:
        if answer == "":
            if int(i) == 0:
                return "0"
            else:
                answer += i[0:len(i)//2]
        else:
            answer += i[0:len(i)//2]

    return answer


# print(solution([3, 30, 34, 5, 9]))
# # print(solution([6, 10, 2]))
# print(solution([0, 0, 0, 0]))
# print(solution([15, 151]))
print(solution([70, 0, 0, 0]), "70000")
print(solution([0, 0, 0, 1000]), "1000000")
print(solution([0, 0, 0, 0]), "0")
print(solution([0, 0, 70]), "7000")


# 보류
