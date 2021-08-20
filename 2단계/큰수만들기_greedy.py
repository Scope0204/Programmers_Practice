def solution(number, k):

    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            # k번만큼 해소되지않을 때 , answer이 있을 때 , 현재 answer 값보다 큰 값이 있을 때
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer)-k])
    # k가 다 해소되지않는 경우. 중복되는 수의 경우 길이만큼은 맞춰야하기때문


# print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("99999", 2))
