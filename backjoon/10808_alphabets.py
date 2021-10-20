s = input()
answer = [0] * 26
# 아스키 코드상 97 ~ 122 까지이다.

for i in s:
    answer[ord(i)-97] += 1

print(" ".join(map(str, answer)))
# 구현, 문자열
