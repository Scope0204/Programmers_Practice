s = list(map(int, (input().split())))

a, b = max(s[0], s[1]), min(s[0], s[1])
c = 1
d = a*b

while c > 0:
    c = a % b
    a, b = b, c

print(a)
print(d//a)

# 유클리드 호제법
