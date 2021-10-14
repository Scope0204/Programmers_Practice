n = int(input())
answer = []
answer2 = []
count = 1
temp = True

for _ in range(n):
    num = int(input())
    while count <= num:
        answer.append(count)
        answer2.append('+')
        count += 1

    if answer[-1] == num:
        answer.pop()
        answer2.append('-')
    else:
        temp = False

if temp == False:
    print("NO")

else:
    for i in answer2:
        print(i)


# 자료구조, 스택
# 메모리, 시간 좀 나옴
