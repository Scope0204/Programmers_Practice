n = int(input())
n_list = list(map(int, input().split()))
dp = [0]*n
dp[0] = n_list[0]

for i in range(1, n):
    dp[i] = max(n_list[i], n_list[i]+dp[i-1])

print(max(dp))
