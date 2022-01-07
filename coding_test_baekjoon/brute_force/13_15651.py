n,m = list(map(int,input().split()))
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
        
    for i in range(start,n+1):
        s.append(i)
        dfs(1) 
        s.pop()

dfs(1)

