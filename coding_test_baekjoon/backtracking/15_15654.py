n,m = list(map(int,input().split()))
l = list(map(int,input().split()))
l.sort()
s = []

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(n):
        if l[i] not in s:
            s.append(l[i]) 
            dfs()
            s.pop()

dfs()
