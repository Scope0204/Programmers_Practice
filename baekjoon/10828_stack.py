"""
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
# 첫째 줄에 주어지는 명령의 수 N

"""

# 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
# input 사용시 시간초과

import sys

n = int(sys.stdin.readline())

answer = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        answer.append(command[1])
    elif command[0] == 'pop':
        if answer:  # answer 스택에 정수가 있는 경우
            print(answer.pop(-1))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(answer))
    elif command[0] == 'empty':
        if answer:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if answer:
            print(answer[-1])
        else:
            print(-1)

# 자료구조, 스택 문제
