n = int(input())
l = list(map(int,input().split()))
k = -1 
for i in range(n-1,0,-1):
    if l[i-1] > l[i]:
        k = i-1
        break
if k == -1:
    print(-1)
else:
    for i in range(n-1,0,-1):
        if l[k] > l[i]:
            l[k],l[i] = l[i],l[k]
            arr = l[k+1:]
            arr.sort(reverse=True)
            l = l[:k+1] + arr
            print(*l)
            break