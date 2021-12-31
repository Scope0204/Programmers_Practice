n = int(input())
a = list(map(int, input().split(" ")))
dp = [0]*n

for i in range(n):
    if a[0] >= a[i]:
        dp[i] = a[i]
    else:
        now, sum = 0,0
        for j in range(i):
           
            if now == 0:
                now = a[j] 
                sum += a[j]
            else:
                if now < a[j] and a[j] < a[i]:
                    now = a[j]
                    sum += a[j]
            

        dp[i] = a[i]+sum
                
print(max(dp))

'''
 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8}
'''