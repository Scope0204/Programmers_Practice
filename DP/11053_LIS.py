n = int(input())
a = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        # if a[i] > a[j]:
        #     dp[i] = max(a[i], a[j]+1)
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

print(max(dp))
# print(dp)

# Longest Increasing Subsequences 알고리즘
# DP로 풀수있는 가장 보편적인 문제
# 문제 풀이 참고 : https://bitwise.tistory.com/215
