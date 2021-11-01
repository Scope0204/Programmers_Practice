N = int(input())
P = [0]+list(map(int, input().split()))
dp = [0]*(N+1)
dp[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        # print(i, j, dp[i], dp[i-j], P[j])
        if j == 1:
            dp[i] = dp[i-j]+P[j]

        elif dp[i] > dp[i-j]+P[j]:
            dp[i] = dp[i-j]+P[j]

print(dp[-1])
