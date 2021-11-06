n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
dp[0] = 1

for i in range(1, n):  # 첫번째는 증가하는 값이 없으니
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1  # 자기 자신보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다
print(max(dp))
# print(dp)

# Longest Increasing Subsequences 알고리즘
# DP로 풀수있는 가장 보편적인 문제
# 문제 풀이 참고 : https://bitwise.tistory.com/215
