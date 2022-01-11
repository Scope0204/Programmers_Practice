import sys

n = int(sys.stdin.readline())
answer = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        answer.append(command[1])
    elif command[0] == "pop":
        if answer:
            print(answer.pop(0))
        else:
            print("-1")
    elif command[0] == "size":
        if answer:
            print(len(answer))
        else:
            print("0")
    elif command[0] == "empty":
        if answer:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if answer:
            print(answer[0])
        else:
            print("-1")
    elif command[0] == "back":
        if answer:
            print(answer[-1])
        else:
            print("-1")
