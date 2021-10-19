# 후위 표기식 : 연산자가 피연산자 뒤에 위치
# 예: 중위 표기법으로 표현된 a+b는 전위 표기법으로는 +ab이고, 후위 표기법으로는 ab+가 된다.

'''
1. 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다.
2. 둘째 줄에는 후위 표기식이 주어진다.
(여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다)
3. 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.

3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다.
그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

소숫점 둘째자리까지 표기한다
'''

n = int(input())
postfix = list(input())
replace_aplpa = []
answer = []


for _ in range(n):
    num = input()

    for i, v in enumerate(postfix):
        index = 0
        if v.isalpha() and v not in replace_aplpa:
            now_aplpa = v
            while index < len(postfix):
                if postfix[index] == now_aplpa:
                    postfix[index] = num
                index += 1

            replace_aplpa.append(now_aplpa)
            break


for v in postfix:

    if v.isdigit():
        answer.append(int(v))
    else:
        a, b = answer[-2], answer[-1]
        answer = answer[0: -2]

        if v == '+':
            answer.append(a + b)
        elif v == '-':
            answer.append(a - b)
        elif v == '*':
            answer.append(a * b)
        elif v == '/':
            answer.append(a / b)


print("{:.2f}".format(answer[-1]))

# 자료구조, 스택
# 좀 긴거같다. 효율적인 풀이 모색
