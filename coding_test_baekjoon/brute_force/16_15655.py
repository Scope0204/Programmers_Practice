n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort()
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n):
        if l[i] not in s:
            s.append(l[i]) 
            dfs(i+1)
            s.pop()

dfs(0)
