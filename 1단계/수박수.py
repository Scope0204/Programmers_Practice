def solution(n):
    answer = ""
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer


print(solution(3))

# 다른 풀이
"""
def water_melon(n):
    s = "수박" * n
    return s[:2]


print("n이 3인 경우: " + water_melon(3))
print("n이 4인 경우: " + water_melon(4))

"""
