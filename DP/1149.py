# 이전 풀이
# 트리식으로 바로 아래의 경우의 수를 따져가며 풀이(x, 오답)
'''
n = int(input())
dp = [[0] * 3 for _ in range(n)]
past = [i for i in range(n)]

for i in range(n):  # n번만큼 반복
    colors = list(map(int, input().split()))

    for j in range(len(colors)):  # colors수만큼 반복(첫번째 값 ~ 마지막 값)
        if i == 0:  # 첫번째 경우
            dp[i][j] = colors[j]
        else:  # 두번째 이후
            past_idx = 0
            num = dp[i-1][j]
            count = 0
            for z in range(len(colors)):
                if z != past[j]:  # 전에 나온 위치와 다른 수
                    if count == 0:
                        num = dp[i-1][j] + colors[z]
                        past_idx = z
                        count += 1
                    else:
                        if dp[i-1][j] + colors[z] < num:
                            num = dp[i-1][j] + colors[z]
                            past_idx = z
            dp[i][j] = num
            past[j] = past_idx


print(min(dp[n-1]))
print(dp)
'''

# 역순으로 그 색이 오기전, 그 색을 제외한, 다른 색 둘의 최솟값을 더한 값을 구해온다
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))  # 이런 식으로도 2차원 배열을 꾸릴 수 있음 참고
for i in range(1, len(dp)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[n - 1]))
