n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = i  # 모든 수는 1^으로 만들 수 있으므로 , 최대 경우의 수 = 해당 수의 값
    for j in range(1, i):
        # 제곱수가 i보다 커지면 break
        if(j**2) > i:
            break

        # 1을 제외하고 작은수들부터 제곱한 수를 지금 기준이 되는 수와 비교해서 하나라도 있으면 그 제곱수를 넣어주고 1을 더해준다.
        # 예를 들어 i =16 j =4 처럼 나누어떨이지는 수가있으면 dp[0] = 0 에 1을 더해서 1개로 만들어준다.
        # dp[i - 1], dp[i - 4], dp[i - 9], dp[i - 16]중 가장 작은 값은 0이고 여기에 1을 더한 값을 dp[i]에 넣어준다.
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1
print(dp[n])

# 다른풀이 (시간초과 해결)
# https://pacific-ocean.tistory.com/205
