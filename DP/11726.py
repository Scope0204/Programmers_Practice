# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램
# 2 * n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력

n = int(input())
dp = [0] * (n+1)
if n <= 3:
    print(n)
else:
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[n] % 10007)

'''
1 - 1 / 2 - 2 / 3 - 3 / 4 - 5 / 5 - 8 / 6 - 13 .....
dp[i] = dp[i-1]+dp[i-2] 의 점화식이 세워짐
'''
# 참고
# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%8011726%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-2xn-%ED%83%80%EC%9D%BC%EB%A7%81-DP
