def euclidean(a, b):
    c = 1
    while c > 0:
        c = a % b
        a, b = b, c
    return a  # 최대공약수


i = int(input())

for _ in range(i):
    s = list(map(int, (input().split())))
    a, b = max(s[0], s[1]), min(s[0], s[1])
    print(a*b//euclidean(a, b))
