s = input()
answer = [-1] * 26

for i, v in enumerate(s):
    if answer[ord(v)-97] == -1:
        answer[ord(v)-97] = i

print(' '.join(map(str, answer)))
