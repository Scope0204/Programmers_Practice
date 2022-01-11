"""
L	: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
      삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	: $라는 문자를 커서 왼쪽에 추가함

"""

'''
import sys

answer = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
cusor = len(answer)  # abcd = 4


for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'L':
        if cusor != 0:
            cusor -= 1
    elif command[0] == 'D':
        if cusor != len(answer):
            cusor += 1
    elif command[0] == "B":
        if cusor != 0:
            cusor -= 1
            answer.pop(cusor)
    elif command[0] == "P":
        answer.insert(cusor, command[1])
        cusor += 1

print(''.join(answer))
'''
# 시간초과


from sys import stdin
stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stk1:
            stk1.pop()
        else:
            continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))

# 자료 구조 , 스택 , 연결 리스트
