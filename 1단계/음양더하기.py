def solution(absolutes, signs):
    answer = 0

    for i, v in enumerate(absolutes):
        if signs[i]:
            answer += v
        else:
            answer -= v
    return answer
