n = int(input())
dp = [1]*10 # 뒤의 자릿수 0~9 가 n이 1일 때

for i in range(n-1):
    for j in range(1,10): # 뒤의 자리가 0인 경우에는 앞이 0인 경우 단 하나이므로 안 바뀜
        dp[j] += dp[j-1] 

print(sum(dp)%10007)