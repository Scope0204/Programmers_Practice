'''
n = int(input())
t = [] 
p = [] 
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

ans = [] 
for j in range(n):
    if j+t[j] < n : 
        idx = j
        money = 0

        while 1:
            money += p[idx]
            if idx + t[idx]>= n:
                break
            else:
                idx += t[idx]
                if idx + t[idx] > n:
                    break


        ans.append(money) 

print(ans)

'''

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n: # 작업해야할 양 + 현재 idx  >  n 
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])

print(dp[0])