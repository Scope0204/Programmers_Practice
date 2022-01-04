n = int(input())
ans = 0
for i in range(len(str(n))):
    if i+1 == len(str(n)):
        ans += (n-(10**i)+1)*(i+1) 
    else:
        ans += 9*(10**i)*(i+1)
print(ans)

'''
1~9 : 9개 , n개 
10~99:99-10+1개  * 2  = 90 * 2 
100~999:999-100+1개 * 3 = 900 * 3 
100~n:n-100+1개 
'''



