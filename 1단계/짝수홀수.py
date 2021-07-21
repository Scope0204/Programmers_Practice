def solution(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(solution(3))

# 다른 풀이
"""
1)
def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"

2)
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]


"""
