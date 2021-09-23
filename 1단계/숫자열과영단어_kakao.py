def solution(s):
    change = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    answer = ''
    now = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            now += i
            if now in change:
                answer += change[now]
                now = ''

    return answer


print(solution("one4seveneight"))

# 다른 풀이 : replace 함수를 써서 해당하는 문자의 값을 바꾸는 방법
"""
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""
