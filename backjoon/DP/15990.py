t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(1, 4):
        # i = 1, 2 ,3
        now = i  # 현재 총 수
        dp = [], before = [i]
        while now != n:
            for j in range(1, 4):
                if j != before:  # 같지않은 경우
                    dp.append(now+j)
