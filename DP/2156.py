n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

dp = [0]*n

if n == 1:
    dp[0] = arr[0]
elif n == 2:
    dp[1] = arr[0]+arr[1]
else:
    dp[0] = arr[0] 
    dp[1] = arr[0]+arr[1]
    dp[2] = max(dp[1],arr[0]+arr[2],arr[1]+arr[2])

    for i in range(3,n):
        dp[i]=max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])

print(max(dp))




# 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

#참고 ) https://www.acmicpc.net/board/view/60664
