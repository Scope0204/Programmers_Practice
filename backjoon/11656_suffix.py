s = input()
answer = []

for i in range(len(s)):
    answer.append(s[i:])

for v in sorted(answer):
    print(v)
