n = int(input())
dp = [0, 1, 2, 4]


for i in range(n):
    num = int(input())

    if num < 4:
        print(dp[num])
    else:
        while len(dp) < num+1:
            dp.append(sum(dp[-3:]))

        print(dp[num])

# f(n) = f(n-1) + f(n-2) + f(n-3) 규칙을 발견할 수 있었음
