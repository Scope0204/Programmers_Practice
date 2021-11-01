# 카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오.
# N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다.
# 즉, 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.

N = int(input())  # 구매하려고 하는 카드의 개수
P = list(map(int, input().split()))  # 카드별 가격
dp = [0]*(N+1)  # 1부터 시작하기 위함
dt = [0]
for i in P:
    dt.append(i)

for i in range(1, N+1):
    if i == 1:
        dp[i] = dt[i]
    else:
        a = 0
        for j in range(1, N+1):  # 0 1 1 6 8 11 1 1 1 1 1 1 1
            if i-j > 0:
                if a < max(dp[i-j]+dt[j], dt[i]):
                    a = max(dp[i-j]+dt[j], dt[i])
        dp[i] = a
print(max(dp))
